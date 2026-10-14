from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self): 
        pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0,8)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100,100, self.x, self.y)

class Zombie:
    def __init__(self):
            self.image = load_image('zombie_run_animation.png')
            self.x, self.y = 100, 170
            self.frame = 0
    
    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5
    
    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame*frame_width, 0, frame_width, frame_height, self.x, self.y, frame_width //2, frame_height //2)

class Ball():
    def __init__(self):
        Ball.small_image = load_image('ball21x21.png')
        Ball.big_image = load_image('ball41x41.png')

        if random.randint(0, 1) == 0:         
            self.image = Ball.small_image
            self.size = 21
        else:
            self.image = Ball.big_image
            self.size = 41

        self.x = random.randint(20,780)
        self.y = 60
        self.speed = random.randint(17, 18) 

    def update(self):
        self.y += self.speed

        if self.y >= 600 - self.size:
            self.y -= 50




    def draw(self):
        self.image.draw(self.x, self.y)

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
    global zombie

    #세계에 존재하는 월드 리스트를 만든다.
    world = []

    running = True
    grass = Grass()
    zombie = Zombie()
    world.append(grass)
    world.append(zombie)

    team = [Boy() for i in range(11)]
    world += [Ball() for i in range(20)]
    world += team

def update_world():

    for o in world:
        o.update()

def render_world():
    clear_canvas()

    for o in world:
        o.draw()

    update_canvas()

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()


