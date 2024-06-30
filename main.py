import pygame
import re

PURPULE = (30,0,60)
WHITE = (255, 255, 255)

pygame.init()

w, h = 444, 600
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("THE BEST CALCULATOR DETONATOR")

font = pygame.font.Font("Comic2.ttf", 24)

symbols = ["1", "2", "3","4","5","6","7","8","9","0","-","+","/","*",]
bg = pygame.transform.scale(pygame.image.load("bg.png"), (444,600))
but = pygame.image.load("but.png")

class button:
    list = []
    def __init__(self, text, cord):
         self.text = text
         self.cord = cord
         
    def draw():
        for i in button.list:
            win.blit(but, i.cord)
            p_text(i.text, (i.cord[0]+but.get_width()/2-5, i.cord[1]+but.get_height()/3.1415))
    

button.list.append(button("1", (16, 132)))
button.list.append(button("2", (123, 132)))
button.list.append(button("3", (230, 132)))
button.list.append(button("+", (337, 132)))
button.list.append(button("4", (16, 245)))
button.list.append(button("5", (123, 245)))
button.list.append(button("6", (230, 245)))
button.list.append(button("-", (337, 245)))
button.list.append(button("7", (16, 358)))
button.list.append(button("8", (123, 358)))
button.list.append(button("9", (230, 358)))
button.list.append(button("*", (337, 358)))
button.list.append(button("C", (16, 471)))
button.list.append(button("0", (123, 471)))
button.list.append(button("=", (230, 471)))
button.list.append(button("/", (337, 471)))

input_text = ""
def main():
    global input_text
    run = True
    while run:
        win.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN or event.unicode == "=":
                    try:
                        input_text = str(eval(input_text))
                    except Exception:
                        input_text = "ERR!"
                else:
                    if event.unicode is not None and event.key != pygame.K_LSHIFT:
                        input_text += event.unicode
                        if not input_text[-1] in symbols:
                            input_text = input_text[:-1]
        button.draw()
        
        p_text(input_text, (16, 16))  
        pygame.display.update()
    pygame.quit()

def p_text(text, cord):
    render = font.render(text, True, WHITE)
    win.blit(render, cord)

        
if __name__ == "__main__":
    main()


