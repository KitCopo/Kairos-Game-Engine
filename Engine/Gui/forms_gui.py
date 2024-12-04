import pygame

class Gui_Forms: 
    def draw_Form1(self,Window,color,size:int|float,posX:int|float,posY:int|float,state:bool):
        if  not state:
            Vertices = (
                (posX + size,posY),
                (posX - size,posY - size * 2),
                (posX - size, posY + size * 2)
            )
        else:
            Vertices = (
                (posX ,posY + size),
                (posX - size*2 ,posY - size),
                (posX + size*2 ,posY - size)
            )

        pygame.draw.polygon(Window,color, (Vertices))

    def Check_Box(self,Window):
        return 0 