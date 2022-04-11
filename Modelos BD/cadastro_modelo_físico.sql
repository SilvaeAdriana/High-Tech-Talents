CREATE DATABASE IF NOT EXISTS cadastro_aluguel_imoveis;
USE cadastro_aluguel_imoveis;

CREATE TABLE imovel(
	id INT(100) NOT NULL AUTO_INCREMENT,
	logradouro VARCHAR(45) NOT NULL UNIQUE,
	cep INT(8) NOT NULL UNIQUE,
	bairro VARCHAR(45) NOT NULL UNIQUE,
	cidade VARCHAR(45) NOT NULL UNIQUE,
	PRIMARY KEY(id)
)DEFAULT CHARSET=utf8;


CREATE TABLE aluguel(
	id INT(100) NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(id),
	CONSTRAINT fk_aluguel_id_imovel FOREIGN KEY (id_imovel) REFERENCES imovel(id),
	CONSTRAINT fk_aluguel_id_inquilino FOREIGN KEY (id_inquilino) REFERENCES inquilino(id)
)DEFAULT CHARSET=utf8;


CREATE TABLE inquilino(
	id INT(100) NOT NULL AUTO_INCREMENT,
	nome VARCHAR(45) NOT NULL UNIQUE,
	telefone VARCHAR(11) NOT NULL,
	email VARCHAR(45) NOT NULL,
	data_nascimento DATE NOT NULL UNIQUE,
	PRIMARY KEY(id),
	CONSTRAINT fk_inquilino_id_imovel FOREIGN KEY (id_imovel) REFERENCES imovel(id)
)DEFAULT CHARSET=utf8;


CREATE TABLE proprietario(
	id INT(100) NOT NULL AUTO_INCREMENT,
	nome VARCHAR(45) NOT NULL UNIQUE,
	telefone VARCHAR(11) NOT NULL,
	email VARCHAR(45) NOT NULL,
	data_nascimento DATE NOT NULL UNIQUE,
	PRIMARY KEY(id),
	CONSTRAINT fk_proprietario_id_imovel FOREIGN KEY (id_imovel) REFERENCES imovel(id)
)DEFAULT CHARSET=utf8;


CREATE TABLE corretor(
	id INT(100) NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(id),
	CONSTRAINT fk_corretor_id_imovel FOREIGN KEY (id_imovel) REFERENCES imovel(id)
)DEFAULT CHARSET=utf8;


CREATE TABLE contrato(
	id INT(100) NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(id),
	CONSTRAINT fk_contrato_id_aluguel FOREIGN KEY (id_aluguel) REFERENCES aluguel(id)
)DEFAULT CHARSET=utf8;