# -*- coding: UTF-8 -*-

class Calculador_de_impostos(object):

    def realiza_calcula(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print valor

if __name__ == '__main__':
    
    from orcamento import Orcamento, Item
    
    #novos imports
    from impostos import ISS, ICMS, ICPP, IKCV

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('ITEM 1', 100))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))


    calculador_de_impostos = Calculador_de_impostos()
    print 'ISS e ICMS'
    calculador_de_impostos.realiza_calcula(orcamento, ISS())
    calculador_de_impostos.realiza_calcula(orcamento, ICMS())

    # cálculo dos novos impostos
    print 'ICPP e IKCV'
    calculador_de_impostos.realiza_calculo(orcamento, ICPP()) # imprime 25.0
    calculador_de_impostos.realiza_calculo(orcamento, IKCV()) # imprime 30.0

    

