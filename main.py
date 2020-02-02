import pygame
from fighter import Fighter
from player import Player


class Main:
    def __init__(self, display=(300, 500)):
        self.window_size = display
        pygame.init()
        self.win = pygame.display.set_mode(display)
        self.fighters = []
        self.player = []
        self.bullets = []


    def on_exec(self):
        fight1 = Fighter(self.win, window_size=self.window_size, villian=True)
        fight2 = Fighter(self.win, window_size=self.window_size, villian=False)
        ani = Player('aniket', self.win)
        f_dir = 'w'
        run = True
        x_cod, y_cod = 0, 0

        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.QUIT]:
                run = False

            if keys[pygame.K_RIGHT]:
                x, y = fight1.get_xy()
                f_dir = 'w'
                x_cod, y_cod = ani.move_right(x, y)

            elif keys[pygame.K_UP]:
                x, y = fight1.get_xy()
                f_dir = 'n'
                x_cod, y_cod = ani.move_up(x, y)
            elif keys[pygame.K_DOWN]:
                x, y = fight1.get_xy()
                f_dir = 's'
                x_cod, y_cod = ani.move_down(x, y)
            elif keys[pygame.K_LEFT]:
                x, y = fight1.get_xy()
                f_dir = 'e'
                x_cod, y_cod = ani.move_left(x, y)
            elif keys[pygame.K_SPACE]:
                head, direction, is_v = fight1.shoot()
                print(head)
                ani.shoot(head, direction)

            self.win.fill((0, 0, 0))
            fight1.draw_fighter(x_cod, y_cod, f_dir)
            fight2.draw_fighter(40, 50, 'e')
            pygame.display.update()
        pygame.quit()


app = Main()
app.on_exec()