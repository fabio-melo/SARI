# SARI
SARI - Sistema de Alocação, Reserva e Inclusão.

Projeto da Disciplina de Métodos de Projeto de Software.


## Hierarquia de Arquivos
```python
.
├── sari
|   ├── configuration
|   |   ├── config.py # configurações do flask e do bd
|   └── database
|   |   ├── schema.sql # esquema do banco de dados
|   |   ├── queries.py # queries em SQL
|   └── infrastructure
|   |   ├── auth # autenticação
|   |   |   ├── context.py # contexto da estratégia
|   |   |   ├── oauth.py # MOCK - autenticação oauth 
|   |   |   ├── password.py # MOCK -- autenticação senha
|   |   |   ├── strategies.py # interface doStrategy 
|   |   ├── control # persistencia e processamentogeral
|   |   |   ├── localstorage.py # Persistencia Local
|   |   |   ├── mariadb.py #Persistencia em Banco de Dados
|   |   |   ├── singleton.py # Classe-Base Singleton
|   |   |   ├── template.py # Padrão Template
|   |   ├── factory # fabrica da aplicação
|   |   |   ├── sistema.py # inicializador do sistema SARI
|   |   |   ├── sfactory.py # fabrica do SARI
|   |   ├── utils # utilidades simples
|   |   |   ├── checking.py # validação de strings 
|   └── models # modelo dos objetos utilizados
|   |   ├── aluguel.py
|   |   ├── produto.py
|   |   ├── usuario.py
|   └── storage # armazenamento em arquivos binários
|   |   ├── aluguel.bin
|   |   ├── produto.bin
|   |   ├── usuario.bin
├── readme.md #este arquivo
├── teste.py # teste das funcionalidades do SARI

```

## Padrões Utilizados
* Façade
* Singleton 
* Strategy
* Template
* Factory


## TO-DO
* Interface Gráfica
* Web-design
* Visualizações do Flask

## Dependências
```text
* Para o banco de dados: MariaDB e mysqlclient: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python

```
