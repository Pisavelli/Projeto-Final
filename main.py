import os, random, time

run = True
menu = True
play = False
about = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 50
HPMAX = 50
ATK = 3
potion = 1
elixir = 0
ouro = 0
x = 0
y = 0

map = [
    #   x = 0        x = 1        x = 2        x = 3        x = 4       x = 5       x = 6
    ["planicies", "planicies", "planicies", "planicies", "floresta", "montanha", "caverna"],    # y = 0
    ["floresta",  "floresta",  "floresta",  "floresta",  "floresta", "colinas",  "montanha"],   # y = 1
    ["floresta",  "campos",    "ponto",     "planicies", "colinas",  "floresta", "colinas"],    # y = 2
    ["planicies", "loja",      "cidade",    "prefeito",  "planicies","colinas",  "montanha"],   # y = 3
    ["planicies", "campos",    "campos",    "planicies", "colinas",  "montanha", "montanha"]    # y = 4
    ]

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "planicies": {
        "t": "PLANICIES",
        "e": True
        },
    "floresta": {
        "t": "FLORESTA",
        "e": True
        },
    "campos": {
        "t": "CAMPOS",
        "e": False
        },
    "ponto": {
        "t": "PONTE",
        "e": True
        },
    "cidade": {
        "t": "CENTRO DA CIDADE",
        "e": False
        },
    "loja": {
        "t": "LOJA",
        "e": False
        },
    "prefeito": {
        "t": "PREFEITO",
        "e": False
        },
    "caverna": {
        "t": "CAVERNA",
        "e": False
        },
    "montanha": {
        "t": "MONTANHA",
        "e": True
        },
    "colinas": {
        "t": "COLINAS",
        "e": True
    }
}

e_list = ["Goblin", "Ork", "Slime", "Gigante", "Bandido", "Lobo"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Ork": {
        "hp": 30,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "hp": 10,
        "at": 1,
        "go": 12
    },
    "Gigante": {
        "hp": 50,
        "at": 2,
        "go": 25
    },
    "Bandido": {
        "hp": 40,
        "at": 3,
        "go": 20
    },
    "Lobo": {
        "hp": 20,
        "at": 3,
        "go": 10
    },
    "Dragão": {
        "hp": 100,
        "at": 8,
        "go": 100
    }
}


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


def draw():
    print("────────────────────────")


def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(potion),
        str(elixir),
        str(ouro),
        str(x),
        str(y),
        str(key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()


def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(name + "'s HP refilled to " + str(HP) + "!")


def battle():
    global fight, play, run, HP, potion, elixir, ouro, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragão"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print(f"Defeat the {enemy}!")
        draw()
        print(f"{enemy}'s HP: {hp}/{hpmax}")
        print(f"{name}'s HP: {HP}/{HPMAX}")
        print(f"POÇÕES: {potion}")
        print(f"ELIXIRES: {elixir}")
        draw()
        print("1 - ATACAR")
        if potion > 0:
            print("2 - USAR POÇÃO (30HP)")
        if elixir > 0:
            print("3 - USAR ELIXIR (50HP)")
        draw()

        choice = input("> ")

        if choice == "1":
            hp -= ATK
            print(f"{name} causou {ATK} de dano ao {enemy}.")
            if hp > 0:
                HP -= atk
                print(f"{enemy} causou {atk} de dano a {name}.")
            input("> ")

        elif choice == "2":
            if potion > 0:
                potion -= 1
                heal(30)
                HP -= atk
                print(f"{enemy} causou {atk} de dano a {name}.")
            else:
                print("Sem Poções!")
            input("> ")

        elif choice == "3":
            if elixir > 0:
                elixir -= 1
                heal(50)
                HP -= atk
                print(f"{enemy} causou {atk} de dano a {name}.")
            else:
                print("Sem Elixires!")
            input("> ")

        if HP <= 0:
            print(f"{enemy} derrotou {name}...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(f"{name} derrotou o {enemy}!")
            draw()
            fight = False
            ouro += g
            print(f"Você encontrou {g} ouro!")
            if random.randint(0, 100) < 30:
                potion += 1
                print("Você encontrou uma poção!")
            if enemy == "Dragão":
                draw()
                print("Parabéns, você terminou o jogo!")
                print("Você derrotou o dragão e salvou a cidade!")
                print("Obrigado por jogar!")
                print("Feito por Pierre e Guilherme.")
                boss = False
                play = False
                run = False
            input("> ")
            clear()


def loja():
    global buy, ouro, potion, elixir, ATK

    while buy:
        clear()
        draw()
        print("Bem-vindo à loja!")
        draw()
        print(f"OURO: {ouro}")
        print(f"POÇÕES: {potion}")
        print(f"ELIXIRES: {elixir}")
        print(f"ATK: {ATK}")
        draw()
        print("1 - COMPRAR POÇÃO (30HP) - 5 OURO")
        print("2 - COMPRAR ELIXIR (MAXHP) - 8 OURO")
        print("3 - MELHORAR ARMA (+2ATK) - 10 OURO")
        print("4 - SAIR DA LOJA")
        draw()

        choice = input("> ")

        if choice == "1":
            if ouro >= 5:
                potion += 1
                ouro -= 5
                print("Você comprou uma poção!")
            else:
                print("Você não tem ouro suficiente!")
            input("> ")

        elif choice == "2":
            if ouro >= 8:
                elixir += 1
                ouro -= 8
                print("Você comprou um elixir!")
            else:
                print("Você não tem ouro suficiente!")
            input("> ")

        elif choice == "3":
            if ouro >= 10:
                ATK += 2
                ouro -= 10
                print("Você melhorou sua arma!")
            else:
                print("Você não tem ouro suficiente!")
            input("> ")

        elif choice == "4":
            buy = False


def prefeito():
    global speak, key

    while speak:
        clear()
        draw()
        print(f"Olá, {name}! Eu sou o prefeito Beicinicus.")
        if ATK < 10:
            print("Você não é forte o suficiente para enfrentar o dragão ainda! Continue praticando e volte mais tarde!")
            key = False
        else:
            print("Você pode querer enfrentar o dragão agora! Pegue esta chave, mas tenha cuidado com a besta!")
            key = True

        draw()
        print("1 - SAIR")
        draw()

        choice = input("> ")

        if choice == "1":
            speak = False


def caverna():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Aqui está a caverna do dragão. O que você vai fazer?")
        draw()
        if key:
            print("1 - USAR CHAVE")
        print("2 - VOLTAR")
        draw()

        choice = input("> ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False

def introducao():
    print("Você não lembra do seu passado, mas sabe que precisa sobreviver. Você acorda em um lugar desconhecido, sem saber como chegou lá.")
    print("\nVocê tem apenas uma espada e um escudo, e precisa explorar o mundo para descobrir mais sobre si mesmo.")
    print("\nVocê pode encontrar monstros, tesouros e pessoas ao longo do caminho.")
    print("\nVocê pode lutar contra os monstros, comprar itens na loja, e descobrir segredos.")
    print("\nUse as teclas do teclado para se mover e realizar ações.")
    print("\nVocê pode salvar o jogo a qualquer momento, e carregar o jogo salvo quando quiser.")
    print("\nBoa sorte, aventureiro!")

while run:
    clear()
    while menu:
        print("1 - INICIAR JOGO")
        print("2 - CARREGAR JOGO")
        print("3 - SOBRE O JOGO")
        print("4 - SAIR")

        if about:
            clear()
            print("Jogo criado para o projeto de Python do curso Raciocínio Algorítmico. Feito por Pierre e Guilherme, futuros Engenheiros de Software.")
            about = False
            choice = ""
            input("> ")
        else:
            choice = input("> ")

        if choice == "1":
            clear()
            introducao()
            time.sleep(6)
            name = input("\nQual é o seu nome, jogador?\n> ").upper()
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    potion = int(load_list[3][:-1])
                    elixir = int(load_list[4][:-1])
                    ouro = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print(f"Bem-vindo de volta, {name}!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Salvamento corrompido!")
                    input("> ")
            except OSError:
                print("Não foi possível carregar o arquivo de salvamento!")
                input("> ")
        elif choice == "3":
            about = True
        elif choice == "4":
            quit()

    while play:
        save()  # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) < 30:
                    fight = True
                    battle()

        if play:
            draw()
            print("LOCALIZAÇÃO: " + biom[map[y][x]]["t"])
            draw()
            print(f"NOME: {name}")
            print(f"HP: {HP}/{HPMAX}")
            print(f"ATK: {ATK}")
            print(f"POÇÕES: {potion}")
            print(f"ELIXIRES: {elixir}")
            print(f"OURO: {ouro}")
            print(f"COORD: {x}, {y}")
            draw()
            print("0 - SALVAR E SAIR")
            if y > 0:
                print("1 - NORTE")
            if x < x_len:
                print("2 - LESTE")
            if y < y_len:
                print("3 - SUL")
            if x > 0:
                print("4 - OESTE")
            if potion > 0:
                print("5 - USAR POÇÃO (30HP)")
            if elixir > 0:
                print("6 - USAR ELIXIR (50HP)")
            if map[y][x] == "loja" or map[y][x] == "prefeito" or map[y][x] == "caverna":
                print("7 - ENTRAR")
            draw()

            dest = input("> ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if potion > 0:
                    potion -= 1
                    heal(30)
                else:
                    print("Sem poções!")
                input("> ")
                standing = True
            elif dest == "6":
                if elixir > 0:
                    elixir -= 1
                    heal(50)
                else:
                    print("Sem elixires!")
                input("> ")
                standing = True
            elif dest == "7":
                if map[y][x] == "loja":
                    buy = True
                    loja()
                if map[y][x] == "prefeito":
                    speak = True
                    prefeito()
                if map[y][x] == "caverna":
                    boss = True
                    caverna()
            else:
                standing = True
                print("Comando inválido!")
                input("> ")