create database billdp;
use billdp;
create table bill(name varchar(30) not null,
email varchar(30) primary key not null,
pwd varchar(30) not null,
ph varchar(20)not null
);

insert into bill(name,email,pwd,ph) values("anguraj","angu@gm.com","123","8220339605");
select * from bill;