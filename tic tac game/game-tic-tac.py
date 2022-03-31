#!/usr/bin/python

import random

def display(r1):
    print(f' {r1[0]} | {r1[1]} | {r1[2]}')
    print('-----------')
    print(f' {r1[3]} | {r1[4]} | {r1[5]}')
    print('-----------')
    print(f' {r1[6]} | {r1[7]} | {r1[8]}')

def user_input():
    place_list = [0,1,2,3,4,5,6,7,8,9]
    user_place = 10
    while user_place not in place_list:
        user_place = input("Please enter the place between 0-9: ")
        if user_place.isdigit() == False:
            print('this is not a digit, please enter a numeric digit')
        else:
            user_place = int(user_place)
            if user_place >= 10:
                print('Please enter a value lower than or equal to 9')
            else:
                pass

def check_game_yes():
    yes_no = input("Do you want to play the game(yes/no): ")
    yes_no = yes_no.lower()
    if 'yes' in yes_no: 
        user1_sel = input("would you like to start as first user(yes/no): ")
        user1_sel = user1_sel.lower()
        if 'yes' in user1_sel:
            user1_sel = 'X'
            user2_sel = 'O'
            print(f'first player key is "{user1_sel}" and second player key is "{user2_sel}"')
        elif 'no' in user1_sel:
            user2_sel = input("would you like to start as second user(yes/no): ")
            user2_sel = user2_sel.lower()
            if 'yes' in user2_sel:
                user1_sel = 'O'
                user2_sel = 'X'
                print(f'first player key is "{user1_sel}" and second player key is "{user2_sel}"')
            else:
                print("as you haven't selected first user or second user, game quit.....")
                game = False
                return game
    else:
        print("quit game.......")
        game = False
        return game

def game_engine(enginetest):
    usertest = ['X','O']
    choice_num = random.choice(enginetest)
    enginetest.remove(choice_num)
    choice_test = random.choice(usertest)
    if r1[choice_num] != 'X' and r1[choice_num] != 'O':
        r1[choice_num] = choice_test
    else:
        pass

def winner_validation():
    if r1[0] == r1[1] == r1[2] and r1[0] == 'X':
        print('you are the winner')
    elif r1[3] == r1[4] == r1[5] and r1[3] == 'X':
        print('you are the winner')
    elif r1[6] == r1[7] == r1[8] and r1[6] == 'X':
        print('you are the winner')
    else: 
        print('you lose')

r1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
enginetest = [0,1,2,3,4,5,6,7,8]

def all_game():
    click = 1
    game = check_game_yes()
    if game != False:
        display(r1)
        while click <= 9:
            user_input()
            game_engine(enginetest)
            print('Current table is now')
            display(r1)
            winner_validation()
            click += 1
        print("Game is completed")

all_game()


  
#winner_validation()





            

