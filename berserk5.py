import time
from random import *

from graphics import *

def isClicked(circle, mousePos):
    try:
        distance = (((mousePos.x - circle.getCenter().x) ** 2) + ((mousePos.y - circle.getCenter().y) ** 2))**0.5
        return distance < (circle.radius**2)/circle.radius
    except AttributeError:
        return None

def main():
    win = GraphWin("berserk5", 500, 500)
    win.setBackground(color_rgb(255, 255, 255))
    
    header = Text(Point(250,200), "berserk5")
    header.setFace('courier')
    header.setSize(30)
    header.draw(win)
    
    rect=Rectangle(Point(175, 300), Point(325, 430))
    rect.setOutline(color_rgb(255, 255, 255))
    rect.draw(win)
    
    play=Text(Point(250, 365), "play")
    play.setFace('courier')
    play.setTextColor(color_rgb(255, 255, 255))
    play.draw(win)
    
    for i in range(256):
        x=255-i
        time.sleep(0.001)
        play.setTextColor(color_rgb(x, x, x))
        rect.setOutline(color_rgb(x, x, x))
    
    win.getMouse()
    win.setBackground(color_rgb(30, 30, 30))
    header.undraw()
    rect.undraw()
    play.undraw()
    
    r1=Rectangle(Point(100, 200), Point(250, 300))
    r1.setFill(color_rgb(70, 70, 255))
    r1.setOutline(color_rgb(30, 30, 30))
    r1.draw(win)
    
    norm=Text(Point(175, 250), "normal")
    norm.setFace('courier')
    norm.draw(win)
    
    r2=Rectangle(Point(250, 200), Point(400, 300))
    r2.setFill(color_rgb(255, 70, 70))
    r2.setOutline(color_rgb(30, 30, 30))
    r2.draw(win)
    
    dif=Text(Point(325, 250), "berserk")
    dif.setFace('courier')
    dif.draw(win)
    
    mousePo=win.getMouse()
    win.setBackground(color_rgb(0, 0, 0))
    r1.undraw()
    r2.undraw()
    norm.undraw()
    dif.undraw()
    v=10
    
    if mousePo.x<250:
        r=21
        lvl=1
        
        c=Circle(Point(250, 250), r)
        c.setFill(color_rgb(255, 255, 255))
        c.draw(win)
        
        lvlTxt=Text(Point(100, 50), "Level:"+str(lvl))
        lvlTxt.setFace('courier')
        lvlTxt.setTextColor(color_rgb(255, 255, 255))
        lvlTxt.draw(win)
        
        count=0
        points=Text(Point(400, 50), str(count)+"/"+str(v))
        points.setFace('courier')
        points.setTextColor(color_rgb(255, 255, 255))
        points.draw(win)
        
        e=False
        z=1
        mousePo=win.checkMouse()
        e=isClicked(c, mousePo)
        
        v=10
            
        
        while lvl<=20:
            lvl+=1
            count=0
            start=time.time()
            now=round(time.time()-start)
            tim=Text(Point(250, 50), now)
            tim.setFace('courier')
            tim.setTextColor(color_rgb(255, 255, 255))
            tim.draw(win)
            
            e=False
            while now<10.0:
                e=False
                now=round(time.time()-start)
                tim.undraw()
                
                tim=Text(Point(250, 50), now)
                tim.setFace('courier')
                tim.setTextColor(color_rgb(255, 255, 255))
                tim.draw(win)
                
                cenX=c.getCenter().getX()
                cenY=c.getCenter().getY()
                
                if cenX>=400:
                    x=randint(-3, -1)
                elif cenX<=100:
                    x=randint(1, 3)
                else:
                    x=randint(-3, 3)
                
                if cenY>=400:
                    y=randint(-3, -1)
                elif cenY<=100:
                    y=randint(1, 3)
                else:
                    y=randint(-3, 3)#change me
                
                c.move(x*z, y*z)
                
                mousePo=win.checkMouse()
                e=isClicked(c, mousePo)
                if e:
                    count+=1
                    
                    points.undraw()
    
                    points=Text(Point(400, 50), str(count)+"/"+str(v))
                    points.setFace('courier')
                    points.setTextColor(color_rgb(255, 255, 255))
                    points.draw(win)
                    
                time.sleep(0.1)
            
            if count>=v:
                count=0
                    
                points.undraw()
    
                points=Text(Point(400, 50), str(count)+"/"+str(v))
                points.setFace('courier')
                points.setTextColor(color_rgb(255, 255, 255))
                points.draw(win)
                
                r-=0
                z+=0.5
                
                lvlTxt.undraw()
                
                lvlTxt=Text(Point(100, 50), "Level:"+str(lvl))
                lvlTxt.setFace('courier')
                lvlTxt.setTextColor(color_rgb(255, 255, 255))
                lvlTxt.draw(win)
                
                d=randint(r, 500-r)
                f=randint(r, 500-r)
                c.undraw()
                pt=Point(d, f)
                
                tim.undraw()
                c=Circle(pt, r)
                c.draw(win)
                c.setFill(color_rgb(255, 255, 255))
            else:
                lvlTxt.undraw()
                c.undraw()
                points.undraw()
                tim.undraw()
                
                yL=Text(Point(250, 250), "You lose...")
                yL.setSize(30)
                yL.setFace('courier')
                yL.setTextColor(color_rgb(255, 255, 255))
                yL.draw(win)
                break
    else:
        r=20
        lvl=1
        
        c=Circle(Point(250, 250), r)
        c.setFill(color_rgb(255, 255, 255))
        c.draw(win)
        
        lvlTxt=Text(Point(100, 50), "Level:"+str(lvl))
        lvlTxt.setFace('courier')
        lvlTxt.setTextColor(color_rgb(255, 255, 255))
        lvlTxt.draw(win)
        
        count=0
        points=Text(Point(400, 50), str(count)+"/"+str(v))
        points.setFace('courier')
        points.setTextColor(color_rgb(255, 255, 255))
        points.draw(win)
        
        e=False
        z=1
        mousePo=win.checkMouse()
        e=isClicked(c, mousePo)
        
        v=10
            
        
        while lvl<=20:
            lvl+=1
            count=0
            start=time.time()
            now=round(time.time()-start)
            tim=Text(Point(250, 50), now)
            tim.setFace('courier')
            tim.setTextColor(color_rgb(255, 255, 255))
            tim.draw(win)
            
            e=False
            while now<10.0:
                e=False
                now=round(time.time()-start)
                tim.undraw()
                
                tim=Text(Point(250, 50), now)
                tim.setFace('courier')
                tim.setTextColor(color_rgb(255, 255, 255))
                tim.draw(win)
                
                cenX=c.getCenter().getX()
                cenY=c.getCenter().getY()
                
                if cenX>=400:
                    x=randint(-3, -1)*z
                elif cenX<=100:
                    x=randint(1, 3)*z
                else:
                    x=randint(-3, 3)*z
                
                if cenY>=400:
                    y=randint(-3, -1)*z
                elif cenY<=100:
                    y=randint(1, 3)*z
                else:
                    y=randint(-3, 3)*z
                
                c.move(x, y)
                
                mousePo=win.checkMouse()
                e=isClicked(c, mousePo)
                if e:
                    count+=1
                    
                    points.undraw()
    
                    points=Text(Point(400, 50), str(count)+"/"+str(v))
                    points.setFace('courier')
                    points.setTextColor(color_rgb(255, 255, 255))
                    points.draw(win)
                    
                time.sleep(0.1)
            
            if count>=v:
                count=0
                v+=1
                    
                points.undraw()
    
                points=Text(Point(400, 50), str(count)+"/"+str(v))
                points.setFace('courier')
                points.setTextColor(color_rgb(255, 255, 255))
                points.draw(win)
                
                r-=1
                z+=1
                
                lvlTxt.undraw()
                
                lvlTxt=Text(Point(100, 50), "Level:"+str(lvl))
                lvlTxt.setFace('courier')
                lvlTxt.setTextColor(color_rgb(255, 255, 255))
                lvlTxt.draw(win)
                
                d=randint(r, 500-r)
                f=randint(r, 500-r)
                c.undraw()
                pt=Point(d, f)
                
                tim.undraw()
                c=Circle(pt, r)
                c.draw(win)
                c.setFill(color_rgb(255, 255, 255))
            else:
                lvlTxt.undraw()
                c.undraw()
                points.undraw()
                tim.undraw()
                
                yL=Text(Point(250, 250), "You lose...")
                yL.setSize(30)
                yL.setFace('courier')
                yL.setTextColor(color_rgb(255, 255, 255))
                yL.draw(win)
                break

    if lvl>=20:
        lvlTxt.undraw()
        c.undraw()
        points.undraw()
        tim.undraw()
        
        yW=Text(Point(250, 250), "You Win!")
        yW.setSize(30)
        yW.setFace('courier')
        yW.setTextColor(color_rgb(255, 255, 255))
        yW.draw(win)

    win.getMouse()
    win.close()


main()

    
