# -*- coding: UTF-8 -*-
def imprime(frase):
    print frase

def imprime_com_destaque(funcao):
    def wrapper(frase):
        print '****'
        funcao(frase)
        print '****'
    return wrapper


@imprime_com_destaque
def imprime(frase):
    print frase

if __name__ == '__main__':

    imprime('Olá')
