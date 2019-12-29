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

# stars_x = random.randrange(0, WIDTH)
# stars_y = random.randrange(0, HEIGHT)

def draw_stars(x, y):
    arcade.draw_circle_filled(x, y, 5, arcade.color.YELLOW)


def draw_alien(x, y):
    arcade.draw_circle_filled(x, y - 26, 24, arcade.color.LIGHT_BLUE)
    arcade.draw_circle_filled(x, y - 28, 20, arcade.color.PURPLE)
    arcade.draw_rectangle_filled(x, y - 65, 40, 30, arcade.color.PURPLE, -90)
    arcade.draw_rectangle_filled(x + 15, y - 90, 20, 10, arcade.color.PURPLE, -60)
    arcade.draw_rectangle_filled(x - 15, y - 90, 20, 10, arcade.color.PURPLE, 60)
    arcade.draw_rectangle_filled(x + 23, y - 50, 20, 10, arcade.color.PURPLE, -340)
    arcade.draw_rectangle_filled(x - 23, y - 50, 20, 10, arcade.color.PURPLE, 340)
    point_list = ((x + 8, y - 12),
              (x + 20, y + 5),
              (x + 30, y - 10))
    arcade.draw_polygon_filled(point_list, arcade.color.PURPLE)
    point_list = ((x - 10, y - 12),
              (x - 23, y + 5),
              (x - 33, y - 10))
    arcade.draw_polygon_filled(point_list, arcade.color.PURPLE)


def draw_human(x, y):
    arcade.draw_circle_filled(x, y - 26, 24, arcade.color.PURPLE)
    arcade.draw_circle_filled(x, y - 28, 20, arcade.color.LIGHT_BLUE)
    arcade.draw_rectangle_filled(x, y - 65, 40, 30, arcade.color.LIGHT_BLUE, -90)
    arcade.draw_rectangle_filled(x + 15, y - 90, 20, 10, arcade.color.LIGHT_BLUE, -60)
    arcade.draw_rectangle_filled(x - 15, y - 90, 20, 10, arcade.color.LIGHT_BLUE, 60)
    arcade.draw_rectangle_filled(x + 23, y - 50, 20, 10, arcade.color.LIGHT_BLUE, -340)
    arcade.draw_rectangle_filled(x - 23, y - 50, 20, 10, arcade.color.LIGHT_BLUE, 340)


def draw_spaceship():
    arcade.draw_ellipse_filled(260, 81, 5, 50, arcade.color.GREEN, 40)
    arcade.draw_ellipse_filled(240, 81, 5, 50, arcade.color.GREEN, 140)
    arcade.draw_ellipse_filled(250, 100, 80, 50, arcade.color.LIGHT_BLUE)
    arcade.draw_ellipse_filled(250, 100, 110, 8, arcade.color.GREEN)

    arcade.draw_ellipse_filled(760, 81, 5, 50, arcade.color.GREEN, 40)
    arcade.draw_ellipse_filled(740, 81, 5, 50, arcade.color.GREEN, 140)
    arcade.draw_ellipse_filled(750, 100, 80, 50, arcade.color.LIGHT_BLUE)
    arcade.draw_ellipse_filled(750, 100, 110, 8, arcade.color.GREEN)


def setup():
    arcade.open_window(1000, 750, "Fun Game")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.schedule(update, 1/100)    
    arcade.run()


def update(delta_time):
    for index in range(len(human_y_positions)):
        human_y_positions[index] -= 5

        if human_y_positions[index] < 0:
            human_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            human_x_positions[index] = random.randrange(WIDTH/2 + 25, WIDTH)

    for index in range(len(alien_y_positions)):
        alien_y_positions[index] -= 5

        if alien_y_positions[index] < 0:
            alien_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            alien_x_positions[index] = random.randrange(0, WIDTH/2 - 25)


def on_draw():
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
    
    for _ in range(50):
        draw_stars(random.randrange(0, WIDTH), random.randrange(0, HEIGHT))

    for x_human, y_human in zip(human_x_positions, human_y_positions):
        draw_human(x_human, y_human)
    
    for x_alien, y_alien in zip(alien_x_positions, alien_y_positions):
        draw_alien(x_alien, y_alien)
    
    draw_spaceship()

    arcade.draw_lrtb_rectangle_filled(WIDTH/2 - 5, WIDTH/2 + 5, HEIGHT, 0, arcade.color.BLACK)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


# Call the main function to get the program started.
if __name__ == '__main__':
    setup()