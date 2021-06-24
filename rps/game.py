import random
while True:
    print("rock paper scissor game")
    player_1 = input("choose any one from these three rock , paper or scissor  ")
    print("you chooser ", player_1)
    player_choises = ["rock","paper","scissor"]
    player_2 =random.choice(player_choises) 
    print("player_2 choose" , player_2)
    if player_1 == player_2:
        print("both choose same its tie ")


    
    if(player_1 == "rock" and player_2 == "paper"):
        print("player_2 wins")

    elif(player_1 == "rock" and player_2 == "scissor"):
        print("player_1 wins")

    if(player_1 == "paper" and player_2 == "scissor"):
        print("player_2 wins")

    elif(player_1 == "paper" and player_2 == "rock"):
        print("player_1 wins")

    

    if(player_1 == "scissor" and player_2 == "paper"):
        print("player_1 wins")

  

    elif(player_1 == "scissor" and player_2 == "rock"):
        print("player_2 wins")
    play_again = input("do you want to play again  y/n  ")
    if play_again == "y":
        continue
    else :
        break


   

   
   

      