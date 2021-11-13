import turtle
import random

##Main Function
def main():
    """Main Function"""
    # Variable declaration
    s = turtle.Screen()
    s.setup(320, 320)
    s.screensize(300, 300)
    w, h = s.screensize()
    t2 = turtle.Turtle()
    t2.ht()
    t3 = turtle.Turtle()
    t3.ht()
    t4 = turtle.Turtle()
    t4.ht()

    s.tracer(0)
    print(w, h)

    rocket_x_value = -w / 2 + 30
    left_meteor_y_value = h / 2 - 50
    right_meteor_y_value = h / 2 - 80

    ##Set Background Pic##
    def set_background():
        '''Function for Background'''
        s.bgpic("background.gif")
    
    ##Dictionary of Game Objects##
    ''' Dictionary for the Game Objects'''
    game_objects = [{
        "t": turtle.Turtle(),
        "x": 0,
        "y": -h / 2 + 15,
        "radius": 12.5,
        "image": "rocket.gif",
        "type": "player"
    }, {
        "t": turtle.Turtle(),
        "x": random.randint(rocket_x_value, w / 2 - 30),
        "y": h / 2 - 20,
        "radius": 12.5,
        "image": "earth.gif",
        "type": "earth"
    }]

    ##Append the left and right obstacles##
    for i in range(4):
        ''' Append Right Meteor'''
        game_objects.append({
            "t": turtle.Turtle(),
            "x": random.randint(-w / 2 + 30, w / 2 - 30),
            "y": left_meteor_y_value,
            "radius": 12.5,
            "image": "meteor.gif",
            "type": "right_meteor"
        })
        left_meteor_y_value -= 60
    for i in range(3):
        ''' Append Left Meteor'''
        game_objects.append({
            "t": turtle.Turtle(),
            "x": random.randint(-w / 2 + 30, w / 2 - 30),
            "y": right_meteor_y_value,
            "radius": 12.5,
            "image": "meteor.gif",
            "type": "left_meteor"
        })
        right_meteor_y_value -= 60

    ##Display the game images##
    def display_game_images():
        '''Display The Game Images'''
        for obj in game_objects:
            s.addshape(obj["image"])
            obj["t"].shape(obj["image"])

    ###<keypress event handler>###
    ## Function for Up Key##
    def up():
        '''Function for Up Key'''
        if game_objects[0]["y"] <= h / 2 - 25:
            game_objects[0]["t"].setheading(90)
            game_objects[0]["y"] += (30)
    ## Function for Down Key##
    def down():
        '''Function for Down Key'''
        if game_objects[0]["y"] > -h / 2 + 15:
            game_objects[0]["t"].setheading(270)
            game_objects[0]["y"] -= (30)
    ## Function for Left Key##
    def left():
        '''Function for Left Key'''
        if game_objects[0]["x"] > -w / 2 + 12.5:
            game_objects[0]["t"].setheading(180)
            game_objects[0]["x"] -= (30)
    ## Function for Right Key##
    def right():
        '''Function for Right Key'''
        if game_objects[0]["x"] < w / 2 - 15:
            game_objects[0]["t"].setheading(0)
            game_objects[0]["x"] += (30)

    ##Screen listen##
    '''Screen Listen'''
    s.listen()
    s.onkey(
        up, "Up"
    )  # This will call the up function if the "Left" arrow key is pressed
    s.onkey(down, "Down")
    s.onkey(left, "Left")
    s.onkey(right, "Right")

    ##Lives Function##
    def display_lives(lives):
        '''Functions for Lives'''
        t2.penup()
        t2.goto(h / 2 - 15, w / 2 - 15)
        lives = lives
        t2.clear()
        t2.color("green")
        t2.write(f"Lives: {lives}", False, "right", font=("Ariel", 10, "bold"))

    ##Score Function##
    def display_score(score):
        '''Function For Display'''
        t3.penup()
        score = score
        t3.clear()
        t3.goto(w / 2 - 15, -h / 2 + 10)
        t3.color("yellow")
        t3.write(f"Score: {score}", False, "right", font=("Ariel", 10, "bold"))

    ##Level Function###
    def display_level(level):
        '''Function for Levels'''
        t4.penup()
        level = level
        t4.clear()
        t4.goto(w / 2 - 15, -h / 2 + 40)
        t4.color("red")
        t4.write(f"Level: {level}", False, "right", font=("Ariel", 10, "bold"))

    ##Animation Loop##
    def animation_loop():
        '''Animation Loop'''
        game_state = "play"
        ##Remaing Lives##
        remaining_lives = 3
        display_lives(remaining_lives)
        #Score
        score = 0
        display_score(score)
        ##Remaing level##
        level = 1
        display_level(level)
        ##set the Speed of the obstalce##
        left_meteor_speed = .1
        right_meteor_speed = .1

        ##While Animation Loop###
        while game_state != "over":
            '''While Game State'''
            ##Function for End Screen##
            def end_screen():
                '''End Screen'''
                s3 = turtle.Screen()
                t3 = turtle.Turtle()
                s3.bgpic("spaces.gif")
                t3.ht()
                s3.bgcolor("grey")
                t3.penup()
                t3.goto(0, 30)
                t3.color("#E93B81")
                t3.write(f"You Died",
                         False,
                         "center",
                         font=("Ariel", 25, "bold"))
                t3.goto(0, -30)
                t3.color("#DEEDF0")
                t3.write(f"Score: {score}",
                         False,
                         "center",
                         font=("Ariel", 20, "bold"))

            ##Clears the Objects##
            for obj in game_objects:
                '''Cleat the Object'''
                obj["t"].clear()

            ###Moves the obstacles##
            for obj in game_objects:
                '''Moves the Obstacles'''
                if obj["type"] == "right_meteor":
                    obj["x"] += right_meteor_speed
                elif obj["type"] == "left_meteor":
                    obj["x"] -= left_meteor_speed

            ###Edge Condition for obstacles###
            for obj in game_objects:
                '''Edge Condtion For obstacles'''
                if obj["type"] == "right_meteor":
                    if obj["x"] > w / 2 + obj["radius"]:
                        obj["x"] = -w / 2 - obj["radius"]
                if obj["type"] == "left_meteor":
                    if obj["x"] < -w / 2 - obj["radius"]:
                        obj["x"] = w / 2 + obj["radius"]

            ##Sets the position##
            for obj in game_objects:
                '''Set the Position'''
                obj["t"].penup()
                obj["t"].goto(obj["x"], obj["y"])
                obj["t"].pendown()

            ##Update game_lives
            for obj in game_objects[2:]:
                '''Update the Game Lives'''
                ##Check for Collision with the game Obstacles###
                if game_objects[0]["t"].distance(
                        obj["t"]) < obj["radius"] + game_objects[0]["radius"]:
                    game_objects[0]["y"] = -h / 2 + game_objects[0]["radius"]
                    ##Decrement the lives###
                    remaining_lives -= 1
                    display_lives(remaining_lives)
                    ##Ends the game & Display End Screen##
                    if remaining_lives == 0:
                        game_state = "over"
                        s.clear()
                        end_screen()

            ##Check collision with Earth##
            if game_objects[0]["t"].distance(
                    game_objects[1]
                ["t"]) < game_objects[0]["radius"] + game_objects[1]["radius"]:
                game_objects[1]["x"] = random.randint(-w / 2 + 30, w / 2 - 30)
                game_objects[0]["y"] = -h / 2 + game_objects[0]["radius"]
                ##Increment the score!
                score += 100
                display_score(score)
                ##Increment the level
                level += 1
                display_level(level)
                ##Increase the speed
                left_meteor_speed += .1
                right_meteor_speed += .1

    #Display the Objects##
            s.update()

    ##Function for Start Screen##
    def start_screen():
        '''Function for Start Screen'''
        s1 = turtle.Screen()
        s1.bgpic("spaces.gif")
        # s1.bgcolor("grey")
        t1 = turtle.Turtle()
        t1.goto(0, -30)
        t1.color("#28FFBF")
        t1.write("Press Enter to Fly",
                 False,
                 "center",
                 font=("Ariel", 15, "bold"))
        t1.penup()
        t1.goto(0, 30)
        t1.color("#FCFFA6")
        t1.write("Go Back to Earth!",
                 False,
                 "center",
                 font=("Ariel", 15, "bold"))
        t1.hideturtle()

        ##Press Enter to Start Game & Display Object##
        def enter():
            '''Function for Enter'''
            t1.clear()
            set_background()
            display_game_images()
            animation_loop()

        s1.listen()
        s1.onkey(enter, "Return")

    ##First Screen to be displayed##
    start_screen()
    '''First Screen'''

    ##Listen if enter was pressed##
    s.listen()

    s.exitonclick()
main()
