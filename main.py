from display import *
from draw import *
import random

screen = new_screen()
white = [ 255, 255, 255 ]

#draw_line(250, 250, 500, 0, screen, white)#slope -1
#draw_line(0, 250, 500, 250, screen, white)#slope 0
#draw_line(250, 250, 500, 500, screen, white)#slope 1

x = 0
while x < 500:
    draw_line(x+50, 500, x+50, 0, screen, white)#draw vertical lines
    x += 50

for i in range(500):
    x = 0
    y = random.randint(250, 500)
    changeY = random.randint(0, 100)

    while x < 250:
        randomR = random.randint(0, 256)
        randomG = random.randint(0, 256)
        randomB = random.randint(0, 256)
        randomcolor = [randomR, randomG, randomB]
        #print x
        #print type(y)
        draw_line(x, y, x+50, y-changeY, screen, randomcolor)#draw refracting lines
        draw_line(0, y, 500, y, screen, white)#draws horizontal line
        draw_line(450-x, y-changeY, 500-x, y, screen, randomcolor)#draws opposite of refracting lines
        x += 50
        y -= changeY
        changeY += random.randint(0, 50)
    
display(screen)
save_extension(screen, 'img.png')
