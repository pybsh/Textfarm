import pygame
from pygame.locals import *
import sys
import DataManager

pygame.init()

WIDTH = 400
HEIGHT = 640

MAINTEXT = (32,32)
BUTTON1 = [(32,416),(367,447)]
BUTTON2 = [(32,464),(367,495)]
BUTTON3 = [(32,512),(367,543)]
BUTTON4 = [(32,560),(367,591)]

DAYS=1
GOLD=500
ENERGY=100
CURRENT="opening"
SEEDS={"carrot":0, "tomato": 0, "corn": 0, "potato": 0}
FIELD=[]
BUYITEM=[]
PLANTSEED=''
HELP_HUNTER = False
HELP_FLOODVICTIM = False

pygame.display.set_caption('TextFarm')
icon = pygame.image.load('./Assets/img/icon.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock  = pygame.time.Clock()
font = pygame.font.SysFont('Neo둥근모', 20)

def background():
    background_normal=pygame.image.load('./Assets/img/background_normal.png')
    screen.blit(background_normal, (0,0))

def background_rain():
    background_rain=pygame.image.load('./Assets/img/background_rain.png')
    screen.blit(background_rain, (0,0))

def opening():
    background()

    opening=pygame.image.load('./Assets/text/main/opening.png')
    screen.blit(opening, MAINTEXT)

    okay=pygame.image.load('./Assets/text/button/okay.png')
    screen.blit(okay, BUTTON1[0])
    screen.blit(okay, BUTTON2[0])
    screen.blit(okay, BUTTON3[0])
    screen.blit(okay, BUTTON4[0])

    pygame.mixer.Sound('./Assets/sound/bgm.wav').play(loops=-1)

def ending():
    ending_normal=pygame.image.load('./Assets/img/ending_normal.png')
    ending_rich=pygame.image.load('./Assets/img/ending_rich.png')
    ending_hero_of_the_village=pygame.image.load('./Assets/img/ending_hero_of_the_village.png')

    hero_of_the_village=pygame.image.load('./Assets/text/main/hero_of_the_village.png')
    rich=pygame.image.load('./Assets/text/main/rich.png')
    normal=pygame.image.load('./Assets/text/main/normal.png')
    
    quit_game=pygame.image.load('./Assets/text/button/quit_game.png')
    if HELP_FLOODVICTIM:
        screen.blit(ending_hero_of_the_village, (0,0))
        screen.blit(hero_of_the_village, MAINTEXT)
    elif GOLD >= 3000:
        screen.blit(ending_rich, (0,0))
        screen.blit(rich, MAINTEXT)
    else:
        screen.blit(ending_normal, (0,0))
        screen.blit(normal, MAINTEXT)
    screen.blit(quit_game, BUTTON4[0])
    global CURRENT
    CURRENT = 'ending'

def main():
    background()

    main=pygame.image.load(f'./Assets/text/main/main_day{DAYS}.png')
    screen.blit(main, MAINTEXT)

    shop=pygame.image.load('./Assets/text/button/shop.png')
    seed=pygame.image.load('./Assets/text/button/seed.png')
    harvest=pygame.image.load('./Assets/text/button/harvest.png')
    finish=pygame.image.load('./Assets/text/button/finish.png')
    screen.blit(shop, BUTTON1[0])
    screen.blit(seed, BUTTON2[0])
    screen.blit(harvest, BUTTON3[0])
    screen.blit(finish, BUTTON4[0])

    global CURRENT
    CURRENT='main'

def shop_select():
    background()

    shop_select=pygame.image.load('./Assets/text/main/shop_select.png')
    screen.blit(shop_select, MAINTEXT)

    buy_seed=pygame.image.load("./Assets/text/button/buy_seed.png")
    buy_food=pygame.image.load("./Assets/text/button/buy_food.png")
    back=pygame.image.load("./Assets/text/button/back.png")
    screen.blit(buy_seed, BUTTON1[0])
    screen.blit(buy_food, BUTTON2[0])
    screen.blit(back, BUTTON3[0])

    global CURRENT
    CURRENT='shop_select'

def shop_seed():
    background()

    shop_select=pygame.image.load('./Assets/text/main/shop_seed.png')
    screen.blit(shop_select, MAINTEXT)

    carrot=pygame.image.load("./Assets/text/button/carrot.png")
    tomato=pygame.image.load("./Assets/text/button/tomato.png")
    corn=pygame.image.load("./Assets/text/button/corn.png")
    potato=pygame.image.load("./Assets/text/button/potato.png")
    screen.blit(carrot, BUTTON1[0])
    screen.blit(tomato, BUTTON2[0])
    screen.blit(corn, BUTTON3[0])
    screen.blit(potato, BUTTON4[0])

    global CURRENT
    CURRENT='shop_seed'

def shop_food():
    background()

    shop_select=pygame.image.load('./Assets/text/main/shop_food.png')
    screen.blit(shop_select, MAINTEXT)

    mushroom_stew=pygame.image.load("./Assets/text/button/mushroom_stew.png")
    bread=pygame.image.load("./Assets/text/button/bread.png")
    corn_soup=pygame.image.load("./Assets/text/button/corn_soup.png")
    baked_potato=pygame.image.load("./Assets/text/button/baked_potato.png")
    screen.blit(mushroom_stew, BUTTON1[0])
    screen.blit(bread, BUTTON2[0])
    screen.blit(corn_soup, BUTTON3[0])
    screen.blit(baked_potato, BUTTON4[0])

    global CURRENT
    CURRENT='shop_food'

def confirm_shop(enough: int):
    background()

    confirm=pygame.image.load('./Assets/text/main/confirm.png')
    screen.blit(confirm, MAINTEXT)

    okay=pygame.image.load("./Assets/text/button/okay.png")
    back=pygame.image.load("./Assets/text/button/back.png")
    not_enough_gold=pygame.image.load("./Assets/text/button/not_enough_gold.png")
    
    global GOLD
    global CURRENT
    if enough > GOLD:
        screen.blit(not_enough_gold, BUTTON1[0])
        screen.blit(back, BUTTON2[0])
        CURRENT='not_enough'
    else:
        screen.blit(okay, BUTTON1[0])
        screen.blit(back, BUTTON2[0])
        CURRENT=f'confirm_shop'

def plant_seed():
    background()

    seed_select=pygame.image.load('./Assets/text/main/seed_select.png')
    screen.blit(seed_select, MAINTEXT)

    carrot=pygame.image.load("./Assets/text/button/carrot.png")
    tomato=pygame.image.load("./Assets/text/button/tomato.png")
    corn=pygame.image.load("./Assets/text/button/corn.png")
    potato=pygame.image.load("./Assets/text/button/potato.png")
    screen.blit(carrot, BUTTON1[0])
    screen.blit(tomato, BUTTON2[0])
    screen.blit(corn, BUTTON3[0])
    screen.blit(potato, BUTTON4[0])

    global CURRENT
    CURRENT='plant_seed'

def confirm_seed(item: str):
    background()

    confirm=pygame.image.load('./Assets/text/main/confirm.png')
    screen.blit(confirm, MAINTEXT)

    okay=pygame.image.load("./Assets/text/button/okay.png")
    back=pygame.image.load("./Assets/text/button/back.png")
    not_enough_seed=pygame.image.load("./Assets/text/button/not_enough_seed.png")
    not_enough_energy=pygame.image.load("./Assets/text/button/not_enough_energy.png")
    global CURRENT

    if ENERGY <= 10:
        screen.blit(not_enough_energy, BUTTON1[0])
        screen.blit(back, BUTTON2[0])
        CURRENT = 'not_enough'
    elif SEEDS[item] >= 1:
        screen.blit(okay, BUTTON1[0])
        screen.blit(back, BUTTON2[0])
        CURRENT = 'confirm_seed'
    else:
        screen.blit(not_enough_seed, BUTTON1[0])
        screen.blit(back, BUTTON2[0])
        CURRENT = 'not_enough'

def harvest():
    background()

    confirm=pygame.image.load('./Assets/text/main/confirm.png')
    screen.blit(confirm, MAINTEXT)

    okay=pygame.image.load("./Assets/text/button/okay.png")
    back=pygame.image.load("./Assets/text/button/back.png")
    not_enough_crops=pygame.image.load("./Assets/text/button/not_enough_crops.png")
    not_enough_energy=pygame.image.load("./Assets/text/button/not_enough_energy.png")

    f=False
    global CURRENT
    for i in FIELD:
        if i[1] <= 0:
            f=True
            break
    
    if ENERGY <= 19:
        screen.blit(not_enough_energy, BUTTON1[0])
        screen.blit(back, BUTTON2[0])
        CURRENT = 'not_enough'
    elif f:
        screen.blit(okay,BUTTON1[0])
        screen.blit(back,BUTTON2[0])
        CURRENT='harvest'
    else:
        screen.blit(not_enough_crops, BUTTON1[0])
        screen.blit(back, BUTTON2[0])
        CURRENT = 'not_enough'

def finish_day():
    background_rain() 

    confirm=pygame.image.load('./Assets/text/main/confirm.png')
    screen.blit(confirm, MAINTEXT)

    okay=pygame.image.load("./Assets/text/button/okay.png")
    back=pygame.image.load("./Assets/text/button/back.png")

    screen.blit(okay,BUTTON1[0])
    screen.blit(back,BUTTON2[0])
    global CURRENT
    CURRENT='finish_day'

def event_treasure(type: str='normal'):
    background_rain()
    
    event_treasure=pygame.image.load('./Assets/text/main/event_treasure.png')
    if type == 'downpour':
        event_treasure=pygame.image.load('./Assets/text/main/event_downpour_treasure.png')
    screen.blit(event_treasure, MAINTEXT)

    okay=pygame.image.load("./Assets/text/button/okay.png")
    screen.blit(okay, BUTTON1[0])
    global CURRENT
    CURRENT='event_treasure'

def event_hunter():
    background_rain()

    event_hunter=pygame.image.load('./Assets/text/main/event_hunter.png')
    screen.blit(event_hunter, MAINTEXT)

    accept=pygame.image.load('./Assets/text/button/accept.png')
    deny=pygame.image.load('./Assets/text/button/deny.png')
    screen.blit(accept, BUTTON1[0])
    screen.blit(deny, BUTTON2[0])
    global CURRENT
    CURRENT='event_hunter'

def event_wildboar():
    background_rain()

    event_wildboar=pygame.image.load('./Assets/text/main/event_wildboar.png')
    screen.blit(event_wildboar, MAINTEXT)

    hunter_help=pygame.image.load('./Assets/text/button/hunter_help.png')
    giveup=pygame.image.load('./Assets/text/button/giveup.png')
    no_hunter=pygame.image.load('./Assets/text/button/no_hunter.png')
    
    global CURRENT
    if HELP_HUNTER:
        screen.blit(hunter_help, BUTTON1[0])
        screen.blit(giveup, BUTTON2[0])
    else:
        screen.blit(no_hunter, BUTTON1[0])
        screen.blit(giveup, BUTTON2[0])
    CURRENT='event_wildboar'
        
def event_downpour():
    background_rain()

    event_downpour=pygame.image.load('./Assets/text/main/event_downpour.png')
    screen.blit(event_downpour, MAINTEXT)

    help=pygame.image.load('./Assets/text/button/help.png')
    deny=pygame.image.load('./Assets/text/button/deny.png')
    screen.blit(help, BUTTON1[0])
    screen.blit(deny, BUTTON2[0])
    
    global CURRENT
    CURRENT = 'event_downpour'

def event_pumpkin():
    background_rain()

    event_pumpkin=pygame.image.load('./Assets/text/main/event_pumpkin.png')
    screen.blit(event_pumpkin, MAINTEXT)

    okay=pygame.image.load("./Assets/text/button/okay.png")
    screen.blit(okay, BUTTON1[0])
    for i in range(10):
        FIELD.append(['pumpkin',3])

    global CURRENT
    CURRENT='event_treasure'

def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def end():
    global DAYS
    fade(400,640)
    pygame.time.delay(30)
    DAYS += 1
    for i in FIELD:
        i[1] -= 1
    print(FIELD)
    if DAYS >= 31:
        ending()
    else:
        main()

def button(number: int):
    global DAYS
    global GOLD
    global BUYITEM
    global ENERGY
    global HELP_FLOODVICTIM
    global HELP_HUNTER
    global PLANTSEED
    
    pygame.mixer.Sound('./Assets/sound/click.wav').play()
    if CURRENT == 'opening':
        main()
    elif CURRENT == 'main':
        if number == 1:
            shop_select()
        elif number == 2:
            plant_seed()
        elif number == 3:
            harvest()
        elif number == 4:
            finish_day()
    elif CURRENT == 'shop_select':
        if number == 1:
            shop_seed()
        elif number == 2:
            shop_food()
        elif number == 3:
            main()
    elif CURRENT == 'shop_seed':
        if number == 1:
            confirm_shop(DataManager.get('crops')['carrot']['buyPrice'])
            BUYITEM=['crops','carrot']
        elif number == 2:
            confirm_shop(DataManager.get('crops')['tomato']['buyPrice'])
            BUYITEM=['crops','tomato']
        elif number == 3:
            confirm_shop(DataManager.get('crops')['corn']['buyPrice'])
            BUYITEM=['crops','corn']
        elif number == 4:
            confirm_shop(DataManager.get('crops')['potato']['buyPrice'])
            BUYITEM=['crops','potato']
    elif CURRENT == 'shop_food':
        if number == 1:
            confirm_shop(DataManager.get('foods')['mushroom_stew']['buyPrice'])
            BUYITEM=['foods','mushroom_stew']
        elif number == 2:
            confirm_shop(DataManager.get('foods')['bread']['buyPrice'])
            BUYITEM=['foods','bread']
        elif number == 3:
            confirm_shop(DataManager.get('foods')['corn_soup']['buyPrice'])
            BUYITEM=['foods','corn_soup']
        elif number == 4:
            confirm_shop(DataManager.get('foods')['baked_potato']['buyPrice'])
            BUYITEM=['foods','baked_potato']
    elif CURRENT == 'not_enough':
        if number == 2:
            main()
    elif CURRENT == 'confirm_shop':
        if number == 1:
            if DAYS == 6:
                GOLD -= int(DataManager.get(BUYITEM[0])[BUYITEM[1]]['buyPrice'] * 0.5)
            else:
                GOLD -= DataManager.get(BUYITEM[0])[BUYITEM[1]]['buyPrice']
            if BUYITEM[0] == 'crops':
                SEEDS[BUYITEM[1]]+=1
            elif BUYITEM[0] == 'foods':
                ENERGY+=DataManager.get(BUYITEM[0])[BUYITEM[1]]['energy']
                if ENERGY > 300:
                    ENERGY = 300
                pygame.mixer.Sound('./Assets/sound/food.wav').play()
            BUYITEM=[]
            main()
        elif number == 2:
            main()
    elif CURRENT == 'plant_seed':
        if number == 1:
            confirm_seed('carrot')
            PLANTSEED='carrot'
        elif number == 2:
            confirm_seed('tomato')
            PLANTSEED='tomato'
        elif number == 3:
            confirm_seed('corn')
            PLANTSEED='corn'
        elif number == 4:
            confirm_seed('potato')
            PLANTSEED='potato'
    elif CURRENT == 'confirm_seed':
        if number == 1:
            SEEDS[PLANTSEED] -= 1
            FIELD.append([PLANTSEED,DataManager.get('crops')[PLANTSEED]['growPeriod']])
            PLANTSEED=''
            ENERGY-=10
            main()
        elif number == 2:
            main()
    elif CURRENT == 'harvest':
        if number == 1:
            pygame.mixer.Sound('./Assets/sound/harvest.wav').play()
            ENERGY-=20
            for i in FIELD:
                if i[1] <= 0:
                    if DAYS == 27:
                        GOLD += int(DataManager.get('crops')[i[0]]['sellPrice']*1.5)
                    else:
                        GOLD += DataManager.get('crops')[i[0]]['sellPrice']
                    FIELD.remove(i)
            print(GOLD)
            main()
        elif number == 2:
            main()
    elif CURRENT == 'finish_day':
        if number == 1:
            pygame.mixer.Sound('./Assets/sound/finish_day.wav').play()
            if DAYS == 3 or DAYS == 9:
                GOLD += 200
                event_treasure()
            elif DAYS == 12:
                event_hunter()
            elif DAYS == 15:
                event_wildboar()
            elif DAYS == 18:
                event_downpour()
            elif DAYS == 21:
                event_pumpkin()
            elif DAYS == 24:
                event_treasure(type='downpour')
                GOLD += 200
            else:
                end()
        elif number == 2:
            main()
    elif CURRENT == 'event_treasure':
        if number == 1:
            end()
    elif CURRENT == 'event_hunter':
        if number == 1:
            HELP_HUNTER=True
            GOLD -= int(GOLD*0.4)
        end()
    elif CURRENT == 'event_wildboar':
        if number == 1:
            if HELP_HUNTER:
                end()
        elif number == 2:
            GOLD -= int(GOLD*0.6)
            end()
    elif CURRENT == 'event_downpour':
        if number == 1:
            GOLD -= int(GOLD*0.7)
            HELP_FLOODVICTIM = True
            end()
        elif number == 2:
            end()
    elif CURRENT == 'ending':
        if number == 4:
            pygame.quit()
            sys.exit()

opening()
while True:
    clock.tick(30)
 
    gold_text = font.render(f"골드: {GOLD}", True, (0,0,0))
    energy_text = font.render(f"에너지: {ENERGY}", True, (0,0,0))
    screen.blit(gold_text, (32,610))
    screen.blit(energy_text, (250, 610))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mx, my = event.pos
            if BUTTON1[0][0] <= mx <= BUTTON1[1][0] and BUTTON1[0][1] <= my <= BUTTON1[1][1]:
                button(1)
            elif BUTTON2[0][0] <= mx <= BUTTON2[1][0] and BUTTON2[0][1] <= my <= BUTTON2[1][1]:
                button(2)
            elif BUTTON3[0][0] <= mx <= BUTTON3[1][0] and BUTTON3[0][1] <= my <= BUTTON3[1][1]:
                button(3)
            elif BUTTON4[0][0] <= mx <= BUTTON4[1][0] and BUTTON4[0][1] <= my <= BUTTON4[1][1]:
                button(4)
    pygame.display.update()
