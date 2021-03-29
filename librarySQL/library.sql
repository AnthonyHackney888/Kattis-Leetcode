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
 
 drop table if exists libEmployee;
 
 create table libEmployee(
	empID int, 
	fname varchar(50),
	lname varchar(50), 
	HoursLogged double,
	HoursScheduled double
	primary key(empID));
	
insert into libEmployee values(1, 'Anthony','notHackney',20.5,33.0);
select * from libEmployee;

drop table if exists libManager;
 
 create table libManager(
	managerID int, 
	fname varchar(50),
	lname varchar(50), 
	HoursLogged double,
	HoursScheduled double
	primary key(managerID));
	

insert into libManager values(1,'Manager', 'Hackney',15,45);
select * from libManager;
