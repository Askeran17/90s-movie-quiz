import time
import pyfiglet
import os


def start_screen():
    """
    Start image
    """
    quiz_image = pyfiglet.figlet_format("The 90´s Movie Quiz")
    print(quiz_image)
    time.sleep(4)
    os.system('clear')


start_screen()

# welcome message and game options
while True:
    print("Welcome to the 90´s Movie Quiz!\n\n")
    start_select = input("Would you like to start? Yes / No: ").lower()
    start_select = start_select.strip()
    if start_select == "yes":
        print("Great! You have to answer 10 questions. Let's start!")
        time.sleep(2)
        os.system('clear')
        break
    elif start_select not in ['yes', 'no']:
        print('This is not a valid input.\n\n')
        time.sleep(2)
        os.system('clear')
    else:
        time.sleep(2)
        os.system('clear')
        sorry_image = pyfiglet.figlet_format("Very sorry ( :")
        print(sorry_image)
        quit()


# class in which questions and answers are stored
class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
