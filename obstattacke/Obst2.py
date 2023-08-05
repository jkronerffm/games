import pgzrun
from pgzero.builtins import Actor
from random import randint

apple = Actor("apple")
orange = Actor ("orange")
pineapple = Actor ("pineapple")
fruits = [ apple, orange, pineapple]
fruit = apple

WIDTH = 1024
HEIGHT = 768
red = 200, 0, 0
box = Rect((512-50, 0),(100,16));
hits = int(0)

def draw():
    global hits
    global fruits
    screen.clear()
    screen.fill((192,192,192))
    screen.draw.rect(box, red)
    screen.draw.textbox(str(hits), box)
    fruit.draw()

def increment_hits():
    global hits
    hits += 1

def decrement_hits():
    global hits
    hits -= 1
    
def place_apple():
    global fruit
    global fruits
    fruit = fruits[randint(0,2)]
    fruit.x = randint (10,1024)
    fruit.y = randint (10,768)

def on_mouse_down(pos):
    global fruit
    if fruit.collidepoint (pos):
        print(str(hits) + " Treffer !")
        increment_hits()
        place_apple()
    else:
        print ("Daneben !")
        decrement_hits()
        if hits > 0:
            place_apple()
        else:
            quit()

place_apple()
hits = 0

pgzrun.go()
