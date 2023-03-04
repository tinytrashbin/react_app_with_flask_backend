-- Database:

DROP TABLE users;

CREATE table users ( id serial primary key, name varchar(100), phone_number varchar(20),  email varchar(100), password varchar(100), profile_pic varchar(1000), role varchar(10));

INSERT into users (name, email, password, role) values ('Admin', 'admin@admin.com', 'password', 'ADMIN');
