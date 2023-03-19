#chat()
class Mensagem:
  usuario = 0
  destinatario = 0
  ordem = 0
  texto = ""
  
  def __init__(self, textoMensagem, ordemMensagem, usuarioMensagem, destinatarioMensagem):
    self.texto = textoMensagem
    self.ordem = ordemMensagem
    self.usuario = usuarioMensagem
    self.destinatario = destinatarioMensagem

mes12_0 = Mensagem("oi user2!",0, "usuario1", "usuario2")
mes12_1 = Mensagem("como vai voce?",1, "usuario1", "usuario2")
mes21_0 = Mensagem("ola, vou bem e voce?",3, "usuario2", "usuario1")

mes31_0 = Mensagem("user1, eu quero comprar suas bolas doces!",0, "usuario3", "usuario1")
mes13_0 = Mensagem("user3 minhas bolas doces acabaram ;-;, mas o user2 esta vendendo bolas doces no palito!!",1, "usuario1", "usuario3")
mes31_1 = Mensagem("serio user1?!, vou comprar as bolas doces no palito dele agora mesmo!",2, "usuario3", "usuario1")

mes32_0 = Mensagem("user2, voce ainda esta vendendo suas bolas doces no palito?!",0, "usuario3", "usuario2")
mes23_0 = Mensagem("estou sim user3, voce pode vir compra las aqui na sala 12 do BJ!",3, "usuario2", "usuario3")




def displayMensagens(Database, usuarioAtual, usuarioDestinatario):
  listaMensagens = []
  
  for usuario in Database:
    if usuario == usuarioAtual or usuario == usuarioDestinatario:
      
      for contato in Database[usuario]:
        if contato == usuarioDestinatario or contato == usuarioAtual:
          
          for menssagem in Database[usuario][contato]:
            listaMensagens.insert(menssagem.ordem, menssagem)


  for menssagem in listaMensagens:
    if(menssagem.usuario == usuarioAtual):
      print(f"voce: \n{menssagem.texto}\n")
    else:
      print(f"Destinatario: \n{menssagem.texto}\n")
  print("==================================================\n\n")


bd = {
  "usuarios" : {
    "usuario1" : {
      "usuario2" : [mes12_0, mes12_1],
      "usuario3" : [mes13_0]
     },
    
    "usuario2" : {
                "usuario1" : [mes21_0],
                "usuario3" : [mes23_0]
               },
    
    "usuario3" : {
                "usuario1" : [mes31_0,mes31_1],
                "usuario2" : [mes32_0]
               }
  }
  
}


usuarioAtual = "usuario3"
usuarioDestinatario = "usuario1"

def chat():
  while True:
    displayMensagens(bd["usuarios"], usuarioAtual, usuarioDestinatario)
    
    print('''\n\n
Digite: 0 para voltar.\n
Digite: 1, para enviar uma menssagem.\n
''')

    op = int(input("o que voce deseja fazer: "))
    
    match op:
    
      case 0:
        break;
        
      case 1:
        print("enviarMensagem")

chat()
    

