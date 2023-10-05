from pico2d import *
import random

# Game object class here
class Grass: #클래스 이름은 대문자로 시작하는 명사..
    def __init__(self):
        self.image = load_image('grass.png')


    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0,7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class BigBall:
    def __init__(self):
        self.x,self.y = random.randint(100,700),599
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 60:
            self.y -= random.randint(1,5)

    def draw(self):
        self.image.clip_draw(0,0,41,41,self.x,self.y)

class SmallBall:
    def __init__(self):
        self.x,self.y = random.randint(100,700),599
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 60:
            self.y -= random.randint(1,5)

    def draw(self):
        self.image.clip_draw(0,0,21,21,self.x,self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global world

    running = True
    world = []

    grass = Grass() #클래스를 이용해 객체를 찍어냄.
    world.append(grass)

    bigball = [BigBall() for i in range(10)]
    smallball = [SmallBall() for i in range(10)]

    world += bigball
    world += smallball

    team = [Boy() for i in range(11)]
    world += team

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def update_world():
    for o in world:
        o.update()

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world() # 객체들의 상호작용 결과 업데이트
    render_world()
    delay(0.05)

# finalization code

close_canvas()
