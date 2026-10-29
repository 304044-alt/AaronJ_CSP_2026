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

# Store game data.
score = 0
misses = 0
maximum_misses = 5
game_running = True

star_colors = ["gold", "orange", "hot pink"]
stars = []

# Create the player-controlled basket
basket = turtle.Turtle()
basket.shape("square")
basket.color("deep sky blue")
basket.shapesize(stretch_wid=1, stretch_len=4)
basket.penup()
basket.goto(0, -240)

# Create a turtle for displaying the score
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.color("white")
score_writer.goto(0, 255)

# Create a turtle for instructions and end-game messages
message_writer = turtle.Turtle()
message_writer.hideturtle()
message_writer.penup()
message_writer.color("white")



screen.mainloop()