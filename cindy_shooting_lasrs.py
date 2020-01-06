import arcade
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750


def draw_laser(x, y, laser_movement):
    #laser
    arcade.draw_rectangle_filled(x, 100 + y + laser_movement, 7, 30, arcade.color.RED)
  

def on_draw(delta_time):
    global laser1_x
    global laser_movement_y


    """ Draw everything"""
    arcade.start_render()

    #draw_laser
    draw_laser(650, 230, laser_movement_y)
    draw_laser(150, 230, laser_movement_y)

    
    # Add one to the x value, making the person move right
    # Negative numbers move left. Larger numbers move faster.
    laser_movement_y += 4

# Create a value that our regular_person1_x will start at.
laser1_x = 100
laser_movement_y = 50



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Arcade Assignment")
    arcade.set_background_color(arcade.color.BLAST_OFF_BRONZE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()