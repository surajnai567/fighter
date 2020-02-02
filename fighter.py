import pygame


class Fighter:
    def __init__(self, win, window_size, villian=False, color=(0, 0, 255)):
        self.is_villian = villian
        self.window_size = window_size
        self.color = color
        if self.is_villian:
            self.color = (255, 255, 255)
        self.win = win
        self.rec_size = 10
        self.dir = 'w'
        self.x_y = [0, 0]
        self.head = [20, 10]

    def get_xy(self):
        return self.x_y[0], self.x_y[1]

    def draw(self, blocks):
        for x, y in blocks:
            pygame.draw.rect(self.win, self.color, (x, y, self.rec_size, self.rec_size))

    def fighter_type(self):
        return self.is_villian

    def draw_rec_block(self, x, y):
        pygame.draw.rect(self.win, self.color, (x, y, self.rec_size, self.rec_size))

    def draw_fighter(self, x, y, direction):
        number_of_block = 5
        if direction == 'w':
            self.dir = 'w'
            self.x_y = [x, y]
            self.head = [x+20, y+10]
            for i in range(5):
                self.draw_rec_block(x, y)
                self.draw_rec_block(x+10, y+10)
                self.draw_rec_block(x, y+20)
                self.draw_rec_block(x+10, y)
                self.draw_rec_block(x+10, y+20)
                self.draw_rec_block(x+20, y+10)   # head

        elif direction == 'n':
            self.dir = 'n'
            self.x_y = [x, y]
            self.head = [x+10, y]
            for i in range(5):
                self.draw_rec_block(x+10, y)  # head
                self.draw_rec_block(x, y+10)
                self.draw_rec_block(x+10, y+10)
                self.draw_rec_block(x+20, y+10)
                self.draw_rec_block(x, y+20)
                self.draw_rec_block(x+20, y+20)

        elif direction == 'e':
            self.dir = 'e'
            self.x_y = [x, y]
            self.head = [x, y+10]
            for i in range(5):
                self.draw_rec_block(x, y+10)  # head
                self.draw_rec_block(x+10, y)
                self.draw_rec_block(x+20, y)
                self.draw_rec_block(x+10, y+10)
                self.draw_rec_block(x+10, y+20)
                self.draw_rec_block(x+20, y+20)

        elif direction == 's':
            self.dir = 's'
            self.x_y = [x, y]
            self.head = [x+10, y+20]
            for i in range(5):
                self.draw_rec_block(x, y)
                self.draw_rec_block(x+20, y)
                self.draw_rec_block(x, y+10)
                self.draw_rec_block(x+10, y+10)
                self.draw_rec_block(x+20, y+10)
                self.draw_rec_block(x+10, y+20)  # head

    def shoot(self):
        return self.head, self.dir, self.is_villian










