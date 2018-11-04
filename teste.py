from sari.infrastructure.factory.sfactory import SARIFactory #pylint: disable=E0401,E0611
from sari.infrastructure.command.interface import CommandInterface #pylint: disable=E0401,E0611
from sari.infrastructure.observer.observer import MainObserver #pylint: disable=E0401,E0611

# Teste simples do funcionamento das estruturas do sistema
fabrica = SARIFactory()

meu_sistema = SARIFactory().criar_sari_por_argumentos("local","password")

sari_com = CommandInterface(meu_sistema)

COMANDO = ["CRIARUSUARIO teste teste@teste.com testando test",
           "REMOVERUSUARIO teste@teste.com"
           ]

COMMANDO_LIST = []

for x in COMANDO: COMMANDO_LIST.append(x.split())

# Nossos Observadores
observador = MainObserver("Comando", [sari_com, sari_com.invoker])
observador = MainObserver("Controle", [meu_sistema.control])
observador = MainObserver("Autenticacao", [meu_sistema.auth])

for x in COMMANDO_LIST: sari_com.add(x)

sari_com.rodar()

"""
db = meu_sistema.control
auth = meu_sistema.auth

auth.entrar('admin', 'admin')

db.criar_usuario("teste","teste@rr.com","testando","test")
db.criar_produto(4,"testado","abc","def")

"""