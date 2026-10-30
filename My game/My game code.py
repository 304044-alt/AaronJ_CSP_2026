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

# Define a star shape using points around its center
star_points = [(0, 12), (3, 4), (12, 4), (5, -2), (8, -11),(0, -6), (-8, -11), (-5, -2), (-12, 4), (-3, 4)]
screen.register_shape("falling_star", tuple(star_points))


#Define all game functions
def update_score():
    score_writer.clear()

    score_text = (player_name + " | Score: " + str(score) + " | Misses: " + str(misses) + "/" + str(maximum_misses))

    score_writer.write(score_text,align="center",font=("Arial", 14, "normal"))

def reset_star(star):
    star.goto(random.randint(-270, 270), random.randint(310, 550))

    color_index = random.randint(0, len(star_colors) - 1)
    star.color(star_colors[color_index])

def move_basket(distance):
    if game_running:
        new_x = basket.xcor() + distance
        new_x = max(-250, min(250, new_x))
        basket.setx(new_x)

def move_left():
    move_basket(-30)


def move_right():
    move_basket(30)

def show_game_over():
    message_writer.clear()
    message_writer.goto(0, 20)

    final_message = ("GAME OVER\n Your final score: " + str(score) + "\nPress SPACE to restart")

    message_writer.write(
        final_message,align="center",font=("Arial", 20, "bold"))

def restart_game():
    global score, misses, game_running

    if not game_running:
        score = 0
        misses = 0
        basket.goto(0, -240)
        message_writer.clear()

        for star in stars:
            reset_star(star)

        game_running = True
        update_score()


screen.mainloop()