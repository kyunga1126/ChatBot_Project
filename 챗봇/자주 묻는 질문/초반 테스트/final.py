import MySQLdb
from flask import Flask, request
import sys


# mysql(3306) or mariadb(3307) 연결
conn = MySQLdb.connect(host="localhost", port=3306, db='chatbot', user='root', password='1234')
#print(dir(conn))
#print()
# conn.cursor?
cursor = conn.cursor()
#print(dir(cursor))
#print()

"""
sql = 'select group_concat(concat(id,"-",count))from test'
cursor.execute(sql)
suppliers = cursor.fetchall()

for supplier in suppliers:
    output = []
    for i in range(len(supplier)):
        output.append(str(supplier[i]))
    print(output)


# sql
sql = 'select * from test order by read_count desc'
cursor.execute(sql)
suppliers = cursor.fetchall()

for supplier in suppliers:
    output = []
    for i in range(len(supplier)):
        output.append(str(supplier[i]))
    print(output)
"""  

sql = 'select ask from customer_ask order by read_count desc'
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
print('사이트에서 자주 묻는 질문은 %s 입니다.'%str2)

cursor.close()
conn.close()    

# %%writefile .\hello_kakao_skill\app.py
# 1. 스킬서버예제(1)

app = Flask(__name__)

# 1) 카카오톡 텍스트형태의 response
@app.route('/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json()
    # print(body)

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "사이트에서 자주 묻는 질문은 "+str2+"입니다."
                    }
                }
            ]
        }
    }

    return responseBody
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80) # web server
