# __author__: Lucky Adogun
# __project__: Arculus Network Pong Test
# __date_submitted__: 09-04-2022
# __VERSION__: v0.0.1


import pygame, sys, random


# initialization
pygame.init()
clock = pygame.time.Clock()

# settings constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480


class Player:
    """
        This version has no implementation to control objection instances.
        The requirement is to create max of 2 players on each side.
        To solve that I proposed 2 players and 2 opponents.

        Find the Opponent() class below

        - `animate()`: interface method that interacts with the screen
    """
    def __init__(self, position=0, speed=0):
        self.position = position
        self.speed = speed
        self.obj = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 - 70,10,140)
    
    def animate(self):
        self.obj.y += self.speed

        if self.obj.top <= 0:
            self.obj.top = 0
        if self.obj.bottom >= SCREEN_HEIGHT:
            self.obj.bottom = SCREEN_HEIGHT


class Opponent:
    """
        The opponent class is slightly similar to the player class
        but currently built to give functionality to the Player class

        - `animate()`: interface method that relates with Ball() object dynamically
        - `_handle_collision()`: internal method that interactives with Balls() and screen
    """
    def __init__(self, position=0, speed=7):
        self.position = position
        self.speed = speed
        self.obj = pygame.Rect(10, SCREEN_HEIGHT/2 - 70, 10, 140)

    def _handle_collision(self):
        if self.obj.top <= 0:
            self.obj.top = 0
        if self.obj.bottom >= SCREEN_HEIGHT:
            self.obj.bottom = SCREEN_HEIGHT

    def animate(self, ball):
        if self.obj.top < ball.y:
            self.obj.top += self.speed
        if self.obj.bottom > ball.y:
            self.obj.bottom -= self.speed

        self._handle_collision()
    

class Ball:
    """
        Interactive object between Player() and Opponent() objects

        - `animate()`: interface method that interacts with Player(), Opponent() and screen randomly
        - `_handle_collision()`: internal method that interactives with Player(), Opponents() and screen
        - `_reset_ball()`: internal method that resets the position of the ball object at the beginiing
                            and end of a game.
    """
    def __init__(self, position=0, speed_x=7, speed_y=7):
        self.position = position
        self.speed_x = speed_x * random.choice((1, -1))
        self.speed_y = speed_y * random.choice((1, -1))
        self.obj = pygame.Rect(SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2 - 15, 30, 30)

    def _reset_ball(self):
        self.obj.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.speed_y *= random.choice((1, -1))
        self.speed_x *= random.choice((1, -1))

    def _handle_collision(self, player, opponent):
        if self.obj.top <= 0 or self.obj.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
        if self.obj.left <= 0 or self.obj.right >= SCREEN_WIDTH:
            self._reset_ball()

        if self.obj.colliderect(player) or self.obj.colliderect(opponent):
            self.speed_x *= -1

    def animate(self, player, opponent):
        self.obj.x += self.speed_x
        self.obj.y += self.speed_y

        self._handle_collision(player, opponent)


class GamingInterface:
    player = Player()
    opponent = Opponent()
    ball = Ball()
    
    title = 'Arculus Pong'
    bg_color = pygame.Color('grey12')
    other_color = pygame.Color(200, 200, 200)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    @staticmethod
    def MOVE_DOWN(event):
        if event.key == pygame.K_DOWN:
            GamingInterface.player.speed += 7
        if event.key == pygame.K_UP:
            GamingInterface.player.speed -= 7

    @staticmethod
    def MOVE_UP(event):
        if event.key == pygame.K_UP:
            GamingInterface.player.speed -= 7
        if event.key == pygame.K_UP:
            GamingInterface.player.speed += 7 

    @classmethod
    def display(cls):
        cls.start_game()

        cls.screen.fill(cls.bg_color)
        pygame.display.set_caption(cls.title)
        pygame.draw.rect(cls.screen, cls.other_color, cls.player.obj)
        pygame.draw.rect(cls.screen, cls.other_color, cls.opponent.obj)
        pygame.draw.ellipse(cls.screen, cls.other_color, cls.ball.obj)
        pygame.draw.aaline(cls.screen, cls.other_color, (SCREEN_WIDTH/2,0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    @classmethod
    def start_game(cls):
        cls.ball.animate(cls.player.obj, cls.opponent.obj)
        cls.player.animate()
        cls.opponent.animate(cls.ball.obj)


if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == 0:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                GamingInterface.MOVE_DOWN(event)

            if event.type == pygame.KEYUP:
                GamingInterface.MOVE_UP(event)
        
        GamingInterface.display()

        # update the window
        pygame.display.flip()
        clock.tick(60)
    









