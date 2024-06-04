# 발화 내용 if문 테스트
# mysqlclient 설치하여 MySQLdb 호출
import MySQLdb
from flask import Flask, request
import sys

# MySQL 객체 등록
conn = MySQLdb.connect(host="localhost", port=3306, db='chatbot', user='root', password='1234')
cursor = conn.cursor()

app = Flask(__name__)

# url 설정과 챗봇 데이터 설정
@app.route('/final', methods=['POST'])
def final():
    # 카카오챗봇에서 발화문 가져오기
    body = request.get_json()
    body=body['userRequest']['utterance']
    print(body) 
    
    # 발화가 시작일 때
    if body=="시작":
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

    elif body=="게임친구":
        sql = 'select ask from friends order by read_count desc'
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        result=[]

        for supplier in suppliers:
            output = []
            for i in range(len(supplier)):
                output.append(str(supplier[i]))
                result=result+output

        result=result[:5]
        str2 = ','.join(result)
        
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
        }

    elif body=="계정":
        sql = 'select ask from users order by read_count desc'
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        result=[]

        for supplier in suppliers:
            output = []
            for i in range(len(supplier)):
                output.append(str(supplier[i]))
                result=result+output

        result=result[:5]
        str2 = ','.join(result)
        
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
        }

    elif body=="기타":
        sql = 'select ask from others order by read_count desc'
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        result=[]

        for supplier in suppliers:
            output = []
            for i in range(len(supplier)):
                output.append(str(supplier[i]))
                result=result+output

        result=result[:5]
        str2 = ','.join(result)
       
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
        }
    
    # 파일에 문제있을 경우
    else:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": { 
                            "text": "파일에 문제있습니다."
                        }
                    }
                ]
            }
        }
    return responseBody

    cursor.close()
    conn.close()

# 서버 실행문
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80) # web server