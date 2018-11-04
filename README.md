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
|   |   ├── command # comandos
|   |   |   ├── commando.py # comandos base e concretos
|   |   |   ├── interface.py # recebe comandos em string
|   |   |   ├── invoker.py # invocador de comandos
|   |   ├── control # persistencia e processamentogeral
|   |   |   ├── localstorage.py # Persistencia Local
|   |   |   ├── mariadb.py #Persistencia em Banco de Dados
|   |   |   ├── singleton.py # Classe-Base Singleton
|   |   |   ├── template.py # Padrão Template
|   |   ├── factory # fabrica da aplicação
|   |   |   ├── sistema.py # inicializador do sistema SARI
|   |   |   ├── sfactory.py # fabrica do SARI
|   |   ├── memento # mementos
|   |   |   ├── snapshot.py # classe que armazena mementos/estados
|   |   ├── observer # observadores
|   |   |   ├── observer.py # instancias de observador
|   |   |   ├── receiver.py # receptor a ser instanciado
|   |   ├── reports # gerador de relatorios
|   |   |   ├── abstrato.py # abstração dos relatorios
|   |   |   ├── geradorCSV.py # gera o relatorio em formato CSV
|   |   |   ├── geradorTXT.py # gera o relatorio em texto puro
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
├── executar.py # teste das funcionalidades do SARI
├── commandos.txt # aonde os comandos serão escritos

```

## Padrões Utilizados
* Command
* Façade
* Memento
* Observer
* Singleton 
* Strategy
* Template
* Factory


## Testes
rodar o executar.py disponível 

## Dependências
```text
* Para o banco de dados: MariaDB e mysqlclient: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

```
