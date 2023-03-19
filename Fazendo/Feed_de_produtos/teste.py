import os

def clear_console():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("chora\n")


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
    

escolha = int(input("Selecione uma categoria por número: "))

clear_console()

print("Schoolyard Finds\t [        Pesquisar       ]\t Lista de desejos | Configurações | Perfil")

print("\n\n", categorias[escolha])

print("|                |       |                |      |                |      |                |")
print("|                |       |                |      |                |      |                |")
print("|    Produto 1   |       |    Produto 2   |      |    Produto 3   |      |    Produto 4   |")
print("|                |       |                |      |                |      |                |")
print("|                |       |                |      |                |      |                |")