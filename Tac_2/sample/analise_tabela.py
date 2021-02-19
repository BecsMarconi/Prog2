"""
Author: Rebeca Marconi Pereira Raboeira
Date: 13/02/2021
Version: 9.0
Last update: 18/02/2021
"""

import estatisticas_script

def main():
    maximo = estatisticas_script.Valor_Maximo()
    print('Máximo: {}'.format(maximo))

    minimo = estatisticas_script.Valor_Minimo()
    print('Mínimo: {}'.format(minimo))

    media = estatisticas_script.Media()
    print('Média: {}'.format( media))

    razao = estatisticas_script.Razao()
    print('Razão: {}'.format(razao))

    print("Encerrando...")
    pass

if __name__ == "__main__":
    main()