create database temp_cus;
use temp_cus;

create table temp_stock(pid integer primary key not null,proname varchar(20),qty varchar(20),
rate float(20),totalrate float(20));

insert into temp_stock(pid,proname,qty,rate,totalrate) values(1,'T-shirt', 5, 12.99, 65.99);

select * from temp_stock;

