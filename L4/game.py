import pgzrun
import random
WIDTH = 600
HEIGHT = 500
bee = Actor("bee")
bee.x = 300
bee.y = 300
flower = Actor("flower")
flower.x = random.randint(20, 580)
flower.y = random.randint(20, 580)
def draw():
    screen.fill((210, 150, 190))
    screen.blit("grass", (0,0))
    bee.draw()
    flower.draw()
def update():
    if keyboard.up:
        bee.y +=-10
    if keyboard.down:
        bee.y +=10
    if keyboard.left:
        bee.x +=-10
    if keyboard.right:
        bee.x +=10
    if bee.colliderect(flower):
        flower.x = random.randint(20, 580)
        flower.y = random.randint(20, 580)
pgzrun.go()