from core.controller.db_logic import *
if __name__ == '__main__':
  x = MariaDBConnector()
  x.criar_usuario("euZIN", "cool@woer.com","massa","boy")
  print(x.__dict__)