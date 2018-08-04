from impostos import ISS, ICMS

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print valor

if __name__ == '__main__':

    from orcamento import Orcamento

    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)
    calculador.realiza_calculo(orcamento, ICMS())
    calculador.realiza_calculo(orcamento, ISS())
