#- 파이썬 PYMYSQL모듈 사용하여 CURD 해보기

##1. 도커설치

##2. 명령어 실행
>: 도커 컨테이너 생성 : # docker run --name r_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:5.6

>: 컨테이너 생성 후 컨테이너 접속 :  # docker exec -it r_mysql bash

>: mysql 접속 :  # mysql -u root -p

>: 패스워드입력

>: 어디서든 접속가능 설정 :  MYSQL> GRANT ALL PRIVILEGES ON *.* TO ‘root’@‘%’;

>: 적용 : MYSQL> FLUSH PRIVILEGES;


##3. 외부 접속
>: 0.0.0.0:3309로 접속 계정은 root 비번은 비번으로

##4. DATABASE생성
>: MYSQL>CREATE DATABASE <데이터베이스명>

##5. 테이블생성 
>: MYSQL> CREATE TABLE <테이블명> ~~

##6. Pymysql 모듈 사용
>: r_pymysql.py 참고


##r_pymysql.py
>: 참고용
