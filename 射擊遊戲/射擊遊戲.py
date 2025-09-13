import tkinter as tk
import random
game = True
a = tk.Tk()
a.geometry("1366x768")
a.title("射擊遊戲")
fly = tk.PhotoImage(file="飛機.png")
fy = tk.Label(a,image=fly)
x = 400
y = 400
kx = random.randint(-200,1000)
ky = random.randint(-200,-50)
ex = 0
ey = 0
fy.place(x=x,y=y)
agg_png = tk.PhotoImage(file="子彈.png")
agg = tk.Label(a,image=agg_png)
agg.place(x=0,y=0)
agg.place_forget()
def up(event):
    global x,y
    y -= 15
    fy.place(x=x,y=y)
def dm(event):
    global x,y
    y += 15
    fy.place(x=x,y=y)
def re(event):
    global x,y
    x += 15
    fy.place(x=x,y=y)
def le(event):
    global x,y
    x -= 15
    fy.place(x=x,y=y)
pu = 0
def fier(event):
    global ex,ey,agg_png,game,pu
    agg.imge = agg_png
    pu =0
    ex = x
    ey = y
    agg.place(x=ex,y=ey)
    def chwai():
        global ex,ey,game,kx,ky,pu
        pu +=1
        ggx =random.randint(-40,40)
        ggy =random.randint(-40,40)
        if ex > kx + ggx:
            ex -= 20
        else:
            ex += 20
        if ey > ky+ggy:
            ey -= 20
        else:
            ey += 20
        agg.place(x=ex,y=ey)
        if abs(kx -ex) < 20 and abs(ky - ey) < 20:
            kx = random.randint(-200,1000)
            ky = random.randint(-200,-50)
            agg.place_forget()
        elif pu == 17:
            agg.place_forget()
            ex = x
            ey = y
        else:
            print(pu)
            a.after(50,chwai)
    chwai()
a.bind("<w>",up)
a.bind("<s>",dm)
a.bind("<a>",le)
a.bind("<d>",re)
a.bind("<space>",fier)
def debug():
    print(f"x={x},y={y}")
    print(f"kx={kx},ky={ky}")
    print(f"game={game}")
dg = tk.Button(text="debug",command=debug)
dg.place(x=400,y=0)
kung_png = tk.PhotoImage(file="敵機.png")
kung = tk.Label(a,image=kung_png)
kung.place(x=kx,y=ky)
def kun():
    global kx,ky,game,agg_png
    kung.place(x=kx,y=ky)
    gg  = random.randint(0,10)
    if gg == 1:
        p = 21
    if gg == 2 or gg == 3:
        p = 17
    else:
        p = 13
    if kx > x:
        kx -= p + round(p/2)
    else:
        kx += p + round(p/2)
    if ky > y:
        ky -= p + round(p/2)
    else:
        ky += p + round(p/2)
    if abs(kx - x) < 50 and abs(ky - y) < 50:
        print("死亡條件已啟動")
        tk.Label(text="game over",font=("",55)).pack()
        game = False
    if game:
        a.after(50,kun)
    else:
        pass
kun()
a.mainloop()