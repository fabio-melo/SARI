from sari.infrastructure.driver.startup import SistemaSARI


# Teste simples do funcionamento das estruturas do sistema

meu_sistema = SistemaSARI()
meu_sistema.iniciar_sistema("local","password")

db = meu_sistema.control
auth = meu_sistema.auth

auth.entrar('admin', 'admin')

db.criar_usuario("teste","teste@rr.com","testando","test")
db.criar_produto(4,"testado","abc","def")
