
from tkinter import *
#Python 3 calls it tkinter not Tkinter.
import pygame


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class TextPrint:
    def __init__(self):
##        self.reset()
##        self.font = pygame.font.Font(None, 20)
        self.root = Tk()
        self.Text = Text(self.root,height=640,width=480)
        self.Text.pack()
##        self.Text.insert(END,"aloha")

    def print(self,textString):
##        textBitmap = self.font.render(textString, True, BLACK)
##        screen.blit(textBitmap, [self.x, self.y])
##        self.y += self.line_height
        #print(textString)
        self.Text.insert(END,textString)
        
    def reset(self):
##        self.x = 10
##        self.y = 10
##        self.line_height = 15
        self.Text.delete(1.0, END)
             
##    def indent(self):
##        self.x += 10
##        self.Text.insert(END,"indent")
             
##    def unindent(self):
##        self.x -= 10
##        self.Text.insert(END,"unindent")
     
##pygame.init()

# Set the width and height of the screen [width,height]
##size = [640, 480]
##screen = pygame.display.set_mode(size)

#pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
##clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
##    for event in pygame.event.get(): # User did something
##        if event.type == pygame.QUIT: # If user clicked close
##            done=True # Flag that we are done so we exit this loop
##        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
##        if event.type == pygame.JOYBUTTONDOWN:
##            print("Joystick button pressed.")
##        if event.type == pygame.JOYBUTTONUP:
##            print("Joystick button released.")
##        if event.type == pygame.JOYAXISMOTION:
##            print("AXISMOTION")
##        if event.type == pygame.JOYBALLMOTION:
##            print("BALLMOTION")
##        if event.type == pygame.JOYHATMOTION:
##            print("HATMOTION")
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
##    screen.fill(WHITE)
    #textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print("Number of joysticks: {}".format(joystick_count) )
##    textPrint.indent()
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textPrint.print("Joystick {}".format(i) )
##        textPrint.indent()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print("Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print("Number of axes: {}".format(axes) )
##        textPrint.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textPrint.print("Axis {} value: {:>6.3f}".format(i, axis) )
##        textPrint.unindent()
            
        buttons = joystick.get_numbuttons()
        textPrint.print("Number of buttons: {}".format(buttons) )
##        textPrint.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
