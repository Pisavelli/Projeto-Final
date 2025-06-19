run = True
menu = True
play = False
rules = False

while run:
    if menu:
        print("Welcome to the game!")
        print("1. Play")
        print("2. Rules")
        print("3. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            menu = False
            play = True
        elif choice == '2':
            menu = False
            rules = True
        elif choice == '3':
            run = False
        else:
            print("Invalid choice, please try again.")

    elif play:
        print("Starting the game...")
        # Game logic goes here
        play = False  # Reset to go back to menu

    elif rules:
        print("Game Rules:")
        print("1. Rule one")
        print("2. Rule two")
        input("Press Enter to return to the menu...")
        rules = False  # Reset to go back to menu