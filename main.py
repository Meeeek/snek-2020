import pygame
import snake
import display
import food

pygame.display.set_caption("Snake")

def main():
    size = (800, 600)
    snake_s = 40

    player = snake.Snake(size, snake_s)
    fud = food.Food(size, snake_s)
    screen = display.Display(size, player, fud)
    clock = pygame.time.Clock()
    
    running = True
    while running:

        # Handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.set_direction('L')
                elif event.key == pygame.K_RIGHT:
                    player.set_direction('R')
                elif event.key == pygame.K_UP:
                    player.set_direction('U')
                elif event.key == pygame.K_DOWN:
                    player.set_direction('D')
        
        # getting food collision
        if player.collides_with(fud.get_rect()):
            fud.new_coords()
            player.add_block()
        player.move()

        # getting if the player is gonna lose
        if player.is_outside() or player.self_hit():
            lose(player.get_length())
            running = False
        screen.update()
        clock.tick(15)

def lose(score):
    highscore = get_highscore()
    print("====================================")
    print(f"you lost your score was {score}")
    print(f"The highscore is {highscore}")
    if score > highscore:
        print(f"Congrats you set the highscore to {score}")
        set_highscore(score)
    else:
        print(f"Better luck next time, \nyou were {highscore-score} from the highscore")
    print("====================================")

# This is for reading the file to get the highscore
def get_highscore() -> int:
    high = 0
    open_f = open("highscore.txt", 'r')
    high = int(open_f.read())
    open_f.close()
    return high

def set_highscore(high) -> None:
    open_f = open("highscore.txt", 'w')
    open_f.write(str(high))
    open_f.close()

if __name__ == '__main__':
    main()
    pygame.quit()
