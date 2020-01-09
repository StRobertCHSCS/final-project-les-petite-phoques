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
human_x_positions_laser = []
human_y_positions_laser = []
alien_x_positions_laser = []
alien_y_positions_laser = []

draw_enemy_rate = 3
draw_meteor_rate = 1

elapsed_time = 0
time = True

if elapsed_time > 30 or 60 or 90:
    draw_enemy_rate += 1
    draw_meteor_rate += 1

# loop 100 times
for _ in range(draw_enemy_rate):
    # generate random x and y values
    x_human = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human = random.randrange(HEIGHT, HEIGHT*2)
    x_alien = random.randrange(75, WIDTH/2 - 75)
    y_alien = random.randrange(HEIGHT, HEIGHT*2)

    # append the x and y values to the appropriate list
    human_x_positions.append(x_human)
    human_y_positions.append(y_human)
    alien_x_positions.append(x_alien)
    alien_y_positions.append(y_alien)

for _ in range(draw_meteor_rate): #this is the meteor's repeat, and i made it a little less than the humans/aliens so there's less of them
    # generate random x and y values
    x_meteor = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_meteor = random.randrange(HEIGHT, HEIGHT*2)
    x_alien_meteor = random.randrange(75, WIDTH/2 - 75)
    y_alien_meteor = random.randrange(HEIGHT, HEIGHT*2)
    
    # append the x and y values to the appropriate list
    meteor_x_positions.append(x_meteor)
    meteor_y_positions.append(y_meteor)
    alien_meteor_x_positions.append(x_alien_meteor)
    alien_meteor_y_positions.append(y_alien_meteor)


spaceship_human_x = 250
spaceship_human_y = 100
spaceship_alien_x = 750
spaceship_alien_y = 100

# alien_width =
# alien_height =
# human_width =
# human_height =
# meteor_height =
# meteor_width =
# alien_meteor_width =
# alien_meteor_height =

up_pressed_human = False
left_pressed_human = False
right_pressed_human = False
fire_laser_human = False

up_pressed_alien = False
left_pressed_alien = False
right_pressed_alien = False
fire_laser_alien = False


def draw_stars(x, y):
    arcade.draw_circle_filled(x, y, 5, arcade.color.YELLOW)


def draw_alien(x, y):
    scale = 0.05
    texture = arcade.load_texture("alien.png")
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


def draw_human(x, y):
    scale = 0.05
    texture = arcade.load_texture("astronaut.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


def draw_human_laser(x, y):
    scale = 0.1 
    texture = arcade.load_texture("laser.png")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                            scale * texture.height, texture, 0)


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



def update(delta_time):
    for index in range(len(human_y_positions)):
        human_y_positions[index] -= 3

        if human_y_positions[index] < 0:
            human_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            human_x_positions[index] = random.randrange(WIDTH/2 + 75, WIDTH - 75)

    for index in range(len(alien_y_positions)):
        alien_y_positions[index] -= 3

        if alien_y_positions[index] < 0:
            alien_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            alien_x_positions[index] = random.randrange(75, WIDTH/2 - 75)

    for index in range(len(meteor_y_positions)):
        meteor_y_positions[index] -= 3

        if meteor_y_positions[index] < 0:
            meteor_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            meteor_x_positions[index] = random.randrange(WIDTH/2 + 75, WIDTH - 75)

    for index in range(len(alien_meteor_y_positions)):
        alien_meteor_y_positions[index] -= 3

        if alien_meteor_y_positions[index] < 0:
            alien_meteor_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            alien_meteor_x_positions[index] = random.randrange(75, WIDTH/2 - 75)  

    for index in range(len(human_y_positions_laser)):
        if human_y_positions_laser[index] < 800:
            human_y_positions_laser[index] += 30

    for index in range(len(alien_y_positions_laser)):
        if alien_y_positions_laser[index] < 800:
            alien_y_positions_laser[index] += 30
     
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, spaceship_human_x, spaceship_alien_x, elapsed_time, time
    
    if left_pressed_human:
        spaceship_human_x -= 5
        if spaceship_human_x < 60:
            spaceship_human_x = 60

    if left_pressed_alien:
        spaceship_alien_x -= 5
        if spaceship_alien_x < 570:
            spaceship_alien_x = 570

    if right_pressed_human:
        spaceship_human_x += 5
        if spaceship_human_x > 430:
            spaceship_human_x = 430

    if right_pressed_alien:
        spaceship_alien_x += 5
        if spaceship_alien_x > 940:
            spaceship_alien_x = 940

    if time == True:
        elapsed_time += delta_time
        round(elapsed_time)
        print(elapsed_time)
    elif time == False:
        elapsed_time = 0


def on_draw():
    global spaceship_human_x, spaceship_human_y, spaceship_alien_x, spaceship_alien_y
    
    arcade.start_render()

    # draw_stars(30, 100)
    # draw_stars(50, 50)
    # draw_stars(400, 200)
    # draw_stars(670, 340)
    # draw_stars(500, 100)
    # draw_stars(20, 700)
    # draw_stars(700, 620)
    # draw_stars(800, 560)
    # draw_stars(430, 450)
    # draw_stars(130, 360)
    # draw_stars(200, 201)
    # draw_stars(240, 459)
    # draw_stars(280, 704)
    # draw_stars(320, 10)
    # draw_stars(360, 372)
    # draw_stars(400, 503)
    # draw_stars(510, 80)
    # draw_stars(610, 123)
    # draw_stars(650, 430)
    # draw_stars(725, 203)
    # draw_stars(750, 520)
    # draw_stars(780, 610)
    # draw_stars(814, 230)
    # draw_stars(840, 491)
    # draw_stars(900, 602)
    # draw_stars(930, 349)
    # draw_stars(950, 503)
    # draw_stars(980, 123)
    
    # for _ in range(50):
    #     draw_stars(random.randrange(0, WIDTH), random.randrange(0, HEIGHT))

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

    arcade.draw_lrtb_rectangle_filled(WIDTH/2 - 5, WIDTH/2 + 5, HEIGHT, 0, arcade.color.BLACK)


def on_key_press(key, modifiers):
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, fire_laser_human, fire_laser_alien, spaceship_human_x, spaceship_human_y, spaceship_alien_x, spaceship_alien_y

    if key == arcade.key.A:
        left_pressed_human = True
     
    if key == arcade.key.LEFT:
        left_pressed_alien = True
    
    if key == arcade.key.D:
        right_pressed_human = True

    if key == arcade.key.RIGHT:
        right_pressed_alien = True

    if key == arcade.key.UP:
        fire_laser_alien = True     
        alien_x_positions_laser.append (spaceship_alien_x)
        alien_y_positions_laser.append (spaceship_alien_y)
    
    if key == arcade.key.W:
        fire_laser_human = True     
        human_x_positions_laser.append (spaceship_human_x)
        human_y_positions_laser.append (spaceship_human_y)


def on_key_release(key, modifiers):
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, laser_fire_key

    if key == arcade.key.A:
        left_pressed_human = False
     
    if key == arcade.key.LEFT:
        left_pressed_alien = False
    
    if key == arcade.key.D:
        right_pressed_human = False

    if key == arcade.key.RIGHT:
        right_pressed_alien = False

    if key == arcade.key.UP: 
        laser_fire_key = False
        
    if key == arcade.key.W:
        laser_fire_key = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(1000, 750, "Fun Game")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.schedule(update, 1/100)    
    arcade.run()


# Call the main function to get the program started.
if __name__ == '__main__':
    setup()
