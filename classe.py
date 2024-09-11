# classe
class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome 
        self.__idade = idade 
        self.__email = email 

    # método de acesso
    # tem que utilizar tanto o get (pegar) quanto o set(definir).

    """def get_nome(self): #forma errada de fazer
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade"""
    
    #método get nome
    @property
    def nome(self):
        return self.__nome
    
    #método set nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    ######################

    @property
    def idade(self):
        return self.__idade

    # método set idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    #######################

    @property
    def email(self):
        return self.__email

    # método set email
    @email.setter
    def email(self, email):
        self.__email = email
