drop table if exists users;
create table users (
  user_id integer primary key autoincrement,
  username text not null,
  password text not null,
  theta real not null DEFAULT 0,
  k real not null DEFAULT 0
);

drop table if exists items;
create table items (
  item_id integer primary key,
  theta real not null DEFAULT 0,
  k real not null DEFAULT 0
);

drop table if exists events;
create table events (
  event_id integer primary key autoincrement,
  event_date date not null,
  user_id integer not null,
  item_id integer not null,
  theta_before real not null,
  theta_change real not null,
  theta_after real not null,
  answered integer not null,
  correct_answer boolean not null,
  k real not null DEFAULT 0
);