/* GERAÇÃO DO BANCO DE DADOS DO SISTEMA SARI */

SET UNIQUE_CHECKS=0;
SET FOREIGN_KEY_CHECKS=0;

DROP DATABASE IF EXISTS sari;
CREATE DATABASE sari;
USE sari;

/* Usuario = Entidade */

DROP TABLE IF EXISTS usuario;

CREATE TABLE usuarios(
	id_usuario INT UNSIGNED NOT NULL AUTO_INCREMENT,
	nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
 	senha VARCHAR(255) NOT NULL,
	bio TEXT,
	foto VARCHAR(255),
	data_criacao TIMESTAMP NOT NULL,
	PRIMARY KEY(id_usuario),
	UNIQUE(email)
);


/* Produto = Entidade */

DROP TABLE IF EXISTS produtos;

CREATE TABLE produtos(
	id_produto INT UNSIGNED NOT NULL AUTO_INCREMENT,
	id_dono INT UNSIGNED NOT NULL,
	nome VARCHAR(255),
	preco VARCHAR(255),
	descricao TEXT,
	data_adicao TIMESTAMP NOT NULL,
	PRIMARY KEY(id_produto),
	FOREIGN KEY(id_dono) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
	UNIQUE(nome_grupo)
);

/* Relacionamento: Produto -> Usuario */


DROP TABLE IF EXISTS aluguel;

CREATE TABLE aluguel(
	id_produto INT UNSIGNED NOT NULL,
	id_alugador INT UNSIGNED NOT NULL,
	data_aluguel TIMESTAMP NOT NULL,
	PRIMARY KEY(id_produto, id_alugador),
	FOREIGN KEY(id_produto) REFERENCES produtos(id_produto) ON DELETE CASCADE, 
	FOREIGN KEY(id_alugador) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);


SET FOREIGN_KEY_CHECKS=1;
SET UNIQUE_CHECKS=1;