import os, random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 50
HPMAX = 50
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

    #    x = 0        x = 1        x = 2        x = 3        x = 4       x = 5       x = 6
map = [["planicies", "planicies", "planicies", "planicies", "floresta", "montanha", "caverna"],     # y = 0
       ["floresta",  "floresta",  "floresta",  "floresta",  "floresta", "colinas",  "montanha"],    # y = 1
       ["floresta",  "campos",    "ponto",     "planicies", "colinas",  "floresta", "colinas"],     # y = 2
       ["planicies", "loja",      "cidade",    "prefeito",  "planicies","colinas",  "montanha"],    # y = 3
       ["planicies", "campos",    "campos",    "planicies", "colinas",  "montanha", "montanha"]]    # y = 4

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "planicies": {
        "t": "PLANICIES",
        "e": True},
    "floresta": {
        "t": "BOSQUE",
        "e": True},
    "campos": {
        "t": "CAMPOS",
        "e": False},
    "ponto": {
        "t": "PONTE",
        "e": True},
    "cidade": {
        "t": "CENTRO DA CIDADE",
        "e": False},
    "loja": {
        "t": "LOJA",
        "e": False},
    "prefeito": {
        "t": "PREFEITO",
        "e": False},
    "caverna": {
        "t": "CAVERNA",
        "e": False},
    "montanha": {
        "t": "MONTANHA",
        "e": True},
    "colinas": {
        "t": "COLINAS",
        "e": True,
    }
}

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Ork": {
        "hp": 35,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "hp": 30,
        "at": 2,
        "go": 12
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
        str(pot),
        str(elix),
        str(gold),
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
    global fight, play, run, HP, pot, elix, gold, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print("Defeat the " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elix > 0:
            print("3 - USE ELIXIR (50HP)")
        draw()

        choice = input("> ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No elixirs!")
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
            gold += g
            print("Você encontrou " + str(g) + " ouro!")
            if random.randint(0, 100) < 30:
                pot += 1
                print("Você encontrou uma poção!")
            if enemy == "Dragon":
                draw()
                print("Parabéns, você terminou o jogo!")
                boss = False
                play = False
                run = False
            input("> ")
            clear()


def shop():
    global buy, gold, pot, elix, ATK

    while buy:
        clear()
        draw()
        print("Bem-vindo à loja!")
        draw()
        print("OURO: " + str(gold))
        print("POÇÕES: " + str(pot))
        print("ELIXIRES: " + str(elix))
        print("ATK: " + str(ATK))
        draw()
        print("1 - COMPRAR POÇÃO (30HP) - 5 OURO")
        print("2 - COMPRAR ELIXIR (MAXHP) - 8 OURO")
        print("3 - MELHORAR ARMA (+2ATK) - 10 OURO")
        print("4 - SAIR DA LOJA")
        draw()

        choice = input("> ")

        if choice == "1":
            if gold >= 5:
                pot += 1
                gold -= 5
                print("Você comprou uma poção!")
            else:
                print("Você não tem ouro suficiente!")
            input("> ")
        elif choice == "2":
            if gold >= 8:
                elix += 1
                gold -= 8
                print("Você comprou um elixir!")
            else:
                print("Você não tem ouro suficiente!")
            input("> ")
        elif choice == "3":
            if gold >= 10:
                ATK += 2
                gold -= 10
                print("Você melhorou sua arma!")
            else:
                print("Você não tem ouro suficiente!")
            input("> ")
        elif choice == "4":
            buy = False


def mayor():
    global speak, key

    while speak:
        clear()
        draw()
        print(f"Hello there, {name}!")
        if ATK < 10:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            key = False
        else:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            key = True

        draw()
        print("1 - LEAVE")
        draw()

        choice = input("> ")

        if choice == "1":
            speak = False


def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        draw()

        choice = input("> ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False



while run:
    clear()
    while menu:
        print("1 - INICIAR JOGO")
        print("2 - CARREGAR JOGO")
        print("3 - REGRAS")
        print("4 - SAIR")

        if rules:
            print("Jogo criado para o projeto de Python do curso Raciocínio Algorítmico.")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("> ")

        if choice == "1":
            clear()
            name = input("Qual é o seu nome, jogador?\n> ")
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
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
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
            rules = True
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
            print("NOME: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: " + str(gold))
            print("COORD:", x, y)
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
            if pot > 0:
                print("5 - USAR POÇÃO (30HP)")
            if elix > 0:
                print("6 - USAR ELIXIR (50HP)")
            if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
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
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print("Sem poções!")
                input("> ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                else:
                    print("Sem elixires!")
                input("> ")
                standing = True
            elif dest == "7":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()
            else:
                standing = True
                print("Comando inválido!")
                input("> ")