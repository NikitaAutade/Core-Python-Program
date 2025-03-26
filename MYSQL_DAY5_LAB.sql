## this all my datbases 
mysql> SHOW DATABASES;
+-------------------------+
| Database                |
+-------------------------+
| automobile_sales        |
| ecommerce               |
| food                    |
| grocery_store           |
| information_schema      |
| mysql                   |
| performance_schema      |
| practice                |
| practice1               |
| preprocess              |
| sakila                  |
| school                  |
| setup                   |
| steel                   |
| studentmanagementsystem |
| sys                     |
| vaishu                  |
| vpmsdb                  |
| world                   |
+-------------------------+
19 rows in set (0.00 sec)

# i have choose studentmanagementsystem for further process

mysql> use studentmanagementsystem;
Database changed

# i have create table stud as given column name 

mysql> create table stud(StudentID varchar(20) not null PRIMARY KEY ,FirstName varchar(20) not null,LastName varchar(20) not null, gender varchar(10) not null , age int not null , address varchar(100) not null , Phone_no int not null);
Query OK, 0 rows affected (0.03 sec)

mysql> desc stud;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| StudentID | varchar(20)  | NO   | PRI | NULL    |       |
| FirstName | varchar(20)  | NO   |     | NULL    |       |
| LastName  | varchar(20)  | NO   |     | NULL    |       |
| gender    | varchar(10)  | NO   |     | NULL    |       |
| age       | int          | NO   |     | NULL    |       |
| address   | varchar(100) | NO   |     | NULL    |       |
| Phone_no  | int          | NO   |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

#I have insert the record in stud table according to column field

mysql>insert into  stud values('1','Poonam', 'Dabhade','Female',22,'pune',87673451),
                               ('2','Vaishnavi', 'Mohite','Female',21,'chakan',89753909),
                               ('3','Asmita', 'pande','Female',23,'pimpri',88753909),
                               ('4','Aishu', 'Mule','Female',22,'bhosari',90753909),
                               ('5','Nikita', 'Autade','Female',24,'Nagar',99753909);
Query OK,5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from stud;
+-----------+-----------+----------+--------+-----+---------+----------+
| StudentID | FirstName | LastName | gender | age | address | Phone_no |
+-----------+-----------+----------+--------+-----+---------+----------+
| 1         | Poonam    | Dabhade  | Female |  22 | pune    | 87673451 |
| 2         | Vaishnavi | Mohite   | Female |  21 | chakan  | 89753909 |
| 3         | Asmita    | pande    | Female |  23 | pimpri  | 88753909 |
| 4         | Aishu     | Mule     | Female |  22 | bhosari | 90753909 |
| 5         | Nikita    | Autade   | Female |  24 | Nagar   | 99753909 |
+-----------+-----------+----------+--------+-----+---------+----------+
5 rows in set (0.00 sec)

# i have applied the order by caluse on lastname and retrieve the data from stud table in ascending order 

mysql> SELECT StudentID, FirstName, LastName,gender,age, address, Phone_no from stud ORDER BY LastName ASC;
+-----------+-----------+----------+--------+-----+---------+----------+
| StudentID | FirstName | LastName | gender | age | address | Phone_no |
+-----------+-----------+----------+--------+-----+---------+----------+
| 5         | Nikita    | Autade   | Female |  24 | Nagar   | 99753909 |
| 1         | Poonam    | Dabhade  | Female |  22 | pune    | 87673451 |
| 2         | Vaishnavi | Mohite   | Female |  21 | chakan  | 89753909 |
| 4         | Aishu     | Mule     | Female |  22 | bhosari | 90753909 |
| 3         | Asmita    | pande    | Female |  23 | pimpri  | 88753909 |
+-----------+-----------+----------+--------+-----+---------+----------+
5 rows in set (0.00 sec)


# this lab2 solution 
# i have count the number of student according to gender for that i have used the group by clause and applied it on gender .

mysql> select gender , count(StudentID) as StudentCount from stud group by gender;
+--------+--------------+
| gender | StudentCount |
+--------+--------------+
| Female |            5 |
+--------+--------------+
1 row in set (0.00 sec)


####   OR SOLUTION FOR LAB 2   ####

mysql> select gender , count(*) as StudentCount from stud group by gender;
+--------+--------------+
| gender | StudentCount |
+--------+--------------+
| Female |            5 |
+--------+--------------+
1 row in set (0.00 sec)

mysql>