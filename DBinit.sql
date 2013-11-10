create ROLE catch22;
alter ROLE catch22 LOGIN password 'That is some catch';
create database catch22;
grant all ON DATABASE catch22 TO catch22;
alter ROLE catch22 CREATEDB;
alter DATABASE catch22 OWNER to catch22;