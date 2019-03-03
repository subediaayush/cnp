import pygame
import chess


def main():
    pygame.init()

    pygame.display.set_caption("cnp")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((640, 480))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
