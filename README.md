# Simple-Turn-Based-Game
A simple turn based game against an AI as basic as they come for learning purposes. Based off this idea: https://www.reddit.com/r/beginnerprojects/comments/1aw0iq/project_turn_based_pokemon_style_game/
   
GOAL

Write a simple game that allows the user and the computer to take turns selecting moves to use against each other. Both the computer and the player should start out at the same amount of health (such as 100), and should be able to choose between the three moves:

1. The first move should do moderate damage and has a small range (such as 18-25).
1. The second move should have a large range of damage and can deal high or low damage (such as 10-35).
1. The third move should heal whoever casts it a moderate amount, similar to the first move.
1. The fourth move increases next attack by 5.
1. The fifth move increases next heal by 5.

After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. Once the user or the computer's health reaches 0, the game should end.

SUBGOALS

1. When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
1. When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
1. Give each move a name.
1. Make AI's of different difficulty.
