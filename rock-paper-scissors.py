import random

emojis = { 'r': '🪨', 'p': '📃','s': '✂️' }

wins = 0
lose = 0
tie = 0

while True:
    moves = ("r","p","s")
    player_move = str(input("Rock,Paper or Scissors (r/p/s): ")).lower()
    if player_move not in moves:
        print("Invalid input")
        continue
    
    computermove = random.choice(moves)
    print(f"The player has {emojis[player_move]}")
    print(f"The computer has {emojis[computermove]}")
    
    
    if player_move == computermove:
        print("Tie")
        tie += 1
        
    elif( 
        (player_move == 'r' and computermove == 's') or 
        (player_move == 's' and computermove == 'p') or 
        (player_move == 'p' and computermove == 'r')):
        print("you win")
        wins += 1
    else:
        print("You loose")
        lose += 1
        
    show_result = input("Wanna check the scores(y/n): ")
    if show_result == 'y':
        print(f"your won {wins} match,You lost {lose} match,You have Tied {tie} match")
        continue
        
    


    should_continue = input("Another Round???(y/n) : ")
    if should_continue == 'n':
        print("Ler's play any other time!!")
        break 

    
