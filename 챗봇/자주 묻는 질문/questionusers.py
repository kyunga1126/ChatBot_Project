# mysqlclient 설치하여 MySQLdb 호출
import MySQLdb
import sys

# flask에 있는 request와 Bluepoint 호출
from flask import Blueprint, request

# MySQL 객체 등록
conn = MySQLdb.connect(host="localhost", port=3306, db='chatbot', user='root', password='1234')
cursor = conn.cursor()

# 블루프린트 객체 등록
bp = Blueprint('questionusers', __name__, url_prefix='/')

# url 설정
@bp.route('/question/user', methods=['POST'])
def questionusers():
    # 카카오챗봇에서 발화문 가져오기
    body = request.get_json()
    body=body['userRequest']['utterance']
    
    # 챗봇 입력 결과가 계정일 때, DB에서 kind가 user인 질문을 출력
    if body=="계정":
        sql = 'select ask from question where kind="user" order by read_count desc'
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        result=[]

        # sql 결과값을 리스트로 처리
        for supplier in suppliers:
            output = []
            for i in range(len(supplier)):
                output.append(str(supplier[i]))
                result=result+output

        # 리스트 각 요소를 설정
        result0=result[0]
        result1=result[1]
        result2=result[2]
        
        # 리스트를 문자열로 변환
        str1 = ''.join(result0)
        str2 = ''.join(result1)
        str3 = ''.join(result2)
        
        # DB에서 답변을 출력
        sql = 'select answer from question where kind="user" order by read_count desc'
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        result=[]

        for supplier in suppliers:
            output = []
            for i in range(len(supplier)):
                output.append(str(supplier[i]))
                result=result+output

        result0=result[0]
        result1=result[1]
        result2=result[2]
        
        str4 = ''.join(result0)
        str5 = ''.join(result1)
        str6 = ''.join(result2)
        
         # 챗봇 출력 시 캐러셀 설정
        responseBody={
            "version": "2.0",
            "template": {
            "outputs": [
                {
                "carousel": {
                    "type": "listCard",
                    "items": [
                    {
                        "header": {
                            "title": str1
                        },
                        "items": [
                        {
                            "description": str4
                        }
                        ]
                    },
                    {
                        "header": {
                            "title": str2
                        },
                        "items": [
                        {
                            "description": str5
                        }
                        ]
                    },
                    {
                        "header": {
                            "title": str3
                        },
                        "items": [
                        {
                            "description": str6
                        }
                        ]
                    }
                    ]
                }
                }
            ]
            }
        }
    return responseBody