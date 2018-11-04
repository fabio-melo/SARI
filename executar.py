from sari.infrastructure.factory.sfactory import SARIFactory #pylint: disable=E0401,E0611
from sari.infrastructure.command.interface import CommandInterface #pylint: disable=E0401,E0611
from sari.infrastructure.observer.observer import MainObserver #pylint: disable=E0401,E0611

# Teste simples do funcionamento das estruturas do sistema
fabrica = SARIFactory()

meu_sistema = SARIFactory().criar_sari_por_argumentos("local","password")

sari_com = CommandInterface(meu_sistema)

command_list = []
with open("comandos.txt",'r') as comandos:
  for x in comandos:
    command_list.append(x.rstrip().split())

print(command_list)

# Nossos Observadores
observador = MainObserver("Comando", [sari_com, sari_com.invoker])
observador = MainObserver("Controle", [meu_sistema.control])
observador = MainObserver("Autenticacao", [meu_sistema.auth])

for x in command_list: sari_com.add(x)

sari_com.rodar()