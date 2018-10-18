"""from core.controller.db_logic import *
if __name__ == '__main__':
  x = MariaDBConnector()
  x.criar_usuario("euZIN", "cool@woer.com","massa","boy")
  #x.excluir_usuario("cool@woer.com")
  #x.excluir_usuario("cool@woer.com")
  x.criar_produto('1', 'coolestshit','2394', 'a cool shit')
"""

from sari.controller.control.run_local import LocalController

lc = LocalController()

lc.carregar_arquivo("usuario.txt","produto.txt", "aluguel.txt")

print(lc.usuarios)


"""
lc.criar_usuario("joao","err@rr.com","cool","eu")
lc.criar_usuario("io3o","err@rr.com","cool","eu")
lc.criar_usuario("roufas","err@rr.com","cool","eu")
lc.criar_usuario("cmai","err@rr.com","cool","eu")
print(lc.usuarios)

lc.salvar_arquivo("usuario.txt", "produto.txt","aluguel.txt")
"""