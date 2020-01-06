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
human_x_positions_laser = []
human_y_positions_laser = []
alien_x_positions_laser = []
alien_y_positions_laser = []

# loop 100 times
for _ in range(10):
    # generate random x and y values
    x_human = random.randrange(WIDTH/2 + 25, WIDTH)
    y_human = random.randrange(HEIGHT, HEIGHT*2)
    x_alien = random.randrange(0, WIDTH/2 - 25)
    y_alien = random.randrange(HEIGHT, HEIGHT*2)

    # append the x and y values to the appropriate list
    human_x_positions.append(x_human)
    human_y_positions.append(y_human)
    alien_x_positions.append(x_alien)
    alien_y_positions.append(y_alien)

spaceship_human_x = 260
spaceship_human_y = 81
spaceship_alien_x = 760
spaceship_alien_y = 81

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
    arcade.draw_ellipse_filled(x, y, 5, 50, arcade.color.GREEN, 40)
    arcade.draw_ellipse_filled(x - 20, y, 5, 50, arcade.color.GREEN, 140)
    arcade.draw_ellipse_filled(x - 10, y + 19, 80, 50, arcade.color.LIGHT_BLUE)
    arcade.draw_ellipse_filled(x - 10, y + 19, 110, 8, arcade.color.GREEN)


def draw_spaceship_alien(x, y):
    arcade.draw_ellipse_filled(x, y, 5, 50, arcade.color.GREEN, 40)
    arcade.draw_ellipse_filled(x - 20, y, 5, 50, arcade.color.GREEN, 140)
    arcade.draw_ellipse_filled(x - 10, y + 19, 80, 50, arcade.color.LIGHT_BLUE)
    arcade.draw_ellipse_filled(x - 10, y + 19, 110, 8, arcade.color.GREEN)


def update(delta_time):
    for index in range(len(human_y_positions)):
        human_y_positions[index] -= 3

        if human_y_positions[index] < 0:
            human_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            human_x_positions[index] = random.randrange(WIDTH/2 + 30, WIDTH)

    for index in range(len(alien_y_positions)):
        alien_y_positions[index] -= 3

        if alien_y_positions[index] < 0:
            alien_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            alien_x_positions[index] = random.randrange(0, WIDTH/2 - 30)

    for index in range(len(human_y_positions_laser)):
        if human_y_positions_laser[index] <750 + 50:
            human_y_positions_laser[index] += 30


    for index in range(len(alien_y_positions_laser)):
        if alien_y_positions_laser[index] < 750 + 50:
            alien_y_positions_laser[index] += 30
    
    global left_pressed_human, left_pressed_alien, right_pressed_human, right_pressed_alien, spaceship_human_x, spaceship_alien_x
    if left_pressed_human:
        spaceship_human_x -= 5

    if left_pressed_alien:
        spaceship_alien_x -= 5
    
    if right_pressed_human:
        spaceship_human_x += 5

    if right_pressed_alien:
        spaceship_alien_x += 5

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

    if key == arcade.key.UP or key == arcade.key.W:
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