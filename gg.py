import pygame
import sys
import random
from math import * 
 
pygame.init()

width = 1750
height = 890
 
# Производит фоновое изображение
background_image = pygame.image.load("assets\\images\\gost.jpg")
background_image = pygame.transform.scale(background_image, (width, height))
 
# Производит изображения призрака
ghost_image = pygame.image.load("assets\\images\\Prizrak.jpg")


display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра попади в призрака и пройди игру до конца)")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
 
margin = 100
lowerBound = 100
 
score = 0
 
white = (230, 230, 230)
lightBlue = (4, 27, 96)
red = (231, 76, 60)
lightGreen = (25, 111, 61)
darkGray = (40, 55, 71)
darkBlue = (64, 178, 239)
green = (35, 155, 86)
yellow = (244, 208, 63)
blue = (46, 134, 193)
purple = (155, 89, 182)
orange = (243, 156, 18)
 
font = pygame.font.SysFont("Arial", 25)


# Производит фоновую музыку
pygame.mixer.music.load("assets\\audio\\poyuschie-prizraki.mp3")
pygame.mixer.music.play(-1)
 
# Производит звуковой эффект взрыва призрака
burst_sound = pygame.mixer.Sound("assets\\audio\\effekt-quotprivideniyaquot-28433.mp3")
 
# Шрифт
instruction_font = pygame.font.Font(None, 30)
heading_font = pygame.font.Font(None, 50)   


def instructions():
    pygame.init()
    background_image = pygame.image.load("assets\\images\\Panda.jpg")
    font = pygame.font.Font (None, 36)
    pygame.init()
    fps = 60
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont('Arial', 40)
    instruction_text = [
        "Инструкция:",
        "1. Используйте мышь, чтобы прицелиться и щелкать, чтобы стрелять в призраков.",
        "2. Уничтожьте как можно больше призраков, прежде чем они достигнут вверха небоскреба",
        "3. Избегайте столкновения с платформой или пропуска призраков",
        "4. Нажмите Q чтобы выйти из игры.",
        "5. Нажмите "R", чтобы перезапустить игру.",
        "6. Удачи) Надеюсь тебе удаться поймать призраков и ты сможешь победить!",
        "",
        "Нажмите в любом месте, чтобы начать игру."
     
    ]
    y_offset = 50
    for line in instruction_text:
        text = instruction_font.render(line, True, white)
        text_rect = text.get_rect(center=(width/2, y_offset))
        display.blit(text, text_rect)
        y_offset += 40
 
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def show_prompt():
    text = font.render("Вы хотите продолжить? (Да(Y)/Нет(N))", True, (255, 255, 255))
    display.blit(text, (50, 50))
    pygame.display.flip()
 
class ghost:
    def __init__(self, speed, ghost_image):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed = -speed
        self.proPool= [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.ghost_image = ghost_image
       
    def move(self):
        direct = random.choice(self.proPool)
 
        if direct == -1:
            self.angle += -10
        elif direct == 0:
            self.angle += 0
        else:
            self.angle += 10
 
        self.y += self.speed*sin(radians(self.angle))
        self.x += self.speed*cos(radians(self.angle))
 
        if (self.x + self.a > width) or (self.x < 0):
            if self.y > height/5:
                self.x -= self.speed*cos(radians(self.angle))
            else:
                self.reset()
        if self.y + self.b < 0 or self.y > height + 30:
            self.reset()
           
    def show(self):
        ghost_rect = self.ghost_image.get_rect(center=(self.x + self.a, self.y + self.b))
        display.blit(self.ghost_image, ghost_rect)
           
    def burst(self):
        global score
        pos = pygame.mouse.get_pos()
 
        if isonghost(self.x, self.y, self.a, self.b, pos):
            score += 1
            # Звукового сопровождение
            burst_sound.play()
            self.reset()
               
    def reset(self):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed -= 0.002
        self.proPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
       

 
# Создает призраков в рандомных местах и много
ghosts = []
noghost = 10
for i in range(noghost):
    obj = ghost(random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4]), ghost_image)
    ghosts.append(obj)
 
def isonghost(x, y, a, b, pos):
    if (x < pos[0] < x + a) and (y < pos[1] < y + b):
        return True
    else:
        return False
   
def pointer():
    pos = pygame.mouse.get_pos()
    r = 25
    l = 20
    color = lightGreen
    for i in range(noghost):
        if isonghost(ghosts[i].x, ghosts[i].y, ghosts[i].a, ghosts[i].b, pos):
            color = red
    pygame.draw.ellipse(display, color, (pos[0] - r/2, pos[1] - r/2, r, r), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] - l/2), (pos[0], pos[1] - l), 4)
    pygame.draw.line(display, color, (pos[0] + l/2, pos[1]), (pos[0] + l, pos[1]), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] + l/2), (pos[0], pos[1] + l), 4)
    pygame.draw.line(display, color, (pos[0] - l/2, pos[1]), (pos[0] - l, pos[1]), 4)
 

def lowerPlatform():
    pygame.draw.rect(display, darkGray, (0, height - lowerBound, width, lowerBound))
   

def showScore(lvl, start_time):
    scoreText = font.render(f"Уничтожено : " + str(score), True, white)
    display.blit(scoreText, (150, height - lowerBound + 50))

    scoreText1 = font.render(f"Уровень : {lvl}", True, white)
    display.blit(scoreText1, (450, height - lowerBound + 50))
    lvl_no = int(lvl[len(lvl)-1])


    if lvl_no==1:
        scoreText2 = font.render(f"Надо уничтожить {int(lvl[len(lvl)-1]) * 15 * 1}", True, white)
        display.blit(scoreText2, (750, height - lowerBound + 50))
    elif lvl_no==2:
        scoreText2 = font.render(f"Надо уничтожить {int(lvl[len(lvl)-1]) * 15 * 1}", True, white)
        display.blit(scoreText2, (750, height - lowerBound + 50))
    else:
        scoreText2 = font.render(f"Надо уничтожить {int(lvl[len(lvl)-1]) * 15 * 4}", True, white)
        display.blit(scoreText2, (750, height - lowerBound + 50))


    elapsed_seconds = count_seconds(start_time)
    




        
    seconds_text = font.render("Прошло секунд: " + str(elapsed_seconds), True, white)


    # Печатает сколько секунд прошло

    display.blit(seconds_text, (990, height - lowerBound + 50))

    pygame.display.update()
    clock.tick(60)


    
   
def close():
    pygame.quit()
    sys.exit()

def display_prompt():
    display.fill((255, 255, 255))  



    prompt_text = font.render("Ты молодец, ты победил этих призраков!", True, (0, 0, 0))
    display.blit(prompt_text, (width // 2 - prompt_text.get_width() // 2, height // 2 - prompt_text.get_height() // 2))
    pygame.display.update()


    prompt2_text = font.render("Перейти на следующий уровень? (да (y)/нет(n))", True, (0, 0, 0))
    display.blit(prompt2_text, (width // 2 - prompt2_text.get_width() // 2, height // 2 + 20 - prompt2_text.get_height() // 2))
    pygame.display.update()


def display_confirmation():
    display.fill((255, 255, 255)) 


    prompt_text = font.render("Ты проиграл, но не расстраивайся,можно начать заново!", True, (0, 0, 0))
    display.blit(prompt_text, (width // 2 - prompt_text.get_width() // 2, height // 2 - prompt_text.get_height() // 2))
    pygame.display.update()


    prompt2_text = font.render("Вы хотите продолжить? (да(y)/нет(n))", True, (0, 0, 0))
    display.blit(prompt2_text, (width // 2 - prompt2_text.get_width() // 2, height // 2 + 20 - prompt2_text.get_height() // 2))
    pygame.display.update()



def show_confirmation():
    waiting_for_input = True

    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    waiting_for_input = False
                    return True
                elif event.key == pygame.K_n:
                    waiting_for_input = False
                    return False

        display_confirmation()
        pygame.time.delay(50)
        clock.tick(60)

def get_yes_no_input():
    waiting_for_input = True

    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    waiting_for_input = False
                    return True
                elif event.key == pygame.K_n:
                    waiting_for_input = False
                    return False

        display_prompt()
        pygame.time.delay(50)
        clock.tick(60)

def count_seconds(start_time):
    current_time = pygame.time.get_ticks()
    elapsed_seconds = (current_time - start_time) // 1000
    return elapsed_seconds

def game(lvl):

    global score
    loop = True
    
    start_time = pygame.time.get_ticks()
    

    while loop:


        elapsed_seconds = count_seconds(start_time)
        
        seconds_text = font.render("Истекшие секунды: " + str(elapsed_seconds), True, (0, 0, 0))

        print(elapsed_seconds)



        if score > 15 and lvl==1 and elapsed_seconds < 60:
            
            score = 0

            lvl = lvl + 1

            start_time = pygame.time.get_ticks()

            response = get_yes_no_input()

            if response:
                print("Пользователь выбрал: Да")
            else:
                print("Пользователь выбрал: Нет")
                sys.exit()

        elif score < 15 and lvl==1 and elapsed_seconds > 60:
            
            response = show_confirmation()

            if response:
                print("Пользователь выбрал: Да")
                game()
            else:
                print("Пользователь выбрал: Нет")
                sys.exit()

        elif score > 30 and lvl == 2 and elapsed_seconds < 60:
            
            score = 0

            lvl = lvl + 1

            start_time = pygame.time.get_ticks()

            response = get_yes_no_input()

            if response:
                print("Пользователь выбрал: Да")
            else:
                print("Пользователь выбрал: Нет")
                sys.exit()

        elif score < 30 and lvl==2 and elapsed_seconds > 60:
            
            response = show_confirmation()

            if response:
                print("Пользователь выбрал: Да")
                game()
            else:
                print("Пользователь выбрал: Нет")
                sys.exit()
        elif score > 60 and lvl == 3 and elapsed_seconds < 60:
            
            score = 0

            lvl = lvl + 1

            start_time = pygame.time.get_ticks()

            response = get_yes_no_input()

            if response:
                print("Пользователь выбрал: Да")
            else:
                print("Пользователь выбрал: Нет")
                sys.exit()

        elif score < 60 and lvl==3 and elapsed_seconds > 60:
            
            response = show_confirmation()

            if response:
                print("Пользователь выбрал: Да")
                game()
            else:
                print("Пользователь выбрал: Нет")
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    score = 0
                    game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        print("Хотите продолжить: Да")
                        continue   
                    elif event.key == pygame.K_n:
                        print("Выйти? 'нет'")
                        loop = False  

 
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(noghost):
                    ghosts[i].burst()
 
        display.blit(background_image, (0, 0))
       
        for i in range(noghost):
            ghosts[i].show()
 
        pointer()
       
        for i in range(noghost):
            ghosts[i].move()
 
       
        lowerPlatform()
        showScore(f'Уровень {lvl}', start_time)
        pygame.display.update()
        clock.tick(60)
       

 # Проверка на достижение вершины небоскреба
        for ghost in ghosts:
            if ghost.y <= 0: 
                hp -= 1
                ghost.y = 600 
                if hp <= 0:
                    pygame.quit()
                    sys.exit()
# Запуск Игра

if __name__=="__main__":

    instructions()
    game(1)

    

    