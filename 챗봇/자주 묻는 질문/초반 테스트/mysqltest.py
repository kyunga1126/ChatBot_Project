import MySQLdb

# mysql(3306) or mariadb(3307) 연결
conn = MySQLdb.connect(host="3.36.9.161", port=52374, db='db01', user='myuser1', password='1234')
# print(dir(conn))
#print()
# conn.cursor?
cursor = conn.cursor()
# print(dir(cursor))

print()

# sql
sql = 'show databases'
cursor.execute(sql)
suppliers = cursor.fetchall()

for supplier in suppliers:
    output = []
    for i in range(len(supplier)):
        output.append(str(supplier[i]))
    print(output)

cursor.close()
conn.close()    