#!/usr/bin/env python3

#define prompt - 
prompt = "\n  > "

#module imports
import random

#define variables
smalldct={}
valid_answers=valid_answers=range(1,11)
my_roll = ''

#define functions
def check_input(current_roll):
    """
    Checks input and handles exceptions
    """
    if current_roll in valid_answers:
        return True
    if not current_roll in valid_answers and current_roll != "quit":
        print("Valid roll values are numbers 1 - 10.")

my_roll=''                                                            
while my_roll != 'quit':                                              
    print("Enter Lone Wolf's current endurance points.")              
    lw_endurance_start = int(input(prompt))                           
    print("Enter Lone Wolf's combat skill.")                          
    lw_cs = int(input(prompt))                                        
    print("Enter enemy's endurance points.")                          
    op_endurance_start = int(input(prompt))                           
    print("Enter enemy's combat skill.")                              
    op_cs = int(input(prompt))                                        
    round_count=1                                                     
    lw_endurance=lw_endurance_start                                   
    op_endurance=op_endurance_start                                   
    combat_ratio = lw_cs-op_cs                                        
#Apply combat skill math if nonnegative and/or even to accomodate table                                                                     
    if combat_ratio > 0 and combat_ratio  % 2 == 0:                   
        combat_ratio-=1                                           
    elif combat_ratio < 0 and combat_ratio % 2 == 0:                  
        combat_ratio+=1  
    elif combat_ratio < 0 and combat_ratio % 2 == 0:    
        combat_ratio+=1                                           
    print("Begin combat.")                                            
    while True:                                                       
        print("Round " + str(round_count))  
        print("Enter your roll.")                                     
        my_roll = int(input(prompt))
        if check_input(my_roll):                                                                                
            damage_values=(smalldct[combat_ratio][my_roll])
            op_endurance=op_endurance-(damage_values[0])
            lw_endurance=lw_endurance-(damage_values[1])         
            if op_endurance <= 0:                     
               print("Lone Wolf hath slain the enemy!")
                break                                            
            elif lw_endurance <=0:                                        
                print("The enemy hath bested Lone Wolf!")                 
                break                                                     
            else:                                                         
                print("Enemy takes: " + str(damage_values[0]) + " damage =====> Enemy Endurance Points:  " + str(op_endurance))                 
                print("Lone Wolf takes: " + str(damage_values[1]) + " damage =====> Lone Wolf Endurance Points: " + str(lw_endurance))
                round_count+=1


