import os

def clear_console():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("chora\n")

def cat(escolha):
    clear_console()

    if escolha < 4 and escolha >= 0:
        print("\n\n")
        print("Schoolyard Finds\t [        Pesquisar       ]\t Lista de desejos | Configurações | Perfil")
        print("\n\n", categorias[escolha])

        print("|                |       |                |      |                |      |                |")
        print("|                |       |                |      |                |      |                |")
        print("|    Produto 1   |       |    Produto 2   |      |    Produto 3   |      |    Produto 4   |")
        print("|                |       |                |      |                |      |                |")
        print("|                |       |                |      |                |      |                |")

    else:
        print("\n\nValor Inválido")


def pes(pesquisa):
    clear_console()

    print("\n\n")
    print("Schoolyard Finds\t", "[        ", pesquisa, "        ]", "\t Lista de desejos | Configurações | Perfil")

    print("|                |       |                |      |                |      |                |")
    print("|                |       |                |      |                |      |                |")
    print("|    Produto 1   |       |    Produto 2   |      |    Produto 3   |      |    Produto 4   |")
    print("|                |       |                |      |                |      |                |")
    print("|                |       |                |      |                |      |                |")

clear_console()

categorias = ["0.arte", "1.utilitarios", "2.tecnologia", "3.alimenticio"]

i = 0

print("Schoolyard Finds\t [        Pesquisar       ]\t Lista de desejos | Configurações | Perfil")

for i in range(4): 
    print("\n\n", categorias[i])

    print("|                |       |                |      |                |      |                |")
    print("|    Produto 1   |       |    Produto 2   |      |    Produto 3   |      |    Produto 4   |")
    print("|                |       |                |      |                |      |                |")

    i +=1

print("0 - Escolher uma Categoria")
print("1 - Pesquisar")
print("2 - Clicar em Produto")

a = int(input("O que desejas fazer?"))

if a == 0:
    escolha = int(input("Selecione uma categoria por número: "))
    cat(escolha)

elif a == 1:
    pesquisa = str(input("O que você deseja pesquisar: "))
    pes(pesquisa)

elif a == 2:
    prod = int(input("Qual produto você deseja clicar: "))
