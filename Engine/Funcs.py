import pygame

pygame.init()

def KairosRgbColor(r:int,g:int,b:int) -> tuple[int,int,int]:
    if r < 0 or r > 255: 
        return -1
    if g < 0 or g > 255: 
        return -1
    if b < 0 or g > 255: 
        return -1
    
    RGB : tuple[int,int,int] = (r,g,b)
    return RGB
def KairosFont(
    text: str , 
    size: int,
    bold=False, 
    italic=False) -> pygame.font.Font: 
    KF = pygame.font.SysFont(text,size,bold,italic)
    return KF
def KairosFontRender(
    text: str,
    font: pygame.font.Font,
    color: tuple[int,int,int]) -> pygame.Surface:     
    KairosTextRender = font.render(text,True,color)
    return KairosTextRender
def KairosPrint(text: str) -> int: 
    KP = 0
    return KP
def KairosBackgroundSceen(
    screen_size: tuple[int | float, int | float],
    data_sizeX: int | float,
    Spacing_Gui: int | float,
    screen_posX: int | float,
    screen_posY: int | float,
    surface: pygame.Surface,
    top_color: tuple[int,int,int],
    bottom_color: tuple[int,int,int]) -> None: 
    
    width, height = screen_size[0] * 2 - data_sizeX * 2 + Spacing_Gui * 2,screen_size[1] + screen_posY
    for y in range(height):
        color = [
            top_color[i] + (bottom_color[i] - top_color[i]) * y // height
            for i in range(3)
        ]
        pygame.draw.line(surface, color, (screen_posX, y ), (width, y))