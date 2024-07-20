 # main.py
# 
#- Expected Outcome: The program should be able to take a user's
#mood as input (e.g., happy, sad, excited) and return a corresponding custom message.

import mood_module

mood = input("How are you feeling today? (happy/sad/ambitious/nervous/bored) ")
print(mood_module.mood_response(mood))