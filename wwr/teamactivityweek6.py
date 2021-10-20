#Author: Joseph Carlson
#Purpose: To determine if someone can ride a roller coaster.

#Inputs from user.
#height_first_rider = int(input('How tall is the first rider? '))
#age_first_rider = input('How old are you? ')
#number_riders = input('How many riders are there? ')
is_there_second_rider = (input('Is there a second rider? ') == "yes")
height_second_rider = int(input('How tall is the second rider? '))
#age_second = input('How old is the second rider? ')

can_ride = False

height_first_rider = int(input('How tall is the first rider? '))
age_first_rider = int(input('How old are you? '))

if is_there_second_rider == "yes":
    height_second_rider = int(input('How tall is the second rider? '))
    age_second = int(input('How old is the second rider? '))

if height_first_rider < 36 or height_second_rider < 36:
    can_ride = False






    




