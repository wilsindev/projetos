#imports
import random
import time
from colorama import Fore, Style, init
import os

# apagar o cmd
os.system('cls' if os.name == 'nt' else 'clear')

#define os contadores para exibir no final
contador_tentativa_senha = 0
contador_tentativa_nome = 0

#colorama
init()
r = Fore.RED
g = Fore.GREEN
reset = Style.RESET_ALL


#define as strings de caracteres disponiveis
alfabeto = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%^&*()-_=+[]{};:'\"\\|/?.,<>"
caracteres = alfabeto + numeros + simbolos
print('Cracker do wilson')
print('Iniciando cracker...')
time.sleep(0.7)
print(f'''{r}
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu          $$u$ $ $u$$       uuu
 u$$$$          $$$$$u$$$$      u$$$$
  $$$$$uu        "$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu  """   uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
      $$$"                         $$$$"
{reset}''')

#marcador de tempo inicial
inicio = time.time()

senha_escolhida = ''
nome_user = ''
for l in range(random.randint(1, 120)):
    caractere_user = random.choice(caracteres)
    nome_user += caractere_user 
for i in range(160):
    caractere_senha = random.choice(caracteres)
    senha_escolhida += caractere_senha

tamanho_senha = len(senha_escolhida)
tamanho_nome = len(nome_user)
nome_tentativa = ''
senha_tentativa = ''
for pos in range(tamanho_senha):

    letra_certa = senha_escolhida[pos]
    tentativa = ""

    while tentativa != letra_certa:
        tentativa = random.choice(caracteres)
        contador_tentativa_senha += 1
    
    senha_tentativa += tentativa
for pos in range(tamanho_nome):

    letra_certa = nome_user[pos]
    tentativa = ""

    while tentativa != letra_certa:
        tentativa = random.choice(caracteres)
        contador_tentativa_nome += 1
    
    nome_tentativa += tentativa
print(f'{g}Concluido, nome: {nome_tentativa}{reset}')
print(f'{g}Concluido, senha: {senha_tentativa}{reset}')

fim = time.time()
tempo_decorrido = fim - inicio
print(f'Tentativas de senha: {r}{contador_tentativa_senha}{reset}')
print(f'Tentativas de nomes: {r}{contador_tentativa_nome}{reset}')
print(f"O código foi executado em: {tempo_decorrido:.2f} segundos")

#Apenas uma tentativa e mais uma prática do wilson. Obrigado(a) pela atenção.