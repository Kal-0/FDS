from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('''home!<br> <img src="https://cdn.discordapp.com/attachments/1081640134371446956/1094364787992973462/Botao_de_Home.png">''')

def feed(request):
    return HttpResponse('''feed!<br> 
                        <div>
                        <p>
                        <img src="https://cdn.discordapp.com/attachments/1081640134371446956/1094364788445958144/fudge-palito.webp">
                        <img src="https://cdn.discordapp.com/attachments/1081640134371446956/1094364790689890385/Receita_cake_pop_Silvia_Oliveira_Eventos_Criativos_07.webp">
                        </p>
                        </div>''')
