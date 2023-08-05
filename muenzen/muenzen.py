import pgzrun
from pgzero.builtins import Actor
from random import randint

WIDTH = 800
HEIGHT = 800
stepsize = 4
fox = Actor ("fox")
fox.pos = 100, 100
coin = Actor ("coin")
coin.pos = 200, 200
score = 0
game_over = False

def draw():
  screen.fill("green")
  fox.draw()
  coin.draw()
  screen.draw.text("Punkte: " + str(score), color="black", topleft=(10,10))

  if game_over:
    screen.fill("pink")
    screen.draw.text("Endstand: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
  coin.x = randint(20, (WIDTH - 20))
  coin.y = randint(20, (HEIGHT - 20))

def time_up():
  global game_over
  game_over = True

def update():
  global score
  global stepsize
  if keyboard.left:
    fox.x = fox.x - stepsize
  elif keyboard.right:
    fox.x = fox.x + stepsize
  elif keyboard.up:
    fox.y = fox.y - stepsize
  elif keyboard.down:
    fox.y = fox.y + stepsize

  coin_collected = fox.colliderect(coin)

  if coin_collected:
    score = score + 10
    place_coin()
 
clock.schedule(time_up, 60.0)
place_coin()

pgzrun.go()

