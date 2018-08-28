# -*- coding: UTF-8 -*-
#novos imports
from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print valor

if __name__ == '__main__':
    
    from orcamento import Orcamento, Item
    
    #novos imports
    from impostos import ISS, ICMS, ICPP, IKCV

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))


    calculador_de_impostos = Calculador_de_impostos()
    print 'ISS e ICMS'
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())

    print 'ISS_com_ICMS'
    # veja, não é necessária mais uma classe. Imposto recebe outro em seu construtor
    ISS_com_ICMS = ISS(ICMS())
    calculador_de_impostos.realiza_calculo(orcamento, ISS_com_ICMS) # imprime 80

    # cálculo dos novos impostos
    print 'ICPP e IKCV'
    calculador_de_impostos.realiza_calculo(orcamento, ICPP()) # imprime 25.0
    calculador_de_impostos.realiza_calculo(orcamento, IKCV()) # imprime 30.0

    print 'ICPP_com_IKCV'
    # veja, não é necessária mais uma classe. Imposto recebe outro em seu construtor
    ICPP_com_IKCV = ICPP(IKCV())
    calculador_de_impostos.realiza_calculo(orcamento, ICPP_com_IKCV) # imprime 55.0
