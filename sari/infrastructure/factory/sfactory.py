from sari.infrastructure.factory.sistema import SistemaSARI

class SARIFactory(object):
  def criar_sari_por_configuracao(self, config):
    """Recebe um dicionario com os atributos {'control': 'db', 'auth': 'oauth'}"""
    try:
      if 'control' in config.keys() and 'auth' in config.keys():
        control, auth = config['control'], config['auth']
        sistema = SistemaSARI(control, auth)
        print(f"SARIFACTORY - Objeto Fabricado - {config['control']}, {config['auth'] }")
        return sistema
      else:
        raise Exception("argumentos faltando, não pode criar o objeto")
    except Exception as e:
      print(e)


  def criar_sari_por_argumentos(self, control, auth):
    try:
      sistema = SistemaSARI(control, auth)
      return sistema
    except Exception as e:
      print(e)