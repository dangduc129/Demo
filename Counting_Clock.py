try: 

    import pygame 
    import math
    import time
    pygame.init()

    screen = pygame.display.set_mode((500,600))

    GREY = (150,150,150)
    WHITE = (255,255,255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 36)  # Chọn font và kích thước chữ

    running = True

    font = pygame.font.SysFont('sans', 50)
    text_1 = font.render('+', True, BLACK)  # Tạo Surface cho các chuỗi
    text_2 = font.render('-', True, BLACK)
    text_3 = font.render('+', True, BLACK)
    text_4 = font.render('-', True, BLACK)
    text_5 = font.render('START', True, BLACK)
    text_6 = font.render('RESET', True, BLACK)

    total_secs = 0
    total = 0
    start = False
    clock = pygame.time.Clock()

    while running: 
        clock.tick(60)
        screen.fill(GREY)
        # sound = pygame.mixer.Sound('alarm.wav')
        mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))
        pygame.draw.rect(screen, WHITE, (100, 150, 50, 50))
        pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
        pygame.draw.rect(screen, WHITE, (200, 150, 50, 50))
        pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
        pygame.draw.rect(screen, WHITE, (300, 150, 150, 50))

        screen.blit(text_1, (100, 50))
        screen.blit(text_2, (100, 150))
        screen.blit(text_3, (200, 50))
        screen.blit(text_4, (200, 150))
        screen.blit(text_5, (300, 50))
        screen.blit(text_6, (300, 150))

        pygame.draw.circle(screen, BLACK, (250, 400), 102)
        pygame.draw.circle(screen, WHITE, (250, 400), 100) # Đối số thứ hai là màu, thứ ba là tọa độ tâm và thứ tư là bán kính
        pygame.draw.circle(screen, BLACK, (250, 400), 2)

        pygame.draw.line(screen, BLACK, (250, 400), (250, 305))
        pygame.draw.line(screen, BLACK, (250, 400), (250, 360))

        pygame.draw.rect(screen, BLACK, (120, 530, 260, 50))
        pygame.draw.rect(screen, WHITE, (125, 535, 250, 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (100 < mouse_x < 150) and (50 < mouse_y < 100):
                        total_secs += 60
                    elif (100 < mouse_x < 150) and (150 < mouse_y < 200):
                        total_secs -= 60
                        if total_secs < 0:
                            total_secs = 0
                    elif (200 < mouse_x < 250) and (50 < mouse_y < 100):
                        total_secs += 1
                    elif (200 < mouse_x < 250) and (150 < mouse_y < 200):
                        total_secs -= 1
                        if total_secs < 0:
                            total_secs = 0
                    elif (300 < mouse_x < 400) and (50 < mouse_y < 100):
                        start = True
                    elif (300 < mouse_x < 400) and (150 < mouse_y < 200):
                        total_secs = 0
                        start = False

        if start and total_secs > 0:
            total_secs -= 1

        mins = int(total_secs/60)
        secs = total_secs - mins*60
        
        time_now = str(mins) + ':' + str(secs)
        
        text_time = font.render(time_now, True, BLACK)
        screen.blit(text_time, (150,300))
        
        x_sec = 250 + 95*math.sin(6* secs *math.pi/180)
        y_sec = 400 - 95*math.cos(6* secs *math.pi/180)
        pygame.draw.line(screen, BLACK, (250, 400), (int(x_sec), int(y_sec)))

        x_min = 250 + 40*math.sin(6* mins * math.pi/180)
        y_min = 400 - 40*math.sin(6* mins * math.pi/180)
        pygame.draw.line(screen, GREY, (250, 400), (int(x_min), int(y_min)))

        if total != 0: 
            pygame.draw.rect(screen, GREY, (120, 530, int(380*(total_secs/total)),30))

        pygame.display.flip()

    pygame.quit()

except Exception as bug:
    print(bug)

input()



