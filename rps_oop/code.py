import random
choicess = ["rock","paper","scissor"]

class player_1():
    
    def choose() :
        choicess = ["rock","paper","scissor"]
        player_1_choose = random.choice(choicess)
        return player_1_choose

class player_2():
    def choose():
        player_2_choose = random.choice(choicess)
        return player_2_choose

class Game():
    def compare_choice(self,player_1,player_2):
        if player_1 == "rock" and player_2 == "paper" or player_1 == "paper" and player_2 == "scissor":

            return "player_2 "
    
        elif player_1 == "rock" and player_2 == "scissor" or player_1 == "scissor" and player_2 == "paper":
            return "player_1 "
            
        elif player_1 == player_2:
            return "tie"

    def play(self):
        player_1_ch = player_1.choose()
        player_2_ch = player_2.choose()
        result = self.compare_choice(player_1_ch,player_2_ch)
        if result == "player_2 ":
            print("player_1 choose",player_1_ch ,"and player_2 choose" , player_2_ch)
            print("player_2 wins")
        elif  result == "player_1 ":
            print("player_1 choose",player_1_ch ,"and player_2 choose" , player_2_ch) 
            print("player_1 wins")

        elif result == "tie":
            
            print("player_1 choose",player_1_ch ,"and player_2 choose" , player_2_ch)
            print("both choose same its tie")
game = Game()
game.play()
