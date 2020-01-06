import arcade

arcade.open_window(1000, 750, "Final Assignment")
arcade.start_render()

def draw_spaceship():
    arcade.draw_ellipse_filled(260, 81, 5, 50, arcade.color.GREEN, 40)
    arcade.draw_ellipse_filled(240, 81, 5, 50, arcade.color.GREEN, 140)
    arcade.draw_ellipse_filled(250, 100, 80, 50, arcade.color.LIGHT_BLUE)
    arcade.draw_ellipse_filled(250, 100, 110, 8, arcade.color.GREEN)

    arcade.draw_ellipse_filled(760, 81, 5, 50, arcade.color.GREEN, 40)
    arcade.draw_ellipse_filled(740, 81, 5, 50, arcade.color.GREEN, 140)
    arcade.draw_ellipse_filled(750, 100, 80, 50, arcade.color.LIGHT_BLUE)
    arcade.draw_ellipse_filled(750, 100, 110, 8, arcade.color.GREEN)

def draw_spaceship_human(x, y):
    arcade.draw_ellipse_filled(x + 10, y - 19, 5, 50, arcade.color.GREEN, 40)
    arcade.draw_ellipse_filled(x - 10, y - 19, 5, 50, arcade.color.GREEN, 140)
    arcade.draw_ellipse_filled(x, y, 80, 50, arcade.color.LIGHT_BLUE)
    arcade.draw_ellipse_filled(x, y, 110, 8, arcade.color.GREEN)


def draw_spaceship_alien(x, y):
    arcade.draw_ellipse_filled(x + 10, y - 19, 5, 50, arcade.color.GREEN, 40)
    arcade.draw_ellipse_filled(x - 10, y - 19, 5, 50, arcade.color.GREEN, 140)
    arcade.draw_ellipse_filled(x, y, 80, 50, arcade.color.LIGHT_BLUE)
    arcade.draw_ellipse_filled(x, y, 110, 8, arcade.color.GREEN)


def main():
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_spaceship()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()

