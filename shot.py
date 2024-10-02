from circleshape import *
from constants import SHOT_RADIUS
#shot is a circleShape object cos we need to use the collision detection in the class
#shot would need to i

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen,
                           radius = self.radius,
                           center = self.position,
                           width = 2,
                           color = "white"
                              )

    def update(self, dt):
        self.position += (self.velocity * dt)