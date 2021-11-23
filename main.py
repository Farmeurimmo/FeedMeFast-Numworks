from random import randrange
import kandinsky
from ion import *
from time import *

kandinsky.fill_rect(0,0,50,50,color=(50,50,50))

x = 30
y = 30
mx = 50
my = 50
fx = 0
fy = 0
s = 10
nnn = True
max = 5000
removenum = 6
size = 3
g1 = []
g2 = []
score = 0
sleeptime = 0
startsleep = 0.002
rangeofi = 20
tttt = True

def spawnPlayer():
    kandinsky.fill_rect(x - 6, y - 6, size * 12
              , size * 12,
              kandinsky.color(0
                    , 153, 204))
    kandinsky.fill_rect(x, y, size * 8
              , size * 8, kandinsky.color(80, 45, 50))


def spawnFood(x, y):
    sleep(0.03)
    kandinsky.fill_rect(x, y, size * 6
              , size * 6, kandinsky.color(255, 255, 0))


def clearFood(x, y):
    kandinsky.fill_rect(x - 20, y - 20, size * 25
              , size * 25,
              kandinsky.color(0
                    , 153, 204))


def Randnumn():
    g1.clear()
    g2.clear()
    mx = randrange(3, 30) * 10
    my = randrange(1, 20) * 10
    spawnFood(mx, my)
    nnn = True
    d = 0
    for i in range(rangeofi):
        g1.append(mx - d)
        d += 1
    d = 0
    for i in range(rangeofi):
        g1.append(mx + d)
        d += 1
    d = 0
    for i in range(rangeofi):
        g2.append(my - d)
        d += 1
    d = 0
    for i in range(rangeofi):
        g2.append(my + d)
        d += 1
    d = 0
    kandinsky.fill_rect(mx, my, size * 3
              , size * 3, kandinsky.color(255, 255, 0))


kandinsky.fill_rect(0, 0, 320, 222, kandinsky.color(255, 255, 255))
kandinsky.fill_rect(20, 100, 280, 10, kandinsky.color(0, 0, 0))
kandinsky.draw_string("Feed Me Fast", 110, 0)
kandinsky.draw_string("Made by Robin Massonnat", 40, 30)
for i in range(280):
    kandinsky.fill_rect(20, 100, i, 10, kandinsky.color(90, 180, 68))
    kandinsky.fill_rect(0, 0, 10, 100, kandinsky.color(255, 255, 255))
    sleep(startsleep)
    if i == 0:
        kandinsky.draw_string("Chargement en cours", 50, 120)
    if i == 30:
        kandinsky.draw_string("Chargement en cours.", 50, 120)
    if i == 60:
        kandinsky.draw_string("Chargement en cours..", 50, 120)
    if i == 90:
        kandinsky.draw_string("Chargement en cours...", 50, 120)
    if i == 130:
        kandinsky.draw_string("Lancement en cours    ", 50, 120)
    if i == 170:
        kandinsky.draw_string("Lancement en cours.    ", 50, 120)
    if i == 210:
        kandinsky.draw_string("Lancement en cours..     ", 50, 120)
    if i == 250:
        kandinsky.draw_string("Lancement en cours...     ", 50, 120)

kandinsky.fill_rect(0, 0, 322, 222, kandinsky.color(0
                                , 153, 204))
spawnPlayer()
Randnumn()
tttt = True
ox = 0
oy = 0

while tttt == True:
    s = s + 1
    ox = x
    oy = y
    if keydown(KEY_UP):
        if y - removenum >= 0:
            y = y - removenum
    if ox != x and oy != y or ox != x or oy != y:
        spawnPlayer()
    ox = x
    oy = y
    if keydown(KEY_DOWN):
        if y + removenum >= 0:
            if y + removenum <= 208:
                y = y + removenum
    if ox != x and oy != y or ox != x or oy != y:
        spawnPlayer()
    ox = x
    oy = y
    if keydown(KEY_LEFT):
        if x - removenum >= 0:
            x = x - removenum
    if ox != x and oy != y or ox != x or oy != y:
        spawnPlayer()
    ox = x
    oy = y
    if keydown(KEY_RIGHT):
        if x + removenum >= 0:
            if x + removenum <= 304:
                 x = x + removenum
    if ox != x and oy != y or ox != x or oy != y:
        spawnPlayer()
    ox = x
    oy = y

    kandinsky.draw_string(str(score),
                0, 0)
    kandinsky.draw_string("   X      ", 220, 0)
    kandinsky.draw_string(str(max), 280, 0)
    kandinsky.draw_string(str(s), 200, 0)
    if x in g1 and y in g2:
        if nnn == True:
            fx = x
            fy = y
            clearFood(fx, fy)
            spawnPlayer()
            if s <= 150:
                max += 50
                score += 10
            else:
                score += 5
                max -= 75
            s = 10
            Randnumn()
            nnn = True

    if s >= max:
        break

kandinsky.display(True)