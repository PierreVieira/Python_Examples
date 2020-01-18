class Produto:
    def __init__(self, nome, descricao, valor):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    def desconto(self, porcentagem):
        """
        Retorna o valor do produto com desconto
        :param porcentagem: O desconto que será dado em porcentagem
        :return: Valor do produto com desconto
        """
        return (self.__valor * (100 - porcentagem)) / 100


produto = Produto('PS4', 'Video Game', 2400)
print(produto.desconto(20))
print(Produto.desconto(produto, 40))
