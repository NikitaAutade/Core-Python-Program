# Q1) You have two tables, employees and departments. Retrieve a list of employees along with their department names using an inner join. 


create database DYPatil;
use DYPatil;
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (department_id, department_name) VALUES 
(1, 'HR'),
(2, 'Finance'),
(3, 'IT'),
(4, 'Marketing');

INSERT INTO employees (employee_id, employee_name, department_id) VALUES 
(101, 'Alice', 1),
(102, 'Bob', 2),
(103, 'Charlie', 3),
(104, 'David', 4),
(105, 'Eve', 2);


SELECT 
    e.employee_id, 
    e.employee_name, 
    d.department_name
FROM employees e
INNER JOIN departments d 
ON e.department_id = d.department_id;

#OUTPUT :
# This INNER JOIN ensures that only employees with a valid department ID in the departments table are included in the result
employee_id	employee_name	department_name
101	             Alice         	HR
102	              Bob	       Finance
103	            Charlie       	IT
104	             David	      Marketing
105	             Eve	       Finance

#Q2) you have two tables, employees and departments. Retrieve a name & department_name  using an left  join ?

SELECT 
    e.employee_name, 
    d.department_name
FROM employees e
LEFT JOIN departments d 
ON e.department_id = d.department_id;

#A LEFT JOIN returns all records from the employees table.
#If an employee has a matching department_id in the departments table, the department name is shown.
#If an employee does not have a corresponding department, NULL is displayed for department_name

#OUTPUT : 
employee_name	department_name
Alice	             HR
Bob	              Finance
Charlie	             IT
David	          Marketing
Eve             	Finance
John                 NULL