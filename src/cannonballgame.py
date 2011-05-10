# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="apurv"
__date__ ="$May 10, 2011 10:24:09 AM$"


from random import *
from tkinter import *
from time import *
from math import *
import string
class Cannonball:
    #Static variables
    no_ofballs=0
    no_ofprojections=0
    u=randint(100,140)
    flag=True
    project=False
    angle=randint(20,80)
    hit=True
    def _init_(self,tk):
        self.tk=tk
    #@staticmethod
    #def Widgets(tk):
     #   frame=Frame(tk)
     #   frame.pack()
     #   button=Button(frame,text="QUIT",fg="black",command=frame.quit)
     #   button.grid(row=400,column=400)
    @staticmethod
    def PerpetualTwinkling(canvas,tk):
        x=randint(-1,1)
        y=randint(-1,1)
        canvas.move("star11",x,y)
        canvas.move("star12",x,y)
        canvas.move("star21",y,x)
        canvas.move("star22",y,x)
        tk.update()
        sleep(.3)
    @staticmethod
    def create_canvas(tk):
        canvas=Canvas(tk,width=1500,height=500,bg="black",bd=15,relief=GROOVE)
        canvas.pack()
        #Objects on the canvas
        def stars():
            for i in range(0,20):
                if i<10:
                    x=randint(20,1500)
                    y=randint(40,250)
                    canvas.create_polygon(x,y,x+5,y+10,x-5,y+10,fill="white",outline="blue",tag="star21")
                    canvas.create_polygon(x-5,y+4,x+5,y+4,x,y+14,fill="white",outline="blue",tag="star22")
                else:
                    x=randint(20,1500)
                    y=randint(40,250)
                    canvas.create_polygon(x,y,x+5,y+10,x-5,y+10,fill="white",outline="blue",tag="star11")
                    canvas.create_polygon(x-5,y+4,x+5,y+4,x,y+14,fill="white",outline="blue",tag="star12")
        stars()
        canvas.create_arc(80,50,160,150,style=ARC,start=125,extent=200,fill="white",outline="white",stipple="gray50",width=2,tag="moon")
        canvas.create_polygon(430,100,435,110,425,110,fill="white",outline="blue",tag="star11")
        canvas.create_polygon(425,104,435,104,430,114,fill="white",outline="blue",tag="star12")
        canvas.create_polygon(830,60,835,70,825,70,fill="white",outline="blue",tag="star21")
        canvas.create_polygon(825,64,835,64,830,74,fill="white",outline="blue",tag="star22")
        canvas.create_rectangle(100,470,140,490,fill="red",outline="pink",width=1,tag="player1")
        canvas.create_rectangle(1240,470,1200,490,fill="blue",outline="lightgreen",width=1,tag="player2")
        canvas.create_line(0,495,1500,495,width=15,stipple="gray75",fill="green",tag="earth")
        canvas.create_polygon(600,300,700,300,900,500,400,500,fill="brown",outline="brown",width=5,tag="mountain1")
        canvas.create_arc(600,280,700,330,style=PIESLICE,start=0,extent=180,fill="brown",outline="brown",width=5,tag="mountaincap")
        canvas.create_text(600,230,fill="pink",text="CANNONBALL tm.",tag="text1")
        canvas.create_text(650,250,fill="green",text="Enter your name and press enter",tag="text2")
        tk.update()
        name="Mojo_Jojo"
        canvas.delete("text1")
        canvas.delete("text2")
        canvas.create_text(900,25,fill="yellow",text=name+"   playing",tag="text3")
        canvas.create_text(500,200,fill="lightgreen",text="Press Tab for controls",tag="text4")
        flag=True
        def blast(x,y):
            canvas.create_oval(x-20,y-20,x+20,y+20,fill="yellow",outline="gold",width=5,tag="blast")
            tk.update()
            sleep(.6)
            canvas.delete("blast")
            tk.update()
        def checkball(x,y):
            if x>1190 and x<1230 and y>470 and y<490:
                canvas.delete("player2")
                Cannonball.flag=False
                canvas.create_text(500,400,fill="cyan",text="YOU WIN")
                canvas.create_text(1000,400,fill="purple",text="Number of shots taken        "+str(Cannonball.no_ofprojections))
                blast(x,y)
                return 1
        def checkball2(x,y):
            if x>100 and x<140 and y>470 and y<490:
                Cannonball.flag=False
                canvas.delete("player1")
                canvas.create_text(500,300,fill="blue",text="You Lose")
                blast(x,y)
                return 1
        def checkball3(x,y,name):
            if y>275 and y<500 and x+y-900>0 and x-y-400<0:
                canvas.delete(name)
                blast(x,y)
                return 1
        def bindings(event):
            if event.keysym=='a' and Cannonball.flag and Cannonball.hit:
                Cannonball.no_ofballs=Cannonball.no_ofballs+1
                Cannonball.no_ofprojections=Cannonball.no_ofprojections+1
                nameball="ball"+str(Cannonball.no_ofballs)
                u=Cannonball.u
                tk.update()
                canvas.create_oval(100,470,105,475,fill="red",outline="gold",width=2,tag=nameball)
                x=105
                usq=u*u
                theta=(3.145/180)*Cannonball.angle
                k=4.9/(usq*cos(theta)*cos(theta))
                yi=475
                y=475
                xi=0
                while x<1400 and y<=475:
                    yaux=(x-105)*tan(theta)-(k*(x-105)*(x-105))
                    y=475-yaux
                    canvas.move(nameball,5,(y-yi))
                    breakpoint1=checkball(x,y)
                    breakpoint2=checkball3(x,y,nameball)
                    if breakpoint1==1 or breakpoint2==1:
                        break
                    tk.update()
                    sleep(.01)
                    xi=x
                    yi=y
                    x=x+5
                canvas.delete(nameball)
                canvas.create_bitmap(50,250,bitmap="hourglass",foreground="purple",tag="wait")
                Cannonball.hit=False
                Cannonball.no_ofballs=Cannonball.no_ofballs-1
            elif event.keysym=='Tab':
                canvas.delete("text4")
                canvas.create_text(400,200,fill="pink",text="Arrow-Up: Increasing projection angle",tag="text5")
                canvas.create_text(400,220,fill="pink",text="Arrow-Down: Decreasing projection angle",tag="text5")
                canvas.create_text(400,240,fill="pink",text="a: Shooting", tag="text5")
                canvas.create_text(400,260,fill="pink",text="Arrow-Left: Decrease projection speed and Arrow-Right: Increase projection speed",tag="text5")
                tk.update()
                sleep(2)
                canvas.delete("text5")
                tk.update()
            elif event.keysym=='Up' and Cannonball.angle<85:
                Cannonball.angle=Cannonball.angle+1
            elif event.keysym=='Down' and Cannonball.angle>10:
                Cannonball.angle=Cannonball.angle-1
            elif event.keysym=='Left' and Cannonball.u>0:
                Cannonball.u=Cannonball.u-5
            elif event.keysym=='Right' and Cannonball.u<130:
                Cannonball.u=Cannonball.u+5
        canvas.bind_all('<KeyPress-a>',bindings)
        canvas.bind_all('<KeyPress-Tab>',bindings)
        canvas.bind_all('<KeyPress-Down>',bindings)
        canvas.bind_all('<KeyPress-Up>',bindings)
        canvas.bind_all('<KeyPress-Left>',bindings)
        canvas.bind_all('<KeyPress-Right>',bindings)
        while(True):
            Cannonball.PerpetualTwinkling(canvas,tk)
            if Cannonball.flag:
                r=randint(0,1000)
                if (r>200 and r<300) or (r>700 and r<750):
                    Cannonball.project=True
                if Cannonball.project and not(Cannonball.hit):
                    canvas.create_oval(1240,470,1245,475,fill="blue",outline="gold",width=2,tag="ball22")
                    a=randint(40,60)
                    x=1245
                    u=110
                    usq=u*u
                    angle=a
                    theta=(3.145/180)*angle
                    k=4.9/(usq*cos(theta)*cos(theta))
                    yi=475
                    y=475
                    xi=0
                    while x>0 and y<=475:
                        yaux=(1245-x)*tan(theta)-(k*(1245-x)*(1245-x))
                        y=475-yaux
                        canvas.move("ball22",-5,(y-yi))
                        breakpoint1=checkball2(x,y)
                        breakpoint2=checkball3(x,y,"ball22")
                        if breakpoint1==1 or breakpoint2==1:
                            break
                        tk.update()
                        sleep(.01)
                        xi=x
                        yi=y
                        x=x-5
                    canvas.delete("ball22")
                    Cannonball.hit=True
                    canvas.delete("wait")
    @staticmethod
    def main():
        tk=Tk()
        Obj_Cannonball=Cannonball()
        Obj_Cannonball._init_(tk)
        Cannonball.create_canvas(Obj_Cannonball.tk)
        #Cannonball.Widgets(Obj_Cannonball.tk)
        Obj_Cannonball.tk.mainloop() #or alternatively tk.mainloop() because class variable self.tk has been pointed to object tk created in main
#Class Ends


if __name__ == "__main__":
    Cannonball.main()
