# -*- coding: UTF-8 -*-

from impostos import ICMS, ISS

class Calculador_de_impostos(object):

    def realizar_calculo(self, orcamento, imposto):
        print imposto.calcula(orcamento)

if __name__ == '__main__':

    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculadora_de_impostos = Calculador_de_impostos()
    
    calculadora_de_impostos.realizar_calculo(orcamento, ICMS())
    calculadora_de_impostos.realizar_calculo(orcamento, ISS())
