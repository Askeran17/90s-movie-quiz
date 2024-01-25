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
    start_select = input("Would you like to start? Yes / No:\n").lower()
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


# list of questions and answer options
questions_list = [
    'What year is the movie "Heat"?\n\n'
    'A: 1995\n'
    'B: 1996\n'
    'C: 1997\n'
    'D: 1998\n',
    'What was the name of the main actor in the film "Cliffhanger" 1993?\n\n'
    'A: Dolf Lundgren\n'
    'B: Sylvester Stallone\n'
    'C: Don Dragon Wilson\n'
    'D: John Travolta\n',
    'What was the name of the movie about the sunken ship 1998?\n\n'
    'A: Titanic\n'
    'B: Britannic\n'
    'C: Concorde\n'
    'D: Heavy metal\n',
    'What year is the movie "Mask"?\n\n'
    'A: 1991\n'
    'B: 1999\n'
    'C: 1993\n'
    'D: 1994\n',
    'In which 1994 film did Jean-Claude Van Damme play a policeman?\n\n'
    'A: Robocop\n'
    'B: Beverly Hills Cop\n'
    'C: Timecop\n'
    'D: The Cop\n',
    'What was the name of the blue ninja in the movie "Mortal Kombat"?\n\n'
    'A: Scorpion\n'
    'B: Sub-Zero\n'
    'C: Reptile\n'
    'D: Smoke\n',
    'What is the name of the movie in which Jim Carrey plays a lawyer?\n\n'
    'A: The Truman Show\n'
    'B: Ace Ventura\n'
    'C: Liar Liar\n'
    'D: Dumb and Dumber\n',
    'The movie in 1990 about mafia where Al Pacino played the main role?\n\n'
    'A: Serpico\n'
    'B: The Scarface\n'
    'C: Goodfellas\n'
    'D: The Godfather 3\n',
    'The name of the 1995 movie where Tom Hanks runs around the world?\n\n'
    'A: Forrest Gump\n'
    'B: Apollo 13\n'
    'C: Cast Away\n'
    'D: Sleepless in Seattle\n',
    'In what 1996 film did Michael Jordan play with cartoons?\n\n'
    'A: Toy Story\n'
    'B: Space Jam\n'
    'C: A Goofy Movie\n'
    'D: The Prince and the Pauper\n'
]

# list of right answers
quiz_answer = [
    Quiz(questions_list[0], 'a'),
    Quiz(questions_list[1], 'b'),
    Quiz(questions_list[2], 'a'),
    Quiz(questions_list[3], 'd'),
    Quiz(questions_list[4], 'c'),
    Quiz(questions_list[5], 'b'),
    Quiz(questions_list[6], 'c'),
    Quiz(questions_list[7], 'd'),
    Quiz(questions_list[8], 'a'),
    Quiz(questions_list[9], 'b'),
]


def play_quiz(quiz_answer):
    """
    Play quiz function
    """
    score = 0

    for questions_quiz in quiz_answer:
        while True:
            print(questions_quiz.question)
            options = input("Please select A, B, C, or D:\n")
            answer_select = options.lower()
            answer_select = answer_select.strip()
            if answer_select not in ['a', 'b', 'c', 'd']:
                print('This is not a valid choice.\n\n')
                time.sleep(2)
                os.system('clear')
            else:
                time.sleep(2)
                break
        if answer_select == questions_quiz.answer:
            score += 1
            print("\nThat is correct answer!\n\n")
            time.sleep(2)
            os.system('clear')
            continue
        else:
            print("\nThat is wrong answer\n\n")
            time.sleep(2)
            os.system('clear')

    print('You answered right ' + str(score) + ' of ' + str(len(quiz_answer)))
    time.sleep(3)
    os.system('clear')
    end_image = pyfiglet.figlet_format("The End")
    print(end_image)
    time.sleep(3)
    os.system('clear')


play_quiz(quiz_answer)


# restart or exit quiz
while True:
    restart_select = input('Restart the quiz? Yes / No:\n').lower()
    restart_select = restart_select.strip()
    if restart_select == "yes":
        time.sleep(2)
        os.system('clear')
        play_quiz(quiz_answer)
    elif restart_select not in ['yes', 'no']:
        print('This is not a valid input.\n\n')
    else:
        time.sleep(2)
        os.system('clear')
        bye_image = pyfiglet.figlet_format("Bye! See you again :)")
        print(bye_image)
        quit()
