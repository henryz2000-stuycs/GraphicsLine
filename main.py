from display import *
from draw import *
import random

screen = new_screen()
white = [ 255, 255, 255 ]

#draw_line(250, 250, 500, 0, screen, white)#slope -1
#draw_line(0, 250, 500, 250, screen, white)#slope 0
#draw_line(250, 250, 500, 500, screen, white)#slope 1

#=====bouquet code=====
'''
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
   
'''
#=====end bouquet code=====

#=====dw test code=====
#'''
c = [0, MAX_COLOR, 0]
s = screen

clear_screen(s);
#octants 1 and 5
draw_line(0, 0, XRES-1, YRES-1, s, c);
draw_line(0, 0, XRES-1, YRES / 2, s, c);
draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c);

#octants 8 and 4
c = [0, MAX_COLOR, 255]
draw_line(0, YRES-1, XRES-1, 0, s, c);
draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
draw_line(XRES-1, 0, 0, YRES/2, s, c);

#octants 2 and 6
c = [255, 0, 0]
draw_line(0, 0, XRES/2, YRES-1, s, c);
draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);

#octants 7 and 3
c = [255, 0, 255]
draw_line(0, YRES-1, XRES/2, 0, s, c);
draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);

#horizontal and vertical
c = [255, 255, 0]
draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);
#'''
#=====end dw test code=====

display(screen)
save_extension(screen, 'img.png')
