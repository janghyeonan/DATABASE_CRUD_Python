#-*- coding:utf-8 -*-
import pymysql
import time

#mysql insert문 순서대로 추출된 로또번호를 DB에 저장함.

#시작시간
start_time = time.time()

#DB 연결
conn = pymysql.connect(host='localhost', user='root', password='암호', db='데이터베이스', charset='utf8')
curs = conn.cursor()

#쿼리문
sql = """insert into 테이블(title, content, 1t, 2t, 3t, 4t, 5t, 6t) values (%s, %s, %s, %s, %s, %s, %s, %s)"""

a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 0
h = 0
l = [0, 0, 0, 0, 0, 0]
j = [0, 0, 0, 0, 0, 0]
for a in range(1, 46):
    for b in range(2, 46):        
            for c in range(3, 46):
                for d in range(4, 46):
                    for e in range(5, 46):
                        for f in range(6, 46):
                            if a != b and a != c and a != d and a != e and a != f:
                                if b != c and b != d and b != e and b != f:
                                    if c != d and c != e and c != f:
                                        if d != e and d != f:
                                            if e != f:
                                                g = g + 1
                                                l[0] = str(a)
                                                l[1] = str(b)
                                                l[2] = str(c)
                                                l[3] = str(d)
                                                l[4] = str(e)
                                                l[5] = str(f)
                                                l.sort()                                                
                                                if j != l:                                                    
                                                    j[0] = str(a)
                                                    j[1] = str(b)
                                                    j[2] = str(c)
                                                    j[3] = str(d)
                                                    j[4] = str(e)
                                                    j[5] = str(f)                                                                                                      
                                                    print("저장되는 l값", l[0], l[1], l[2], l[3], l[4], l[5])
                                                    chong = l[0]+", "+l[1]+", "+l[2]+", "+l[3]+", "+l[4]+", "+l[5]
                                                    #입력되는 값
                                                    curs.execute(sql, (str(g) + '번째 조합', str(chong), l[0], l[1], l[2], l[3], l[4], l[5]  ))
                                                    conn.commit()                                                    
                                                    print("==[", str(g), "]===========f값은 : ", str(f),)
                                                    time.sleep(2)
                                                  
       
print("실행 수 : " + str(g) + "번");
#연결 종료
conn.close()


#걸린시간 체크
end_time = time.time()
count_time = end_time - start_time

print("걸린시간 : " + str(count_time).split('.')[0] + " sec")