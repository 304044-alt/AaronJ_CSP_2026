import turtle
import random

# Set up the game window
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Catch the Stars")
screen.bgcolor("midnight blue")
screen.tracer(0)

# Store the player's name and clean up the entered string
player_name = screen.textinput("Catch the Stars", "Enter your name:")
if player_name is None or player_name.strip() == "":
    player_name = "Player"
else:
    player_name = player_name.strip().title()[:15]

screen.mainloop()