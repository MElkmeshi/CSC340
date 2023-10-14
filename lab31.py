from __future__ import annotations
import math
class Point:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
    def show(self):
        print(f"x: {self.x},y: {self.y}")
    def move(self,x:int,y:int):
        self.x = x
        self.y = y
    def dist(self,p2:Point):
        return math.sqrt(pow(self.x-p2.x,2)+pow(self.y-p2.y,2))

def main():
    p1 = Point(x=4,y=1)
    p2 = Point(x=7,y=3)
    print(p1.dist(p2=p2))
    p1.move(x=1,y=2)
    p1.show()