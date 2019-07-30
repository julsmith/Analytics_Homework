DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
   emp_no INT NOT NULL,
   birth_date DATE NOT NULL,
   first_name VARCHAR(40) NOT NULL,
   last_name VARCHAR(40) NOT NULL,
   gender VARCHAR(1) NOT NULL,
   hire_date DATE NOT NULL,
   PRIMARY KEY (emp_no)
);

DROP TABLE IF EXISTS dept_emp;
CREATE TABLE dept_emp(
emp_no INT NOT NULL,
dept_no VARCHAR(10) NOT NULL,
from_date DATE NOT NULL,
to_date DATE NOT NULL,
PRIMARY KEY (emp_no, dept_no)
);

DROP TABLE IF EXISTS dept_manager;
CREATE TABLE dept_manager(
dept_no VARCHAR(10) NOT NULL,
emp_no INT NOT NULL,
from_date DATE NOT NULL,
to_date DATE NOT NULL,
PRIMARY KEY (emp_no, dept_no )
);

DROP TABLE IF EXISTS departments;
CREATE TABLE departments(
dept_no VARCHAR(4) NOT NULL,
dept_name VARCHAR(40),
PRIMARY KEY (dept_no)
);

DROP TABLE IF EXISTS salaries;
CREATE TABLE salaries(
emp_no INT NOT NULL,
salary INT NOT NULL,
from_date DATE NOT NULL,
to_date DATE NOT NULL,
PRIMARY KEY (emp_no)
);

DROP TABLE IF EXISTS titles;
CREATE TABLE titles(
emp_no INT NOT NULL,
title VARCHAR(30) NOT NULL,
from_date DATE NOT NULL,
to_date DATE NOT NULL,
PRIMARY KEY (emp_no)
);











