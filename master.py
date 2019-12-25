import arcade


def draw_stars(x, y):
    arcade.draw_circle_filled(x, y, 5, arcade.color.YELLOW)


def draw_alien(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.PURPLE)
    arcade.draw_rectangle_filled(x, y - 65, 80, 60, arcade.color.PURPLE, -90)
    arcade.draw_rectangle_filled(x + 22, y - 100, 40, 20, arcade.color.PURPLE, -45)
    arcade.draw_rectangle_filled(x - 22, y - 100, 40, 20, arcade.color.PURPLE, 45)
    arcade.draw_rectangle_filled(x + 23, y - 50, 40, 20, arcade.color.PURPLE, -340)
    arcade.draw_rectangle_filled(x - 23, y - 50, 40, 20, arcade.color.PURPLE, 340)
    # point_list = ((x + 40, y + 40),
              # (x + 80, y + 60),
              # (x + 140, y + 50))
    # arcade.draw_polygon_filled(point_list, arcade.color.PURPLE)


def draw_human(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.LIGHT_BLUE)
    arcade.draw_rectangle_filled(x, y - 65, 80, 60, arcade.color.LIGHT_BLUE, -90)
    arcade.draw_rectangle_filled(x + 22, y - 100, 40, 20, arcade.color.LIGHT_BLUE, -45)
    arcade.draw_rectangle_filled(x - 22, y - 100, 40, 20, arcade.color.LIGHT_BLUE, 45)
    arcade.draw_rectangle_filled(x + 23, y - 50, 40, 20, arcade.color.LIGHT_BLUE, -340)
    arcade.draw_rectangle_filled(x - 23, y - 50, 40, 20, arcade.color.LIGHT_BLUE, 340)


def on_draw(delta_time):
    arcade.start_render()

    draw_stars(30, 100)
    draw_stars(50, 50)
    draw_stars(400, 200)
    draw_stars(670, 340)
    draw_stars(500, 100)
    draw_stars(20, 700)
    draw_stars(700, 620)
    draw_stars(800, 560)
    draw_stars(430, 450)
    draw_stars(130, 360)
    draw_stars(200, 201)
    draw_stars(240, 459)
    draw_stars(280, 704)
    draw_stars(320, 10)
    draw_stars(360, 372)
    draw_stars(400, 503)
    draw_stars(510, 80)
    draw_stars(610, 123)
    draw_stars(650, 430)
    draw_stars(725, 203)
    draw_stars(750, 520)
    draw_stars(780, 610)
    draw_stars(814, 230)
    draw_stars(840, 491)
    draw_stars(900, 602)
    draw_stars(930, 349)
    draw_stars(950, 503)
    draw_stars(980, 123)
    
    draw_alien(600, 200)
    draw_human(300, 200)


def main():
    arcade.open_window(1000, 750, "Fun Game")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()