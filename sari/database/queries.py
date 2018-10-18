#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" SQL Queries - Definições de todas as queries que fazemos ao banco de dados """

# Minhas Queries
# (modificação usuário)
DB_CRIAR_USUARIO = "INSERT INTO usuarios(nome, email, senha, bio) VALUES (%s,%s,%s,%s);"
DB_EXCLUIR_USUARIO = "DELETE FROM usuarios WHERE id_usuario = %s;"
DB_EXCLUIR_USUARIO_POR_EMAIL = "DELETE FROM usuarios WHERE email = %s;"
# (modificação produto)
DB_CRIAR_PRODUTO = "INSERT INTO produtos(id_dono, nome, preco, descricao) VALUES (%s,%s,%s,%s);"
DB_EXCLUIR_PRODUTO = "DELETE FROM produtos WHERE id_produto = %s;"

# (modificar aluguel)

DB_CRIAR_ALUGUEL = "INSERT INTO aluguel(id_produto, id_alugador) VALUES (%s,%s,%s);"
DB_EXCLUIR_ALUGUEL = "DELETE FROM produtos WHERE id_produto = %s AND id_alugador = %s;"

# (busca usuario)

DB_PROCURAR_USUARIO_POR_NOME = "SELECT * FROM usuarios WHERE nome = %s;"
DB_PROCURAR_USUARIO_POR_ID = "SELECT * FROM usuarios WHERE id_usuario = %s;"
DB_PROCURAR_USUARIO_POR_EMAIL = "SELECT * FROM usuarios WHERE email = %s;"

DB_LISTAR_USUARIOS = "SELECT id_usuario,nome,email,bio FROM usuarios;"

# (busca produtos)

DB_PROCURAR_PRODUTO_POR_NOME = \
  "SELECT dono.nome, id_produto, id_dono, nome, preco, descricao, data_adicao \
   FROM produtos \
   INNER JOIN usuarios dono ON dono.id_dono = usuarios.id_usuario \
   WHERE nome = %s;"

DB_PROCURAR_PRODUTO_POR_ID = \
  "SELECT dono.nome, id_produto, id_dono, nome, preco, descricao, data_adicao \
   FROM produtos \
   INNER JOIN usuarios dono ON dono.id_dono = usuarios.id_usuario \
   WHERE id_produto = %s;"


DB_PROCURAR_PRODUTO_POR_DONO = \
  "SELECT usr.nome, id_produto, id_dono, nome, preco, descricao, data_adicao \
   FROM produtos \
   INNER JOIN usuarios usr ON usr.id_usuario = produtos.id_dono \
   WHERE id_dono = %s;"

DB_LISTAR_PRODUTOS = "Select * FROM produtos;"

# (buscar alugueis)

DB_PROCURAR_ALUGUEIS_POR_ALUGADOR = \
  "SELECT alugador.nome, id_produto, id_dono, nome, preco, descricao, data_adicao \
   FROM aluguel \
   INNER JOIN usuarios alugador ON alugador.id_usuario = aluguel.id_alugador \
   WHERE id_alugador = %s;"