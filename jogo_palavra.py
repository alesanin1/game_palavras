from time import sleep
from random import randint

print((' '*15), 'Jogo da Adivinhação da Palavra')
print('-='*30)
print('''Palavra sendo escolhida Aleatóriamente da seleção de lista...
 \nDica do tema das palavras: PYTHON.''')
sleep(2)
list_words=('backend','laços','codigos','programa','variaveis')
PALAVRA_SECRET=list_words[randint(0,len(list_words)-1)]
Palavra_codif=list(len(PALAVRA_SECRET)*'*')
Tentativas=0
Parar=' '

while True:
    LETRA=str(input('Diga apenas uma letra: '))
    
    if len(LETRA) != 1:
        print('ERRO, Digite apenas uma letra!')
        continue
    else:
        Parar=' '
        if LETRA in PALAVRA_SECRET:
            for k,v in enumerate (PALAVRA_SECRET):
                if LETRA in v:
                    Palavra_codif[k]=LETRA
                    
                else:
                    pass
            print(*Palavra_codif)
        else:
            print('Nao tem')
            print(*Palavra_codif)
        Tentativas+=1
        if Palavra_codif == list(PALAVRA_SECRET):
            break
        while Parar not in 'sn':
            Parar=str(input('Deseja parar?[s/n]')).lower()[0]
        if 's' in Parar:
            print(f'Que pena não conseguir, a palavra era {PALAVRA_SECRET}')
            break
print('A palavra ficou',*Palavra_codif)
print(f'Você tentou {Tentativas} vezes.')
