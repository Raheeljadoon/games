import random
print("rock paper scissor game")
player_1 = input("choose any one from these three rock , paper or scissor  ")
player_choises = ["rock","paper","scissor"]
player_2 =random.choice(player_choises) 
print("player_2 choose" , player_2)

if(player_1 =="rock" and player_2 == "rock"):
   
    print("tie")
elif(player_1 == "rock" and player_2 == "paper"):
    print("player_2 wins")

elif(player_1 == "rock" and player_2 == "scissor"):
    print("player_1 wins")
   