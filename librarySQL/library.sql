create database if not exits libraryUsers;

drop table if exists userDb;

 create table userDb(id int,
 fname varchar(50),
 lname varchar(50), 
 numBookCheckedOut double,
 qty int,
 primary key(id));
 
 insert into userDb values(1, 'Anthony', 'Hackney', 5,0);
 insert into userDb values(2, 'Viola', 'Svern', 2,1);
 select * from userDb;