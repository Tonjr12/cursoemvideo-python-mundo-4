from rich import print
from rich import inspect

class Funcionario:
    #atributos de classe
    Empresa = "Curso em Video "

    def __init__(self,nome,setor,cargo):
        #atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentação(self) -> str:
        return (f':handshake:Olá,sou [blue] {self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {Funcionario.Empresa}')


#Func   ionario.Empresa = "TOM DESENVOLVIMENTO"
c1 = Funcionario("Maria","RH","Gestora")
print(c1.apresentação())
#print(c1)
#print(c1.nome)
#inspect(c1)#inspect vai inspencionar e deixar tudo organizado
#print(c1.__dict__)#__dict__= vai aparecer em um dicionario
#inspect(c1,methods = True)#apresenta os metodos
#inspect(c1,dunder=True)

c2= Funcionario("Washington","TI","Programador")
print(c2.apresentação())