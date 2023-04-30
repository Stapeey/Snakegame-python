import sys, pygame, random
pygame.init()

tile = 40
tile_amount = 20
size=(tile_amount*tile,tile_amount*tile)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

facing_default = False
point=random.randint(1,4)

def restart():
    global pointing_to
    global changepos_x
    global changepos_y
    global food_locx 
    global food_locy 
    global snake_len 
    global soon_to_be_body 
    global snake_body_coords
    global food_rect
    if facing_default:
        if point == 1:
            pointing_to = [-1, 0]
        elif point == 2:
            pointing_to = [1, 0]
        elif point == 3:
            pointing_to = [0, -1]
        else:
            pointing_to = [0, 1]
            print("ok4")
    changepos_x = 10
    changepos_y = 10
    food_locx = random.randint(0,tile_amount-1)
    food_locy = random.randint(0,tile_amount-1)
    snake_len = 1
    soon_to_be_body = []
    snake_body_coords = []
    food_rect = pygame.Rect(food_locx*tile+0.05*tile/2, food_locy*tile+0.05*tile/2, tile*0.95, tile*0.95)

def gen_foodx():
    x = random.randint(0,tile_amount-1)
    return x
def gen_foody():
    y = random.randint(0,tile_amount-1)
    return y

def create_snake_body(lista):
    lista = lista[::-1]
    a = 0 ; b = 1
    for i in lista:
        if a == len(lista)-1:
            break
        lista[a]=lista[b]
        a += 1 ; b+=1
    return lista[::-1]

def create_list_len(list_len, lista):
    while len(lista) <= list_len:
        lista.append("fasz")
    return lista
    
falhalal = True
#pointing_to = [-1, 0]
if point == 1:
    pointing_to = [-1, 0]
elif point == 2:
    pointing_to = [1, 0]
elif point == 3:
    pointing_to = [0, -1]
else:
    pointing_to = [0, 1]



restart()
while True:
    if facing_default:
        point = random.randint(1,4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if is_keypressed:
                    continue
                else:
                    if pointing_to[0] == 1:
                        continue
                    pointing_to[0] = -1
                    pointing_to[1] = 0
                    is_keypressed = True
            if event.key == pygame.K_d:
                if is_keypressed:
                    continue
                else:
                    if pointing_to[0] == -1:
                        continue
                    pointing_to[0] = 1
                    pointing_to[1] = 0
                    is_keypressed = True
            if event.key == pygame.K_w:
                if is_keypressed:
                    continue
                else:
                    if pointing_to[1] == -1:
                        continue
                    pointing_to[1] = 1
                    pointing_to[0] = 0
                    is_keypressed = True
            if event.key == pygame.K_s:
                if is_keypressed:
                    continue
                else:  
                    if pointing_to[1] == 1:
                        continue
                    pointing_to[1] = -1
                    pointing_to[0] = 0
                    is_keypressed = True
            if event.key == pygame.K_r:
                restart()
            if event.key == pygame.K_f:
                falhalal = not falhalal
            if event.key == pygame.K_c:
                facing_default = not facing_default
                
    if pointing_to[0] == 1:
        changepos_x += 1
    if pointing_to[0] == -1:
        changepos_x -= 1
    if pointing_to[1] == 1:
        changepos_y -= 1
    if pointing_to[1] == -1:
        changepos_y += 1

    if changepos_x < 0:
        if falhalal:
            restart()
        else:
            changepos_x += tile_amount
    if changepos_y < 0:
        if falhalal:
            restart()
        else:
           changepos_y += tile_amount
    if changepos_x >= tile_amount:
        if falhalal:
            restart()
        else:
            changepos_x -= tile_amount
    if changepos_y >= tile_amount:
        if falhalal:
            restart()
        else:
            changepos_y -= tile_amount

    main_rect = pygame.Rect(changepos_x*tile+0.05*tile/2, changepos_y*tile+0.05*tile/2, tile*0.95, tile*0.95)

    if main_rect.colliderect(food_rect):
        food_locx = gen_foodx()
        food_locy = gen_foody()
        snake_len += 1
        food_rect = pygame.Rect(food_locx*tile+0.05*tile/2, food_locy*tile+0.05*tile/2, tile*0.95, tile*0.95)

    screen.fill('black')
    for i in range(tile_amount):
        for j in range(tile_amount):
            pygame.draw.rect(screen,(0,255,0),pygame.Rect(j*tile, i*tile, tile, tile)) #offsetben rajzolódik a fekete kocka utána FIXED
            pygame.draw.rect(screen,(0,0,0),pygame.Rect(j*tile+0.05*tile/2, i*tile+0.05*tile/2, tile*0.95, tile*0.95))
            j += tile
        i += tile
    pygame.draw.rect(screen, (255,0,0),main_rect)
    soon_to_be_body = create_list_len(snake_len,soon_to_be_body)
    soon_to_be_body = create_snake_body(soon_to_be_body)
    soon_to_be_body[0] = main_rect
    snake_body_coords = soon_to_be_body[1:len(soon_to_be_body)-1]
    for i in snake_body_coords:
        if i.colliderect(main_rect):
            restart()
        pygame.draw.rect(screen,(255,0,0),i)
    if food_rect in snake_body_coords:
        while food_rect in snake_body_coords:
            food_locx = gen_foodx()
            food_locy = gen_foody()
            food_rect = pygame.Rect(food_locx*tile+0.05*tile/2, food_locy*tile+0.05*tile/2, tile*0.95, tile*0.95)
    pygame.draw.rect(screen, (255,255,255),food_rect)
    is_keypressed = False
    pygame.display.flip()
    clock.tick(4)

#random pos még lehet de i think its pointless