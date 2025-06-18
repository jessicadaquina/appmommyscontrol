use mommy;
show tables;
to_do_list
create table if not exists to_do_list(
cpf int primary key,
task_named varchar(150) not null,
task_completed boolean default 0,
task_not_completed boolean default 0
);
