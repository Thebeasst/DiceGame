import time
import random
from graphics import *
from Button import *
def roll():
    num = random.randint(1,100)
    return num

def rwin(r):
    if r >= 60:
        return True
    
def rlose(r):
    if r < 60:
        return True

def error(i,w):
    i.draw(w)
    time.sleep(0.2)
    i.setFill("red")
    time.sleep(0.2)
    i.setFill("white")
    time.sleep(0.2)
    i.setFill("red")
    time.sleep(0.2)
    i.setFill("white")
    time.sleep(0.2)
    i.setFill("red")
    time.sleep(0.2)
    i.setFill("white")
    time.sleep(0.2)
    i.setFill("red")
    time.sleep(0.2)
    i.setFill("white")
    time.sleep(0.2)
    i.undraw()
    



def main():
    Balance = 500
    ro = roll()
    win = GraphWin("Dice", 400, 400)
    win.setCoords(0,0,400,400)
    win.setBackground(color_rgb(69,69,69))
    #dice
    dicenum = Text(Point(200,200),str(ro))
    dicenum.setSize(30)
    dicenum.setFill("white")
    dicenum.setStyle("bold")

    e = Text(Point(200,100),"INSUFICIENT FUNDS!!!!")
    e.setStyle("bold")
    e.setSize(20)
    e.setFill("white")
    #placeBet
    Bet = Entry(Point(200,165),8)
    
    
    #Roll
    r = Button(win,Point(200,250),150,50,"Roll")
    r.activate()
    r.setColor("white")
    r.changeLabelColor("black")
    r.changeLabelStyle("bold")
    r.changeLabelSize(20)
    #Upper Title
    
    TitleBox = Rectangle(Point(0,330),Point(450,400))
    TitleBox.setFill(color_rgb(34,139,34))
    
    #Balance
    
    Bal = Text(Point(85,15),("Balance: " + str(Balance)))
    Bal.setSize(25)
    Bal.setFill("white")

    
    
    #Title
    
    Title = Text(Point(200,365),"Dice Game")
    Title.setFill("white")
    Title.setStyle("bold")
    Title.setSize(25)
    
    #Draw
    
    TitleBox.draw(win)
    Bal.draw(win)
    Title.draw(win)
    dicenum.draw(win)
    Bet.draw(win)
    q = Button(win,Point(375,375),25,25,"Quit")
    q.activate()
    q.setColor("red")
    p = win.getMouse()
    while 1 == 1:
        if q.clicked(p):
            win.close()
        if r.clicked(p):
            intbet = int(Bet.getText())
            if intbet < Balance + 1:
                Pot = intbet * 2.0
                Balance = Balance - intbet
                print Pot
                ro = roll()
                if rwin(ro) == True:
                    print "win"
                    Balance = Balance + Pot
                elif rlose(ro) == True:
                    print "lose"
                dicenum.setText(str(ro))
                Bal.setText("Balance: " + str(Balance))
            else:
                print "You dont have enough for that bet!!"
                error(e,win)
        p = win.getMouse()
    win.close()

main()
