"""
-------------------------------------------------------------------------------
Name:		master.py
Purpose:		
The final version of Astronauts VS Aliens, an arcade game!

Author:		Gu.C and Shu.S

Created:	26/01/2020
------------------------------------------------------------------------------
"""

import random
import arcade

# the dimensions of our screen
WIDTH = 1000
HEIGHT = 750

# empty lists set up to calculate positions of dropping/shot objects
human_x_positions = []
human_y_positions = []
alien_x_positions = []
alien_y_positions = []

human_meteor_x_positions = []
human_meteor_y_positions = []
alien_meteor_x_positions = []
alien_meteor_y_positions = []

human_x_positions_shooting_star = []
human_y_positions_shooting_star = []
alien_x_positions_shooting_star = []
alien_y_positions_shooting_star = []

human_x_positions_laser = []
human_y_positions_laser = []
alien_x_positions_laser = []
alien_y_positions_laser = []

# number of objects that will drop from the top
draw_enemy_rate = 4
draw_meteor_rate = 2
draw_shooting_star_rate = 1

# the speed at which objects will drop
game_speed = 3

# the time elapsed after the pressing of the spacebar to run the game
elapsed_time = 0

# boolean values to control the progress of various game screens
start_game = True
run_game = False
final_stage_game = False
end_game = False

# coordinates of the spaceships at the beginning of the game
spaceship_human_x = 750
spaceship_human_y = 100
spaceship_alien_x = 250
spaceship_alien_y = 100

#set width and height for each object in the game
alien_width = 60
alien_height = 74
human_width = 60
human_height = 80
human_spaceship_width = 130
human_spaceship_height = 50
alien_spaceship_width = 130
alien_spaceship_height = 50
human_shooting_star_width = 35
human_shooting_star_height = 26
alien_shooting_star_width = 35
alien_shooting_star_height = 26

# set laser positions 
x_human_laser = 0
y_human_laser = 0
x_alien_laser = 0
y_alien_laser = 0

# booleans to compute if a key has been pressed
up_pressed_human = False
left_pressed_human = False
right_pressed_human = False
fire_laser_human = False
up_pressed_alien = False
left_pressed_alien = False
right_pressed_alien = False
fire_laser_alien = False

# counts the number of points accumulated by the player
alien_points = 0
human_points = 0

# counts the number of times each spaceship is hit by 
human_times_hit = 0
alien_times_hit = 0

# delay counter system -- allows for shooting stars to only appear every 10 seconds
human_shooting_star_delay_counter = 0
alien_shooting_star_delay_counter = 0
human_shooting_star_start_time = 0
alien_shooting_star_start_time = 0

# increases the number of enemies/meteors that fall after certain time intervals
if 19.00 < elapsed_time < 21.00 or 39.00 < elapsed_time < 41.00:
    draw_enemy_rate += 1
    draw_meteor_rate += 1

for _ in range(draw_enemy_rate): # this is the repeat for the falling astronauts/aliens
    # generate random x and y values
    x_human = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human = random.randrange(HEIGHT, HEIGHT * 2)
    x_alien = random.randrange(75, WIDTH/2 - 75)
    y_alien = random.randrange(HEIGHT, HEIGHT * 2)
    # append the x and y values to the appropriate list
    human_x_positions.append(x_human)
    human_y_positions.append(y_human)
    alien_x_positions.append(x_alien)
    alien_y_positions.append(y_alien)

for _ in range(draw_meteor_rate): # this is the repeat for the falling meteors
    # generate random x and y values
    x_human_meteor = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human_meteor = random.randrange(HEIGHT, HEIGHT + 50)
    x_alien_meteor = random.randrange(75, WIDTH/2 - 75)
    y_alien_meteor = random.randrange(HEIGHT, HEIGHT + 50)
    # append the x and y values to the appropriate list
    human_meteor_x_positions.append(x_human_meteor)
    human_meteor_y_positions.append(y_human_meteor)
    alien_meteor_x_positions.append(x_alien_meteor)
    alien_meteor_y_positions.append(y_alien_meteor)

for _ in range(draw_shooting_star_rate): # this is the repeat for the shooting stars
    # generate random x and y values
    x_human_shooting_star = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human_shooting_star = random.randrange(HEIGHT, HEIGHT + 50)
    x_alien_shooting_star = random.randrange(75, WIDTH/2 - 75)
    y_alien_shooting_star = random.randrange(HEIGHT, HEIGHT + 50)
    # append the x and y values to the appropriate list
    human_x_positions_shooting_star.append(x_human_shooting_star)
    human_y_positions_shooting_star.append(y_human_shooting_star)
    alien_x_positions_shooting_star.append(x_alien_shooting_star)
    alien_y_positions_shooting_star.append(y_alien_shooting_star)

def update(delta_time: float):
    """computes what is drawn or run in the game at a given time
    
    Arguments:
        delta_time {float} -- represents a duration of time
    
    Returns:
        updated drawings for humans, aliens, meteors, shooting stars, human and alien lasers, and human and alien spaceships 
    
    """
    global elapsed_time, draw_enemy_rate, draw_meteor_rate, game_speed, run_game
    global human_shooting_star_delay_counter, alien_shooting_star_delay_counter
    global human_shooting_star_start_time, alien_shooting_star_start_time, human_hit, alien_hit
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, spaceship_human_x, spaceship_alien_x

    if run_game or final_stage_game: # events apply for both the normal game and the final stage
        
        # calculates elapsed_time based on delta_time variable
        elapsed_time += delta_time
        elapsed_time = round(elapsed_time, 2)

        # allows for the spaceships to move left and right with respective key presses
        if left_pressed_human:
            spaceship_human_x -= 5
            if spaceship_human_x < 570:
                spaceship_human_x = 570

        if left_pressed_alien:
            spaceship_alien_x -= 5
            if spaceship_alien_x < 60:
                spaceship_alien_x = 60

        if right_pressed_human:
            spaceship_human_x += 5
            if spaceship_human_x > 940:
                spaceship_human_x = 940

        if right_pressed_alien:
            spaceship_alien_x += 5
            if spaceship_alien_x > 430:
                spaceship_alien_x = 430

        removed_human_lasers = 0
        for index in range(len(human_y_positions_laser)):
            if human_y_positions_laser[index - removed_human_lasers] < 765:
                human_y_positions_laser[index - removed_human_lasers] += 30
            else:
                del human_x_positions_laser[index - removed_human_lasers]
                del human_y_positions_laser[index - removed_human_lasers]
                removed_human_lasers += 1

        removed_alien_lasers = 0
        for index in range(len(alien_y_positions_laser)):
            if alien_y_positions_laser[index - removed_alien_lasers] < 765:
                alien_y_positions_laser[index - removed_alien_lasers] += 30
            else:
                del alien_x_positions_laser[index - removed_alien_lasers]
                del alien_y_positions_laser[index - removed_alien_lasers]
                removed_alien_lasers += 1 
        
        if run_game == True: # these elements only happen after space is pressed to start the game

            # controls how fast the aliens/humans, meteors, and stars fall
            # generates a new alien/human, meteor, or star after they reach the bottom of the screen
            for index in range(len(human_y_positions)):
                human_y_positions[index] -= game_speed

                if human_y_positions[index] < 0:
                    human_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 50)
                    human_x_positions[index] = random.randrange(WIDTH/2 + 75, WIDTH - 75)

            for index in range(len(alien_y_positions)):
                alien_y_positions[index] -= game_speed

                if alien_y_positions[index] < 0:
                    alien_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 50)
                    alien_x_positions[index] = random.randrange(75, WIDTH/2 - 75)

            for index in range(len(human_meteor_y_positions)):
                human_meteor_y_positions[index] -= game_speed

                if human_meteor_y_positions[index] < 0:
                    human_meteor_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 50)
                    human_meteor_x_positions[index] = random.randrange(WIDTH/2 + 75, WIDTH - 75)

            for index in range(len(alien_meteor_y_positions)):
                alien_meteor_y_positions[index] -= game_speed

                if alien_meteor_y_positions[index] < 0:
                    alien_meteor_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 50)
                    alien_meteor_x_positions[index] = random.randrange(75, WIDTH/2 - 75)


            # starts a counter between each time a new shooting star should appear
            human_shooting_star_delay_counter += delta_time
            alien_shooting_star_delay_counter += delta_time

            # allows for shooting stars to appear only after 60 seconds of elapsed gameplay *FIX THIS*
            if elapsed_time > 60.00:
                for index in range(len(human_y_positions_shooting_star)):
                    human_y_positions_shooting_star[index] -= game_speed

                    if human_y_positions_shooting_star[index] < 0:
                        if human_shooting_star_start_time == 0:
                            human_shooting_star_start_time = human_shooting_star_delay_counter
                        elif human_shooting_star_delay_counter - human_shooting_star_start_time > 10:
                            human_shooting_star_start_time = 0
                            human_y_positions_shooting_star[index] = random.randrange(HEIGHT, HEIGHT + 50)
                            human_x_positions_shooting_star[index] = random.randrange(WIDTH/2 + 75, WIDTH - 75)

                for index in range(len(alien_y_positions_shooting_star)):
                    alien_y_positions_shooting_star[index] -= game_speed

                    if alien_y_positions_shooting_star[index] < 0:
                        if alien_shooting_star_start_time == 0:
                            alien_shooting_star_start_time = alien_shooting_star_delay_counter
                        elif alien_shooting_star_delay_counter - alien_shooting_star_start_time > 10:
                            alien_shooting_star_start_time = 0
                            alien_y_positions_shooting_star[index] = random.randrange(HEIGHT, HEIGHT + 50)
                            alien_x_positions_shooting_star[index] = random.randrange(75, WIDTH/2 - 75)

            # increases the game speed after time intervals, where the game "levels-up"
            if 19.99 <= elapsed_time <= 20.00 or 39.99 <= elapsed_time <= 40.00:
                game_speed += 0.5
            elif elapsed_time > 60.00:
                game_speed = 5
        

def draw_main_screen(x: int, y: int):
    """"computes if the starting screen is drawn 
    
    Arguments:
        x {int} -- between 0 and 1000 inclusive 
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        a simple but artistic start screen with alien, human and meteor animation
    
    """  
    # coordinates of elements on the main screen
    main_screen_alien_x = 10
    main_screen_alien_y = 10
    main_screen_human_x = 10
    main_screen_human_y = 740
    main_screen_meteor1_x = 0
    main_screen_meteor2_x = 1000
    main_screen_meteor1_degree = 0
    main_screen_meteor2_degree = 0

    # sets a new background, draws title text
    scale = 0.3
    texture = arcade.load_texture("space.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)

    arcade.draw_text("Welcome to...", 385, 600, arcade.color.BLACK, 25)
    arcade.draw_text("ASTRONAUTS VS ALIENS!", 30, 375, arcade.color.BLACK, 65)
    arcade.draw_text("press space to start", 350, 130, arcade.color.BLACK, 25)

    # creates animations for the flying astronauts, aliens, and meteors at the beginning
    if main_screen_alien_x < 500:
        main_screen_alien_x += 3
        main_screen_alien_y += 4
    elif main_screen_alien_x >= 500:
        main_screen_alien_x += 3
        main_screen_alien_y -= 4

    scale = 0.08
    texture = arcade.load_texture("alien.png")
    arcade.draw_texture_rectangle(main_screen_alien_x, main_screen_alien_y, scale * texture.width,
                                  scale * texture.height, texture, 0)

    if main_screen_human_x < 500:
        main_screen_human_x += 3
        main_screen_human_y -= 4
    elif main_screen_human_x >= 500:
        main_screen_human_x += 3
        main_screen_human_y += 4

    scale = 0.08
    texture = arcade.load_texture("astronaut.png")
    arcade.draw_texture_rectangle(main_screen_human_x, main_screen_human_y, scale * texture.width,
                                  scale * texture.height, texture, 0)

    if main_screen_alien_x > 1000:
        main_screen_meteor1_x += 5
        main_screen_meteor2_x -= 5
        main_screen_meteor1_degree += 5
        main_screen_meteor2_degree -= 5

        scale = 0.08
        texture = arcade.load_texture("meteor.png")
        arcade.draw_texture_rectangle(main_screen_meteor1_x, 250, scale * texture.width,
                                      scale * texture.height, texture, main_screen_meteor1_degree)

        scale = 0.08
        texture = arcade.load_texture("meteor.png")
        arcade.draw_texture_rectangle(main_screen_meteor2_x, 525, scale * texture.width,
                                      scale * texture.height, texture, main_screen_meteor2_degree)


def draw_end_screen(x: int, y: int):
    """"determines if the end screen is drawn 
    
    Arguments:
        x {int} -- between 0 and 1000 inclusive 
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        an eye pleasing end screen 
    
    """
    global alien_points, human_points, elapsed_time

    # sets a new background, draws end game text
    scale = 1.1
    texture = arcade.load_texture("space2.jpg")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)

    arcade.draw_text("GAME OVER!", 270, 500, arcade.color.WHITE, 65)
    arcade.draw_text("press enter to restart", 350, 100, arcade.color.WHITE, 25)

    # computes who won the game based on lives lost/points gathered, and draws the appropriate text
    if human_times_hit >= 3:
        arcade.draw_text("The Humans have Won Control!", 
                        175, 400, arcade.color.WHITE, 40)
    elif alien_times_hit >= 3:
        arcade.draw_text("The Aliens have Won Control!", 
                        200, 400, arcade.color.WHITE, 40)
    elif alien_points > human_points:
        arcade.draw_text("The Humans have Won Control!", 
                        200, 400, arcade.color.WHITE, 40)
    elif human_points > alien_points:
        arcade.draw_text("The Aliens have Won Control!", 
                        175, 400, arcade.color.WHITE, 40)
    else:
        arcade.draw_text("It's a tie! Peace has been achieved.", 
                                150, 400, arcade.color.BLACK, 40)
        arcade.draw_text("For now...", 800, 350, arcade.color.BLACK, 25)


def draw_background(x: int, y: int):
    """"determines if a background image is drawn
    
    Arguments:
        x {int} -- between 0 and 1000 inclusive 
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        a beautiful space image is drawn as the background of our game 
    
    """
    # draws a night sky background for the running of the game
    scale = 1
    texture = arcade.load_texture("night_sky.jpg")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def alien_points_counter():
    """"computes and shows the number of points for the human spaceship side (the side shooting the aliens)
    
    Returns:
        arcade drawing of the number of points the player has accumulated so far
    
    """
    # draws the point counter for the side where aliens are falling
    arcade.draw_text("Points: " + str(alien_points),
                     50, 600, arcade.color.WHITE, 15)


def human_points_counter():
    """"computes and shows the number of points for the alien spaceship side (the side shooting the humans)
    
    Returns:
        arcade drawing of the number of points the player has accumulated so far
    
    """
    # draws the point counter for the side where astronauts are falling
    arcade.draw_text("Points: " + str(human_points),
                     880, 600, arcade.color.WHITE, 15)


def lives(x: int, y: int):
    """"drawns out the heart images to represent player lives
    
    Arguments:
        x {int} -- between 62 and 940 inclusive 
        y {int} -- stationed at 580
    
    Returns:
        arcade drawing of the number of lives a given player has left
    
    """
    # draws the 3 hearts (lives) for the side where aliens are falling
    scale = 0.06
    texture = arcade.load_texture("heart.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_human(x: int, y: int):
    """"draws humans
    
    Arguments:
        x {int} -- between 505 and 1000 inclusive
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        picture of an astronaut set to a certain scale
    
    """
    # draws a small human that will fall
    scale = 0.05
    texture = arcade.load_texture("astronaut.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_alien(x: int, y: int):
    """"draws aliens
    
    Arguments:
        x {int} -- between 0 and 495 inclusive
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        picture of an alien set to a certain scale
    
    """
    # draws a small alien that will fall
    scale = 0.05
    texture = arcade.load_texture("alien.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_human_laser(x: int, y: int):
    """"draws lasers to hit the humans 
    
    Arguments:
        x {int} -- between 505 and 1000 inclusive
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        picture of a laser set to a certain scale
    
    """
    # draws a laser image that will be used when shooting astronauts
    scale = 0.1
    texture = arcade.load_texture("laser.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_alien_laser(x: int, y: int):
    """"draws lasers to hit the aliens 
    
    Arguments:
        x {int} -- between 0 and 495 inclusive
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        picture of a laser set to a certain scale
    
    """
    # draws a laser image that will be used when shooting aliens
    scale = 0.1
    texture = arcade.load_texture("laser.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_human_meteor(x: int, y: int):
    """"draws meteors for the human side of the game
    
    Arguments:
        x {int} -- between 505 and 1000 inclusive
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        picture of a meteor that is set to a certain scale 
    
    """
    # draws a meteor image that will fall with the falling humans

    scale = 0.05
    texture = arcade.load_texture("meteor.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_alien_meteor(x: int, y: int):
    """"draws meteors for the alien side of the game 
    
    Arguments:
        x {int} -- between 0 and 495 inclusive
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        picture of a meteor that is set to a certain scale 
    
    """
    # draws a meteor image that will fall with the falling aliens
    scale = 0.05
    texture = arcade.load_texture("meteor.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_human_shooting_star(x: int, y: int):
    """"draws shooting stars for the human side of the game
    
    Arguments:
        x {int} -- between 505 and 1000 inclusive
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        picture of a shooting star that is set to a certain scale 
    
    """
    # draws a shooting star image that will fall with the falling humans
    scale = 0.06
    texture = arcade.load_texture("shooting star.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, - 20)


def draw_alien_shooting_star(x: int, y: int):
    """"draws shooting stars for the alien side of the game 
    
    Arguments:
        x {int} -- between 0 and 495 inclusive
        y {int} -- between 0 and 750 inclusive
    
    Returns:
        picture of a shooting star that is set to a certain scale 
    
    """
    # draws a meteor image that will fall with the falling aliens
    scale = 0.06
    texture = arcade.load_texture("shooting star.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, - 20)


def draw_spaceship_human(x: int, y: int):
    """"draws a spaceship for the human side of the game
    
    Arguments:
        x {int} -- between 505 and 1000 inclusive
        y {int} -- stationed at 100
    
    Returns:
        picture of a spaceship that is set to a certain scale 
    
    """
    # draws a spaceship image that will be controlled to shoot humans
    scale = 0.4
    texture = arcade.load_texture("spaceship.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_spaceship_alien(x: int, y: int):
    """"draws a spaceship for the alien side of the game 
    
    Arguments:
        x {int} -- between 0 and 495 inclusive
        y {int} -- stationed at 100
    
    Returns:
        picture of a spaceship that is set to a certain scale 
    
    """
    # draws a spaceship image that will be controlled to shoot aliens
    scale = 0.4
    texture = arcade.load_texture("spaceship.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_final_human(x: int, y: int):
    """"draws a big astronaut for the final stage
    
    Arguments:
        x {int} -- stationed at 750
        y {int} -- stationed at 375
    
    Returns:
        picture of an astronaut that is set to a certain scale 
    
    """
    # draws an astronaut image that will be shot in the final stage
    scale = 0.3
    texture = arcade.load_texture("astronaut.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def draw_final_alien(x: int, y: int):
    """"draws a big alien for the final stage
    
    Arguments:
        x {int} -- stationed at 250
        y {int} -- stationed at 375
    
    Returns:
        picture of an alien that is set to a certain scale 
    
    """
    # draws an alien image that will be shot in the final stage
    scale = 0.3
    texture = arcade.load_texture("alien.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width,
                                  scale * texture.height, texture, 0)


def pause_screen():
    """"draws a pause screen
    
    Returns:
        picture of a black pause screen activated in the middle of the game
    
    """
    # draws a black pause screen that is activated with the ESC key
    scale = 0.5
    texture = arcade.load_texture("pause_screen.jpg")
    arcade.draw_texture_rectangle(500, 350, scale * texture.width,
                                scale * texture.height, texture, 0)


def add_more_humans():
    """"adds more humans randomly within a certain range
    
    Returns:
        picture of humans that fall randomly
    
    """
    global human_x_positions, human_y_positions

    # when a human position is deleted from the list via being shot, adds a human back
    x_human = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human = random.randrange(HEIGHT, HEIGHT + 50)

    human_x_positions.append(x_human)
    human_y_positions.append(y_human)


def add_more_aliens():
    """"adds more aliens randomly within a certain range
    
    Returns:
        pictures of aliens that fall randomly
    
    """
    global alien_x_positions, alien_y_positions

    # when an alien position is deleted from the list via being shot, adds a alien back
    x_alien = random.randrange(75, WIDTH/2 - 75)
    y_alien = random.randrange(HEIGHT, HEIGHT + 50)

    alien_x_positions.append(x_alien)
    alien_y_positions.append(y_alien)


def add_more_human_meteors():
    """"adds more meteors randomly within a certain range
    
    Returns:
        pictures of meteors that fall randomly on the human side
    
    """
    global human_meteor_x_positions, human_meteor_y_positions

    # when a meteor position is deleted from the list via being shot, adds a meteor back
    x_human_meteor = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human_meteor = random.randrange(HEIGHT, HEIGHT + 50)

    human_meteor_x_positions.append(x_human_meteor)
    human_meteor_y_positions.append(y_human_meteor)


def add_more_alien_meteors():
    """"adds more meteors randomly within a certain range
    
    Returns:
        pictures of meteors that fall randomly on the alien side
    
    """
    global alien_meteor_x_positions, alien_meteor_y_positions

    # when a meteor position is deleted from the list via being shot, adds a meteor back
    x_alien_meteor = random.randrange(75, WIDTH/2 - 75)
    y_alien_meteor = random.randrange(HEIGHT, HEIGHT + 50)

    alien_meteor_x_positions.append(x_alien_meteor)
    alien_meteor_y_positions.append(y_alien_meteor)


def add_more_human_shooting_stars():
    """"adds more shooting stars randomly within a certain range
    
    Returns:
        pictures of shooting stars that fall randomly on the human side
    
    """
    global human_x_positions_shooting_star, human_y_positions_shooting_star

    # when a shooting star position is deleted from the list via being shot, adds a shooting star back
    x_human_shooting_star = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human_shooting_star = random.randrange(HEIGHT, HEIGHT + 50)
    
    human_x_positions_shooting_star.append(x_human_shooting_star)
    human_y_positions_shooting_star.append(y_human_shooting_star)


def add_more_alien_shooting_stars():
    """"adds more shooting stars randomly within a certain range
    
    Returns:
        pictures of shooting stars that fall randomly on the alien side
    
    """
    global alien_x_positions_shooting_star, alien_y_positions_shooting_star 
    
    # when a shooting star position is deleted from the list via being shot, adds a shooting star back
    x_alien_shooting_star = random.randrange(75, WIDTH/2 - 75)
    y_alien_shooting_star = random.randrange(HEIGHT, HEIGHT + 50)
    
    alien_x_positions_shooting_star.append(x_alien_shooting_star)
    alien_y_positions_shooting_star.append(y_alien_shooting_star)


def laser_human_collision():
    """"computes if the alien's lasers will collide with the humans
    
    Returns:
        deletes the laser and human it collided with if there is a collision, and 
        if there isn't, 1 will be added to the human laser index and the human index
    
    """
    global human_x_positions_laser, human_y_positions_laser
    global x_human_laser, y_human_laser
    global human_width, human_height, human_points

    hit_sound = arcade.load_sound("hit.wav")
    human_index = 0

    # delete the human and laser x and y positions when the laser hits a human 
    for x_human, y_human in zip(human_x_positions, human_y_positions):
        human_laser_index = 0

        for x_human_laser, y_human_laser in zip(human_x_positions_laser, human_y_positions_laser):
            if (x_human - human_width/2 <= x_human_laser <= x_human + human_width/2) and (y_human - human_height/2 <= y_human_laser <= y_human + human_height/2):
                del human_x_positions[human_index]
                del human_y_positions[human_index]

                del human_x_positions_laser[human_laser_index]
                del human_y_positions_laser[human_laser_index]
                
                # add coordinate positions back to make up for the deleted positions
                add_more_humans()

                # play a hit sound effect, add ten points to the player point counter
                arcade.sound.play_sound(hit_sound)
                human_points += 10
                continue

        human_index += 1


def laser_alien_collision():
    """"computes if the human's lasers will collide with the aliens
    
    Returns:
        deletes the laser and alien it collided with if there is a collision, and if 
        there isn't, 1 will be added to the alien laser index and the alien index
    
    """
    global alien_x_positions_laser, alien_y_positions_laser
    global x_alien_laser, y_alien_laser
    global alien_width, alien_height, alien_points

    hit_sound = arcade.load_sound("hit.wav")
    alien_index = 0

    # delete the alien and laser x and y positions when the laser hits a human
    for x_alien, y_alien in zip(alien_x_positions, alien_y_positions):
        alien_laser_index = 0

        for x_alien_laser, y_alien_laser in zip(alien_x_positions_laser, alien_y_positions_laser):
            if (x_alien - alien_width/2 <= x_alien_laser <= x_alien + alien_width/2) and (y_alien - alien_height/2 <= y_alien_laser <= y_alien + alien_height/2):

                del alien_x_positions[alien_index]
                del alien_y_positions[alien_index]

                del alien_x_positions_laser[alien_laser_index]
                del alien_y_positions_laser[alien_laser_index]

                # add coordinate positions back to make up for the deleted positions
                add_more_aliens()

                # play a hit sound effect, add ten points to the player point counter
                arcade.sound.play_sound(hit_sound)
                alien_points += 10
                continue

        alien_index += 1


def human_meteor_spaceship_collision():
    """"computes if the falling meteors will hit the human spaceship 
    
    Returns:
        deletes the meteor if it hits the spaceship and generates more meteors to replace the ones deleted
    
    """
    global spaceship_human_x, spaceship_human_y
    global human_meteor_x_positions, human_meteor_y_positions
    global human_spaceship_width, human_spaceship_height
    global human_times_hit

    meteor_index = 0

    # delete the human meteors' x and y positions when the meteor hits a spaceship
    for x_human_meteor, y_human_meteor in zip(human_meteor_x_positions, human_meteor_y_positions):

        if (x_human_meteor - human_spaceship_width/2 <= spaceship_human_x <= x_human_meteor + human_spaceship_width/2) and (y_human_meteor - human_spaceship_height/2 <= spaceship_human_y <= y_human_meteor + human_spaceship_height/2):

            del human_meteor_x_positions[meteor_index]
            del human_meteor_y_positions[meteor_index]

            # add one to the hit counter, which controls player lives
            human_times_hit += 1
            
            # add coordinate positions back to make up for the deleted positions
            add_more_human_meteors()
            continue
        
        else:
            meteor_index += 1


def alien_meteor_spaceship_collision():
    """"computes if the falling meteors will hit the alien spaceship 
    
    Returns:
        deletes the meteor if it hits the spaceship and generates more meteors to replace the ones deleted
    
    """
    global spaceship_alien_x, spaceship_alien_y
    global alien_meteor_x_positions, alien_meteor_y_positions
    global alien_spaceship_width, alien_spaceship_height
    global alien_times_hit

    alien_meteor_index = 0

    # delete the alien meteors x and y positions when the meteor hits a spaceship
    for x_alien_meteor, y_alien_meteor in zip(alien_meteor_x_positions, alien_meteor_y_positions):

        if (x_alien_meteor - alien_spaceship_width/2 <= spaceship_alien_x <= x_alien_meteor + alien_spaceship_width/2 ) and (y_alien_meteor - alien_spaceship_height/2 <= spaceship_alien_y <= y_alien_meteor + alien_spaceship_height/2 ):

            del alien_meteor_x_positions[alien_meteor_index]
            del alien_meteor_y_positions[alien_meteor_index]
            
            # add one to the hit counter, which controls player lives
            alien_times_hit += 1
            
            # add coordinate positions back to make up for the deleted positions
            add_more_alien_meteors() 
            continue

        else:
            alien_meteor_index += 1


def laser_human_shooting_star_collision():
    """"computes if the lasers will hit the shooting shars on the human side
    
    Returns:
        deletes the laser and shooting star it collided with if there is a collision, and if 
        there isn't, 1 will be added to the human laser index and the human shooting star index
    
    """
    global human_x_positions_laser, human_y_positions_laser
    global x_human_laser, y_human_laser
    global human_shooting_star_width, human_shooting_star_height, human_times_hit, human_points

    human_shooting_star_index = 0
    hit_sound = arcade.load_sound("hit.wav")

    # delete the human shooting star and laser's x and y positions when the laser hits the shooting star
    for x_human_shooting_star, y_human_shooting_star in zip(human_x_positions_shooting_star, human_y_positions_shooting_star):
        human_laser_index = 0 
        
        for x_human_laser, y_human_laser in zip(human_x_positions_laser, human_y_positions_laser):
            if (x_human_shooting_star - human_shooting_star_width/2 <= x_human_laser <= x_human_shooting_star + human_shooting_star_width/2) and (y_human_shooting_star - human_shooting_star_height/2 <= y_human_laser <= y_human_shooting_star + human_shooting_star_height/2):
                
                del human_x_positions_shooting_star[human_shooting_star_index]
                del human_y_positions_shooting_star[human_shooting_star_index]

                del human_x_positions_laser[human_laser_index]
                del human_y_positions_laser[human_laser_index]
                
                
                # add coordinate positions back to make up for the deleted positions
                add_more_human_shooting_stars()

                # play a hit sound effect, add ten points to the player point counter
                arcade.sound.play_sound(hit_sound)
                human_points += 15
                
                # ensures that one life is regained if lives have been lost
                if human_times_hit > 0:
                    human_times_hit -= 1
                
                continue

        human_shooting_star_index += 1    


def laser_alien_shooting_star_collision():
    """"computes if the lasers will hit the shooting shars on the alien side
    
    Returns:
        deletes the laser and shooting star it collided with if there is a collision, and if 
        there isn't, 1 will be added to the human laser index and the alien shooting star index
    
    """
    global alien_x_positions_laser, alien_y_positions_laser
    global x_alien_laser, y_alien_laser
    global alien_shooting_star_width, alien_shooting_star_height, alien_times_hit, alien_points

    alien_shooting_star_index = 0
    hit_sound = arcade.load_sound("hit.wav")

    # delete the alien shooting star and laser's x and y positions when the laser hits the shooting star
    for x_alien_shooting_star, y_alien_shooting_star in zip(alien_x_positions_shooting_star, alien_y_positions_shooting_star):
        alien_laser_index = 0
        
        for x_alien_laser, y_alien_laser in zip(alien_x_positions_laser, alien_y_positions_laser):
            if (x_alien_shooting_star - alien_shooting_star_width/2 <= x_alien_laser <= x_alien_shooting_star + alien_shooting_star_width/2) and (y_alien_shooting_star - alien_shooting_star_height/2 <= y_alien_laser <= y_alien_shooting_star + alien_shooting_star_height/2):
                
                del alien_x_positions_shooting_star[alien_shooting_star_index]
                del alien_y_positions_shooting_star[alien_shooting_star_index]

                del alien_x_positions_laser[alien_laser_index]
                del alien_y_positions_laser[alien_laser_index]

                # add coordinate positions back to make up for the deleted positions
                add_more_alien_shooting_stars()

                # play a hit sound effect, add ten points to the player point counter
                arcade.sound.play_sound(hit_sound)
                alien_points += 15

                # ensures that one life is regained if lives have been lost
                if alien_times_hit > 0:
                    alien_times_hit -= 1
                
                continue
        
        alien_shooting_star_index += 1


def human_final_stage_collision():
    """"computes if the alien's lasers will collide with the big human
    
    Returns:
        deletes the laser and adds points if there is a collision, and if 
        there isn't, 1 will be added to the alien laser index
    
    """
    global human_x_positions_laser, human_y_positions_laser
    global x_human_laser, y_human_laser
    global human_points

    human_laser_index = 0
    hit_sound = arcade.load_sound("hit.wav")

    # delete the human laser's x and y positions
    for x_human_laser, y_human_laser in zip(human_x_positions_laser, human_y_positions_laser):
        
        if (700 <= x_human_laser <= 800) and (370 <= y_human_laser <= 380):

            del human_x_positions_laser[human_laser_index]
            del human_y_positions_laser[human_laser_index]
            
            arcade.sound.play_sound(hit_sound)
            human_points += 10
            continue


def alien_final_stage_collision():
    """"computes if the human's lasers will collide with the big alien
    
    Returns:
        deletes the laser and adds points if there is a collision, and if 
        there isn't, 1 will be added to the alien laser index        
    
    """
    global alien_x_positions_laser, alien_y_positions_laser
    global x_alien_laser, y_alien_laser
    global alien_points

    alien_laser_index = 0
    hit_sound = arcade.load_sound("hit.wav")

    # delete the alien laser's x and y positions
    for x_alien_laser, y_alien_laser in zip(alien_x_positions_laser, alien_y_positions_laser):      
        if (200 <= x_alien_laser <= 300) and (370 <= y_alien_laser <= 380):

            del alien_x_positions_laser[alien_laser_index]
            del alien_y_positions_laser[alien_laser_index]
            
            arcade.sound.play_sound(hit_sound)
            alien_points += 10
            continue


def on_draw():
    """"draws out and runs the different elements in the game 
    
    Returns:
        if various boolean variables are true, stages of the game will be drawn out and run
    
    """
    global spaceship_human_x, spaceship_human_y, spaceship_alien_x, spaceship_alien_y, start_game
    global run_game, end_game, final_stage_game, elapsed_time, draw_enemy_rate, draw_meteor_rate

    # starts the rendering of the game
    arcade.start_render()

    if start_game: # draws the main screen when the start_game variable is true (only at the beginning)
        draw_main_screen(500, 375)
    
    if run_game: # draws the game elements when the spacebar is pressed

        start_game = False # stops the drawing of the main screen

        # draws the game background and middle divide line
        draw_background(500, 375)
        arcade.draw_lrtb_rectangle_filled(WIDTH/2 - 5, WIDTH/2 + 5, HEIGHT, 0, arcade.color.WHITE)
        
        # draws text to show which side is fighting for which creature
        arcade.draw_text("HUMAN SPACESHIP", 145, 700, arcade.color.WHITE, 20)
        arcade.draw_text("ALIEN SPACESHIP", 665, 700, arcade.color.WHITE, 20)
        
        # calls the activation of collision sequences
        laser_human_collision()
        laser_alien_collision()
        human_meteor_spaceship_collision()
        alien_meteor_spaceship_collision()

        # draws falling objects based on the updating lists of coordinate positions
        for x_human, y_human in zip(human_x_positions, human_y_positions):
            draw_human(x_human, y_human)

        for x_alien, y_alien in zip(alien_x_positions, alien_y_positions):
            draw_alien(x_alien, y_alien)

        for x_human_meteor, y_human_meteor in zip(human_meteor_x_positions, human_meteor_y_positions):
            draw_human_meteor(x_human_meteor, y_human_meteor)

        for x_alien_meteor, y_alien_meteor in zip(alien_meteor_x_positions, alien_meteor_y_positions):
            draw_alien_meteor(x_alien_meteor, y_alien_meteor)

        for x_human_laser, y_human_laser in zip(human_x_positions_laser, human_y_positions_laser):
            draw_human_laser(x_human_laser, y_human_laser)

        for x_alien_laser, y_alien_laser in zip(alien_x_positions_laser, alien_y_positions_laser):
            draw_alien_laser(x_alien_laser, y_alien_laser)
        
        # draws the player-controlled spaceships
        draw_spaceship_human(spaceship_human_x, spaceship_human_y)
        draw_spaceship_alien(spaceship_alien_x, spaceship_alien_y)

        # a sound effect for when the game levels up (normally once every 20/30 seconds)
        level_up_sound = arcade.load_sound("level_up.wav")

        # draws shooting stars and activates collision only when the game has gone on for 60 seconds
        if elapsed_time > 60.00:
            for x_human_shooting_star, y_human_shooting_star in zip(human_x_positions_shooting_star, human_y_positions_shooting_star):
                draw_human_shooting_star(x_human_shooting_star, y_human_shooting_star)

            for x_alien_shooting_star, y_alien_shooting_star in zip(alien_x_positions_shooting_star, alien_y_positions_shooting_star):
                draw_alien_shooting_star(x_alien_shooting_star, y_alien_shooting_star)
            
            laser_human_shooting_star_collision()
            laser_alien_shooting_star_collision()
        
        # draws a "level up" label about once every 20/30 seconds
        elif 19 < elapsed_time < 21 or 39 < elapsed_time < 41 or 59 < elapsed_time < 61:
            arcade.draw_rectangle_filled(500, 375, 370, 100, arcade.color.BLACK)
            arcade.draw_text("LEVEL UP!", 320, 342, arcade.color.WHITE, 65)

        # plays level up sound effect near the same time as the label comes up
        if 18.95 < elapsed_time < 19 or 38.95 < elapsed_time < 39 or 58.95 < elapsed_time < 59:
            arcade.sound.play_sound(level_up_sound)

        # activates the point counter
        alien_points_counter()
        human_points_counter()

        # counts the number of times a player has been hit to draw a certain number of lives
        if human_times_hit == 0:
            lives(890, 580)
            lives(915, 580)
            lives(940, 580)

        elif human_times_hit == 1:
            lives(915, 580)
            lives(940, 580)

        elif human_times_hit == 2:
            lives(940, 580)

        if alien_times_hit == 0:
            lives(62, 580)
            lives(87, 580)
            lives(112, 580)

        elif alien_times_hit == 1:
            lives(87, 580)
            lives(112, 580)

        elif alien_times_hit == 2:
            lives(112, 580)

    if 105 <= elapsed_time <= 120: # draws the final stage of the game after 105 seconds of gameplay
        
        # the run_game events stop, and the final_stage events start
        final_stage_game = True
        run_game = False

        # the background, divider, label text, point counters, and lasers all still run the same way as the normal game
        draw_background(500, 375)
        arcade.draw_lrtb_rectangle_filled(WIDTH/2 - 5, WIDTH/2 + 5, HEIGHT, 0, arcade.color.WHITE)
        
        arcade.draw_text("HUMAN SPACESHIP", 145, 700, arcade.color.WHITE, 20)
        arcade.draw_text("ALIEN SPACESHIP", 665, 700, arcade.color.WHITE, 20)

        draw_spaceship_human(spaceship_human_x, spaceship_human_y)
        draw_spaceship_alien(spaceship_alien_x, spaceship_alien_y)

        alien_points_counter()
        human_points_counter()

        for x_human_laser, y_human_laser in zip(human_x_positions_laser, human_y_positions_laser):
            draw_human_laser(x_human_laser, y_human_laser)

        for x_alien_laser, y_alien_laser in zip(alien_x_positions_laser, alien_y_positions_laser):
            draw_alien_laser(x_alien_laser, y_alien_laser)
        
        # the big final_stage aliens and humans are drawn, and given collision
        draw_final_alien(250, 375)
        draw_final_human(750, 375)

        human_final_stage_collision()
        alien_final_stage_collision()
        
        # text comes up to warn the players of the final boss
        if 105 <= elapsed_time <= 108:
            arcade.draw_rectangle_filled(500, 375, 450, 100, arcade.color.YELLOW)
            arcade.draw_text("FINAL BOSS", 310, 342, arcade.color.BLACK, 65)

        # an onscreen counter counts down the last three seconds of the game
        elif 116 <= elapsed_time <= 119:
            arcade.draw_rectangle_filled(500, 375, 50, 100, arcade.color.BLACK)
            arcade.draw_text(str(int(120 - elapsed_time)), 475, 342, arcade.color.WHITE, 65)
        
        # text comes up to tell the players that time is up
        elif elapsed_time >= 120:
            arcade.draw_rectangle_filled(500, 375, 390, 100, arcade.color.BLACK)
            arcade.draw_text("TIME'S UP!", 320, 342, arcade.color.WHITE, 65)
    
    # after about 120 seconds of gameplay, the game ends and the end screen appears
    elif elapsed_time >= 121:
        final_stage_game = False
        end_game == True
    
    # after one player loses all three lives, the game ends and the end screen appears
    if human_times_hit >= 3 or alien_times_hit >= 3:
        run_game = False
        end_game = True
    
    # when end_game is activated, the end_screen is drawn
    if end_game:
        draw_end_screen(500, 375)
    
    # the pause_screen is activated when all other game stages are not (controlled by the ESC key)
    if not run_game and not start_game and not final_stage_game and not end_game:
        pause_screen()


def on_key_press(key, modifiers):
    """"computes if a key is pressed and if it is, the action assigned to the key is executed
    
    Arguments:
        key {str} -- the key on a computer keyboard that is pressed 
        modifiers {str} -- a key that changes execution if pressed in combination with other keys
    
    Returns:
        the action that is assigned to the key is executed 
    
    """
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, fire_laser_human 
    global fire_laser_alien, spaceship_human_x, spaceship_human_y, spaceship_alien_x, spaceship_alien_y 
    global run_game, time, delta_time, start_game, run_game, end_game

    laser_sound = arcade.load_sound("laser.wav")

    # when LEFT/RIGHT is pressed for the right side player, and A/D for the left side player, the spaceship moves left and right
    if key == arcade.key.LEFT:
        left_pressed_human = True

    if key == arcade.key.A:
        left_pressed_alien = True

    if key == arcade.key.RIGHT:
        right_pressed_human = True

    if key == arcade.key.D:
        right_pressed_alien = True

    # when UP is pressed for the right side player, and W for the left side player, a laser is shot with a sound
    if key == arcade.key.W:
        fire_laser_alien = True
        alien_x_positions_laser.append(spaceship_alien_x)
        alien_y_positions_laser.append(spaceship_alien_y)
        arcade.sound.play_sound(laser_sound)

    if key == arcade.key.UP:
        fire_laser_human = True
        human_x_positions_laser.append(spaceship_human_x)
        human_y_positions_laser.append(spaceship_human_y)
        arcade.sound.play_sound(laser_sound)

    # the space bar starts the game after the main screen
    if key == arcade.key.SPACE:
        run_game = True

    # the escape key stops the execution of all other game stages, pausing the game
    if key == arcade.key.ESCAPE:
        run_game = False
        start_game = False
        final_stage_game = False
        end_game = False

    # the enter key restarts the game
    if key == arcade.key.ENTER:
        end_game = False
        run_game = True

        
def on_key_release(key, modifiers):
    """"computes if a key is released after being pressed and if it is, no new action is executed 
    
    Arguments:
        key {str} -- the key on a computer keyboard that is released or no longer pressed 
        modifiers {str} -- allows the key released commands to be accessed 
    
    Returns:
        the execution of the action that was assigned to the key is stopped
    
    """
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, laser_fire_key

    # when the LEFT/RIGHT/A/D keys are no longer pressed, the spaceships stop moving
    if key == arcade.key.LEFT:
        left_pressed_human = False

    if key == arcade.key.A:
        left_pressed_alien = False

    if key == arcade.key.RIGHT:
        right_pressed_human = False

    if key == arcade.key.D:
        right_pressed_alien = False

    # when the UP/W keys are no longer pressed, lasers stop firing
    if key == arcade.key.W:
        laser_fire_key = False

    if key == arcade.key.UP:
        laser_fire_key = False
    

def setup():
    """"the main set-up function before the final code is executed 
    
    Returns:
        the arcade windown is drawn, functions override the typical arcade functions, 
        the schedule is set, the game runs
    
    """
    # opens a window with specified dimensions
    arcade.open_window(WIDTH, HEIGHT, "Astronauts VS Aliens!")

    # overrides the default arcade functions with our own game functions
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    # sets an updating schedule of once every 1/100 of a second
    arcade.schedule(update, 1/100)

    # calls the program to run all events
    arcade.run()


# calls the main function to get the program started
if __name__ == '__main__':
    setup()