import pygame
import random

pygame.font.init()

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BG_IMG = pygame.image.load("assets/background.png")
BG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

PLAYER_SHIP = pygame.image.load("assets/player_ship.png")
PLAYER_LASER = pygame.image.load("assets/player_laser.png")

ENEMY_RED = pygame.image.load("assets/enemy_red.png")
ENEMY_BLUE = pygame.image.load("assets/enemy_blue.png")
ENEMY_GREEN = pygame.image.load("assets/enemy_green.png")

LASER_RED = pygame.image.load("assets/laser_red.png")
LASER_BLUE = pygame.image.load("assets/laser_red.png")
LASER_GREEN = pygame.image.load("assets/laser_red.png")

TITLE_FONT = pygame.font.SysFont("comicsans", 128)
MAIN_FONT = pygame.font.SysFont("comicsans", 64)

ENEMY_COLOUR_MAP = {
        # List of possible Enemy and Laser colour combinations.
        "red": (ENEMY_RED, LASER_RED),
        "blue": (ENEMY_BLUE, LASER_BLUE),
        "green": (ENEMY_GREEN, LASER_GREEN)
    }

COOLDOWN = 30
FPS = 60

class Ship:
    def __init__(self, x, y, health=100):
        """ Create a new Ship object. """
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cooldown = 0

    def draw(self, window):
        """ Draw this Ship object on the screen. """
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        """ Move all Laser objects for this Ship object. """
        self.cooldown_counter()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown_counter(self):
        """ Update cooldown variable to prevent Laser spamming. """
        if self.cooldown >= COOLDOWN:
            self.cooldown = 0
        elif self.cooldown > 0:
            self.cooldown += 1

    def shoot(self):
        """ Create a new Laser object and add this Ship's Lasers. """
        if self.cooldown == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cooldown = 1

    def get_width(self):
        """ Return width of Ship image. """
        return self.ship_img.get_width()

    def get_height(self):
        """ Return height of Ship image. """
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        """ Create a new Player(Ship) object. """
        super().__init__(x, y, health)
        self.ship_img = PLAYER_SHIP
        self.laser_img = PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.score = 0

    def move_lasers(self, vel, objs):
        self.cooldown_counter()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.score += 10
                        print("Score:", self.score)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, int(self.ship_img.get_width() * (self.health/self.max_health)), 10))

class Enemy(Ship):
    def __init__(self, x, y, colour, health=100):
        """ Create a new Enemy(Ship) object. """
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = ENEMY_COLOUR_MAP[colour]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        """ Move this Enemy object further down the screen. """
        self.y += vel

class Laser:
    def __init__(self, x, y, img):
        """ Create a new Laser object. """
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        """ Draw this Laser object onto the screen."""
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        """ Move this Laser object further down the screen. """
        self.y += vel

    def off_screen(self, height):
        """ Return true if this Laser object has moved off the screen. """
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        """ Return true if this Laser has collided with another object. """
        return collide(self, obj)

def collide(obj1, obj2):
    """ Return True if obj1 has collided with obj2. """
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def play_game():
    run = True
    lives = 5

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 5

    player = Player(350, 450)
    player_name = "treetops"

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WINDOW.blit(BG, (0,0))
        lives_label = MAIN_FONT.render(f"Lives: {lives}", 1, (255,255,255))
        score_label = MAIN_FONT.render(f"Score: {player.score}", 1, (255,255,255))
        player_name_label = MAIN_FONT.render(f"Player: {player_name}", 1, (255,255,255))

        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(player_name_label, (WIDTH - player_name_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WINDOW)

        player.draw(WINDOW)

        if lost:
            lost_label = TITLE_FONT.render("YOU LOSE!", 1, (255,255,255))
            lost_x = int(WIDTH/2 - lost_label.get_width()/2)
            lost_y = int(HEIGHT/2 - lost_label.get_height()/2)
            WINDOW.blit(lost_label, (lost_x, lost_y))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice([
                  "blue",
                  "green",
                ]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Quit game on window close.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Player ship movement.
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if player.x - player_vel > 0:
                player.x -= player_vel
        if keys[pygame.K_RIGHT]:
            if player.x + player_vel + player.get_width() < WIDTH:
                player.x += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        # Enemy ship movement.
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

def main():
    run = True
    title = TITLE_FONT.render("SPACE INVADERS", 1, (255,255,255))
    title_x = int(WIDTH/2 - title.get_width()/2)
    title_y = int(HEIGHT/2 - title.get_height()/2)
    while run:
        # Render the background and title card.
        WINDOW.blit(BG, (0,0))
        WINDOW.blit(title, (title_x, title_y))
        pygame.display.update()

        # Start the game if the user clicks on the screen.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # The user clicked. Start playing the game!
                play_game()

    pygame.quit()

if __name__ == "__main__":
    main()
