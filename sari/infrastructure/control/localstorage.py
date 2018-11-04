from sari.infrastructure.control.template import ControlAbstract
from sari.infrastructure.control.singleton import Singleton
from sari.model.usuario import Usuario
from sari.model.aluguel import Aluguel
from sari.model.produto import Produto
from sari.infrastructure.observer.receiver import Receiver

import pickle

class LocalController(ControlAbstract,Singleton):

  def __init__(self):
    self.receiver = Receiver()
    self.usuarios = {}
    self.produtos = {}
    self.alugueis = {}
    self.prox_usuario = 0
    self.prox_produto = 0
    self.prox_aluguel = 0

  def inicializar_sistema(self):
    ## no caso do controlador local, única necessidade é carregar o arquivo
    self.carregar_arquivo('sari/storage/usuario.bin','sari/storage/produto.bin', 'sari/storage/aluguel.bin')

  def notificar_admin(self):
    self.receiver.notificar_todos("SISTEMA SARI INICIADO - MODO ARMAZENAMENTO LOCAL")

  def finalizar_sistema(self):
    self.salvar_arquivo('sari/storage/usuario.bin','sari/storage/produto.bin', 'sari/storage/aluguel.bin')

  def notificar_admin_final(self):
    self.receiver.notificar_todos("SISTEMA SARI FINALIZADO - MODO ARMAZENAMENTO LOCAL")


  def carregar_arquivo(self, a_usuarios, a_produtos, a_alugueis):
    with open(a_usuarios,'rb') as a_usuarios:
      self.usuarios = pickle.load(a_usuarios)
    with open(a_produtos,'rb') as a_produtos:
      self.produtos = pickle.load(a_produtos)
    with open(a_alugueis,'rb') as a_alugueis:
      self.alugueis = pickle.load(a_alugueis)
    self.prox_usuario = len(self.usuarios)
    self.prox_produto = len(self.produtos)
    self.prox_aluguel = len(self.alugueis)

  def salvar_arquivo(self, a_usuarios, a_produtos, a_alugueis):
    with open(a_usuarios,'wb') as a_usuarios:
      pickle.dump(self.usuarios, a_usuarios)
    with open(a_produtos,'wb') as a_produtos:
      pickle.dump(self.produtos, a_produtos)
    with open(a_alugueis,'wb') as a_alugueis:
      pickle.dump(self.alugueis, a_alugueis)

  def criar_usuario(self, nome, email, senha, bio):
    id_usuario = self.prox_usuario
    self.prox_usuario += 1
    
    usr = Usuario(id_usuario, email, nome, senha, bio)
    self.usuarios[id_usuario] = usr
    self.receiver.notificar_todos(f"ID: {id_usuario} Usuario {nome} Criado")
    
  
  def excluir_usuario(self, email):
    try:
      for key, value in self.usuarios.items():
        if value.email == email:
          self.usuarios.pop(key)
    except:
      self.receiver.notificar_todos(f'Usuario {email} não encontrado')

  def criar_produto(self, id_dono, nome, preco, descricao):
    id_produto = self.prox_produto
    self.prox_produto += 1
    
    prod = Produto(id_produto, id_dono, nome, preco, descricao)
    self.produtos[id_produto] = prod
    self.receiver.notificar_todos(f'PRODUTO {id_produto}: {nome} CRIADO')
      
  def excluir_produto(self, id_produto): 
    try:
      if id_produto in self.produtos.keys():
        self.usuarios.pop(id_produto)
    except:
      self.receiver.notificar_todos(f'Produto {id_produto} não encontrado')

  def criar_aluguel(self, id_produto, id_alugador, data_aluguel): 
    id_trans = self.prox_aluguel
    self.prox_aluguel += 1
    alg = Aluguel(id_trans,id_produto, id_alugador, data_aluguel)
    self.alugueis[id_trans] = alg
    self.receiver.notificar_todos(f'ALUGUEL {id_trans} {id_alugador} CRIADO')


  def excluir_aluguel(self, id_trans): 
    try:
      if id_trans in self.alugueis.keys():
        self.alugueis.pop(id_trans)
    except:
      self.receiver.notificar_todos(f'Aluguel {id_trans} não encontrado')
