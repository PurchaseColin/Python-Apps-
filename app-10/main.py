import pygame 
import random 
import time 
pygame.init()

WIDTH, HEIGHT = 650,650

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Confetti !!!')

FPS = 60 

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
RANDOM1 =  (88,0,44)
RANDOM2 =  (99,44,76)
RANDOM3 =  (56,27,84)
RANDOM4 =  (0,58,99)
RANDOM5 =  (254,96,177)
RANDOM6 =  (200,6,99)
RANDOM7 =  (50,74,9)
RANDOM8 =  (80,60,89)
RANDOM9 =  (0,50,60)
RANDOM10 =  (50,0,60)
COLORS = [RED, GREEN, BLUE, WHITE,RANDOM1,RANDOM2,RANDOM3,RANDOM4,RANDOM5,RANDOM6,RANDOM7,RANDOM8,RANDOM9,RANDOM10 ]





class Square: 
 def __init__ (self, x, y, width, height, y_vel, color, x_vel ): 
  self.x = self.original_x = x
  self.y = y 
  self.width = width 
  self.height = height 
  self.y_vel = y_vel
  self.color = color
  self.x_vel = x_vel 

 def draw(self, win): 
  pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


 def move(self):
  self.y = self.y + self.y_vel 
  self.x += self.x_vel 


class Circle: 
 def __init__ (self, x, y, radius, y_vel, color, x_vel): 
  self.x = self.original_x = x 
  self.y = y 
  self.radius = radius 
  self.color = color
  self.y_vel = y_vel 
  self.x_vel = x_vel 

 def draw(self, win): 
  pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

 def move(self): 
  self.y += self.y_vel 
  self.x += self.x_vel 



class Triangle: 
 def __init__ (self, x,y, y_vel, color, x_vel): 
  self.x = self.original_x = x 
  self.y = y 
  self.color = color 
  self.y_vel = y_vel 
  self.x_vel = x_vel 
 
 def draw(self, win):
  pygame.draw.polygon(win, self.color, ((self.x,self.y), (self.x-8,self.y+8), (self.x+8, self.y+8))) 

 def move(self): 
  self.y += self.y_vel 
  self.x += self.x_vel 



def draw(win, squares, circles, triangles):
 win.fill(BLACK)
 
 
 # putting in my square 
 for square in squares:
  if square.y < HEIGHT:  
   square.draw(win)
  else: 
   square.y = 0

   
 for circle in circles: 
  if circle.y < HEIGHT: 
    circle.draw(win)
  else:
    circle.y = 0 

 for triangle in triangles: 
  if triangle.y < HEIGHT: 
   triangle.draw(win)
  else: 
   triangle.y = 0 



 pygame.display.update()



def main(): 
 run = True 
 clock = pygame.time.Clock()
 squares = []
 for idx in range(15): 
    squares.append(Square(random.randint(0,650) ,0,10,10,random.randint(2,10), random.choice(COLORS), random.randint(-2,2)))

 circles = []
 for idx in range(15): 
  circles.append(Circle(random.randint(0,650),0, 5, random.randint(2,10), random.choice(COLORS), random.randint(-2,2)))


 triangles = []
 for idx in range(15): 
  triangles.append(Triangle(random.randint(0,650), 0, random.randint(2,10), random.choice(COLORS),random.randint(-2,2)))


 while run: 
  clock.tick(FPS)
  now = time.time()

  for event in pygame.event.get():
   if event.type == pygame.QUIT: 
    run = False 
 
  
  for square in squares: 
   square.move()

  for circle in circles: 
   circle.move()

  for triangle in triangles: 
   triangle.move()

  
  draw(WIN, squares, circles, triangles )
 
 quit()


if __name__ == '__main__': 
 main()