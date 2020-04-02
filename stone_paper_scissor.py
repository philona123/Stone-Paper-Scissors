# import random module 
import random 
  
# Print multiline instruction 
# performstring concatenation of string 
print("Welcome to the game of Stone, Paper and Scissors!!") 
  
while True: 
    print("ENTER YOUR CHOICE \n 1. STONE \n 2. PAPER \n 3. SCISSOR \n") 
      
    # take the input from user 
    choice = int(input("User turn: ")) 
  
    # OR is the short-circuit operator 
    # if any one of the condition is true 
    # then it return True value 
      
    # looping until user enter invalid input 
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: ")) 
          
  
    # initialize value of choice_name variable 
    # corresponding to the choice value 
    if choice == 1: 
        choice_name = 'Stone'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'
          
    # print user choice  
    print("user choice is: " + choice_name) 
    print("\nNow its computer turn.......") 
  
    # Computer chooses randomly any number  
    # among 1 , 2 and 3. Using randint method 
    # of random module 
    comp_choice = random.randint(1, 3) 
      
    # looping until comp_choice value  
    # is equal to the choice value 
    while comp_choice == choice: 
        comp_choice = random.randint(1, 3) 
  
    # initialize value of comp_choice_name  
    # variable corresponding to the choice value 
    if comp_choice == 1: 
        comp_choice_name = 'Stone'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print("\nComputer choice is: " + comp_choice_name) 
  
    print("\n" + choice_name + " V/s " + comp_choice_name) 
  
    # condition for winning 
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )): 
        print("PAPER WINS! ", end = "") 
        result = "paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("STONE WINS!", end = "") 
        result = "Stone"
    else: 
        print("SCISSOR WINS!", end = "") 
        result = "scissor"
  
    # Printing either user or computer wins 
    if result == choice_name: 
        print("\n<== USER WINS! CONGRATS..! ==>") 
    else: 
        print("\n<== COMPUTER WINS! BETTER LUCK NEXT TIME..! ==>") 
          
    print("Do you want to play again? (Y/N)") 
    ans = input() 
  
  
    # if user input n or N then condition is True 
    if ans == 'n' or ans == 'N': 
        break
      
# after coming out of the while loop 
# we print thanks for playing 
print("\nTHANKS FOR PLAYING")
