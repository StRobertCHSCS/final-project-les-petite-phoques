import random
import arcade


WIDTH = 1000
HEIGHT = 750

#rain = arcade.ShapeElementList()

# first set up empty lists
human_x_positions = []
human_y_positions = []
alien_x_positions = []
alien_y_positions = []

meteor_x_positions = []
meteor_y_positions = []
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

draw_enemy_rate = 4
draw_meteor_rate = 2
draw_shooting_star_rate = 1
game_speed = 3

elapsed_time = 0
time = False

if 19.00 < elapsed_time < 21.00 or 39.00 < elapsed_time < 41.00:
        draw_enemy_rate += 1
        draw_meteor_rate += 1

for _ in range(draw_enemy_rate):
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

for _ in range(draw_meteor_rate): #this is the meteor's repeat, and i made it a little less than the humans/aliens so there's less of them
    # generate random x and y values
    x_meteor = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_meteor = random.randrange(HEIGHT, HEIGHT + 50)
    x_alien_meteor = random.randrange(75, WIDTH/2 - 75)
    y_alien_meteor = random.randrange(HEIGHT, HEIGHT + 50)
    
    # append the x and y values to the appropriate list
    meteor_x_positions.append(x_meteor)
    meteor_y_positions.append(y_meteor)
    alien_meteor_x_positions.append(x_alien_meteor)
    alien_meteor_y_positions.append(y_alien_meteor)

for _ in range(draw_shooting_star_rate):
    x_human_shooting_star = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human_shooting_star = random.randrange(HEIGHT, HEIGHT + 50)
    x_alien_shooting_star = random.randrange(75, WIDTH/2 - 75)
    y_alien_shooting_star = random.randrange(HEIGHT, HEIGHT + 50)
    
    # append the x and y values to the appropriate list
    human_x_positions_shooting_star.append(x_human_shooting_star)
    human_y_positions_shooting_star.append(y_human_shooting_star)
    alien_x_positions_shooting_star.append(x_alien_shooting_star)
    alien_y_positions_shooting_star.append(y_alien_shooting_star)

spaceship_human_x = 750
spaceship_human_y = 100
spaceship_alien_x = 250
spaceship_alien_y = 100

alien_width = 60
alien_height = 74
human_width = 60
human_height = 80
meteor_height = 60 
meteor_width = 60
alien_meteor_width = 60
alien_meteor_height = 60

x_human_laser = 0
y_human_laser = 0
x_alien_laser = 0
y_alien_laser = 0

up_pressed_human = False
left_pressed_human = False
right_pressed_human = False
fire_laser_human = False

up_pressed_alien = False
left_pressed_alien = False
right_pressed_alien = False
fire_laser_alien = False

run_game = False

main_screen_alien_x = 10
main_screen_alien_y = 10
main_screen_human_x = 10
main_screen_human_y = 740
main_screen_meteor1_x = 0
main_screen_meteor2_x = 1000
main_screen_meteor1_degree = 0
main_screen_meteor2_degree = 0

alien_points = 0
human_points = 0


def update(delta_time):
    global elapsed_time, draw_enemy_rate, draw_meteor_rate, game_speed
    
    if time == True:
        elapsed_time += delta_time
        elapsed_time = round(elapsed_time, 2)
    
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

    for index in range(len(meteor_y_positions)):
        meteor_y_positions[index] -= game_speed

        if meteor_y_positions[index] < 0:
            meteor_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 50)
            meteor_x_positions[index] = random.randrange(WIDTH/2 + 75, WIDTH - 75)

    for index in range(len(alien_meteor_y_positions)):
        alien_meteor_y_positions[index] -= game_speed

        if alien_meteor_y_positions[index] < 0:
            alien_meteor_y_positions[index] = random.randrange(HEIGHT, HEIGHT + 50)
            alien_meteor_x_positions[index] = random.randrange(75, WIDTH/2 - 75)  

    if elapsed_time > 60.00:
        for index in range(len(human_y_positions_shooting_star)):
            human_y_positions_shooting_star[index] -= game_speed

            if human_y_positions_shooting_star[index] < 0:
                human_y_positions_shooting_star[index] = random.randrange(HEIGHT, HEIGHT + 50)
                human_x_positions_shooting_star[index] = random.randrange(WIDTH/2 + 75, WIDTH - 75) 
        
        for index in range(len(alien_y_positions_shooting_star)):
            alien_y_positions_shooting_star[index] -= game_speed

            if alien_y_positions_shooting_star[index] < 0:
                alien_y_positions_shooting_star[index] = random.randrange(HEIGHT, HEIGHT + 50)
                alien_x_positions_shooting_star[index] = random.randrange(75, WIDTH/2 - 75) 
    
    if elapsed_time == 20.00 or elapsed_time == 40.00:
        game_speed += 0.5
    elif elapsed_time > 60:
        game_speed = 4.5

    global human_hit, alien_hit

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
            
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, spaceship_human_x, spaceship_alien_x
    
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


def draw_main_screen(x, y):
    global main_screen_alien_x, main_screen_alien_y, main_screen_human_x, main_screen_human_y, main_screen_meteor1_x, main_screen_meteor1_y, main_screen_meteor2_x, main_screen_meteor2_y, main_screen_meteor1_degree, main_screen_meteor2_degree

    scale = 0.3
    texture = arcade.load_texture("space.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                                    scale * texture.height, texture, 0)
    
    arcade.draw_text("Welcome to...", 385, 600, arcade.color.BLACK, 25)
    arcade.draw_text("ASTRONAUTS VS ALIENS!", 30, 375, arcade.color.BLACK, 65)
    arcade.draw_text("press space to start", 350, 130, arcade.color.BLACK, 25)

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


def draw_end_screen(x, y):
    global alien_points, human_points, elapsed_time
    
    scale = 1.67
    texture = arcade.load_texture("space2.jpg")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                                    scale * texture.height, texture, 0)
    
    arcade.draw_text("GAME OVER!", 270, 500, arcade.color.BLACK, 65)
    arcade.draw_text("press space to restart", 350, 75, arcade.color.BLACK, 25)

    if alien_points > human_points:
        arcade.draw_text("The Humans Have Won Control!", 175, 400, arcade.color.BLACK, 40)
    elif human_points > alien_points:
        arcade.draw_text("The Aliens Have Won Control!", 200, 400, arcade.color.BLACK, 40)
    else:
        arcade.draw_text("It's a tie! Peace has been achieved.", 150, 400, arcade.color.BLACK, 40)
        arcade.draw_text("For now...", 800, 350, arcade.color.BLACK, 25)


def draw_background(x, y):
    scale = 1
    texture = arcade.load_texture("night_sky.jpg")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                                    scale * texture.height, texture, 0)


def alien_points_counter():
    arcade.draw_text("Points: " + str(alien_points), 50, 600, arcade.color.WHITE, 15)


def human_points_counter():
    arcade.draw_text("Points: " + str(human_points), 880, 600, arcade.color.WHITE, 15)


def alien_lives(x, y):
    scale = 0.06
    texture = arcade.load_texture("heart.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                                    scale * texture.height, texture, 0)


def human_lives(x, y):
    scale = 0.06
    texture = arcade.load_texture("heart.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                                    scale * texture.height, texture, 0)


def draw_human(x, y):
    scale = 0.05
    texture = arcade.load_texture("astronaut.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


def draw_alien(x, y):
    scale = 0.05
    texture = arcade.load_texture("alien.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


def draw_human_laser(x, y):
    scale = 0.1 
    texture = arcade.load_texture("laser.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


def draw_alien_laser(x, y):
    scale = 0.1
    texture = arcade.load_texture("laser.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


def draw_human_meteor(x, y):
    scale = 0.05
    texture = arcade.load_texture("meteor.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


def draw_alien_meteor(x, y):
    scale = 0.05
    texture = arcade.load_texture("meteor.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


def draw_human_shooting_star(x, y):
    scale = 0.1
    texture = arcade.load_texture("shooting star.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, - 20)


def draw_alien_shooting_star(x, y):
    scale = 0.1
    texture = arcade.load_texture("shooting star.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, - 20)


def draw_spaceship_human(x, y):
    scale = 0.4
    texture = arcade.load_texture("spaceship.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


def draw_spaceship_alien(x, y):
    scale = 0.4
    texture = arcade.load_texture("spaceship.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


def add_more_humans():
    global human_x_positions, human_y_positions

    # generate random x and y values
    x_human = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human = random.randrange(HEIGHT, HEIGHT + 50)

    # append the x and y values to the appropriate list
    human_x_positions.append(x_human)
    human_y_positions.append(y_human)


def add_more_aliens():
    global alien_x_positions, alien_y_positions

    # generate random x and y values
    x_alien = random.randrange(75, WIDTH/2 - 75)
    y_alien = random.randrange(HEIGHT, HEIGHT + 50)

    # append the x and y values to the appropriate list
    alien_x_positions.append(x_alien)
    alien_y_positions.append(y_alien)


def laser_human_collision():
    global human_x_positions_laser, human_y_positions_laser
    global x_human_laser, y_human_laser
    global human_width, human_height, human_points
   
    human_index = 0
    
    for x_human, y_human in zip(human_x_positions, human_y_positions):
        human_laser_index = 0

        for x_human_laser, y_human_laser in zip(human_x_positions_laser, human_y_positions_laser):
            if (x_human - human_width/2 <= x_human_laser <= x_human + human_width/2) and (y_human - human_height/2 <= y_human_laser <= y_human + human_height/2):
                del human_x_positions[human_index]
                del human_y_positions[human_index]

                del human_x_positions_laser[human_laser_index]
                del human_y_positions_laser[human_laser_index]
                
                add_more_humans()
                human_points += 10
                continue

            else: 
                human_laser_index += 1

        human_index += 1


def laser_alien_collision():
    global alien_x_positions_laser, alien_y_positions_laser
    global x_alien_laser, y_alien_laser
    global alien_width, alien_height, alien_points

    alien_index = 0

    for x_alien, y_alien in zip(alien_x_positions, alien_y_positions):
        alien_laser_index = 0

        for x_alien_laser, y_alien_laser in zip(alien_x_positions_laser, alien_y_positions_laser):
            if (x_alien - alien_width/2 <= x_alien_laser <= x_alien + alien_width/2) and (y_alien- alien_height/2 <= y_alien_laser <= y_alien + alien_height/2):
            
                del alien_x_positions[alien_index]
                del alien_y_positions[alien_index]

                del alien_x_positions_laser[alien_laser_index]
                del alien_y_positions_laser[alien_laser_index]
                
                add_more_aliens()
                alien_points += 10
                continue
                
            else: 
                alien_laser_index += 1
        alien_index += 1


def on_draw():
    global spaceship_human_x, spaceship_human_y, spaceship_alien_x, spaceship_alien_y, run_game, time, elapsed_time, draw_enemy_rate, draw_meteor_rate
    
    arcade.start_render()
    
    draw_main_screen(500, 375)
    
    if run_game == True:
        draw_background(500, 375)
        laser_human_collision()
        laser_alien_collision()
        time = True
        print(elapsed_time)

        for x_human, y_human in zip(human_x_positions, human_y_positions):
            draw_human(x_human, y_human)
        
        for x_alien, y_alien in zip(alien_x_positions, alien_y_positions):
            draw_alien(x_alien, y_alien)

        for x_meteor, y_meteor in zip(meteor_x_positions, meteor_y_positions):
            draw_human_meteor(x_meteor, y_meteor)
        
        for x_alien_meteor, y_alien_meteor in zip(alien_meteor_x_positions, alien_meteor_y_positions):
            draw_alien_meteor(x_alien_meteor, y_alien_meteor)

        draw_spaceship_human(spaceship_human_x, spaceship_human_y)
        draw_spaceship_alien(spaceship_alien_x, spaceship_alien_y)
        
        for x_human_laser, y_human_laser in zip(human_x_positions_laser, human_y_positions_laser):
            draw_human_laser(x_human_laser, y_human_laser)
        
        for x_alien_laser, y_alien_laser in zip(alien_x_positions_laser, alien_y_positions_laser):
            draw_alien_laser(x_alien_laser, y_alien_laser)

        arcade.draw_lrtb_rectangle_filled(WIDTH/2 - 5, WIDTH/2 + 5, HEIGHT, 0, arcade.color.WHITE)

        # if elapsed_time > 30.00:
        if elapsed_time > 60:
            for x_human_shooting_star, y_human_shooting_star in zip(human_x_positions_shooting_star, human_y_positions_shooting_star):
                draw_human_shooting_star(x_human_shooting_star, y_human_shooting_star)
            
            for x_alien_shooting_star, y_alien_shooting_star in zip(alien_x_positions_shooting_star, alien_y_positions_shooting_star):
                draw_alien_shooting_star(x_alien_shooting_star, y_alien_shooting_star)
        
        elif 19 < elapsed_time < 21 or 39 < elapsed_time < 41 or 59 < elapsed_time < 61:
            arcade.draw_rectangle_filled(500, 375, 370, 100, arcade.color.BLACK)
            arcade.draw_text("LEVEL UP!", 320, 342, arcade.color.WHITE, 65)

        alien_points_counter()
        human_points_counter()

        alien_lives(62, 580)
        alien_lives(87, 580)
        alien_lives(112, 580)

        alien_lives(890, 580)
        alien_lives(915, 580)
        alien_lives(940, 580)
    
    if elapsed_time > 5:
        run_game = False
        draw_end_screen(500, 375)


def on_key_press(key, modifiers):
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, fire_laser_human, fire_laser_alien, spaceship_human_x, spaceship_human_y, spaceship_alien_x, spaceship_alien_y, run_game, time, delta_time

    if key == arcade.key.LEFT:
        left_pressed_human = True
     
    if key == arcade.key.A:
        left_pressed_alien = True
    
    if key == arcade.key.RIGHT:
        right_pressed_human = True

    if key == arcade.key.D:
        right_pressed_alien = True

    if key == arcade.key.W:
        fire_laser_alien = True     
        alien_x_positions_laser.append(spaceship_alien_x)
        alien_y_positions_laser.append(spaceship_alien_y)
    
    if key == arcade.key.UP:
        fire_laser_human = True     
        human_x_positions_laser.append(spaceship_human_x)
        human_y_positions_laser.append(spaceship_human_y)

    if key == arcade.key.SPACE:
        run_game = True
        time = False
        delta_time = True


def on_key_release(key, modifiers):
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, laser_fire_key

    if key == arcade.key.LEFT:
        left_pressed_human = False
     
    if key == arcade.key.A:
        left_pressed_alien = False
    
    if key == arcade.key.RIGHT:
        right_pressed_human = False

    if key == arcade.key.D:
        right_pressed_alien = False

    if key == arcade.key.W: 
        laser_fire_key = False
        
    if key == arcade.key.UP:
        laser_fire_key = False


def setup():
    arcade.open_window(1000, 750, "Astronauts VS Aliens!")
    
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.schedule(update, 1/100)    
    arcade.run()


# Call the main function to get the program started.
if __name__ == '__main__':
    setup()
