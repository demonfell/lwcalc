#!/usr/bin/env python3

#define variables
smalldct={}
valid_answers=valid_answers=range(1,11)
my_roll = ''
prompt = "\n  > "

#define functions
def check_input(current_roll):
    """
    Checks input and handles exceptions
    """
    if current_roll in valid_answers:
        return True
    if not current_roll in valid_answers and current_roll != "quit":
        print("Valid roll values are numbers 1 - 10.")

#define combat results table as dictionary
smalldct = {-11:{1:(0,100),2:(0,100),3:(0,8),4:(0,8),5:(1,7),6:(2,6),7:(3,5),8:(4,4),9:(5,3),10:(6,0)}, 
-9:{1:(0,100),2:(0,8),3:(0,7),4:(1,7),5:(2,6),6:(3,6),7:(4,5),8:(5,4),9:(6,3),10:(7,0)},
-7:{1:(0,8),2:(0,7),3:(1,6),4:(2,6),5:(3,6),6:(4,5),7:(5,4),8:(6,3),9:(7,2),10:(8,0)},
-5:{1:(0,6),2:(1,6),3:(2,5),4:(3,5),5:(4,4),6:(5,4),7:(6,3),8:(7,2),9:(8,0),10:(9,0)},
-3:{1:(1,6),2:(2,5),3:(3,5),4:(4,4),5:(5,4),6:(6,3),7:(7,2),8:(8,1),9:(9,0),10:(10,0)},
-1:{1:(2,5),2:(3,5),3:(4,4),4:(5,4),5:(6,3),6:(7,2),7:(8,2),8:(9,1),9:(10,0),10:(11,0)},
0:{1:(3,5),2:(4,4),3:(5,4),4:(6,3),5:(7,2),6:(8,2),7:(9,1),8:(10,0),9:(11,0),10:(12,0)},
1:{1:(4,5),2:(5,4),3:(6,3),4:(7,3),5:(8,2),6:(9,2),7:(10,1),8:(11,0),9:(12,0),10:(14,0)},
3:{1:(5,4),2:(6,3),3:(7,3),4:(8,2),5:(9,2),6:(10,2),7:(11,1),8:(12,0),9:(14,0),10:(16,0)},
5:{1:(6,4),2:(7,3),3:(8,3),4:(9,2),5:(10,2),6:(11,1),7:(12,0),8:(14,0),9:(16,0),10:(18,0)},
7:{1:(7,4),2:(8,3),3:(9,2),4:(10,2),5:(11,1),6:(12,1),7:(14,0),8:(16,0),9:(18,0),10:(100,0)},
9:{1:(8,3),2:(9,3),3:(10,),4:(11,2),5:(12,2),6:(14,1),7:(16,0),8:(18,0),9:(100,0),10:(100,0)},
11:{1:(9,3),2:(10,2),3:(11,2),4:(12,2),5:(14,1),6:(16,1),7:(18,0),8:(100,0),9:(100,0),10:(100,0)}}

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


