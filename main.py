from classe import *

if __name__ == '__main__':
    nome = input('informe o nome: ')
    idade = int(input('informe a idade: '))
    email = input('informe o email: ')

   
    # instancia o objeto
    usuario = Pessoa(nome, idade, email)
    
    #saída de dados
    print(f'Nome: {usuario.nome}')
    print(f'Idade: {usuario.idade}')
    print(f'Email: {usuario.email}')
