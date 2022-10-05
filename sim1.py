from classes import *
import pgzrun
import random
import math
import csv
cells = []
GREEN = "#42f45f"
RED = "#f44141"
WIDTH = 800
HEIGHT = 600
time = 0
class Cell:
    def __init__(self, color):
        self.pos = Point(random.uniform(7, 793), random.uniform(7, 593))
        self.vel = Vector(random.uniform(-2, 2), random.uniform(-2, 2))
        self.size = 7
        self.color = color

    def move_cell(self, cells): #we need to add the other cells as an argument so we can see if they collide. 
        self.pos.move(self.vel)
        if self.pos.x >= WIDTH - 7:
            self.pos.x = WIDTH - 7
            self.vel.h *= -1
        if self.pos.x <= 7:
            self.pos.x = 7
            self.vel.h *= -1
        if self.pos.y >= HEIGHT - 7:
            self.pos.y = HEIGHT - 7
            self.vel.v *= -1
        if self.pos.y <= 7:
            self.pos.y = 7
            self.vel.v *= -1        
        for cell in cells:
            distance = self.pos.distance(cell.pos)
            if distance <= 2*self.size:
                if self.color == GREEN and cell.color == RED:
                    self.color = RED

    def draw_cell(self):
        screen.draw.filled_circle((self.pos.x,self.pos.y),self.size,self.color)
def count_time():
    global time
    time += 1
for i in range(50):
    if i == 40:
        cell = Cell(RED)
        cells.append(cell)
    else:
        cell = Cell(GREEN)
        cells.append(cell)
def draw():
    screen.clear()
    for cell in cells:
        cell.draw_cell()

def update():
    global time
    count = 0
    for cell in cells:
        index = cells.index(cell)
        cells.remove(cell)
        pass_cells = cells
        cell.move_cell(pass_cells)
        cells.insert(index, cell)
        if cell.color == RED:
            count += 1
    if count == len(cells):
        f = open("sim1Data.txt", "a")
        csvwriter = csv.writer(f)
        dataline = [time]
        csvwriter.writerow(dataline)
        clock.unschedule(count_time)
        time = 0
        clock.schedule_interval(count_time, 1.0)
        count = 0
        cells.clear()
        for i in range(50):
            if i == 40:
                cell = Cell(RED)
                cells.append(cell)
            else:
                cell = Cell(GREEN)
                cells.append(cell)
pgzrun.go()
