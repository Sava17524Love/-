from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('1632448069_21-idei-club-p-psikhbolnitsa-myagkaya-komnata-interer-kra-26 - копия - копия.jpg'), (win_width, win_height))

game = True
clock = time.Clock()
FPS = 60

#mixer.init()
#mixer.music.load('')
#mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,60))
        self.rect = self.image.get_rect()
        self.speed.x = player_x
        self.speed.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        kyes = key.get_pressed()
        if kyes[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if kyes[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if kyes[K_DOWN] and self.rect.y < win_width - 70:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'lelf'
        if self.direction == 'left':
                self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.well_height = well_height
        self.image = Sueface((self.wall_width, self.well_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
w1 = Wall(154, 205, 50, 100, 20, 450, 10)

player = Player('Penguins-transformed - копия - копия.png', 5, win_height - 80, 4)

monster = GameSprite('Penguins-transformed - копия - копия.png', win_width - 80, 280, 3)

goal = GameSprite('', 400, 420, 0)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    player.update()
    monster.update()
    player.reset()
    monster.reset()
    goal.reset()
    w1.draw_wall()
    display.update()
    clock.tick(FPS)

