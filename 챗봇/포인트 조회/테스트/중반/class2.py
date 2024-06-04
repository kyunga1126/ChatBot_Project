from flask import Flask, request, jsonify
import MySQLdb

app = Flask(__name__)

# 데이터베이스 연결
def get_db_connection():
    connection = MySQLdb.connect(
        user='root',
        password='12345',
        database='point_class'
    )
    return connection

# 등급별 사용자 조회 함수
def get_users_by_class(point_class):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        if point_class == '브론즈':
            cursor.execute("SELECT name FROM class WHERE point < 500")
        elif point_class == '실버':
            cursor.execute("SELECT name FROM class WHERE point >= 500 AND point < 1000")
        elif point_class == '골드':
            cursor.execute("SELECT name FROM class WHERE point >= 1000 AND point < 1500")
        elif point_class == 'VIP':
            cursor.execute("SELECT name FROM class WHERE point >= 1500")

        result = cursor.fetchall() # 데이터베이스 쿼리 결과 가져오고, 'fetchall()'는 쿼리의 모든 결과 행을 반환.
        users = [row[0] for row in result] # 각 행의 첫번째 값을 추출하여 'users'리스트를 생성. 튜플로 반환.

        if users:
            response_text = f"{point_class} 등급의 사용자: " + ", ".join(users) # users리스트에 있는 사용자 이름들을 쉼표로 구분하여 문자열로 만듦.
        else:
            response_text = f"{point_class} 등급의 사용자가 없습니다."

    except Exception as e:
        response_text = f"오류가 발생했습니다: {e}"

    cursor.close()
    connection.close()

    return response_text

@app.route('/class', methods=['POST'])
def webhook():
    data = request.get_json()  # 요청받은 json데이터를 추출하여 변수명 data에 저장
    print("Received data:", data)  # 요청데이터 확인용
    # 오류 확인용
    if 'userRequest' in data and 'utterance' in data['userRequest']: # data에 userRequest와 그 안에 utterance 키가 존재하는지 확인
        utterance = data['userRequest']['utterance']  # 발화 내용 추출
        print("Received utterance:", utterance)  # 발화 내용 확인용

        # 발화 내용을 기반으로 등급 추출
        if '브론즈' in utterance:
            point_class = '브론즈'
        elif '실버' in utterance:
            point_class = '실버'
        elif '골드' in utterance:
            point_class = '골드'
        elif 'VIP' in utterance:
            point_class = 'VIP'
        else:
            response_text = "조회할 등급을 입력해주세요. 등급은 브론즈, 실버, 골드, VIP로 구성되어 있습니다."
            return jsonify({
                'version': '2.0',
                'template': {
                    'outputs': [{
                        'simpleText': {
                            'text': response_text
                        }
                    }]
                }
            })


        if point_class:
            response_text = get_users_by_class(point_class)
        else:
            response_text = "등급이 제공되지 않았습니다."
    else:
        response_text = "발화가 제공되지 않았습니다."

    return jsonify({
        'version': '2.0',
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': response_text
                }
            }]
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
