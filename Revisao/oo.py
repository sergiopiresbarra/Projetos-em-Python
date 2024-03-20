class Veiculo:
    def movimentar(self):
        print(f'sou um veiculo e me desloco!')
    
    def __init__(self, fabricante, modelo):
        #atributos privados com dois "__", exemplo: self.__atributo
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_regintro = None
    
    #setter
    def set_num_registro(self, registro):
        self.__num_regintro = registro

    #getter
    def get_fabr_modelo(self):
        print(f'modelo: {self.__modelo}, fabricante: {self.__fabricante}\n')

    def get_num_registro(self):
        return self.__num_regintro


class Carro(Veiculo):
    #metodo init será herdado
    def movimentar(self):
        print(f'sou um carro e me movimento!')

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'corro muito!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)
    def get_categoria(self):
        return self.__cat
    def movimentar(self):
        print('eu voo alto!')


if __name__ == '__main__':
    meu_veiculo = Veiculo('GM','Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('490321-1')
    print(f'registro: {meu_veiculo.get_num_registro()}')

    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    moto = Motocicleta('Harley', 'Nigthster Special')
    moto.movimentar()
    moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'{meu_aviao.get_categoria()}')