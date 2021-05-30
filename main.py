import pygame as pg
import random as r

pg.init()
pg.mixer.init()
pg.font.init()


#color
white= (255,255,255)
red=(255,0,0)
black=(0,0,0)

#clock
clock=pg.time.Clock()

#font
font=pg.font.SysFont("Arial Rounded MT Bold",100)


#display
screen_width=700
screen_length=900
bgimg=pg.image.load('gallery/bg.jpeg')
bgimg=pg.transform.scale(bgimg,(screen_length,screen_width))
snakes_head=pg.image.load('gallery/snakes_head.png')
#snakes_head=pg.transform.scale(snakes_head,(screen_length,screen_width))

apple=pg.image.load('gallery/apple.png')
frontimg=pg.image.load('gallery/welcome.png')
frontimg=pg.transform.scale(frontimg,(screen_length,screen_width))
gmover=pg.image.load('gallery/gameover.png')
gmover=pg.transform.scale(gmover,(screen_length,screen_width))
window=pg.display.set_mode((screen_length,screen_width))
pg.display.set_caption("Slytherin")
pg.display.update()

#functions
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    window.blit(screen_text, [x,y])
    
def plt_snake(window,color,snake_list,snake_size):
    for x,y in snake_list:          #pg.draw.rect(window,color,[x, y, snake_size,snake_size])
          window.blit(snakes_head, [x,y])
    
def welcome():
    pg.mixer.music.load('gallery/naagin.mp3')
    pg.mixer.music.play()
    exit_game= False
    while not exit_game:
            window.fill((198, 209, 153))
            window.blit(frontimg,(0,0))
            
            
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    exit_game=True
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_SPACE:
                        game_loop()
            pg.display.update()
            clock.tick(30)
    


def game_loop():      

    #variables
    exit_game=False
    over_game=False
    snake_x=screen_width/2
    snake_y=screen_length/3
    v_x=0
    v_y=0
    score=0
    food_x=r.randint(20,screen_length-20)
    food_y=r.randint(20,screen_width-20)
    snake_size=25
    food_size=25
    fps=30
    
    snake_list=[]
    snake_len=1
    
    with open('gallery/High_score.txt' , 'r') as f:
        hi_score=f.read()

    while not exit_game:
        if over_game is True:
            window.fill(white)
            window.blit(gmover,(0,0))
            with open('gallery/High_score.txt' , 'w') as f:
                f.write(str(hi_score))
            text_screen('Score: '+ str(score),white,50,600)
            text_screen('High Score: '+ str(hi_score),white,50,500)
          
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    exit_game=True
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RETURN:
                        welcome()
            
            
        else:
            window.fill(white)
            window.blit(bgimg,(0,0))
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    exit_game=True
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RIGHT:
                        v_x=12
                        v_y=0
                    if event.key==pg.K_LEFT:
                        v_x=-12
                        v_y=0
                    if event.key==pg.K_UP:
                        v_y=-12
                        v_x=0
                    if event.key==pg.K_DOWN:
                        v_y=12
                        v_x=0
            snake_x=snake_x+v_x
            snake_y=snake_y+v_y
            if abs(snake_x-food_x)<25 and abs(snake_y-food_y)<25 :
                pg.mixer.music.load('gallery/food.mp3')
                pg.mixer.music.play()
                score+=10
                snake_len+=4
                food_x=r.randint(50,screen_length-50)
                food_y=r.randint(50,screen_width-50)
                
                if score>int(hi_score):
                    hi_score=score

                
            window.fill(white)
            window.blit(bgimg,(0,0))
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            #pg.draw.ellipse(window, red, [food_x,food_y,food_size,food_size])
            window.blit(apple, (food_x,food_y))
            
            plt_snake(window,white,snake_list,snake_size)
            text_screen('SCORE: ' +str(score), (222, 247, 186), 5, 5)
           
            if len(snake_list)>snake_len:
                del snake_list[0]
            if head in snake_list[:-1]:
                over_game=True
                pg.mixer.music.load('gallery/gameover.mp3')
                pg.mixer.music.play()
            if(snake_x>screen_length or snake_x<0 or snake_y>screen_width or snake_y<0):
                over_game=True
                pg.mixer.music.load('gallery/gameover.mp3')
                pg.mixer.music.play()

        pg.display.update()
        clock.tick(fps)
    pg.quit()
    quit()
welcome()