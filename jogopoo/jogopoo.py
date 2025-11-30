from colorama import Fore, Style, init
import random
import time
import os
# apagar o cmd
os.system('cls' if os.name == 'nt' else 'clear')

# iniciar colorama
init()

#definir cores
r = Fore.RED
g = Fore.GREEN
p = Fore.MAGENTA
reset = Style.RESET_ALL

#Jogar dado
def d20():
    resultado = random.randint(1, 20)
    return resultado

# Ver vida
def ver_status():
    print(f'''Status de {heroi.name}: 
          Vida: {heroi.hp} ''')
    print(f'''Status de {monstro.name}:
          Vida: {monstro.hp}''')
    
# classe com os basicos de um personagem
class Personagem:
    def __init__(self, name, hp, atk_min, atk_max):
        self.name = name
        self.hp = hp
        self.atk_min = atk_min
        self.atk_max = atk_max
    def atacar(self):
        return random.randint(self.atk_min, self.atk_max)

    def levar_dano(self, dano):
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0
    def vivo(self):
        return self.hp > 0

# Classe heroi com metodo unico (cura)
class Heroi(Personagem):
    def curar(self):
        cura = random.randint(10, 40)
        self.hp += cura
        print(f"{self.name} se curou em {cura} de vida!")

# Classe monstro vai herdar o personagem pra não repetir code
class Monstro(Personagem):
    pass

#main
print(5*'-' + 'RPG do wilsu' + 5*'-')
nome = input("Digite o nome do seu feiticeiro: ")
while True:
    heroi = Heroi(nome, hp=100, atk_min=1, atk_max=50)
    
    #lista de monstro disponiveis
    monstros = [
        ("Dagon", 70, 5, 20),
        ("Mahito", 90, 20, 90),
        ("Sukuna", 120, 10, 80),
        ("Hanami", 60, 1, 70)
    ]
    
    #separa os elementos que foram escolhidos da tupla.
    m_nome, m_vida, m_min, m_max = random.choice(monstros)
    monstro = Monstro(m_nome, m_vida, m_min, m_max)
    
    print(f'Um {monstro.name} com vida {monstro.hp} apareceu!')
    
    while monstro.vivo() and heroi.vivo():
        print('''
                [1] - atacar
                [2] - curar
                [3] - fugir''')
        op = input("Qual ação deseja fazer: ")
        # Parte feiticeiro
        if op == '1':
            dano = heroi.atacar()
            #critico
            if d20() <= 18 and  d20() > 16:
                dano *= 2
                print(f'{heroi.name} conseguiu acertar um {r}blackflash{reset}! Dano critico de {dano}!')
                monstro.levar_dano(dano)
            elif d20() == 20:
                print(f'{heroi.name} conseguiu uma {g}brecha!{reset} {p}Hollow Technique: Purple!{reset}')
                dano = 200
                monstro.levar_dano(dano)
            elif d20() < 10:
                dano = 0
                print(f'{heroi.name} tenta atacar mas... {monstro.name} conseguiu se {r}esquivar!{reset}')
            else:
                print(f'{heroi.name} causou {dano} de dano em {monstro.name}')
                monstro.levar_dano(dano)
        elif op == '2':
            heroi.curar()
        elif op == '3':
            print(f'{heroi.name} fugiu! Que covarde...')
            break
        else:
            print("opção inválida.")
            continue
        time.sleep(0.5)
        # Parte do Monstro
    
        if monstro.vivo():
            print(f'Turno de {monstro.name}')
            time.sleep(0.4)
            dano_m = monstro.atacar()
            if d20() <= 18 and  d20() > 16:
                dano_m *= 2
                print(f'{monstro.name} conseguiu acertar um {r}blackflash{reset}! Dano critico de {dano_m}!')
                heroi.levar_dano(dano_m)
            elif d20() == 20:
                print(f'{monstro.name} conseguiu uma {r}brecha!{reset} {r}DOMAIN EXPANSION: Fukuma Mizushi. {reset}')
                dano_m = 200
                heroi.levar_dano(dano_m)
            elif d20() < 10:
                dano_m = 0
                print(f'{monstro.name} tenta atacar mas... {heroi.name} conseguiu se {g}esquivar!{reset}')
            else:
                print(f'{monstro.name} causou {dano_m} de dano em {heroi.name}')
                heroi.levar_dano(dano_m)
        else:
            print(f'{monstro.name} foi derrotado pelo nosso heroi {heroi.name}!')
            break
        if not heroi.vivo():
            print(f"{heroi.name} foi derrotado pelo {monstro.name}...")
        print()
        ver_status()
    voltar = input("Fim de jogo. Deseja jogar novamente? (sim/nao): ").lower().strip()
    if voltar == 'sim':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        break