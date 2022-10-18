from pygame import *
from check_files import check_files
#inzialate fonts and mixer
font.init()
mixer.init()
score1 = 0 #score racket1
score2 = 0 #score racket2
FPS = 60 
speed_x = 3 #Racket Speed on x 
speed_y = 3 #Racket Speed on y
game = True
finish = False
back = (200,255,255)
win_width = 600
win_height = 500
required_files = ['sprites//ball.png','sprites//racket.png','sound_fx//racket_hit.wav','sound_fx//wall.wav']
#audio
racket_hit = mixer.Sound('sound_fx//racket_hit.wav')
wall = mixer.Sound('sound_fx//wall.wav')
#fonts
font_score = font.Font(None,35)

check_files(required_files)



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def to_spawn(self,x,y):
        window.blit(self.image,(x,y))
        self.rect.x = x
        self.rect.y = y
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed   
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
class Bot(GameSprite):
    def bot_on(self,target):
        if self.rect.y > target.rect.y:
            self.rect.y -= self.speed
        if self.rect.y < target.rect.y:
            self.rect.y += self.speed

# objects
racket1 = Player('sprites//racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('sprites//racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('sprites//ball.png', 200, 200, 4, 50, 50)

#izializate window
display.set_caption('Pong')
window = display.set_mode((win_width,win_height))
window.fill(back)
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
            window.fill(back)
            ball.rect.x += speed_x
            ball.rect.y += speed_y
            if ball.rect.y > win_height-50 or ball.rect.y < 0:
                speed_y *= -1
                wall.play()
            if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
                speed_x *= -1
                racket_hit.play()
            if ball.rect.x < 0:
                score2 += 1
                ball.to_spawn(200,200)
                racket1.to_spawn(30,200)
                racket2.to_spawn(520,200)
            if ball.rect.x > 550:
                score1 += 1
                ball.to_spawn(200,200)
                racket1.to_spawn(30,200)
                racket2.to_spawn(520,200)
            score_disp = font_score.render('{}:{}'.format(str(score1),str(score2)),True,(0,0,0))
            window.blit(score_disp,(280,0))
            racket1.update_l()
            racket2.update_r()
            ball.reset()
            racket1.reset()
            racket2.reset()
    display.update()
    clock.tick(FPS)
