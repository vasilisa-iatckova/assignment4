#!/usr/bin/env python

# Imports:
import time
import numpy as np
import pandas as pd

# Variables and Outputs:
quit = False
# Read saved hunger and age data:
df = pd.read_csv('pypet.csv', index_col='variable')
# Keeping time
last_interaction = time.time()
# What our pet looks like
pet = "<O.O>"

# metrics:
hunger = int(df.loc['hunger'].values) 
age = int(df.loc['age'].values) 
happiness = int(df.loc['happiness'].values) # read from csv

# Add interactions:
while (not(quit)):
    # Display pet status:
    print('=================')
    print(pet)
    print('Your pet is {} seconds old'.format(int(age)))
    print('Hunger level: ', hunger)
    print('Happiness level: ', happiness) # check on pet's mood
    if hunger == 100: # otherwise, pet is never VERY hungry
        print('Your pet is VERY hungry')
    elif hunger > 50:
        print('Your pet is hungry')
    
 

    # User input for interactions
    answer = input("What do you want to do? Your options are 'play', 'feed', 'pet', 'quit'. ")
    print("You want to: ", answer)

    # time manager:
    time_passed = time.time() - last_interaction
    age = age + time_passed
    last_interaction = time.time() #Reset last_interaction to now

    # Command manager:
    if (answer == 'quit') or (answer == 'exit'):
        quit = True
    if answer == 'feed':
        hunger = hunger - 20
        print("hunger level: ", hunger)
        if hunger <= 0:
            hunger = 0
            print("Pet is full")
    if answer == 'play':
        print("You played with the pet")
        hunger = hunger + 10 + (40 * np.random.random())
    
    # Hunger manager:
    hunger = hunger + int(time_passed)
    if hunger > 100:
        hunger = 100
    hunger = int(hunger)

    # Happiness manager
    happiness = happiness - int(time_passed)/2
    if happiness <=0:
        happiness = 0
        happiness = int(happiness)
    


df.loc['hunger'] = hunger
df.loc['age'] = age
df.loc['happiness'] = happiness # write to csv
df.to_csv("pypet.csv")