from sari.infrastructure.reports.abstrato import RelatorioAbstract
import csv
class RelatorioCSV(RelatorioAbstract):

  def gerar_relatorio_de_usuario(self): 
    mock_text = """
    produto, alugador, data
    carro, joão, 2/10/2018
    casa, joão, 23/10/2019
    """
    with open('relatorio.csv','r') as rel:
      rel.write(mock_text)


  def gerar_relatorio_de_sistema(self): 
    mock_text = """
    eventos, usuario, horario, data
    entrada, joao@j.com, 22h40, 23/05/2018
    saida, nando@nan.com, 23h10, 29/10/2018
    instabilidade, NONE, 23h50, 30/10/2018
    """
    with open('relatorio_sistema.csv','r') as rel:
      rel.write(mock_text)