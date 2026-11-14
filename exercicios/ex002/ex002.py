#Declaração de classes
class Gafanhoto:
    """
    Essa classe cria um gafanhoto que é uma pessoa com nome e idade.
    Para criar um gafanhoto uma classe use
    variavel = Gafanhoto('nome', idade)
    """
    def __init__(self,nome="Vazio ",idade = 0):#metódo construtor
        #atributos de instância
        self.nome = nome
        self.idade = idade

    #metodos de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):#Dunder Method
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado : nome = {self.nome}, idade = {self.idade}"
#Declaração de objetos
g1 = Gafanhoto("Antonio",21)
g1.aniversario()
#print(g1)
print(g1.__dict__)#Attribute
print(g1.__getstate__())#Method
print(g1.__doc__)#Dunder Attribute
print(g1.__class__)