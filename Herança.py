class Pessoa:
    # Classe Pessoa é mãe de Cliente e Funcionário
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return self.__nome + ' ' + self.__sobrenome


class Cliente(Pessoa):
    # Cliente herda de Pessoa
    def __init__(self, renda, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionário herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.matricula = matricula
