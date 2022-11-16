                               ###########################               
                               ##   RESEARCH TRACK 1    ##
                               ##      ASSIGNMENT 1     ##
                               ##         2022          ##  
                               ##  NOT AUTONOMOUS CODE  ##
                               ###########################  

from __future__ import print_function

import time

from sr.robot import *

a_th = 2.0                                     # Float: Threshold for the control of the linear distance                                 
d_th = 0.4                                     # Float: Threshold for the control of the orientation                                               

silver = True                                  # Boolean: variable for letting the robot know if it has to look for a silver or for a golden marker
R = Robot()                                    # Instance of the classRobot

silver_tokens_offset_number = [3,2,1,0,5,4]    # Array: All offset numbers of the silver tokens already added to the array manually 
golden_tokens_offset_number = [11,10,9,8,7,6]  # Array: All offset numbers of the golden tokens already added to the array manually
a=0                                            # Integer: To find out how many silver token taken
b=0                                            # Integer: To find out how many golden token taken





###############################################################################################

def drive (speed, second):                     # Function for setting an angular velocity 
    
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed               # Args: speed (int): the speed of the wheels

    time.sleep(second)                         # Seconds (int): the time interval

    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

###############################################################################################

def turn (speed, second):                      # Function for setting an angular velocity 
    
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed              # Args: speed (int): the speed of the wheels

    time.sleep(second)                         # Seconds (int): the time interval

    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

###############################################################################################

def find_silver_token(offset):                 # Function to find dist and rot_y values of the given offset number of the silver token
   
    dist=100                                   # Maxsimum distance for tokens
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and token.info.offset == offset:
            dist=token.dist                    # dist (float): distance of the closest silver token (-1 if no silver token is detected)
	    rot_y=token.rot_y                  # rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

###############################################################################################

def find_golden_token(offset_golden):          # Function to find dist and rot_y values of the given offset number of the golden token

    dist=100                                   # Maxsimum distance for tokens
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and token.info.offset == offset_golden:
            dist=token.dist                    # dist (float): distance of the closest golden token (-1 if no golden token is detected)
	    rot_y=token.rot_y                  # rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected) 
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

###############################################################################################

while 1:
    
 if silver == True:                            # if silver is True, than we look for a silver token, otherwise for a golden one
    	 
	dist, rot_y = find_silver_token(silver_tokens_offset_number[a]) # Get dist and rot_y values of the given offset number of the silver token
	if dist==-1:                           # if no token is detected, we make the robot turn 
		print("I don't see any token!!")
		turn(+50, 0.1)
    	elif dist <d_th:                       # if we are close to the token, we try grab it.
        	print("Found it!")
        	if R.grab():                   # Grab silver token
            		print("Gotcha!")
	    		
                      
	    		silver = not silver    # Change the value of the variable silver, so that in the next step we will look for the golden token
		else:
            		print("Aww, I'm not close enough.")
    	elif -a_th<= rot_y <= a_th:           # if the robot is well aligned with the token, we go forward
		print("Ah, that'll do.")
        	drive(80, 0.1)
    	elif rot_y < -a_th:                   # if the robot is not well aligned with the token, we move it on the left or on the right
        	print("Left a bit...")
        	turn(-2, 0.5)
    	elif rot_y > a_th:
        	print("Right a bit...")
        	turn(+2, 0.5)

 else:
	dist, rot_y = find_golden_token(golden_tokens_offset_number[b]) # Get dist and rot_y values of the given offset number of the silver token
    	if dist==-1:                          # if no token is detected, we make the robot turn 
		print("I don't see any token!!")
		turn(+50, 0.1)
    	elif dist <0.6:                       # if we are close to the token, we try grab it.
        	print("Found it!")
        	if R.release():               # if we released the token
        	
            		print("Gotcha!")
	    		drive(-80,0.3)
	    		b=b+1                 # We arrived to golden token and add 
	    		a=a+1
	    		silver = not silver   # Change the value of the variable silver, so that in the next step we will look for the silver token
		else:
            		print("Aww, I'm not close enough.")
    	elif -a_th<= rot_y <= a_th:          # if the robot is well aligned with the token, we go forward
		print("Ah, that'll do.")
        	drive(80, 0.1)
    	elif rot_y < -a_th:                  # if the robot is not well aligned with the token, we move it on the left or on the right
        	print("Left a bit...")
        	turn(-2, 0.5)
    	elif rot_y > a_th:
        	print("Right a bit...")
        	turn(+2, 0.5)

 if a == 6 and b == 6:                   # if we take all 6 silver tokens and used all 6 golden tokens our Mission is done we can end the system
    		
    		print("Well done assignment completed successfully")
    		exit()





        
