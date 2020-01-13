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

draw_enemy_rate = 6
draw_meteor_rate = 2
sec = 0
mins = 0

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

def add_more_humans():
    global human_x_positions, human_y_positions
    
    # generate random x and y values
    x_human = random.randrange(WIDTH/2 + 75, WIDTH - 75)
    y_human = random.randrange(HEIGHT, HEIGHT*2)
    
    # append the x and y values to the appropriate list
    human_x_positions.append(x_human)
    human_y_positions.append(y_human)

def add_more_aliens():
    global alien_x_positions, alien_y_positions

    # generate random x and y values
    x_alien = random.randrange(75, WIDTH/2 - 75)
    y_alien = random.randrange(HEIGHT, HEIGHT*2)

    # append the x and y values to the appropriate list
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

if sec == 30:
    draw_enemy_rate += 1
    draw_meteor_rate += 1

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

sec = 0
mins = 0

def draw_background(x, y):
    scale = 1
    texture = arcade.load_texture("night_sky.jpg")
    arcade.draw_texture_rectangle(x, y, scale * texture.width, 
                                    scale * texture.height, texture, 0)

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

def start_timer():
    import time
    import sys
    global sec
    global mins

    time_start = time.time()

    while True:
        time.sleep(1)
        sec = int(time.time() - time_start) - mins * 60
        if sec > 30:
            sec = 0

def laser_human_collision():
    global human_x_positions_laser, human_y_positions_laser
    global x_human_laser, y_human_laser
    global human_width, human_height

    human_hit = False 
    human_index = 0
    
    for x_human, y_human in zip(human_x_positions, human_y_positions):
        human_laser_index = 0

        for x_human_laser, y_human_laser in zip(human_x_positions_laser, human_y_positions_laser):
            if (x_human - human_width/2 <= x_human_laser <= x_human + human_width/2 ) and (y_human - human_height/2 <= y_human_laser <= y_human + human_height/2 ):
              
                del human_x_positions[human_index]
                del human_y_positions[human_index]

                del human_x_positions_laser[human_laser_index]
                del human_y_positions_laser[human_laser_index]
                human_hit = True 
                add_more_humans()
                break 
            
            else: human_laser_index +=1

        if human_hit == False: 
                human_index +=1
        else: 
            break

def laser_alien_collision():
    global alien_x_positions_laser, alien_y_positions_laser
    global x_alien_laser, y_alien_laser
    global alien_width, alien_height

    alien_hit = False 
    alien_index = 0

    for x_alien, y_alien in zip(alien_x_positions, alien_y_positions):
        alien_laser_index = 0

        for x_alien_laser, y_alien_laser in zip(alien_x_positions_laser, alien_y_positions_laser):
            if (x_alien - alien_width/2 <= x_alien_laser <= x_alien + alien_width/2 ) and (y_alien- alien_height/2 <= y_alien_laser <= y_alien + alien_height/2 ):
              
                del alien_x_positions[alien_index]
                del alien_y_positions[alien_index]

                del alien_x_positions_laser[alien_laser_index]
                del alien_y_positions_laser[alien_laser_index]
                alien_hit = True                               
                add_more_aliens()
                break 
            

            else: alien_laser_index +=1

        if alien_hit == False: 
                alien_index +=1
        else: 
            break

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


def on_draw():
    global spaceship_human_x, spaceship_human_y, spaceship_alien_x, spaceship_alien_y
    
    arcade.start_render()
    draw_background(500, 375)
    laser_human_collision()
    laser_alien_collision()


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


def on_key_press(key, modifiers):
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, fire_laser_human, fire_laser_alien, spaceship_human_x, spaceship_human_y, spaceship_alien_x, spaceship_alien_y

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
        alien_x_positions_laser.append (spaceship_alien_x)
        alien_y_positions_laser.append (spaceship_alien_y)
    
    if key == arcade.key.UP:
        fire_laser_human = True     
        human_x_positions_laser.append (spaceship_human_x)
        human_y_positions_laser.append (spaceship_human_y)
        

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
