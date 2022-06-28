from gtts import gTTS
from pygame import mixer

print("O que deseja falar? (Digite sair para fechar a aplicação)")
mensagem = input("> ")
mixer.init()

while (mensagem != "sair"):
  voz = gTTS(mensagem, lang="pt")#gravação da mensagem de voz na linguagem portg
  voz.save("voz.mp3") #salvando...
  print('Falando ...') #exibição na tela

  #para leitura da mensagem
  mixer.music.load("./voz.mp3")
  mixer.music.play()
  mensagem = input("> ")
