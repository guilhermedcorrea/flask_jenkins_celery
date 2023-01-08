CREATE DATABASE teste;
USE teste;

CREATE TABLE User(

    idusuario SERIAL primary key,
    nome varchar(400),
    sobrenome varchar(400)

);