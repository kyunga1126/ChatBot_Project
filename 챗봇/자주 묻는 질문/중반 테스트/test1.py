# 블록 스킬 연결 테스트
# mysqlclient 설치하여 MySQLdb 호출
import MySQLdb
from flask import Flask, request
import sys

# MySQL 객체 등록
conn = MySQLdb.connect(host="localhost", port=3306, db='chatbot', user='root', password='1234')
cursor = conn.cursor()

# DB에서 내림차순으로 질문 출력
sql = 'select ask from test order by read_count desc'
cursor.execute(sql)
suppliers = cursor.fetchall()
result=[]

# sql 결과값을 리스트로 처리
for supplier in suppliers:
    output = []
    for i in range(len(supplier)):
        output.append(str(supplier[i]))
        result=result+output

# 리스트에서 5번째 요소까지를 저장
result=result[:5]
# 리스트를 문자열로 변환
str2 = ','.join(result)
# print('사이트에서 자주 묻는 질문은 <%s> 입니다.'%str2)

cursor.close()
conn.close()

app = Flask(__name__)

# url 설정과 챗봇 데이터 설정
@app.route('/say', methods=['POST'])
def sayHello():
    # 카카오챗봇에서 발화문 가져오기
    body = request.get_json()
    print(body)
    
    """
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "사이트에서 자주 묻는 질문은 <"+str2+">입니다."
                    }
                }
            ]
        }
    } """

    responseBody={
        "version": "2.0",
        "template": {
            "outputs": [
                {
                "textCard": {
                    "title": "질문 유형을 선택하세요",
                    "description": "",
                    "buttons": [
                        {
                        "action": "block",
                        "label": "계정",
                        "block": "계정"
                        },
                        {
                        "action": "block",
                        "label": "게임친구",
                        "block": "게임친구"
                        },
                        {
                        "action": "block",
                        "label": "기타",
                        "block": "기타"
                        }
                    ]
                }
                }
            ]
        }
    }
    
    return responseBody
    
# 서버 실행문
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80) # web server
