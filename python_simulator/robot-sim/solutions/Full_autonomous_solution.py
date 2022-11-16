                               ############################               
                               ##    RESEARCH TRACK 1    ##
                               ##      ASSIGNMENT 1      ##
                               ##         2022           ##  
                               ##  FULL AUTONOMOUS CODE  ##
                               ############################  

from __future__ import print_function

import time

from sr.robot import *


a_th = 2.0                        # Float: Threshold for the control of the linear distance
d_th = 0.4                        # Float: Threshold for the control of the orientation                                               
Golden_th = 0.6                   # Float: Treshold for the releasing silver token

silver = True                     # Boolean: variable for letting the robot know if it has to look for a silver or for a golden marker

complete = 0      # Integer: variable for letting the robot know how many times it checked if there is any other untaken silver token left

R = Robot()                       # Instance of the classRobot

Taken_tokens = []                 # Array: Hollding offset numbers of the taken silver and golden tokens

####################################################################################################

def drive(speed, seconds):        # Function for setting an angular velocity    

    R.motors[0].m0.power = speed        
    R.motors[0].m1.power = speed  # Args: speed (int): the speed of the wheels     

    time.sleep(seconds)           # Seconds (int): the time interval              

    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

####################################################################################################

def turn(speed, seconds):         # Function for setting an angular velocity   


    R.motors[0].m0.power = speed       
    R.motors[0].m1.power = -speed # Args: speed (int): the speed of the wheels   

    time.sleep(seconds)           # Seconds (int): the time interval             

    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

####################################################################################################

def find_silver_token():          # Function to find the closest silver token and its offset number
                      
    offset_silver=None            # Integer: To return taken offset number of the silver token
    dist=100                      # Maxsimum distance for tokens 

    for token in R.see():           

        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:

            dist=token.dist       # dist (float): distance of the closest silver token (-1 if no silver token is detected)
 	    rot_y=token.rot_y     # rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
	    offset_silver=token.info.offset       # offset_silver (integer): offset number of the closest silver token

    if dist==100:                  

	return -1, -1 , offset_silver

    else:

   	return dist, rot_y , offset_silver

#####################################################################################################

def find_golden_token():          # Function to find the closest golden token and its offset number
                                   
    offset_golden= None           # Integer: To return taken offset number of the golden token
    dist=100                      # Maxsimum distance for tokens 

    for token in R.see():

        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:

            dist=token.dist       # dist (float): distance of the closest silver token (-1 if no silver token is detected)
	    rot_y=token.rot_y     # rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
	    offset_golden=token.info.offset       # offset_golden (integer): offset number of the closest golden token

    if dist==100:

	return -1, -1 ,offset_golden

    else:

   	return dist, rot_y ,offset_golden

#####################################################################################################

while 1:

 if silver == True: # if silver is True, than we look for a silver token, otherwise for a golden one

    	dist, rot_y,offset = find_silver_token()     # Take the return values from find_silver_token() funtion

	if offset in Taken_tokens:                   # Check if the taken silver token offset number is in the Taken_tokens array 

		turn(+40, 0.1)                       # If it is in the Taken_tokens; turn
		print("Looking for not already taken Silver Token")
		complete = complete + 1  
		if complete == 24:   # When coplete equal 24 this mean we turned the robot 360 degree 
				print("I turned 360 degree and couldn`t see any not taken  silver Token")
				print("MISSION COMPLETE")
				exit()                # And the System because there is no any silver token left
	        

	elif dist==-1:                               # if no token is detected, we make the robot turn 

		print("I don't see any token silver token!!")

		turn(+50, 0.1)

	elif dist <d_th:                             # if we are close to the token, we try grab it.

	        print("Found it!")

	        if R.grab():                         # if we grab the token 
			print("Gotcha!")
			Taken_tokens.append(offset)   # Add grapped silver token`s offset to the Taken_token array
  
            		turn(-30,1) 
            		                
            		complete = 0  # Refresh the value of complete
  	    		silver = not silver           # Change the value of the variable silver, so that in the next step we will look for the golden token

		else:

            		print("Aww, I'm not close enough.")

	elif -a_th<= rot_y <= a_th:                  # if the robot is well aligned with the token, we go forward

		print("Closest silver token offset number is: {0} and Distance is: {1}!".format(offset,dist))

        	drive(80, 0.1)

	elif rot_y < -a_th:                          # if the robot is not well aligned with the token, we move it on the left or on the right

	        print("Left a bit...")

        	turn(-5, 0.1)

	elif rot_y > a_th:

	        print("Right a bit...")

	        turn(+5, 0.1)

 else:

	dist, rot_y,offset = find_golden_token()     # Take the return values from find_silver_token() funtion
	if offset in Taken_tokens:                   # Check if the taken golden token offset number is in the Taken_tokens array 

		turn(+40, 0.1)                       # If it is in the Taken_tokens; turn
		print("Looking for not already taken Golden Token")
		
		
			
	elif dist==-1:                               # if no token is detected, we make the robot turn 

		print("I don't see any golden token!!")

		turn(+50, 0.1)

	elif dist <Golden_th:                        # if we are close to the golden token, we try to release silver token

		print("Found it!")

		if R.release():                      # if we released the token

			print("Released!")

			drive(-80,0.3)
	    		
	    		Taken_tokens.append(offset)  # Add grapped silver token`s offset to the Taken_token array
	    		complete = 0 # Refresh the value of complete
     
	    		silver = not silver          # Change the value of the variable silver, so that in the next step we will look for the silver token

		else:

			print("Aww, I'm not close enough.")

	elif -a_th<= rot_y <= a_th:                 # if the robot is well aligned with the token, we go forward

		print("Closest golden token offset number is: {0} and Distance is: {1}!".format(offset,dist))
		
        	drive(80, 0.1)

	elif rot_y < -a_th:                         # if the robot is not well aligned with the token, we move it on the left or on the right

		print("Left a bit...")

        	turn(-5,0.1)

	elif rot_y > a_th:

        	print("Right a bit...")

        	turn(+5, 0.1)




