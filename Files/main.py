import hashlib
import time
import os
import importlib
import webbrowser

def cls():
        os.system('clear')


def remove_spaces(input):
        output = input.replace(" ", "")
        return output

def join(str1, str2):
    return str1 + str2


def web():
        cls()
        print("Web Browser -- K-OS 3")
        url = input("URL: ")
        webbrowser.open(url)


def games():
    games = []
    current_directory = os.path.dirname(os.path.abspath(__file__))
    dir = os.path.join(current_directory, "Apps")
    print(current_directory)

    for file in os.listdir(dir):
        if file.endswith('.py') and file != 'main.py':
            games.append(file[:-3])  # Remove the ".py" extension

    if not games:
        print("No games found in the current directory.")
        return

    cls()
#    print(current_directory) #debug code lol
    print("Available games:")
    for i, game in enumerate(games):
        print(f"{i + 1}. {game}")

    choice = input("Select a game by entering its number: ")
    os.system('clear')

    try:
        choice = int(choice)
        if 1 <= choice <= len(games):
            game_name = games[choice - 1]
            try:
                game_module = importlib.import_module(game_name)
                game_module.main()
            except ImportError:
                print(f"Failed to import the game module: {game_name}. Make sure it exists.")
            except AttributeError:
                print(f"The game module {game_name} does not have a 'main' function.")
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")






def settings():
        cls()
        print("Settings:")
        print("1. Change Username")
        print("2. Change Password")
        selected = input("")
        if selected == "1":
                newuser = input("Choose a new username: ")
                with open('username.txt', 'w') as file:
                        file.write(newuser)
        elif selected == "2":
                newpass = input("Choose a new password: ")
                with open('password.txt', 'w') as file:
                        file.write(newpass)





#//debug code lol - ignore
def debug():
        data = "test"
        hash = hashlib.sha256()
        hash.update(data.encode('utf-8'))
        sumpass = hash.hexdigest()
        print(sumpass)


def logon():
        # i have no idea what imma do here lol :3
        cls()
        print("K-OS 3")
        print("1. Settings")
        print("2. Games")
        print("3. Web Browser")
        app = input("Choose an app: ")
        if app == "1":
                settings()
        elif app == "2":
                games()
        elif app == "3":
                web()
        else:
                print("Not an option.")

with open('password.txt', 'r') as file:
        passwd = file.read()

with open('username.txt', 'r') as file:
    # Read the contents of the file and store it in the 'user' variable
    user = file.read()

def checksum(data):
    #this code checksums (duh)
    hash_object = hashlib.sha256()
    hash_object.update(data.encode('utf-8'))
    checksum = hash_object.hexdigest()
    return checksum

def start(): # this took me so long to figure out, fuck you nano formatting.
        global loggedon
        loggedon = 0
        cls()
        print("login as "+user)
        login = input("- ")
        sum = checksum(login)
        if sum == passwd:
                loggedon == 1
                logon()
        else:
                print(RED+"Incorrect."+RESET)

#//ANSI escape codes to colour text
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"

start()

if __name__ == "__main__" and loggedon == "1":
        logon()
