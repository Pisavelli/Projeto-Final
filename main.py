import os, time

run = True
menu = True
play = False

HP = 100
ATK = 3
name = ""

def slow_print(text, delay=0.002):
    """Prints text slowly with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line after printing the text

def draw():
    slow_print("────────────────────────")

def clear():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def save():
    data = {
        "Name": name,
        "HP": HP,
        "ATK": ATK
    }
    with open("save.txt", "w") as f:
        f.write(str(data))

while run:
    if menu:
        clear()
        draw()
        slow_print("Bem-vindo ao jogo!")
        slow_print("1. Iniciar Jogo")
        slow_print("2. Carregar Jogo")
        slow_print("3. Sair do Jogo")
        draw()

        choice = slow_print("Por favor, escolha uma opção: ")
        draw()
        slow_print("Sua escolha: ")
        choice = input()

        if choice == '1':
            clear()
            menu = False
            play = True
            name = slow_print("Digite seu nome: ")
            name = input()  # Get the player's name
            clear()
            slow_print(f"Olá, {name}! Vamos começar o jogo.")

        elif choice == '2':
            clear()
            try:
                with open("save.txt", "r") as f:
                    data = eval(f.read())
                    name = data.get("Name", "")
                    HP = data.get("HP", 100)
                    ATK = data.get("ATK", 3)
                    slow_print(f"Bem-vindo de volta, {name}!")
            except FileNotFoundError:
                slow_print("Nenhum arquivo de salvamento encontrado.")
            menu = False
            
        elif choice == '3':
            clear()
            run = False
            quit_choice = input("Tem certeza de que deseja sair? (sim/não): ")
            if quit_choice.lower() == 'sim':
                clear()
                slow_print("Obrigado por jogar!")
                slow_print("Saindo do jogo...")
                quit()
            elif quit_choice.lower() == 'não':
                clear()
                slow_print("Retornando ao menu...")
                menu = True
            else:
                clear()
                slow_print("Escolha inválida. Retornando ao menu...")
                menu = True

        else:
            clear()
            slow_print("Escolha inválida, por favor tente novamente.")

    elif play:
        clear()
        save()
        slow_print("Iniciando o jogo...")
        slow_print(name)
        play = False  # Reset to go back to menu
