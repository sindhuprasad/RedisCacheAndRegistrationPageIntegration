drop table if exists user;

create table user (
  id integer primary key AUTO_INCREMENT,
  firstname VARCHAR(100) not null,
  lastname VARCHAR(100) not null,
  email VARCHAR(100), 
  ssn VARCHAR(100),
  phone VARCHAR(100) ,
  url VARCHAR(200),
  password VARCHAR(50),
  passwordStrngth VARCHAR(100),
  dob VARCHAR(100),
  dobWithTime VARCHAR(100),
  creditcardnumber VARCHAR(100)
);
