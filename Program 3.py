"""
Design Prolog 

Karthik Nayak

Date: 6th Oct 2015

Purpose:  to play the Chuck-A-Luck game with a user, letting

            them bet on the outcome of 3 dice rolls

           Play continues until the user quits or until they lose all their money

Pre-conditions:  amount to bet, number to bet on, yes/no to continue

Post-conditions:  displays rolls as dice, reports on win/loss, asks play again?

"""
from graphics import *
from random import *

"""
********************************************

getbet

Purpose:  get the amount of the bet from the user

     while not letting the user bet less than 1 dollar and not more

      than they have in the pot

Pre-conditions:  (int) the amount of the pot and the graphics window

Post-conditions:  (int) the validated user's input (from 1 to amount of pot)
"""

def get_bet(pot,win):
    
    #prompt the user for an amount
    txt1 = Text(Point(250, 100), "What do you want to bet?(1-"+str(pot)+")")
    txt1.setSize(20)
    txt1.draw(win)
    
    #get user's input
    entry = Entry(Point(250, 135), 20)  
    entry.setFill("white") 
    entry.setText("1")
    entry.draw(win)
    
    win.getMouse()
    bet = int(entry.getText())     
    
    #validate the user's input
    while(bet not in range(1,pot+1)):
        
        if bet > pot:
            txt2 = Text(Point(250, 180),"bet amount too high, re-enter")
            txt2.setSize(10)
            txt2.draw(win)           
        
        else:
            txt2 = Text(Point(250, 180),"bet amount too low, re-enter")
            txt2.setSize(10)
            txt2.draw(win)
        
        #get user's input
        win.getMouse()
        txt2.undraw()
        bet = int(entry.getText())  
    
    #clean up any objects drawn   
    txt1.undraw()
    entry.undraw()
    
    #return validated user's input
    return bet    

"""
********************************************

getnumber

Purpose:

    get the die number the user wants to bet on (1-6)

Pre-conditions:  graphics window

Post-conditions:   validated user's input (1-6)
"""

def get_number(win):
    
    #prompt the user for a number
    txt1 = Text(Point(250, 100),"Enter a die number to bet on(1-6)")
    txt1.setSize(20)
    txt1.draw(win)  
    
    entry = Entry(Point(250, 130), 20)  
    entry.setFill("white") 
    entry.draw(win)    
    
    win.getMouse()
    number = entry.getText()
    
    #validate the user's input 
    while(number < "1" or number > "6" or len(number) > 1):
        txt2 = Text(Point(250, 200),"That's not a valid bet!")
        txt2.setSize(20)
        txt2.draw(win)    
        
        #get user's input
        win.getMouse()
        txt2.undraw()
        number = entry.getText()   
    
    #convert user's input to an integer
    number = int(entry.getText())
    
    #clean up any objects drawn
    txt1.undraw()
    entry.undraw()
    
    #return validated user's input
    return number 



"""
********************************************
draw_dice

Purpose:

   draw a dice image on the screen at the location given, using

     the corresponding gif file

Pre-conditions:  (int) x and y of location, (int) number of the die, 

     (GraphWin) graphics window

Post-condition:  (Image) returns the Image object created
"""

def draw_die(die_pt,roll,win):
    
    #create filename string using number of the die and ".gif"
    filename = str(roll) + ".gif"
    
    #create the image object with the point and the correct die gif
    dieimage = Image(die_pt,filename)
    
    #draw image
    dieimage.draw(win)
    
    #return image
    return dieimage



"""
********************************************

check_matches 

Purpose:  compare the user's roll to the three rolls 

     and find out if there are 0, 1, 2, or 3 matches

Pre-conditions:  three rolls and user's roll

Post-conditions:  0-3, number of matches
"""

def check_matches(roll1,roll2,roll3,user_roll):
    
    #initialize counter to zero
    counter = 0 
    
    if roll1 == user_roll:
        counter += 1
    if roll2 == user_roll:
        counter += 1 
    if roll3 == user_roll:
        counter += 1 
    
    #return counter
    return counter


"""
********************************************
in_box 

Purpose:  

    to test a point to see if it is in a box defined by

     two other points (upper right and lower left) 

Pre-conditions:  two points that define the box, a third point

Post-conditions:  True if point3 is inside the box,

    False if not
"""

def in_Box(left_pt,right_pt,user_click):
    x = user_click.getX()
    y = user_click.getY()     
    x1 = left_pt.getX()
    y1 = left_pt.getY()
    x2 = right_pt.getX()
    y2 = right_pt.getY()   
    if(y2> y >y1 and x2> x >x1):
        return True
    else: 
        return False

"""
********************************************

playagain

Purpose:  

   ask the user if they want to play again, get their

    Yes or No response, validated by ignoring any clicks

    anywhere on the screen except in the Yes and No boxes

Pre-conditions:   the graphics window

Post-conditions:  a bool value, True means the user chose Yes,

    False otherwise
"""

def play_again(win):
    #display a prompt "do you want to play another game?"
    prompt = Text(Point(250, 180), "Do you want to play another game?")
    prompt.setSize(20)
    prompt.draw(win)    
    
    #draw two boxes and label one Yes and one No
    b1_left_pt = Point(100,350)
    b1_right_pt = Point(200,450)
    yes_box = Rectangle(Point(100,350),Point(200,450))
    yes_box.draw(win)
    
    yes = Text(Point(150, 400), "YES")
    yes.setSize(20)
    yes.draw(win)    
    
    b2_left_pt = Point(300,350)
    b2_right_pt = Point(400,450)    
    no_box = Rectangle(Point(300,350),Point(400,450))
    no_box.draw(win)    
    
    no = Text(Point(350, 400), "NO")
    no.setSize(20)
    no.draw(win)    
    
    #get a user's click
    user_click = win.getMouse()
    
    #while the user does not click in one of the boxes
    while(not(in_Box(b1_left_pt,b1_right_pt,user_click) or in_Box(b2_left_pt,b2_right_pt,user_click))):
        
        #tell them that is not a valid response
        invalid = Text(Point(250, 250), "Invalid response!")
        invalid.setSize(20)
        invalid.draw(win)        
        user_click = win.getMouse() 
        invalid.undraw()
    
    #clean up objects drawn
    prompt.undraw()
    yes_box.undraw()
    yes.undraw()
    no_box.undraw()
    no.undraw() 
    
    #return True if the user chose the Yes box, False otherwise 
    if in_Box(b1_left_pt,b1_right_pt,user_click):       
        return True
    else:            
        return False 

def main():
    
    #initialize playagain flag 
    playagain = True
    
    #set initial pot amount
    pot = 100
    
    #Creating the main window
    win = GraphWin("Entry", 500, 600)
    
    #display title    
    msg = Text(Point(250, 50), "Chuck-A-Luck")
    msg.setSize(25)
    msg.setFill('green')
    msg.draw(win)
    
    while(playagain == True and pot > 0):
        
        #get the user's bet amount ($
        bet = get_bet(pot,win)
        
        #get the number the user wants to bet on (1-6
        user_roll = get_number(win)
        
        #get three random numbers for the three rolls 
        roll1 = randrange(1,7)
        roll2 = randrange(1,7)
        roll3 = randrange(1,7)
        
        die_pt1 = Point(100,450)
        die_pt2 = Point(250,450)
        die_pt3 = Point(400,450)
        
        #draw the corresponding dice using draw_dice
        img1 = draw_die(die_pt1,roll1, win)
        img2 = draw_die(die_pt2,roll2, win)
        img3 = draw_die(die_pt3,roll3, win)
        
        #find out the number of matches using check_matches
        matches = check_matches(roll1,roll2,roll3,user_roll)
        
        win_amt = 0    
        if matches == 0:
            pot -= bet
        elif matches == 1:
            win_amt = bet
            pot += win_amt
        elif matches == 2:
            win_amt = bet*5
            pot += win_amt
        else:
            win_amt = bet*10
            pot += win_amt
        
        #report the result and the amount of the pot
        report = Text(Point(250, 200),"Number of matches: "+str(matches)+", you win: $"+str(win_amt))
        report.setSize(20)
        report.draw(win)
        
        amount = Text(Point(250, 250),"You have: $"+str(pot))
        amount.setSize(20)
        amount.draw(win)        
        
        #wait for click
        win.getMouse()
        
        report.undraw()
        amount.undraw() 
        img1.undraw()
        img2.undraw()
        img3.undraw()
        
        #if the pot isn't zero,
        if pot != 0:
            #ask the user if they want to play again
            playagain = play_again(win)
    
    #show the final results of the game
    if pot > 0:
        result = Text(Point(250, 240),"You are leaving with $"+str(pot))
        result.setSize(20)
        result.draw(win) 
    else:
        result = Text(Point(250, 240),"Sorry you lost!")
        result.setSize(20)
        result.draw(win)        
    
    #wait for click
    win.getMouse()
    
    #shut down window and program
    win.close()
    
main()             