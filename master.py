import arcade


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
   
    draw_alien(250, 500)
    draw_human(750, 500)
    draw_spaceship()

    arcade.draw_lrtb_rectangle_filled(495, 505, 750, 0, arcade.color.BLACK)


def main():
    arcade.open_window(1000, 750, "Fun Game")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()