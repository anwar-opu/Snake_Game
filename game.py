import turtle
import time
import random

# Configuration 
DELAY = 0.1 
segments = []
score = 0  # Initialize score
high_score = 0  # Track the high score

# Set boundaries for walls
BORDER_LIMIT = 290  # Screen size is 600x600; wall limits are at -290 and +290

# List of colors for random food color
food_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange']

# Configure the window
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor('black')
window.setup(width=600, height=600)
window.tracer(0)

# Create the snake head
head = turtle.Turtle()
head.shape('circle')
head.color('orange')
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food for the snake
food = turtle.Turtle()
food.shape('circle')
food.color(random.choice(food_colors))  # Random initial color
food.penup()
food.goto(50, 60)

# Create the score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color('white')
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Function to update score display
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Functions for movement
def go_up():
    if head.direction != "down":  # Prevent going directly backwards
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

# Listen for keyboard input
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")

# Function to move the snake
def move():
    MOVE_BY = 15
    if head.direction == "up":
        current_position_y = head.ycor()
        head.sety(current_position_y + MOVE_BY)
    if head.direction == "down":
        current_position_y = head.ycor()
        head.sety(current_position_y - MOVE_BY)
    if head.direction == "left":
        current_position_x = head.xcor()
        head.setx(current_position_x - MOVE_BY)
    if head.direction == "right":
        current_position_x = head.xcor()
        head.setx(current_position_x + MOVE_BY)

# Function to reset the game after a collision
def reset_game():
    global score, segments
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)  # Move them off-screen

    segments.clear()  # Clear the list of segments
    score = 0  # Reset the score
    update_score()  # Update the score display

# Main game loop
while True:
    window.update()

    # Check for collision with the walls
    if head.xcor() > BORDER_LIMIT or head.xcor() < -BORDER_LIMIT or head.ycor() > BORDER_LIMIT or head.ycor() < -BORDER_LIMIT:
        reset_game()

    # Check if the snake eats food
    if head.distance(food) < 20:
        # Move the food to a random spot
        food.goto(random.randint(-BORDER_LIMIT+10, BORDER_LIMIT+10), random.randint(-BORDER_LIMIT, BORDER_LIMIT))

        # Change food color randomly
        food.color(random.choice(food_colors))

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10

        # Update high score if necessary
        if score > high_score:
            high_score = score

        # Update the score display
        update_score()

    # Move the snake body
    for index in range(len(segments) - 1, 0, -1):
        x_cor = segments[index - 1].xcor()
        y_cor = segments[index - 1].ycor()
        segments[index].goto(x_cor, y_cor)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x_cor = head.xcor()
        y_cor = head.ycor()
        segments[0].goto(x_cor, y_cor)

    move()

    # Slow down the game
    time.sleep(DELAY)

window.mainloop()
