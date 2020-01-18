#  Atributos públicos
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


#  Atributos privados
class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha


#  Lembre-se que o Name Mangling não impede que acessamos o atributo por fora. Isso é apenas uma convenção!
user = Acesso('pierrevieiraggg@gmail.com', 'senha')
print(user._Acesso__senha)  # Temos acesso. Mas não deveríamos fazer esse acesso.


class ProdutoImposto:
    imposto = 1.05  # Atributo de classe

    def __init__(self, nome, descricao, valor):
        self.nome = nome  # Atributo de isntância
        self.descricao = descricao  # Atributo de isntância
        self.valor = valor * ProdutoImposto.imposto  # Atributo de isntância


p1 = ProdutoImposto('PS4', 'Video Game', 2300)
p2 = ProdutoImposto('Xbox S', 'Video Game', 4500)

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de intância
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de intância

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(ProdutoImposto.imposto)

# Atributos dinâmicos
p2.peso = '5kg'
print(p2.peso)