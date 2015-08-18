from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,100):
  move(i)
  turn(93)
  color(colors[i%3])

  
from tealight.art import(line,
                         spot,
                         circle,
                         box,
                         rectangle)

