import random
import time

class Player:
    def __init__ (self, name):
        self.name = name
        self.hand = ''
        return
    
    #player hand
    def hands(self):
        self.hand = ''
        self.hand = input ('Choose rock, paper or siccors: ')
        answers = ['rock', 'paper', 'siccors']
        while self.hand not in answers:
            self.hand = input ('Sorry, input invalid.\nChoose rock, paper or siccors: ')
        return
    
class CPU:
    def __init__(self):
        self.hand = ''
        return
    
    #computer choice
    def cpuhand(self):
        answers = ['rock', 'paper', 'siccors']
        random.shuffle(answers)
        self.hand = answers[1]
        return 

#results
def outcome(phand,chand):
    #add suspense
    print('ROCK')
    time.sleep(1)
    print('PAPER')
    time.sleep(1)
    print('SICCORS')
    time.sleep(1)
    print('SHOOT')

    if phand == chand:
        print(f'TIE!\nYour {phand} draws with CPUs {chand} ')
        return
    elif (phand == 'rock' and chand == 'siccors') or (phand == 'paper' and chand == 'rock') or (phand == 'siccors' and chand == 'paper'):
        print(f'VICTORY!\nYour {phand} wins CPUs {chand} ')
        return
    else:
        print(f'DEFEAT!\nYour {phand} loses to CPUs {chand} ')
        return

#Play again
def gameon():
    answer = ''
    answer = input('Rematch? Y/N: ').capitalize()
    while answer not in ['Y','N']:
        answer = input('Sorry, input invalid.\nRematch? Y/N: ').capitalize()

    if answer == 'Y':
        return True
    elif answer == 'N': 
        print('Thanks for playing!! Goodbye')
        return False

def main():
    playername = input ('Input username: ')
    player = Player(playername)
    computer = CPU()
    game_on = True
    while game_on:
        player.hands()
        computer.cpuhand()
        outcome(player.hand, computer.hand)
        game_on = gameon()
    return

main()
