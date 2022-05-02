import math, time, sys, pygame

class Triangle:
    def __init__(self,
                 p_0   = [  0,  0,  1],
                 p_1   = [  0,  1,  0],
                 p_2   = [  1,  0,  0],
                 color = [225,  0,255],
                 fill  = True,
                 width = 4):
        self.p0    = p_0
        self.p1    = p_1
        self.p2    = p_2
        self.color = color
        self.fill  = fill
        self.width = width

    # What defines the triangles center of rotation?
    def rotate(self, angle_x, angle_y, angle_z):
        new_points = []
        for point in [self.p0,self.p1,self.p2]:
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
                new_points.append([x, y, z])

        # Where do these new points get written to?
        # Does each triangle need an absolute and temporary
        # point coordinate list?
        return new_points

    def draw(self,surface,offset,distance=3,xfactor=.05,clear=True):

        d = distance
        x = xfactor

        # map 3D points to 2D screen plane with mystery math

        # d is equivalent to distance
        ## When d is zero, possible div0 error. FIX?
        
        # x is a magnification factor?
        ## When x is negative, polygon coordinates are inverted
        
        pA = (self.p0[0]*(1.0/(self.p0[2]+d)+x)*60+offset[0],
              self.p0[1]*(1.0/(self.p0[2]+d)+x)*60+offset[1])
        pB = (self.p1[0]*(1.0/(self.p1[2]+d)+x)*60+offset[0],
              self.p1[1]*(1.0/(self.p1[2]+d)+x)*60+offset[1])
        pC = (self.p2[0]*(1.0/(self.p2[2]+d)+x)*60+offset[0],
              self.p2[1]*(1.0/(self.p2[2]+d)+x)*60+offset[1])

        if self.fill == True:
            pygame.draw.polygon(surface,self.color,[pA,pB,pC])
            
        if self.width > 0:
            pygame.draw.line(surface,(0,0,0),pA,pB,self.width)
            pygame.draw.line(surface,(0,0,0),pB,pC,self.width)
            pygame.draw.line(surface,(0,0,0),pC,pA,self.width)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Triangle Test Program')
    background = pygame.Surface((800,600))
    clock = pygame.time.Clock()
    pygame.draw.rect(background,[127,127,127],[0,0,800,600])
    
    # x: - is left, + is right
    # y: - is up, + is down
    # z: - is closer until points cross view-plane
    
    triA  = Triangle([-1,1,0],[-1,-1,0],[1,1,0],[127,0,0],fill=True)
    triB  = Triangle([1,-1,0],[-1,-1,0],[1,1,0],[0,127,0],fill=True)
    
    tick = 0

    while True:

        tick += 1
        
        screen.blit(background,(0,0))

        d = abs(1000-(tick%2000))/1000
        e = abs(1000-(tick%2000))/1000

        g = 1#abs(300-(tick%600))/50
        h = 1#abs(300-(tick%600))/50
        
        triA.draw(screen, [400,300], d, g)
        triB.draw(screen, [400,300], e, h)
                
        pygame.display.flip()
        clock.tick(120)

if __name__ == "__main__":
    main()
