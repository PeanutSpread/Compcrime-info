# Importing pygame and rando while initializing music and graphics.
import pygame
import random
pygame.mixer.init()
pygame.init()

# A class for allowing images to be animated with ease from sprite sheets.
class anim(object):

    # Getting the information required for the entire class.
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name)

    # Making part of the original sprite sheet its own message.
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]) 
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0,0,0))

        # Returning the image.
        return image
    
# Setting up the game window.
SIZE = (800,600)
screen = pygame.display.set_mode(SIZE)
myClock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# Defining the constants of colours.
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BACKER = (0,0,100)
RAND = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# Loading the images.
Box = pygame.image.load('Menu_Button1.png')
Box_Pressed = pygame.image.load('Menu_Button2.png')
Quit = pygame.image.load('Power_Button1.png')
Quit_Pressed = pygame.image.load('Power_Button2.png')
Back = pygame.image.load('Back_Button1.png')
Back_Pressed = pygame.image.load('Back_Button2.png')

# Loading the music.
pygame.mixer.music.load('Puzzle Plank Galaxy 8 Bit.mp3')

# Getting all the fonts and text set up
fontMenu = pygame.font.SysFont("Times New Roman",50)
fontexplain = pygame.font.SysFont("Base",32)
text = fontMenu.render("Computer Science Information",1,(0,255,0))
text2 = fontMenu.render("Computer Virus",1,(0,0,0))
text3 = fontMenu.render("Computer Virus",1,(255,255,255))
text4 = fontMenu.render("Computer Crime",1,(0,0,0))
text5 = fontMenu.render("Computer Crime",1,(255,255,255))
virus = fontexplain.render("Computer viruses are lines of code that are designed to harm",1,(0,0,0)) 
virus2 = fontexplain.render("your computer by destroying files, damaging programs or",1,(0,0,0))
virus3 = fontexplain.render("reformatting the hard drive. Most viruses restrict your acess to",1,(0,0,0))
virus4 = fontexplain.render("the internet and slow down your computer by taking up memory",1,(0,0,0))
virus5 = fontexplain.render("causing frequent crashes. Viruses often spread through",1,(0,0,0))
virus6 = fontexplain.render("networks, emails and by piggybacking on the back of programs.",1,(0,0,0))
virus7 = fontexplain.render("Viruses can be avoided by updating your operating system,",1,(0,0,0))
virus8 = fontexplain.render("increase browser security settings, download antivirus",1,(0,0,0))
virus9 = fontexplain.render("software and do not open spam emails and delete them",1,(0,0,0))
virus10 = fontexplain.render("right away.",1,(0,0,0))

crime = fontexplain.render("Computer crimes, also known as cyber crimes, are crimes",1,(0,0,0)) 
crime2 = fontexplain.render("committed on the computer or on the internet with more of an ",1,(0,0,0))
crime3 = fontexplain.render("impact on the outside world. Crimes include the shut down of ",1,(0,0,0))
crime4 = fontexplain.render("websites, robberies, identity theft and stalking people online.",1,(0,0,0))
crime5 = fontexplain.render("Ways to avoid these crimes from affecting you include being",1,(0,0,0))
crime6 = fontexplain.render("aware of the websites you acces, limiting what information you",1,(0,0,0))
crime7 = fontexplain.render("post online. Don't go on shady websites or connect to servers",1,(0,0,0))
crime8 = fontexplain.render("and networks that you determine to be unsafe or illegal. A less",1,(0,0,0))
crime9 = fontexplain.render("intense cyber crime is committed when illegaly downloading",1,(0,0,0))
crime10 = fontexplain.render("movies/games.",1,(0,0,0))

# Variables used for the placement of multiple moving objects
a = 0 # y variable for chip backgroud
b = 0 # y variable for chip backgroud
c = 536 # y variable for lines of code
f = 400 # x variable for the little jumping guy
g = 508 # y variable for the little jumping guy
z = 0 # Used for animation by cycling through frames
x = 0 # mouse x loc
y = 0 # mouse y loc
state = 0 # Determining which menu you're in
but = True # game loop
jump = False # jumping variable for the little jumping guy
jump_check = False # making sure that the little jumping guy can fall
time = 0 # making a timer for smooth animation

# Loading the individual frames of each image.
cursor = anim('Pointer.png')
Background = anim('comp_chip.png')
code = anim('comp_code.png')
Guy = anim('Astro-Skull.png')
Back_me_up = Background.get_image(0,0,1600,1200)
listen = [cursor.get_image(0,0,16,16),cursor.get_image(16,0,16,16),cursor.get_image(32,0,16,16),cursor.get_image(48,0,16,16),cursor.get_image(64,0,16,16),cursor.get_image(80,0,16,16)]
listen2 = [code.get_image(0,0,32,64),code.get_image(64,0,32,64),code.get_image(128,0,32,64),code.get_image(192,0,32,64),code.get_image(256,0,32,64),code.get_image(320,0,32,64)]
listen3 = [pygame.transform.scale(Guy.get_image(0,0,152,184),(76,92)),pygame.transform.scale(Guy.get_image(152,0,152,184),(76,92)),pygame.transform.scale(Guy.get_image(304,0,152,184),(76,92)),pygame.transform.scale(Guy.get_image(456,0,152,184),(76,92)),pygame.transform.scale(Guy.get_image(608,0,152,184),(76,92)),pygame.transform.scale(Guy.get_image(760,0,152,184),(76,92)),pygame.transform.scale(Guy.get_image(912,0,152,184),(76,92)),pygame.transform.scale(Guy.get_image(1064,0,152,184),(76,92))]

# Setting up the music to play.
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# Main game loop.
while but == True:
    
################################################################################
    
    # Main Menu
    if state == 0:
        
        # Background thats animated
        pygame.draw.rect(screen,RAND,(0,0,800,600))
        screen.blit(Back_me_up,(b,a))
        pygame.draw.rect(screen,BACKER,(85,110,625,50))
        screen.blit(text,(85,100)) 
        
        # Swapping button images based off mouse location
        if x <= 750 and x >=50 and y <= 450 and y >= 350:
            screen.blit(Box_Pressed,(50,350))
            screen.blit(text5,(220,365))
        else:
            screen.blit(Box,(50,350))
            screen.blit(text4,(220,365))
            
        if x <= 750 and x >=50 and y <= 300 and y >= 200:
            screen.blit(Box_Pressed,(50,200))
            screen.blit(text3,(225,215))
        else:
            screen.blit(Box,(50,200))
            screen.blit(text2,(225,215))
            
        if x <= 800 and x >=750 and y <= 50 and y >= 0:
            screen.blit(Quit_Pressed,(750,0))       
        else:
            screen.blit(Quit,(750,0))


################################################################################
   
    # Virus information
    if state == 1:
        
        # Background and code border.
        pygame.draw.rect(screen,RAND,(0,0,800,600))
        screen.blit(listen2[z],(20,c))     
        screen.blit(listen2[z],(750,c))
        screen.blit(listen2[z],(20,c - 64))
        screen.blit(listen2[z],(750,c - 64))
        screen.blit(listen2[z],(20,c + 64))
        screen.blit(listen2[z],(750,c + 64))
        pygame.draw.rect(screen,GREEN,(50,20,700,440))
        
        # Text about viruses.
        screen.blit(text2,(50,20))
        screen.blit(virus,(50,110))
        screen.blit(virus2,(50,146))
        screen.blit(virus3,(50,182))
        screen.blit(virus4,(50,217))
        screen.blit(virus5,(50,254))
        screen.blit(virus6,(50,290))
        screen.blit(virus7,(50,326))        
        screen.blit(virus8,(50,362))
        screen.blit(virus9,(50,398))
        screen.blit(virus10,(50,434))
        
        # Swapping button images based off mouse location.
        if x <= 800 and x >=750 and y <= 50 and y >= 0:
            screen.blit(Back_Pressed,(750,0))          
        else:
            screen.blit(Back,(750,0))
            
################################################################################    
    
    # Computer crime information
    if state == 2:
       
        # Background and code border.        
        pygame.draw.rect(screen,RAND,(0,0,800,600))
        screen.blit(listen2[z],(20,c))  
        screen.blit(listen2[z],(750,c))
        screen.blit(listen2[z],(20,c - 64))
        screen.blit(listen2[z],(750,c - 64))
        screen.blit(listen2[z],(20,c + 64))
        screen.blit(listen2[z],(750,c + 64))        
        pygame.draw.rect(screen,YELLOW,(50,20,700,440))
        
        # Text about computer crimes.        
        screen.blit(text4,(50,20))
        screen.blit(crime,(50,110))
        screen.blit(crime2,(50,146))
        screen.blit(crime3,(50,182))
        screen.blit(crime4,(50,218))
        screen.blit(crime5,(50,254))
        screen.blit(crime6,(50,290))
        screen.blit(crime7,(50,326))        
        screen.blit(crime8,(50,362))
        screen.blit(crime9,(50,398))
        screen.blit(crime10,(50,434))
        
        # Swapping button images based off mouse location.        
        if x <= 800 and x >=750 and y <= 50 and y >= 0:
            screen.blit(Back_Pressed,(750,0))          
        else:
            screen.blit(Back,(750,0))
            
################################################################################
    
    # The event for getting input.
    woah = pygame.event.get()
    for event in woah:    
        mouse = pygame.mouse.get_pos()
        x = mouse[0]
        y = mouse[1]
    
        # Getting feedback to change the program based off of mouse clicks.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if state == 0:
                if x <= 750 and x >=50 and y <= 300 and y >= 200:
                    state = 1
                if x <= 750 and x >=50 and y <= 450 and y >= 350:
                    state = 2              
                if x <= 800 and x >=750 and y <= 50 and y >= 0:
                    but = False
                    break 
            elif state == 1:
                if x <= 800 and x >=750 and y <= 50 and y >= 0:
                    state = 0
            elif state == 2:
                if x <= 800 and x >=750 and y <= 50 and y >= 0:
                    state = 0
    
    # Timer used for frames of animation.
    time += 1
    
    # every value divisible by 10 is a new frame animation.
    if time % 10 == 0:
        
        # Used for main chip background
        if b <= -600:
            b = 0
            a = 0
        else:
            b -= 1
            a -= int(4/3)
        
        # Used for animation.
        if z == 5:
            z = 0
        else:
            z += 1
        
        # Used for moving the lines of code.
        if c <= 0:
            c = 536
        else:
            c -= 20

    # Used for animating the little jumping guy
    if time % 2 == 0:
        
        # Checking where the guy is compared to the mouse.
        if f + 38 != x:
            if f + 38 > x:
                f -= 1
            elif f + 38 < x:
                f += 1
        
        # Making sure the jump for the guy is smooth
        if jump == True and jump_check == True:
            if g > 462:
                g -= 2
            else:
                jump = False
                jump_check = False
        elif jump == False and g < 508:
            g += 2
            

    # Time to change the background
    if time % 60 == 0:
        RAND = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    # Drawing and moving the jumping little guy
    if f + 38 > x:
        jump = False
        jump_check = True
        screen.blit(pygame.transform.flip(listen3[z],True,False),(f,g))
    elif f + 38 < x:
        jump = False
        jump_check = True
        screen.blit(listen3[z],(f,g))
    elif f + 38 == x:
        if g == 508:
            jump_check = True
        if jump_check == True:
            screen.blit(listen3[3],(f,g))
            jump = True
        if jump_check == False:
            screen.blit(listen3[0],(f,g))
        
    # Drawing the custom animated guy.
    screen.blit(listen[z],(x,y))
    
    # Setting the frame rate to 120.
    myClock.tick(120)
    
    # putting the pictures on screen.
    pygame.display.flip()

# Stoping the music.    
pygame.mixer.quit

# Stopping the Menu
pygame.quit()