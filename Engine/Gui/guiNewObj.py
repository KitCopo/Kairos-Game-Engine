import pygame  
from objects.objects import Types

class Context_new_obj: 
    def __init__(self,window) -> None:
        self.Window = window
        self.Conteiner_Color = (40,40,40)
        self.sceen = pygame.image.load('./Assents/Node2D.svg')
        self.square = pygame.image.load('./Assents/CollisionShape2D.svg')
        self.Circle = pygame.image.load('./Assents/CircleShape2D.svg')
        self.Camera2D = pygame.image.load('./Assents/Camera2D.svg')
        self.Polygon = pygame.image.load('./Assents/Polygon2D.svg')
        self.icons = [self.sceen,self.Camera2D,self.Polygon,self.square,self.Circle]
        self.Names = ['Sceen2D','Camera2D','Polygon2D','Square','Circle']

        self.font2 = pygame.font.SysFont('Arial',12,True)
        self.click = False
        self.Changes_Datas()
   
    def Changes_Datas(self) -> None: 
        self.Conteiner_Size = [self.Window.get_width() / 4, self.Window.get_height() / 2 ]
        self.Conteiner_Vector = [self.Window.get_width() / 2 - self.Conteiner_Size[0] / 2,50]
        self.button_Size = [int(self.Conteiner_Size[0] * 0.25),int(self.Conteiner_Size[1] * 0.09)]
        self.Size_font = (int(self.button_Size[0] * 0.15))
        self.fontPersonalizado = pygame.font.SysFont('Arial',self.Size_font, (200,200,200))
        self.criar = self.fontPersonalizado.render('Criar',True , (200,200,200))
        self.cancelar = self.fontPersonalizado.render('Cancelar',True, (200,200,200))

    def Create_Conteiner(self) -> None:
        self.Changes_Datas()
        pygame.draw.rect(self.Window,self.Conteiner_Color, (self.Conteiner_Vector[0],self.Conteiner_Vector[1],self.Conteiner_Size[0],self.Conteiner_Size[1]))
    
    def Create_Logic(self) -> None: 
        self.Changes_Datas()
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

    def Create_Buttons(self) -> None:
        self.Changes_Datas() 
        pygame.draw.rect(self.Window,(30,30,30), (self.Conteiner_Vector[0] + self.button_Size[0] / 4,self.Conteiner_Vector[1] + self.Conteiner_Size[1] - self.button_Size[1] - 20,self.button_Size[0],self.button_Size[1]))
        pygame.draw.rect(self.Window,(30,30,30), (self.Conteiner_Vector[0] + self.Conteiner_Size[0] - self.button_Size[0] - 25 ,self.Conteiner_Vector[1] + self.Conteiner_Size[1] - self.button_Size[1] - 20,self.button_Size[0],self.button_Size[1]))
        self.Window.blit(self.criar, (self.Conteiner_Vector[0] + self.button_Size[0] / 4 + self.criar.get_width() / 2 + self.button_Size[0] / 4 - self.criar.get_width() / 2,self.Conteiner_Vector[1] + self.Conteiner_Size[1] - self.button_Size[1] - 20 + self.button_Size[1] / 4))
        self.Window.blit(self.cancelar,(self.Conteiner_Vector[0] + self.Conteiner_Size[0] - self.button_Size[0] - 25 + self.cancelar.get_width() / 2 + self.button_Size[0] / 4 - self.cancelar.get_width() / 2,self.Conteiner_Vector[1] + self.Conteiner_Size[1] - self.button_Size[1] - 20+ self.button_Size[1] / 4))

    def Create_Objs(self) -> None:
        self.Changes_Datas()
        VectorY = 0
        Vector2Y = 0
        for icon in self.icons: 
            self.Window.blit(icon, (self.Conteiner_Vector[0] + icon.get_width() / 2,self.Conteiner_Vector[1] + 10 + VectorY))
            VectorY += icon.get_height() + 10
        for Name in self.Names:
            text =  self.font2.render(f'{Name}',True, (200,200,200))
            self.Window.blit(text, (self.Conteiner_Vector[0] + icon.get_width() / 2 + 30,self.Conteiner_Vector[1] + 12 + Vector2Y))
            Vector2Y += text.get_height() + 12
    
    def render(self,state) -> None:
        if state:
            self.Create_Conteiner()
            self.Create_Objs()
            self.Create_Buttons()
            self.Create_Logic()