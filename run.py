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