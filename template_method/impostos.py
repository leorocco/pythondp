# -*- coding: UTF-8 -*-

class ISS(object):
    def calcula(self, orcameto):
        return orcamento.valor * 0.1

class ICMS(object):
    def calcula(self, orcamento):
        return orcameto.valor * 0.06

class ICPP(object):
    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return orcamento.valor * 0.05

class IKCV(object):
    def calcula(self, orcamento):
        if orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento):
            return orcameto.valor * 0.1
        else:
            return orcameto.valor * 0.06
        

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcameto.obter_itens():
            if item.valor > 100:
                return True
        return False
