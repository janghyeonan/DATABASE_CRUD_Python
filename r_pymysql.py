#mysql selet문
import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='pass', db='database', charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
sql = "select * from test"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows
print(rows[0][0])  # 첫번째 row

#insert
insert_sql = """insert into test(name) values (%s)"""
curs.execute(insert_sql, '홍길동')
conn.commit()

#update
update_sql = """update test set name = '차길동' where id= '2'"""
curs.execute(update_sql)
conn.commit()

#delete
delete_sql = "delete from test where id=3"
curs.execute(delete_sql)
conn.commit()
 
# Connection 닫기
conn.close()