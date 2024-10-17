import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 
  
  
# set the fillcolor 
t.fillcolor('red') 
  
# start the filling color 
t.begin_fill() 
s = 250
# drawing the triangle of side s 
for _ in range(3): 
  t.forward(s) 
  t.right(-120) 
  
# ending the filling of the color 
t.end_fill() 
turtle.done()