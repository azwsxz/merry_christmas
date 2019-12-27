from threading import Thread
from turtle import *
from random import randint
from playsound import playsound

def music():
    playsound("LastChristmas.mp3")


music = Thread(target=music)
music.start()

colores = ["Cyan", "Dodger Blue", "Yellow", "Green Yellow", "Deep Pink", "Dark Orchid", "Medium Slate Blue",
           "Deep Sky Blue", "Dark Turquoise", "Spring Green", "Gold", "Orange Red", "Red", "Yellow", "Orange"]

code = ["HND-656", "BLK-417", "MIAA-059", "PRED-170", "GENM-013", "MIAA-085", "YMDD-156", "WANZ-850", "MEYD-493",
        "GENM-015", "FCH-035", "EKDV-586", "CJOD-182", "CJOD-193", "MIAA-041", "MIAA-037", "PRED-193", "IPX-219",
        "SSNI-369", "SSNI-348", "SSNI-326", "SSNI-081", "SSNI-178", "AVOID-301", "SSNI392", "SSNI-305", "SSNI-014",
        "SSNI-413", "SSNI-946", "SSNI-970", "OFJE-181", "OFJE-112", "OAE-122"]

tree = Turtle()
tree.speed(10)
tree.shape("triangle")
# tree.screen.bgcolor("black")
tree.screen.bgpic("noel1.gif")
tree.screen.title("Merry Christmas")
tree.color("Yellow")
tree.pensize(3)


# -------Star-------
def star():
    for i in range(5):
        # tree.color("Yellow")
        tree.forward(60)
        tree.right(144)


tree.penup()
tree.goto(-30, 325.5)
tree.pendown()
star()  # ve ngoi sao
# --------La Cay-----------
tree.color("Lime Green")  # ve cay
tree.penup()
tree.goto(0, 300)
tree.pendown()

x = 10
y = 270
for i in range(14):
    tree.goto(-x, y)
    tree.goto(x, y)
    x = x + 20
    y = y - 30

# ------Than Cay -------
tree.color("Saddle Brown")
tree.penup()
tree.goto(0, -140)
tree.pendown()
tree.pensize(10)
tree.goto(0, -230)

# ----- Text ----------
rand_code = randint(0, 33)
while True:
    tree.penup()
    tree.goto(0, -320)  # Khoang cach chu voi than duoi
    a = randint(0, 14)
    tree.color(colores[a])
    tree.write("Chúc giáng sinh vui vẻ!", True, "center", font=("Comic Sans MS", 35))
    tree.write(code[rand_code], True)
    tree.hideturtle()

done()
