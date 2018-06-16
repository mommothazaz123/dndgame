import pygame

from game import Game

if __name__ == '__main__':
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load("music/Wepa.ogg")
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((640, 480))
    screen.fill(pygame.Color("white"))

    game = Game(screen)
    game.init()
    pygame.display.flip()

    clock = pygame.time.Clock()

    frame = 0
    while game.running:
        frame += 1
        game.run(frame)
        clock.tick_busy_loop(30)
        print(clock.get_fps())

    pygame.quit()
