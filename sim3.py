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
    def __init__(self, color, vax_status, social_distance):
        self.pos = Point(random.uniform(7, 793), random.uniform(7, 593))
        self.vel = Vector(random.uniform(-2, 2), random.uniform(-2, 2))
        self.size = 7
        self.color = color
        self.num_cells_infected = 0
        self.vaccinated = vax_status
        self.social_distance = social_distance

    def move_cell(self, cells):  
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
            contact_distance = random.uniform(0, 14)#the number of pixels away from the cell it can infect others
            if distance <= 28 and self.social_distance == True:
                self.vel = self.pos.makeVectorTo(cell.pos)
                self.vel.multiply(-1)
                self.vel.normalize()
            if self.vaccinated == True:
                if distance <= (2*self.size) and cell.num_cells_infected < 7:
                    if self.color == GREEN and cell.color == RED:
                        self.color = RED
                        cell.num_cells_infected += 1
            else:
                if  distance <= (2*self.size) + contact_distance and cell.num_cells_infected < 7 and self.color == GREEN and cell.color == RED:
                        self.color = RED
                        cell.num_cells_infected += 1
#make 3 parts
#"social distancing" of trying to stay 28 pixels away from other cells
#only max infections at 7 cells per cell(R0)
#80% of cells are vaccinated meaning lower contact distance
    def draw_cell(self):
        screen.draw.filled_circle((self.pos.x,self.pos.y),self.size,self.color)
def count_time():
    global time
    time += 1
for i in range(50):
    cell = Cell(GREEN, True, True)
    cells.append(cell)
    
for cell in random.sample(cells, 10):
    cell.vaccinated = False
for cell in random.sample(cells, 1):
    cell.color = RED
for cell in random.sample(cells, 25):
    cell.social_distance = False
clock.schedule_interval(count_time, 1.0)
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
        f = open("sim3Data.txt", "a")
        csvwriter = csv.writer(f)
        dataline = [time]
        csvwriter.writerow(dataline)
        clock.unschedule(count_time)
        time = 0
        clock.schedule_interval(count_time, 1.0)
        count = 0
        cells.clear()

        for i in range(50):
            cell = Cell(GREEN, True, True)
            cells.append(cell)
            
        for cell in random.sample(cells, 10):
            cell.vaccinated = False
        for cell in random.sample(cells, 1):
            cell.color = RED
        for cell in random.sample(cells, 25):
            cell.social_distance = False
pgzrun.go()
