import pgzrun
import pygame
from pgzero.builtins import Actor
from random import randint

apple = Actor("apple")
orange = Actor ("orange")
pineapple = Actor ("pineapple")
fruit = pineapple
beep = tone.create('C4', 0.2)

WIDTH = 1400
HEIGHT = WIDTH / 16 * 10

print("Width * Height = " + str(WIDTH) + "x" + str(HEIGHT));

def draw():
    screen.clear()
    screen.fill((0,0,0))
    fruit.draw()
    
def place_apple():
    fruit.x = randint (10,WIDTH)
    fruit.y = randint (10,HEIGHT)

def on_mouse_down(pos):
    if fruit.collidepoint (pos):
        print(" Treffer!")
        place_apple()
        beep.play()
    else:
        print (" Daneben!")
        quit()

place_apple()

pgzrun.go()
