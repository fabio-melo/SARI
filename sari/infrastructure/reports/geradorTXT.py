from sari.infrastructure.reports.abstrato import RelatorioAbstract

class RelatorioTXT(RelatorioAbstract):

  def gerar_relatorio_de_usuario(self): 
    mock_text = """
    RELATORIO DE USUARIO DO SISTEMA.
    PRODUTOS ALUGADOS: 12345
    DINHEIRO ARRECADADO: R$ 123,45

    PRODUTO TV ALUGADO A USUARIO JOÃO POR R$40,00
    PRODUTO CARRO ALUGADO A USUARIO MARIA POR R$80,00
    PRODUTO RÁDIO ALUGADO A USUARIO EDNALDO POR R$10,00    

    """
    with open('relatorio.txt','r') as rel:
      rel.write(mock_text)


  def gerar_relatorio_de_sistema(self): 
    mock_text = """
    RELATORIO ADMINISTRATIVO DO SISTEMA.
    PRODUTOS ALUGADOS: 9999999
    DINHEIRO TOTAL CIRCULADO: R$ 55.123,45

    -> LOG DE PRODUTOS
    USUARIO X
    PRODUTO TV ALUGADO A USUARIO JOÃO POR R$40,00
    PRODUTO CARRO ALUGADO A USUARIO MARIA POR R$80,00
    PRODUTO RÁDIO ALUGADO A USUARIO EDNALDO POR R$10,00    

    """
    with open('relatorio_sistema.txt','r') as rel:
      rel.write(mock_text)