#Declaração de classes
class Gafanhoto:
    def __init__(self):#metódo construtor
        #atributos de instancia
        self.nome = " "
        self.idade = 0
    #metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade!"

#Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Antonio"
g1.idade = 21
g1.aniversario()
print(g1.mensagem())


