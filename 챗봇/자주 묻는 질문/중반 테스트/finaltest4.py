"""
# 리스트형 적용 전 최종본

# mysqlclient 설치하여 MySQLdb 호출
import MySQLdb
import sys

# flask에 있는 request와 Bluepoint 호출
from flask import Blueprint, request

# MySQL 객체 등록
conn = MySQLdb.connect(host="localhost", port=3306, db='chatbot', user='root', password='1234')
cursor = conn.cursor()

# 블루프린트 객체 등록
bp = Blueprint('final3', __name__, url_prefix='/')

# 블루프린트가 적용됨에 따른 url 설정
@bp.route('/final', methods=['POST'])
def questionstart():
    # 카카오챗봇에서 발화문 가져오기
    body = request.get_json()
    body=body['userRequest']['utterance']
    #print(body) 
    
    # 챗봇 입력 결과가 시작일 때
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
    return responseBody

@bp.route('/question/rest', methods=['POST'])
def final3():
    body = request.get_json()
    body=body['userRequest']['utterance']
    
    if body=="게임친구":
        sql = 'select ask from question where kind="friend" order by read_count desc'
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
        
        # DB에서 질문을 출력
        str1 = ''.join(result0)
        str2 = ''.join(result1)
        str3 = ''.join(result2)
        
        sql = 'select answer from question where kind="friend" order by read_count desc'
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

    elif body=="계정":
        sql = 'select ask from question where kind="user" order by read_count desc'
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
        
        str1 = ''.join(result0)
        str2 = ''.join(result1)
        str3 = ''.join(result2)
        
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

    elif body=="기타":
        sql = 'select ask from question where kind="other" order by read_count desc'
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
        
        str1 = ''.join(result0)
        str2 = ''.join(result1)
        str3 = ''.join(result2)
        
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

    # 카카오챗봇이나 파일에 문제있을 경우
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
    return responseBody """