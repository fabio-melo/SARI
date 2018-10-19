from sari.infrastructure.factory.sfactory import SARIFactory

# Teste simples do funcionamento das estruturas do sistema
fabrica = SARIFactory()

meu_sistema = fabrica.criar_sari_por_argumentos("local","password")

db = meu_sistema.control
auth = meu_sistema.auth

auth.entrar('admin', 'admin')

db.criar_usuario("teste","teste@rr.com","testando","test")
db.criar_produto(4,"testado","abc","def")

