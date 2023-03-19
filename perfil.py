#perfil()
def perfil():
  while True:
    print('''Digite: 0 para voltar.\n
  Digite: 1 para acessar as configuracoes.\n
  Digite: 2 para ver produtos.\n
  Digite: 3 para acessar os detalhes do usuario.\n
  Digite: 4 para acessar o chat do usuario.\n
  Digite: 5 para avaliar usuario.\n
  Digite: 6 para acessar as opções do perfil.
  ''')
    
    
    op = int(input("o que voce deseja fazer: "))
    
    match op:
    
      case 0:
        break;
        
      case 1:
        print("menuConfiguracao()")
        
      case 2:
        print("verProdutos()")
  
      case 3:
        print("detalhesUsuario()")
  
      case 4:
        print("chat()")
  
      case 5:
        print("avaliarUsuario()")
  
      case 6:
        print("opcoesPerfil()")
  
