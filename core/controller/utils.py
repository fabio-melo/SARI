import re


def check_value(value, min = 3, max = 64, regex = '[A-Za-z0-9]+$'):
    """ Checagem simples, para inicialização de valores """
    if not isinstance(value, str): 
      raise Exception('ERRO: Valor recebe apenas strings')
    if not bool(re.match(regex, value)):
      raise Exception('ERRO: String possui caracteres inválidos')
    elif len(value) < min or len(value) > max:
      raise Exception(f'ERRO: String deve possuir no mínimo {min} e no máximo {max} caracteres')
    else: 
      return value