# Function to calculate Area of a circle
# Inputs: radius(float)
# Outputs: area(float)
def calculateAreaOfCircle(radius):
    from math import pi
    area = pi * (radius**2)
    return area

# Function to compute MPG for a car.
# Inputs: miles driven (float), gallons used(float) 
# Output: MilesPerGalon(float)
def calculateMpg(milesDriven,galonsUsed):
    milesPerGalon = milesDriven/galonsUsed
    return milesPerGalon

# Function to convert fahrenheit to celsius. (Formula: Deduct 32, then multiply by 5, then divide by 9)
# Input: degreesFarenheit(int)
# Output: degreesCelcius(float)
def convertFahrenheitToCelsius(farenheit):
    celcius = ((farenheit - 32) * 5) / 9
    return round(celcius,2)

# Function to calculate distance between 2 points
# Inputs: Point one(array) and Point two(array)
# Output: Distance(float) 
def calculateDistanceBetweenPoints(point1, point2):
    from math import sqrt, pow
    x1 = int(point1[0])
    y1 = int(point1[1])
    x2 = int(point2[0])
    y2 = int(point2[1])
    distance = sqrt(pow((x2-x1),2) + pow((y2-y1),2))
    return distance

# Function to reset and clear the backlight color of the gfxhat
# Input: none
# Output: none
def clearBacklight():
    from gfxhat import backlight
    backlight.set_all(0, 0, 0)
    backlight.show()

# Function to draw a horizontal line in the gfxhat given the desired y pixel
# Input: y (int) > pixel of the gfxhat to make the horizontal line
# Output: none
def drawHorizontalLine(y):
    from gfxhat import lcd, backlight
    from time import sleep
    from rios0021Library import clearBacklight
    # Clear the lcd
    lcd.clear()
    lcd.show()
    # Clear backlight
    clearBacklight()
    r = 255
    g = 0
    # Draw the line at y
    for x in range(0, 128):
        lcd.set_pixel(x,y,1)
        lcd.show()
        # Additional code to make a color transition while drawing line
        backlight.set_all(r, g, 0)
        backlight.show()
        if (g < 252):
            g += 4
        elif(r > 3):
            r -= 4
    # Turn off backlight after 2 seconds
    sleep(2)
    clearBacklight()
    lcd.clear()
    lcd.show()

# Function to draw a vertical line in the gfxhat given the desired X pixel
# Input: x (int) > pixel of the gfxhat to make the vertical line
# Output: none
def drawVerticalLine(x):
    from gfxhat import lcd, backlight
    from time import sleep
    from rios0021Library import clearBacklight
    # Clear the lcd
    lcd.clear()
    lcd.show()
    # Clear backlight
    clearBacklight()
    g = 255
    b = 0
    # Draw the line at x
    for y in range(0, 64):
        lcd.set_pixel(x,y,1)
        lcd.show()
        # Additional code to make a color transition while drawing line
        backlight.set_all(0, g, b)
        backlight.show()
        if (b < 248):
            b += 7
        elif(g > 5):
            g -= 10
    # Turn off backlight after 2 seconds
    sleep(2)
    clearBacklight()
    lcd.clear()
    lcd.show()

# Function to print a stair in the gfxhat given the start coordinate, the width and height of each stair
# Input: coordenate (2 int list), width(int), height(int), orientation(char either r or l)
# Output: none
def drawStair(coordenate, width, height, orientation):
    from gfxhat import lcd, backlight
    from time import sleep
    # Clear the lcd
    lcd.clear()
    lcd.show()
    # Convert string coordenates to int
    x = int(coordenate[0])
    y = int(coordenate[1])
    # Set the while to run only if the coordenates are inside of the gfxhat display screen
    while(x >= 0 and x <= 127 and y >= 0 and y <= 63):
        for aux in range(0,int(width)):
            #If the x limit is reached within the for, break to prevent gfxhat error
            if (x < 0 or x > 127):
                x = -1
                y = -1
                break
            else: 
                lcd.set_pixel(x,y,1)
                lcd.show()
                if(orientation == "l"):
                    x -= 1
                else:
                    x += 1
        for aux in range(0, int(height)):
                # If the y limit is reached within the for, break
                if (y < 0):
                    y = -1
                    break
                else:
                    lcd.set_pixel(x,y,1)
                    lcd.show()
                    y -= 1
    # clear screen after 4 seconds
    sleep(4)
    lcd.clear()
    lcd.show()

# Function to color the leds in a rainbow motion
# Input: numberOfLoops (int)
def colorRainbow(numberOfLoops):
    from gfxhat import lcd, backlight
    from time import sleep
    from rios0021Library import clearBacklight
    aux = 0
    r = 255
    g = 0 
    b = 0
    lcd.clear()
    lcd.show()
    backlight.set_all(r, g, b)
    backlight.show()
    while (aux < numberOfLoops):
        if(r == 255 and g < 255 and b == 0):
            g += 5
            backlight.set_all(r, g, b)
            backlight.show()
        elif(r != 0 and g == 255):
            r -= 5
            backlight.set_all(r, g, b)
            backlight.show()
        elif(r == 0 and b < 255 and g == 255):
            b += 5
            backlight.set_all(r, g, b)
            backlight.show()
        elif(g != 0 and b == 255):
            g -= 5
            backlight.set_all(r, g, b)
            backlight.show()
        elif(g == 0 and r < 255 and b == 255):
            r += 5
            backlight.set_all(r, g, b)
            backlight.show()
        else:
            b -= 5
            backlight.set_all(r, g, b)
            backlight.show()
            if (b == 0):
                aux += 1
    # Turn off backlight after 2 seconds
    sleep(2)
    clearBacklight()

# Function to display random pixels in gfxhat screen for the amount of seconds required
# Input: seconds(int)
# Output: none
def drawRandomPixels(seconds):
    from random import randint
    from gfxhat import lcd, backlight
    from time import sleep
    from rios0021Library import clearBacklight
    # Clear the lcd
    lcd.clear()
    lcd.show()
    # Clear backlight
    clearBacklight()
    time = 0.0
    # Show a nice blue color
    backlight.set_all(0, 255, 255)
    backlight.show()
    # Loop determined by the number of seconds to draw random pixels every .2 seconds
    while(int(time) != int(seconds)):
        x = randint(0,127)
        y = randint(0,63)
        lcd.set_pixel(x,y,1)
        lcd.show()
        sleep(0.2)
        time += 0.2
    # Show green as signal the pixel drawing has finished
    backlight.set_all(0, 255, 0)
    backlight.show()
    sleep(0.5)
    backlight.set_all(0, 255, 255)
    backlight.show()
    # Clear the lcd and backlight after 4 seconds
    sleep(4)
    lcd.clear()
    lcd.show()
    clearBacklight()

# Function to clear the screen of the gxfhat
def clearScreen():
    from gfxhat import lcd
    lcd.clear()
    lcd.show()

# Function to show a random color on each of the Leds of the gfx hat
def randomLedColor():
    from gfxhat import backlight
    from random import randint
    for x in range(6):
        backlight.set_pixel(x ,randint(0,255),randint(0,255),randint(0,255))
    backlight.show()

# Function to display text in the gfx hat at given coordinates
def displayText(text,x,y):
    from gfxhat import lcd,  fonts, backlight
    from PIL import Image, ImageFont, ImageDraw
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.BitbuntuFull , 10)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 

# Function to Draw a pixel to the right of the given gfxhat coordenates, and return the new x coordenate
def drawPixelRight(x,y):
    from gfxhat import lcd
    x += 1
    if (x > 127):
        x = 0
    lcd.set_pixel(x,y,1)
    lcd.show()
    return x

# Function to Draw a pixel to the left of the given gfxhat coordenates, and return the new x coordenate
def drawPixelLeft(x,y):
    from gfxhat import lcd
    x -= 1
    if (x < 0):
        x = 127
    lcd.set_pixel(x,y,1)
    lcd.show()
    return x

# Function to Draw a pixel up of the given gfxhat coordenates, and return the new y coordenate
def drawPixelUp(x,y):
    from gfxhat import lcd
    y -= 1
    if (y < 0):
        y = 63
    lcd.set_pixel(x,y,1)
    lcd.show()
    return y

# Function to Draw a pixel down of the given gfxhat coordenates, and return the new y coordenate
def drawPixelDown(x,y):
    from gfxhat import lcd
    y += 1
    if (y > 63):
        y = 0
    lcd.set_pixel(x,y,1)
    lcd.show()
    return y

# Etch a sketch function,use arrows to draw in the gfxhat exit pressing 'q'
def etchSketch():
    import click
    from gfxhat import lcd, backlight
    from random import randint
    import os
    print("Etch a Sketch running, use arrow keys to draw, 's' to restart or 'q' to exit...")
    exit = False
    x = 64
    y = 32
    clearScreen()
    displayText("Etch a Sketch", 40, 54)
    while(exit != True):
        keyPressed = click.getchar()
        if(keyPressed == '\x1b[A'):
            y = drawPixelUp(x,y)
            randomLedColor()
        elif(keyPressed == '\x1b[B'):
            y = drawPixelDown(x,y)
            randomLedColor()
        elif(keyPressed == '\x1b[C'):
            x = drawPixelRight(x,y)
            randomLedColor()
        elif(keyPressed == '\x1b[D'):
            x = drawPixelLeft(x,y)
            randomLedColor()
        elif(keyPressed == 'q' or keyPressed == 'Q'):
            exit = True
            clearScreen()
            clearBacklight()
        elif(keyPressed == 's' or keyPressed == 'S'):
            clearScreen()
            displayText("Etch a Sketch", 40, 54)
        os.system("cls||clear")
        print("Etch a Sketch running, use arrow keys to draw, 's' to restart or 'q' to exit...")

# Function that displays an object represented as a tuple or a list on the gfxhat at position x,y
# Input: obj(tuple/list), x(int), y(int)
# Output: none
def displayObject(obj,x,y):
    from gfxhat import lcd
    navX = x
    navY = y
    for aux in obj:
        for aux2 in aux:
            if(aux2 == 1 or aux2 == '1'):
                lcd.set_pixel(navX,navY,1)
            navX += 1
            if(navX > 127):
                navX = 0
        navY += 1
        if(navY > 63):
            navY = 0
        navX = x
    lcd.show()

# Function that erases an object represented as a tuple or a list on the gfxhat at position x,y
# Input: obj(tuple/list), x(int), y(int)
# Output: none
def eraseObject(obj,x,y):
    from gfxhat import lcd
    startX = x
    for aux in obj:
        for aux2 in aux:
            if(aux2 == 1):
                lcd.set_pixel(x,y,0)
            x += 1
            if(x > 127):
                x = 0
        y += 1
        if(y > 63):
            y = 0
        x = startX
    lcd.show()



# Function that moves (erases and redraws) an object given the object, current position
# and velicity for each axis, returns the new position for the object
# Input: obj(tuple/list), x(int), y(int), vx(int), vy(int)
# Output:(x,y)list (the new position for the object)
def moveObject(obj, x, y, vx, vy):
    eraseObject(obj,x,y)
    x += vx
    y += vy
    displayObject(obj, x, y)
    return (x,y)

def checkCollision(obj, x, y, vx, vy):
    aux1 = x+(len(obj[0]))
    aux2 = y+(len(obj))
    collide = False
    if (vx > 0):
        if ((aux1 + vx) > 127):
            vx = vx * -1
    if (vx < 0):
        if ((x + vx) < 0):
            vx = vx * -1
    if (vy > 0):
        if ((aux2 + vy) > 63):
            vy = vy * -1
    if (vy < 0):
        if ((y + vy) < 0):
            vy = vy * -1
    return vx,vy

# Function to translate any given coordinates(int) to a real pixel inside the gfxhat
# Input: x(int), y(int)
def convertCoordToDisplay(x,y):
    # Translate any given coordenate to a real gfxhat pixel (validation for any user input)
    while(x < 0 or y < 0 or x > 127 or y > 63):
        if(x < 0):
            x = 128+x
        if(y < 0):
            y = 64+y
        if(x > 127):
            x = x-128
        if(y > 63):
            y = y-63
    return x,y