import pygame
pygame.init() 

# створення головного вікна
window = pygame.display.set_mode((1000, 720))

get_point = pygame.mixer.Sound("take_apple.mp3") 
lose = pygame.mixer.Sound("take_apple.mp3")


background_image = pygame.image.load("field.png")  # Замість 'background.jfif' вкажіть шлях до вашого зображення фону
background_image = pygame.transform.scale(background_image, (1000, 720)) # задання розмірів фонового зображення

font = pygame.font.Font(None, 100)  # Створення шрифту для відображення тексту
text = font.render("You WIN!", True, "yellow")  # Створення тексту рахунку
text1 = font.render("You Lose", True, "red") 
text_rect = text.get_rect(center=(window.get_width() // 2, window.get_height() // 2))

def update_score_text(score):
        return font.render(f"Score: {score}", True, "white")

score =  0
score_text = update_score_text(score)

class Wall():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)


wall44 = Wall(800, 480, 200, 20)
wall45 = Wall(600, 500, 20, 200)
wall46 = Wall(0, 480, 200, 20)
wall47 = Wall(800, 480, 200, 20)
game_won = False
walls = [
    Wall(200, 100, 20, 200),
    Wall(400, 420, 20, 200),
    Wall(600, 300, 20, 200),
    Wall(600, 200, 20, 200),
    Wall(200,  0,  20, 200),
    Wall(200, 200, 20, 200),
    Wall(200, 300, 20, 200),
    Wall(400, 520, 20, 200),
    Wall(400, 320, 20, 200),
    Wall(400, 220, 20, 200),
    Wall(600, 100, 20, 200),
    Wall(600,  0,  20, 200),
    Wall(600, 480, 200, 20),
    Wall(600, 630, 20, 200),
    Wall(600, 630, 200, 20),
    Wall(700, 630, 200, 20),
    Wall(800, 630, 200, 20)
]  

walls.append(wall44)
walls.append(wall45)
bullets = []
bullet = []
wall_color = (0,0,0)

class Bullet():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 12, 12)

    def move(self):
        self.rect.x -= 5

class Player(): # клас для створення шаблону персонажа
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect() # "межі" персонажа
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота
        self.direction = "right"
    def update_score_text(score):
        return font.render(f"Score: {score}", True, "white")
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        bullets.append(bullet)
    def move(self):
        keys = pygame.key.get_pressed() # зберігаємо всі можливі натиснуті клавіші в список keys
        if keys[pygame.K_LEFT]: # якщо натиснута клавіша "стрілка ліворуч"
            self.rect.x -= 10  # змінюємо координати гравця по x на -2
        if keys[pygame.K_UP]: # якщо натиснута клавіша "стрілка вверх"
            self.rect.y -= 10 # змінюємо координати гравця по y на -2
        if keys[pygame.K_RIGHT]: # якщо натиснута клавіша "стрілка праворуч"
            self.rect.x += 10 # змінюємо координати гравця по x на +2
        if keys[pygame.K_DOWN]: # якщо натиснута клавіша "стрілка вниз
            self.rect.y += 10 # змінюємо координати гравця по y на +2 
    
    def ryh(self):
        if self.rect.x > 510:
            self.direction = 'left'
        elif self.rect.x < 220:
            self.direction = 'right'
        
        
        if self.direction == 'right':
            self.rect.x += 6
        else:
            self.rect.x -= 6

    def display_score():
        score_text = font.render("Score: " + str(score), True, "red")
        window.blit(score_text, (10, 10))     

    score_text = update_score_text(score)
# створення персонажа
# player - назва об'єкту персонажа (може бути змінена)
#              ( x    y  width height     'png')  
player = Player(100, 100, 75, 75, "snake.png")

Apple1 = Player(250, 175, 50, 50, 'apple.png')  
Apple2 = Player(400, 130, 50, 50, 'apple.png')  
Apple3 = Player(500, 500, 50, 50, 'apple.png')       
Apple4 = Player(700, 535, 50, 50, "apple.png")
Apple5 = Player(290, 421, 50, 50, "apple.png")
Apple6 = Player(480, 300, 50, 50, "apple.png")
Apple7 = Player(100, 300, 50, 50, "apple.png")
Apple8 = Player(100, 500, 50, 50, "apple.png")
Apple9 = Player(290, 645, 50, 50, "apple.png")
Apple10 = Player(145, 645 ,50, 50, "apple.png")
Apple11 = Player(-200, 100, 50, 50, "apple.png")
Apple12 = Player(-100, 600, 50, 50, "apple.png")
Apple13 = Player(-200, 535, 50, 50, "apple.png")


Trophy = Player(700, 200, 200, 180, 'trophy.png')
Trophy2 = Player(-200, 0, 200, 180, "trophy.png")
Trophy3 = Player(-200, 200, 200, 180, "trophy.png")
#створення ворогів   
Enemy = Player(210, 275, 95, 90, "bomb.png")
Enemy2 = Player(345, 575, 95 , 90, "octopus.png")
Enemy3 = Player(-590, 90, 95 , 90, "octopus.png")

# кольори
white = (255, 255, 255)
black = (0, 0, 0)
# Завантаження музики
pygame.mixer.music.load('funny.mp3')
# Відтворення музики 
pygame.mixer.music.play()

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# подія "постріл" кожних 2 секунди
SHOOT_EVENT = pygame.USEREVENT = 0
pygame.time.set_timer(SHOOT_EVENT, 1100) # 2000 - кількість секунд (2 сек)

# змінні для відслідковування левелів


# головний цикл гри
game = True
while game:
    
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    # виклик функції пострілу
        if event.type == SHOOT_EVENT:
            Enemy2.shoot()
            Enemy3.shoot()



    window.blit(background_image,(0, 0))
    
    for wall in walls:
        pygame.draw.rect(window, wall_color, wall.rect)
    
    for wall in walls:
        if player.rect.colliderect(wall.rect):
            # якщо відбулася зіткнення, перешкоджаємо руху персонажа
            if player.rect.left < wall.rect.right and player.rect.right > wall.rect.left:
                if player.rect.top < wall.rect.bottom and player.rect.bottom > wall.rect.top:
                    if player.rect.right > wall.rect.left and player.rect.left < wall.rect.left:
                        player.rect.right = wall.rect.left
                    elif player.rect.left < wall.rect.right and player.rect.right > wall.rect.right:
                        player.rect.left = wall.rect.right
                    elif player.rect.bottom > wall.rect.top and player.rect.top < wall.rect.top:
                        player.rect.bottom = wall.rect.top
                    elif player.rect.top < wall.rect.bottom and player.rect.bottom > wall.rect.bottom:
                        player.rect.top = wall.rect.bottom

    # відображення персонажа на екрані
    window.blit(player.image, (player.rect.x, player.rect.y))
    
    window.blit(Trophy.image, (Trophy.rect.x, Trophy.rect.y))
    window.blit(Trophy.image, (Trophy2.rect.x, Trophy2.rect.y))
    window.blit(Trophy3.image, (Trophy3.rect.x, Trophy3.rect.y))

    window.blit(Apple1.image, (Apple1.rect.x, Apple1.rect.y))
    window.blit(Apple2.image, (Apple2.rect.x, Apple2.rect.y))
    window.blit(Apple3.image, (Apple3.rect.x, Apple3.rect.y))
    window.blit(Apple4.image, (Apple4.rect.x, Apple4.rect.y))
    window.blit(Apple5.image, (Apple5.rect.x, Apple5.rect.y))
    window.blit(Apple6.image, (Apple6.rect.x, Apple6.rect.y))
    window.blit(Apple7.image, (Apple7.rect.x, Apple7.rect.y))
    window.blit(Apple8.image, (Apple8.rect.x, Apple8.rect.y))
    window.blit(Apple9.image, (Apple9.rect.x, Apple9.rect.y))
    window.blit(Apple10.image, (Apple10.rect.x, Apple10.rect.y))
    window.blit(Apple11.image, (Apple11.rect.x, Apple11.rect.y))
    window.blit(Apple12.image, (Apple12.rect.x, Apple12.rect.y))
    window.blit(Apple13.image, (Apple13.rect.x, Apple13.rect.y))

    window.blit(Enemy.image, (Enemy.rect.x, Enemy.rect.y))
    window.blit(Enemy2.image, (Enemy2.rect.x, Enemy2.rect.y))
    window.blit(Enemy3.image, (Enemy3.rect.x, Enemy3.rect.y))

    if player.rect.colliderect(Apple1.rect):
        Apple1.rect.x = -200 
        score += 1  
        score_text = update_score_text(score)
        get_point.play()
    if player.rect.colliderect(Apple2.rect):
        Apple2.rect.x = -200
        score += 1
        score_text = update_score_text(score)
        get_point.play()
    if player.rect.colliderect(Apple3.rect):
        Apple3.rect.x = -200
        score += 1
        score_text = update_score_text(score)
        get_point.play()
    if player.rect.colliderect(Apple5.rect):
        Apple5.rect.x = -200
        score += 1
        score_text = update_score_text(score)
        get_point.play()
    if player.rect.colliderect(Apple6.rect):
        Apple6.rect.x = -200
        score += 1
        score_text = update_score_text(score)
        get_point.play()
    if player.rect.colliderect(Apple7.rect):
        Apple7.rect.x = -200
        score += 1
        score_text = update_score_text(score)
        get_point.play()
    if player.rect.colliderect(Apple8.rect):
        Apple8.rect.x = -200
        score += 1
        score_text = update_score_text(score)
        get_point.play()
    
    if player.rect.colliderect(Apple4.rect):
        wall44.rect.x = -200
        Apple4.rect.x = -200 
        score += 1
        score_text = update_score_text(score)
        get_point.play()
    if player.rect.colliderect(Apple9.rect):
        Apple9.rect.x = -200
        score += 1
        score_text = update_score_text(score)
        wall45.rect.x = -200
        get_point.play()
    if player.rect.colliderect(Apple10.rect):
        Apple10.rect.x = -200
        score += 1
        score_text = update_score_text(score)
        get_point.play()
    if player.rect.colliderect(Apple11.rect):
        Apple11.rect.x = -200
        score += 1
        score_text = update_score_text(score)
        Apple12.rect.x = 100
        get_point.play()
    if player.rect.colliderect(Apple12.rect):
        Apple12.rect.x = -200
        wall46.rect.x = -200     
        score += 1
        score_text = update_score_text(score)
        get_point.play()
    if player.rect.colliderect(Apple13.rect):
        Apple13.rect.x = - 200
        wall47.rect.x = -200
        score += 1
        score_text = update_score_text(score)

    if game_won is True:  
        window.blit(text, text_rect)
    
    if player.rect.colliderect(Trophy.rect):
        Trophy.rect.x = -200
        Trophy2.rect.x = 5
        Trophy2.rect.y = 205
        Enemy2.rect.x = 590
        Enemy2.rect.y = 90
        Enemy3.rect.x = -200
        Apple11.rect.x = 375
        Apple11.rect.y = 45
        walls.append(wall46)
    if player.rect.colliderect(Trophy2.rect):
        Trophy2.rect.x = -200
        Trophy3.rect.x = 700
        Enemy2.rect.x = 345
        Enemy2.rect.y = 525
        Enemy3.rect.x = 590
        Enemy3.rect.y = 90
        Apple13.rect.x = 650
        walls.append(wall47)
    if player.rect.colliderect(Trophy3.rect):
        Trophy3.rect.x = -200
        Enemy.rect.x = -20000
        Enemy2.rect.x = -200
        Enemy3.rect.x = -200
        score += 89
        game_won = True


    if Enemy.rect.colliderect(player.rect):
        player.rect.x = -200
        window.blit(text1, text_rect)
        pygame.mixer.music.stop()      
        player.rect.x = -200
        player.rect.y = -200
        Enemy.rect.x = -2000000
        Enemy2.rect.x = -200
        Enemy3.rect.x = -200
        game = False
        

    window.blit(score_text, (650, 80))

    # виклик функції руху до обраного персонажа
    player.move()

    Enemy.ryh()
    # задання частоти кадрів та оновлення екрану
    
    # У головному циклі гри, після оновлення позиції гравця:if

    # Перевірка, чи вийшов гравець за межі екрану
    if player.rect.left < 0:  # Перевірка лівої межі екрану
        player.rect.left = 0  # Зупинка руху гравця вліво
    elif player.rect.right > 1000:  # Перевірка правої межі екрану
        player.rect.right = 1000  # Зупинка руху гравця вправо
    if player.rect.top < 0:  # Перевірка верхньої межі екрану
        player.rect.top = 0  # Зупинка руху гравця вверх
    elif player.rect.bottom > 720:  # Перевірка нижньої межі екрану
        player.rect.bottom = 720  # Зупинка руху гравця вниз


    for bullet in bullets:
        bullet.move()
        pygame.draw.rect(window, (255, 10, 50), bullet.rect)
        if bullet.rect.colliderect(player.rect):   
            game = False
            bullet.remove(bullet)
     
    
    clock.tick(30)  
    pygame.display.update()

# Зупинка відтворення музики при завершенні програми


pygame.mixer.music.stop()
pygame.quit()
