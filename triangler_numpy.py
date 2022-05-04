import math, time, sys, pygame
import numpy as np

WIDTH = 0
HEIGHT = 0

class Triangle:
    def __init__(self,
                 points   = np.array(((0,0,1),
                                      (0,1,0),
                                      (1,0,0))),
                 color    = [225,  0,255],
                 distance = 5,
                 fill     = True,
                 width    = 4):
        # Absolute coords for three points
        self.abs_pts  = points
        # Temporary coords before draw
        self.tmp_pts  = points
        # Flattened x,y,z --> x,y pairs
        self.flt_pts  = np.array(((0,0),(0,0),(0,)))
        
        self.color    = color
        self.fill     = fill
        self.width    = width
        self.distance = distance

    # What defines the triangles center of rotation?
    def rotate(self, angle_x, angle_y, angle_z):
        
        for point in [self.tp0,self.tp1,self.tp2]:
                x = point[0]
                y = point[1]
                z = point[2]
                new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
                new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
                y = new_y
                # isn't math fun, kids?
                z = new_z
                new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
                new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
                x = new_x
                z = new_z
                new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
                new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
                x = new_x
                y = new_y
                point = [x, y, z]
 
    def translate(self, d_x, d_y, d_z):

        self.tp0[0] = self.p0[0] + d_x
        self.tp0[1] = self.p0[1] + d_y
        self.tp0[2] = self.p0[2] + d_z
        self.tp1[0] = self.p1[0] + d_x
        self.tp1[1] = self.p1[1] + d_y
        self.tp1[2] = self.p1[2] + d_z
        self.tp2[0] = self.p2[0] + d_x
        self.tp2[1] = self.p2[1] + d_y
        self.tp2[2] = self.p2[2] + d_z

    def flatten(self):

        if self.tp0[2] == 0:
            self.tp0[2] += 0.001
        if self.tp1[2] == 0:
            self.tp1[2] += 0.001
        if self.tp2[2] == 0:
            self.tp2[2] += 0.001
        
        self.fp0[0] = int(self.tp0[0]*(1.0/(self.tp0[2]+self.distance))*600)+int(WIDTH/2)
        self.fp0[1] = int(self.tp0[1]*(1.0/(self.tp0[2]+self.distance))*600)+int(HEIGHT/2)
        self.fp1[0] = int(self.tp1[0]*(1.0/(self.tp1[2]+self.distance))*600)+int(WIDTH/2)
        self.fp1[1] = int(self.tp1[1]*(1.0/(self.tp1[2]+self.distance))*600)+int(HEIGHT/2)
        self.fp2[0] = int(self.tp2[0]*(1.0/(self.tp2[2]+self.distance))*600)+int(WIDTH/2)
        self.fp2[1] = int(self.tp2[1]*(1.0/(self.tp2[2]+self.distance))*600)+int(HEIGHT/2)

        print(self.fp0[0],self.fp0[1])

    def draw(self,surface):

        self.translate(0,0,self.distance)
        self.flatten()

        if self.fill == True:
            pygame.draw.polygon(surface,self.color,(self.fp0,self.fp1,self.fp2),0)
            
        if self.width > 0:
            pygame.draw.line(surface,(0,0,0),self.fp0,self.fp1,self.width)
            pygame.draw.line(surface,(0,0,0),self.fp1,self.fp2,self.width)
            pygame.draw.line(surface,(0,0,0),self.fp2,self.fp0,self.width)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Triangle Test Program')
    background = pygame.Surface((800,600))
    global WIDTH
    global HEIGHT

    # This is only redundant for the moment
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()
    
    clock = pygame.time.Clock()
    pygame.draw.rect(background,[127,127,127],[0,0,WIDTH,HEIGHT])
    
    # x: - is left, + is right
    # y: - is up, + is down
    # z: - is closer until points cross view-plane
    
    triA  = Triangle([-1,1,0],[-1,-1,0],[1,1,0],[127,0,0],fill=True)
    triB  = Triangle([1,-1,0],[-1,-1,0],[1,1,0],[0,127,0],fill=True)
    
    tick = 0

    while True:

        tick += 1
        
        screen.blit(background,(0,0))
        
        triA.draw(screen)
        triB.draw(screen)
        triA.translate(tick/100,0,0)
        triB.translate(0,tick/100,0)
                
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
