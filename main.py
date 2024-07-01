import pygame
import re

PURPLE = (30, 0, 60)
WHITE = (255, 255, 255)

pygame.init()

w, h = 444, 600
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("THE BEST CALCULATOR DETONATOR")

font = pygame.font.Font("Comic2.ttf", 24)

symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "+", "/", "*"]
bg = pygame.transform.scale(pygame.image.load("bg.png"), (444, 600))
but = pygame.image.load("but.png")

input_text = ""

class Button:
    list = []
    but = pygame.Rect((0, 0, 91, 97))
    
    def __init__(self, text, cord, action):
        self.text = text
        self.cord = cord
        self.action = action
        Button.list.append(self)
        
    def draw(self):
        win.blit(but, self.cord)
        p_text(self.text, (self.cord[0] + but.get_width() / 2 - 5, self.cord[1] + but.get_height() / 3.1415))
        
    def check_col(self, mouse_pos):
        Button.but.topleft = self.cord
        if Button.but.collidepoint(mouse_pos):
            self.action()

# Define actions
def add_char(char):
    global input_text
    input_text += char

def clear_input():
    global input_text
    input_text = ""

def calculate_result():
    global input_text
    try:
        input_text = str(eval(input_text))
    except Exception:
        input_text = "ERR!"

# Create buttons
Button("1", (16, 132), lambda: add_char('1'))
Button("2", (123, 132), lambda: add_char('2'))
Button("3", (230, 132), lambda: add_char('3'))
Button("+", (337, 132), lambda: add_char('+'))
Button("4", (16, 245), lambda: add_char('4'))
Button("5", (123, 245), lambda: add_char('5'))
Button("6", (230, 245), lambda: add_char('6'))
Button("-", (337, 245), lambda: add_char('-'))
Button("7", (16, 358), lambda: add_char('7'))
Button("8", (123, 358), lambda: add_char('8'))
Button("9", (230, 358), lambda: add_char('9'))
Button("*", (337, 358), lambda: add_char('*'))
Button("C", (16, 471), clear_input)
Button("0", (123, 471), lambda: add_char('0'))
Button("=", (230, 471), calculate_result)
Button("/", (337, 471), lambda: add_char('/'))

def main():
    global input_text
    run = True
    while run:
        win.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN or event.unicode == "=":
                    calculate_result()
                else:
                    if event.unicode is not None and event.key != pygame.K_LSHIFT:
                        input_text += event.unicode
                        if not input_text[-1] in symbols:
                            input_text = input_text[:-1]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for btn in Button.list:
                    btn.check_col(mouse_pos)
        
        for btn in Button.list:
            btn.draw()
        
        p_text(input_text, (16, 16))  
        pygame.display.update()
    pygame.quit()
    sys.exit()

def p_text(text, cord):
    render = font.render(text, True, WHITE)
    win.blit(render, cord)

if __name__ == "__main__":
    main()
