from display import *

#returns the octent number
def octent(x0, y0, x1, y1):
    try:
        m = float((y1 - y0)) / float((x1 - x0))
        #print m
    except: #vertical line
        #print "vertical line"
        return 0
    
    if ((m >= 0) and (m <= 1)):
        return 1
    elif (m > 1):
        return 2
    elif ((m >= -1) and (m < 0)):
        return 8
    elif (m < -1):
        return 7

def draw_line(x0, y0, x1, y1, screen, color):
    if (x0 > x1):
        draw_line(x1, y1, x0, y0, screen, color)
    else:
        x = x0
        y = y0

        A = y1-y0
        B = x0-x1

        m = octent(x0, y0, x1, y1)
        
        #vertical line
        if (m == 0):
            if (y1 < y):
                y = y1
                y1 = y0
            while (y <= y1 and y <= 500):
                #print "y = "
                #print y
                plot(screen, color, x, y)
                y += 1
        
        #octent I
        elif (m == 1):
            #print "octent I"
            d = 2*A + B
            while x <= x1:
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += 2*B
                x += 1
                d += 2*A
            
        #octent II
        elif (m == 2):
            #print "octent II"
            d = A + 2*B
            while y <= y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += 2*A
                y += 1
                d += 2*B

        #octent VIII
        elif (m == 8):
            #print "octent VIII"
            d = 2*A - B
            while x <= x1:
                plot(screen, color, x, y)
                if d < 0:
                    y -= 1
                    d -= 2*B
                x += 1
                d += 2*A

        #octent VII
        elif (m == 7):
            #print "octent VII"
            d = A - 2*B
            while y >= y1:
                plot(screen, color, x, y)
                if d > 0:
                    x += 1
                    d += 2*A
                y -= 1
                d -= 2*B
    #end
    
