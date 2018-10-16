from core.controller.db_logic import *
if __name__ == '__main__':
  x = MariaDBConnector()
  x.criar_usuario("euZIN", "cool@woer.com","massa","boy")
  #x.excluir_usuario("cool@woer.com")
  #x.excluir_usuario("cool@woer.com")
  x.criar_produto('1', 'coolestshit','2394', 'a cool shit')
