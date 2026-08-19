# First project: Worm Game
# Created by: Sebatian Nordanger
# Inspired by content creator: TokyoEdtech (Link to YouTube profile: https://www.youtube.com/@TokyoEdTech )
# Documentation used for turtle: https://docs.python.org/3/library/turtle.html

import turtle  # Chosen module for the creation of the Worm Game
import time  # Used for testing purposes: animations, etc.
import random  # Used for game functionalities: Placement of the worm food, etc.


# Different game variables for game functions:
delay = 0.1  # For testing purpose

# Count score:
score_count = 0
high_score_count = 0

# Tracking for game status:
game_run = False
game_pause = False

# Power ups for Worm game:
speed_boost = False
speed_boost_duration = 3  # For how long the speed boost will last
speed_boost_start_time = 0  # When the boost applies, should be no delay to better flow of gameplay


# Specifications for visuals and functionalities:
# Screen specifications:
game_window = turtle.Screen()
game_window.title("Project1: Worm Game (Sebastian Nordanger)")
game_window.bgcolor("grey")
game_window.setup(width=500, height=500)
game_window.tracer(0)  # Turn off automatic screen updates

# Worm head specifications:
worm_head = turtle.Turtle()  # Initialize module
worm_head.speed(0)  # Animation speed of the turtle module
worm_head.shape("circle")
worm_head.color("Green")
worm_head.penup()  # Remove the lines from the objects on screen
worm_head.goto(0, 0)  # Makes it so that the worm starts at the center of the screen, (x, y) coordinate.
worm_head.direction = "stop"  # For testing directions (movement)

# Worm food specifications:
worm_food = turtle.Turtle()
worm_food.speed(0)
worm_food.shape("square")
worm_food.color("red")
worm_food.penup()
worm_food.goto(0, 20)

# Visual score counter specifications:
visual_score = turtle.Turtle()
visual_score.speed(0)
visual_score.shape("square")
visual_score.color("black")
visual_score.penup()
visual_score.hideturtle()
visual_score.goto(0, 210)  # Placement of text on screen

# Speed power-up specifications:
speed_power_up = turtle.Turtle()
speed_power_up.speed(0)
speed_power_up.shape("triangle")
speed_power_up.color("gold")
speed_power_up.penup()
speed_power_up.goto(random.randint(-220, 220), random.randint(-220, 220))

# Start screen specifications:
game_start_screen = turtle.Turtle()
game_start_screen.speed(0)
game_start_screen.shape("square")
game_start_screen.color("blue")
game_start_screen.penup()
game_start_screen.hideturtle()
game_start_screen.goto(0, 200)
game_start_screen.write("Press 'Space' to start! (p:Pause, n:Change Skin)", align="center", font=("Comic Sans MS", 16, "normal"))

# Game over screen specifications:
game_over_screen = turtle.Turtle()
game_over_screen.speed(0)
game_over_screen.shape("square")
game_over_screen.color("red")
game_over_screen.penup()
game_over_screen.hideturtle()
game_over_screen.goto(0, 0)

# Worm Skins:
worm_skins = ["green", "blue", "orange", "purple"]
current_skin_index = 0

# List for containing segments:
body_segment = []


# Functionalities for Worm movement:
def go_up():
    if game_run and worm_head.direction != "down":
        worm_head.direction = "up"


def go_down():
    if game_run and worm_head.direction != "up":
        worm_head.direction = "down"


def go_left():
    if game_run and worm_head.direction != "right":
        worm_head.direction = "left"


def go_right():
    if game_run and worm_head.direction != "left":
        worm_head.direction = "right"


def move():
    if worm_head.direction == "up":
        y = worm_head.ycor()
        worm_head.sety(y + 20)

    if worm_head.direction == "down":
        y = worm_head.ycor()
        worm_head.sety(y - 20)

    if worm_head.direction == "left":
        x = worm_head.xcor()
        worm_head.setx(x - 20)

    if worm_head.direction == "right":
        x = worm_head.xcor()
        worm_head.setx(x + 20)


# Functions for game controls:
def start_game():
    global game_run, game_pause, score_count, high_score_count, delay  # Using "global" to change variable values outside of scope
    # Clear messages from screen:
    game_over_screen.clear()
    game_start_screen.clear()

    worm_head.goto(0, 0)
    worm_head.direction = "stop"
    score_count = 0
    update_score()
    game_run = True
    delay = 0.1  # Use of delay, to smoothen transition of new game
    game_pause = False
    change_skin()


def pause_game():
    global game_pause
    if game_run:
        game_pause = not game_pause  # Sets the game to pause


def game_over():
    global game_run
    game_run = False
    game_over_screen.write("Game Over! (Press 'Space' to Restart)", align="center", font=("Comic Sans MS", 20, "normal"))


def update_score():
    visual_score.clear()
    visual_score.write("Score:  {}  High Score:  {}".format(score_count, high_score_count), align="center",
                           font=("Comic Sans MS", 15, "normal"))  # Tells what the score and high score is on the screen


# Functions for worm skins:
# Change worm skin:
def change_skin():
    worm_head.color(worm_skins[current_skin_index])

# Cycle through worm skins:
def next_skin():
    global current_skin_index
    current_skin_index = (current_skin_index + 1) % len(worm_skins)
    change_skin()


# Keyboard bindings:
game_window.listen()
game_window.onkeypress(go_up, "w")
game_window.onkeypress(go_up, "W")
game_window.onkeypress(go_down, "s")
game_window.onkeypress(go_down, "S")
game_window.onkeypress(go_left, "a")
game_window.onkeypress(go_left, "A")
game_window.onkeypress(go_right, "d")
game_window.onkeypress(go_right, "D")
game_window.onkeypress(start_game, "space")
game_window.onkeypress(pause_game, "p")
game_window.onkeypress(pause_game, "P")
game_window.onkeypress(next_skin, "n")
game_window.onkeypress(next_skin, "N")


# Loop for the Main game:
while True:
    game_window.update()

    if game_pause:
        continue  # Will skip the rest of the loop if game is paused

    if game_run:
        # Check for collision (border):
        if worm_head.xcor() > 275 or worm_head.xcor() < -275 or worm_head.ycor() > 275 or worm_head.ycor() < -275:
            time.sleep(1)

            # Hide the segments:
            for segment in body_segment:
                segment.goto(1000, 1000)  # Hides outside the screen

            # Removes the segments, so that it resets upon going out of the screen:
            body_segment.clear()

            game_over()

    # Check for collision (food):
    if worm_head.distance(worm_food) < 20:
        # Directions for the movement of the food (Preventing it from going outside the screen (x and y values)):
        x = random.randint(-220, 220)
        y = random.randint(-220, 220)
        worm_food.goto(x, y)

        # Add segments to the body of the worm:
        new_body_segment = turtle.Turtle()
        new_body_segment.speed(0)
        new_body_segment.shape("circle")
        new_body_segment.color("blue")
        new_body_segment.penup()  # Avoid drawn lines
        body_segment.append(new_body_segment)

        # Shorten delay when body getting to big with turtle module:
        delay -= 0.001

        # Increase the score when food eaten:
        score_count += 1

        if score_count > high_score_count:
            high_score_count = score_count

        update_score()

    # Check for collision (speed boost power-up):
    if worm_head.distance(speed_power_up) < 20:
        speed_power_up.goto(random.randint(-220, 220), random.randint(-220, 220))
        speed_boost = True
        speed_boost_start_time = time.time()
        delay = 0.06  # Increases the speed of the worm

    # Move the end segment for the worm body first in reverse order:
    for i in range(len(body_segment) - 1, 0, -1):
        x = body_segment[i - 1].xcor()
        y = body_segment[i - 1].ycor()
        body_segment[i].goto(x, y)

    # Move segment 0 (segment after the head) to where the head is:
    if len(body_segment) > 0:
        x = worm_head.xcor()
        y = worm_head.ycor()
        body_segment[0].goto(x, y)

    move()

    # Check for collision (body):
    for segment in body_segment:
        if segment.distance(worm_head) < 20:
            time.sleep(1)

            for segment in body_segment:
                segment.goto(1000, 1000)

            body_segment.clear()

            game_over()

    # Check speed boost status:
    if speed_boost and time.time() - speed_boost_start_time > speed_boost_duration:
        speed_boost = False
        delay = 0.1  # Resets to normal speed

    time.sleep(delay)


game_window.mainloop()  # Keep the window open

