import os

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Tomáš Vaško
email: t.vasko@seznam.cz
"""

# Definice globálních proměnných
board = [" " for _ in range(9)]
current_player = "X"

def clear_screen():
    """Funkce pro vyčištění obrazovky."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board():
    """Funkce zobrazí aktuální stav hrací plochy s uzavřenými čtverci a obvodovým ohraničením."""
    print("\n")
    print("┌───┬───┬───┐")
    print(f"│ {board[0]} │ {board[1]} │ {board[2]} │")
    print("├───┼───┼───┤")
    print(f"│ {board[3]} │ {board[4]} │ {board[5]} │")
    print("├───┼───┼───┤")
    print(f"│ {board[6]} │ {board[7]} │ {board[8]} │")
    print("└───┴───┴───┘")
    print("\n")

def greet_user():
    """Funkce pozdraví uživatele a vypíše pravidla hry."""
    print("Vítejte ve hře Piškvorky!")
    print("Pravidla: Vyberte pozici na hrací ploše (1-9) a pokuste se vytvořit řadu tří kamenů.")
    print("Hráč 1 je 'X' a hráč 2 je 'O'. Pojďme hrát!\n")

def validate_input(input_str):
    """Funkce ověří, zda je vstup platný."""
    if not input_str.isdigit():
        print("Chyba: Vstup musí být číslo od 1 do 9.")
        return False
    position = int(input_str) - 1
    if position < 0 or position > 8:
        print("Chyba: Vyberte číslo v rozmezí 1 až 9.")
        return False
    if board[position] != " ":
        print("Chyba: Tato pozice je již obsazena.")
        return False
    return True

def check_winner():
    """Funkce kontroluje, zda je na hrací ploše výherní kombinace."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontální řady
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertikální řady
        (0, 4, 8), (2, 4, 6)              # Diagonální řady
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    return None

def is_board_full():
    """Funkce kontroluje, zda je hrací plocha plná (pro remízu)."""
    return " " not in board

def play_game():
    """Hlavní funkce pro spuštění hry."""
    clear_screen()
    greet_user()
    display_board()
    global current_player
    
    while True:
        # Vstup hráče
        position = input(f"Hráč {current_player}, zvolte pozici (1-9): ")
        if not validate_input(position):
            continue
        
        # Aktualizace hrací plochy
        board[int(position) - 1] = current_player
        clear_screen()
        display_board()
        
        # Kontrola výhry nebo remízy
        winner = check_winner()
        if winner:
            print(f"Gratulace! Hráč {winner} vyhrál!")
            break
        if is_board_full():
            print("Remíza! Hrací plocha je plná.")
            break
        
        # Přepnutí hráče
        current_player = "O" if current_player == "X" else "X"

# Spuštění hry
play_game()

