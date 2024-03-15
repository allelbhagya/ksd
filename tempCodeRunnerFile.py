running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x < WIDTH // 3:
                counter_right += 1
                cars.add(Car(mouse_x, mouse_y, 'right', CAR_SPEED, 1))
            elif mouse_x > WIDTH // 3 * 2:
                counter_left += 1
                cars.add(Car(mouse_x, mouse_y, 'left', CAR_SPEED, 3))
            elif mouse_y < HEIGHT // 3:
                counter_down += 1
                cars.add(Car(mouse_x, mouse_y, 'down', CAR_SPEED, 2))
            elif mouse_y > HEIGHT // 3 * 2:
                counter_up += 1
                cars.add(Car(mouse_x, mouse_y, 'up', CAR_SPEED, 4))
