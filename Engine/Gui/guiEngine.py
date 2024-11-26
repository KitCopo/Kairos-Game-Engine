import pygame
import os
from Config.config_project import *
from Config.config_engine import *
from Config.config import *
from Scene_2D.compilador import *
from Gui.forms_gui import *
from Funcs import *
from random import randint
from Console.console import *
from objects.objects import Types
import configparser

config_file_path = os.path.join(os.path.dirname(__file__), './Console/configs.ini')
config = configparser.ConfigParser()
if os.path.exists(config_file_path):
    config.read(config_file_path)
else:
    print(f"Config file {config_file_path} not found!")
    
class Data_OBJS: 
    def __init__(self, Window):
        self.visible = True 
        self.config = ConFig()
        self.Gui_Forms = Gui_Forms()
        config_path = self.config.get_project_path()
        config_name = self.config.get_project_name()
        dentro_do_path = os.path.join(config_path,config_name)
        self.config_project = ProjectConfig(dentro_do_path)
        self.Window = Window
        self.Color = [34, 34, 34]
        self.Color_inspector = [80, 80, 80]
        self.font = pygame.font.SysFont('Arial', 12)
        self.KF = KairosFont('Arial',12)
        self.font2 = pygame.font.SysFont('Arial',12,True)
        self.text_name = KairosFontRender('Name',self.KF,(255,255,255))
        self.text_surface = self.font.render('Properties', True, (255, 255, 255))
        self.transformer_text = self.font2.render('Transform',True,(255,255,255))
        self.Position_text = self.font2.render('Position',True,(200,200,200))
        self.Rotation_text = self.font2.render('Rotation',True,(200,200,200))
        self.VectorX = self.font2.render('X',True,(200,200,200))
        self.VectorY = self.font2.render('Y',True,(200,200,200))
        self.Ray = self.font2.render('Ray',True,(200,200,200))
        self.Scale_text = self.font2.render('Scale',True,(200,200,200))
        self.cube_img = pygame.image.load('Assents/3d.png')
        self.close_img = pygame.image.load('Assents/close (2).png')
        self.close_img = pygame.transform.scale(self.close_img,(8,8))
        self.Name_img = pygame.image.load('Assents/letter-n (1).png')
        self.eixo_img = pygame.image.load('Assents/eixo.png')
        self.active = False
        self.state_1 = False
        self.click = False
        self.ColorInput = (0,0,0)
        self.input = 'padrao text'
        self.update_size_position()

    def update_size_position(self):
        if self.visible:
           self.Size = [int(self.Window.get_width() * 0.2), self.Window.get_height()]
        else:
           self.Size = [0,0]
        self.Vec = [self.Window.get_width() - self.Size[0], 20]
        
        self.Vec_side_bar = [self.Vec[0],0]
        self.Size_sid_bar = [self.Size[0],int(self.Size[1] * 0.025)]
        self.Vec_Inspector = [self.Vec[0],0]
        self.Size_Inspector = [int(self.Size[0] * 0.4), 25]

        self.Vec_text = [self.Vec_Inspector[0] + 30, self.Vec_Inspector[1] + 6]
        self.Vec_img = [self.Vec_Inspector[0] + 10, self.Vec_Inspector[1] + 4]
        self.Vec_close = [self.Window.get_width() - 20, 7]
        self.VecX_vector_transformer = [self.Vec[0] + self.transformer_text.get_width() + int(self.Size[0] * 0.25)]
        self.VecY_vector_trasformer = [self.VecX_vector_transformer[0] + int(self.Size[0] * 0.25)]
        #medidads dos input do transformer
        self.VecX_input_transformer = [self.VecX_vector_transformer[0] + 15]
        self.VecY_input_transformer = [self.VecY_vector_trasformer[0] + 15]
        self.Size_input_transformer = [int(self.Size[0] * 0.25) - 20,20]
    
    def render_top_Data_objs(self):
        self.update_size_position()
        pygame.draw.rect(self.Window,(19,19,19), (self.Vec_side_bar,self.Size_sid_bar))
        pygame.draw.rect(self.Window, self.Color, (*self.Vec_Inspector, *self.Size_Inspector))
        self.Window.blit(self.cube_img, (self.Vec_img))
        self.Window.blit(self.close_img,(self.Vec_close))
        self.Window.blit(self.text_surface, (self.Vec_text))
    
    def collision_gui(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        close_rect = pygame.Rect(self.Vec_close[0],self.Vec_close[1],self.close_img.get_width(),self.close_img.get_height())
        
        trasformer_mesh_rect = pygame.Rect(self.Vec[0],self.Vec[1] + 99,self.transformer_text.get_width() *2,self.transformer_text.get_height())
        if mouse_pressed[0]:
            if close_rect.collidepoint(mouse_pos):
                self.visible = False
            
            if not self.click:
                if trasformer_mesh_rect.collidepoint(mouse_pos):
                    if self.state_1:
                       self.state_1 = False
                    else: 
                       self.state_1 = True
                self.click = True
        else: 
            self.click = False
    
    def render_transformer(self,obj_type,obj_size,obj_pos): 
        self.Gui_Forms.draw_Form1(self.Window,(100,100,100),2.5,self.Vec[0] + 6,self.Vec[1] + 100,self.state_1)
        self.Window.blit(self.transformer_text,(self.Vec[0] + self.transformer_text.get_width() / 2,self.Vec[1] + 100 - self.transformer_text.get_height() / 2 - 1))
    
        if self.state_1:

            self.Window.blit(self.Position_text,(self.Vec[0] + self.transformer_text.get_width() / 2,self.Vec[1] + 110 - self.transformer_text.get_height() / 2 - 1 + self.Position_text.get_height()))
            self.Window.blit(self.VectorX,(self.VecX_vector_transformer[0],self.Vec[1] + 110 - self.transformer_text.get_height() / 2 - 1 + self.Position_text.get_height()))
            self.Window.blit(self.VectorY,(self.VecY_vector_trasformer[0],self.Vec[1] + 110 - self.transformer_text.get_height() / 2 - 1 + self.Position_text.get_height()))
            pygame.draw.rect(self.Window,(10,10,10),(self.VecX_input_transformer[0],self.Vec[1] + 110 - self.transformer_text.get_height() / 2 - 1 + self.Position_text.get_height(),self.Size_input_transformer[0],self.Size_input_transformer[1]),border_radius=5)
            pygame.draw.rect(self.Window,(10,10,10),(self.VecY_input_transformer[0],self.Vec[1] + 110 - self.transformer_text.get_height() / 2 - 1 + self.Position_text.get_height(),self.Size_input_transformer[0],self.Size_input_transformer[1]),border_radius=5)
            text_obj_posX = self.font2.render(f'{obj_pos[0]}',True,(200,200,200))
            text_obj_posY = self.font2.render(f'{obj_pos[1]}',True,(200,200,200))
            self.Window.blit(text_obj_posX, (self.VecX_input_transformer[0] + text_obj_posX.get_width() / 2,self.Vec[1] + 110 - self.transformer_text.get_height() / 2 - 1 + self.Position_text.get_height() + text_obj_posX.get_height()/4))
            self.Window.blit(text_obj_posY, (self.VecY_input_transformer[0] + text_obj_posX.get_width() / 2,self.Vec[1] + 110 - self.transformer_text.get_height() / 2 - 1 + self.Position_text.get_height() + text_obj_posY.get_height()/4))

            self.Window.blit(self.Rotation_text,(self.Vec[0] + self.transformer_text.get_width() / 2,self.Vec[1] + 135 - self.transformer_text.get_height() / 2 - 1 + self.Rotation_text.get_height()))
            self.Window.blit(self.VectorX,(self.VecX_vector_transformer[0],self.Vec[1] + 135 - self.transformer_text.get_height() / 2 - 1 + self.Rotation_text.get_height()))
            self.Window.blit(self.VectorY,(self.VecY_vector_trasformer[0],self.Vec[1] + 135 - self.transformer_text.get_height() / 2 - 1 + self.Rotation_text.get_height()))
            pygame.draw.rect(self.Window,(10,10,10),(self.VecX_input_transformer[0],self.Vec[1] + 135 - self.transformer_text.get_height() / 2 - 1 + self.Rotation_text.get_height(),self.Size_input_transformer[0],self.Size_input_transformer[1]),border_radius=5)
            pygame.draw.rect(self.Window,(10,10,10),(self.VecY_input_transformer[0],self.Vec[1] + 135 - self.transformer_text.get_height() / 2 - 1 + self.Rotation_text.get_height(),self.Size_input_transformer[0],self.Size_input_transformer[1]),border_radius=5)

            self.Window.blit(self.Scale_text,(self.Vec[0] + self.transformer_text.get_width() / 2,self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height()))
            
            if obj_type in Types and obj_type != Types[1]: 
                self.Window.blit(self.VectorX,(self.VecX_vector_transformer[0],self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height()))
                self.Window.blit(self.VectorY,(self.VecY_vector_trasformer[0],self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height()))
                pygame.draw.rect(self.Window,(10,10,10),(self.VecX_input_transformer[0],self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height(),self.Size_input_transformer[0],self.Size_input_transformer[1]),border_radius=5)
                pygame.draw.rect(self.Window,(10,10,10),(self.VecY_input_transformer[0],self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height(),self.Size_input_transformer[0],self.Size_input_transformer[1]),border_radius=5)            
                text_obj_sizeX = self.font2.render(f'{obj_size[0]}',True,(200,200,200))
                text_obj_sizeY = self.font2.render(f'{obj_size[1]}',True,(200,200,200))
                self.Window.blit(text_obj_sizeX, (self.VecX_input_transformer[0] + text_obj_sizeX.get_width() / 2,self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height() + text_obj_sizeX.get_height()/4))
                self.Window.blit(text_obj_sizeY, (self.VecY_input_transformer[0] + text_obj_sizeY.get_width() / 2,self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height() + text_obj_sizeY.get_height()/4))
            elif obj_type == Types[1]:
                self.Window.blit(self.Ray,(self.VecX_vector_transformer[0],self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height()))
                pygame.draw.rect(self.Window,(10,10,10),(self.VecX_input_transformer[0] + 15,self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height(),self.Size_input_transformer[0],self.Size_input_transformer[1]),border_radius=5)
                text_obj_Ray = self.font2.render(f'{obj_size[0]}',True,(200,200,200))
                self.Window.blit(text_obj_Ray, (self.VecX_input_transformer[0] + 15 + text_obj_Ray.get_width() / 2,self.Vec[1] + 160 - self.transformer_text.get_height() / 2 - 1 + self.Scale_text.get_height() + text_obj_Ray.get_height()/4))           
            elif obj_type not in Types: 
                print('Error (num: 01)')
                
    def render_propieties(self, obj_type, obj_id,obj_size,obj_pos):
        # Desenha a caixa de entrada
        pygame.draw.rect(self.Window, (10, 10, 10), (self.Vec_Inspector[0] + 5, self.Vec_Inspector[1] + 30, self.Size_Inspector[0] - 40, self.Size_Inspector[1]), border_radius=8)
        self.Window.blit(self.cube_img, (self.Vec_img[0], self.Vec_img[1] + 30))

        # Renderizando o tipo de objeto e ID
        text_type = KairosFontRender(f'{obj_type}', self.KF, (255, 255, 255))
        text_id = KairosFontRender(f'ID: {obj_id}', self.KF, (150, 150, 150))
        self.Window.blit(text_id, (self.Vec[0] + self.Size[0] / 2, self.Vec_Inspector[1] + text_id.get_height() / 2 + 28))
        self.Window.blit(text_type, (self.Vec_img[0] + text_type.get_width() / 2 + 5, self.Vec_Inspector[1] + text_type.get_height() / 2 + 28))
        
        # Imagem do nome
        self.Window.blit(self.Name_img, (self.Vec_img[0] + text_type.get_width() / 2 + 5, self.Vec_Inspector[1] + text_type.get_height() + 48))
        self.Window.blit(self.text_name, (self.Vec_img[0] + text_type.get_width() + 10, self.Vec_Inspector[1] + text_type.get_height() + 48))
        # Caixa de input
        # KairosInput(self.Window,self.ColorInput,(12,12,12),(self.Vec[0] + self.Size[0] / 2 - 5, self.Vec_Inspector[1] + text_type.get_height() + 48),(int(self.Size[0] * 0.5), 22),BorderRadius=10)
        self.render_transformer(obj_type,obj_size,obj_pos)
                        
    def render_input(self,obj_name,obj_id):
        input_rect = pygame.Rect(self.Vec[0] + self.Size[0] / 2 - 5, self.Vec_Inspector[1] + 12 + 48, int(self.Size[0] * 0.5), 20)
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        if mouse_pressed[0] and input_rect.collidepoint(mouse_pos):
            self.active = not self.active
            self.ColorInput = (12, 12, 12)
            
        if mouse_pressed[0] and not input_rect.collidepoint(mouse_pos):
            self.active = False
            self.ColorInput = (0, 0, 0)

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN and self.active:
        #         if event.key == pygame.K_RETURN:
        #             # Atualiza o JSON com o novo nome
        #             self.update_object_name_in_json(obj_id,obj_name)
        #             self.input = ''
        #         elif event.key == pygame.K_BACKSPACE:
        #             self.input = self.input[:-1]
        #         else:
        #             if len(self.input) < 15:
        #                 self.input += event.unicode
        
        pygame.draw.rect(self.Window, self.ColorInput, (self.Vec[0] + self.Size[0] / 2 - 5, self.Vec_Inspector[1] + 12 + 48, int(self.Size[0] * 0.5), 22), border_radius=10)               
        self.Window.blit(KairosFontRender(obj_name, self.KF, (255, 255, 255)), (self.Vec[0] + self.Size[0] / 2, self.Vec_Inspector[1] + 14 + 48))
    
    def update_object_name_in_json(self, obj_id, new_name):
        # Carrega os objetos do JSON
        objects = self.config_project.get_objects()
        # Encontra o objeto com o ID correspondente e atualiza o nome
        for obj in objects:
            if obj['indece'] == obj_id:
                obj['name'] = new_name
                break
        # Salva de volta no arquivo JSON
        self.config_project.save_config()
                    
    def render_not_prop(self):
        text_not_select = KairosFontRender('Nothing Selected',self.KF,(255,255,255))
        self.Window.blit(text_not_select, (self.Vec_img[0] + text_not_select.get_width() / 2 + 5,self.Vec_Inspector[1] + text_not_select.get_height()/2 + 28))
    
    def render(self):
        if self.visible:
            self.update_size_position()
            self.collision_gui()
            pygame.draw.rect(self.Window, self.Color, (*self.Vec, *self.Size))
            self.render_top_Data_objs()

class Assents_OBJS: 
    def __init__(self, Window, data_objs):
        self.visible = True
        self.data_objs = data_objs 
        self.Window = Window 
        self.console_api = Console(self.Window,self.data_objs)
        self.console_api.addMensageBank('Mensage','Kairos Engine v0.0.1B Stable.Official (py) 2024 - ????, Marcos Antônio')
        self.console_api.addMensageBank('Kairos', '--- Pygame Server Started ---')
        self.Color = [34, 34, 34]
        self.Color_console = [10,10,10]
        self.Color_assents = [26,26,26]
        self.ColorOutput = [22, 22, 22]
        self.ColorClearOutput = [51,51,51]
        self.Color_inspector = [60, 60, 60]
        self.font = pygame.font.SysFont('Arial', 12)
        self.text_surface = self.font.render('Assent Browser', True, (255, 255, 255))
        self.text_surface2 = self.font.render('Console', True, (255, 255, 255))
        self.text_Clear = self.font.render('Clear',True, (255,255,255))
        self.folderAddImg = pygame.image.load('./Assents/add-folder.png')
        self.folderImg = pygame.image.load('./Assents/pasta (2).png')
        self.redimensionar_img = pygame.image.load('./Assents/redimensionar.png')
        self.icon1 = pygame.image.load('./Assents/folder (2).png')
        self.icon1 = pygame.transform.scale(self.icon1, (16,16))
        self.icon2 = pygame.image.load('./Assents/command-line.png')
        self.icon2 = pygame.transform.scale(self.icon2, (16,16))
        self.folderImg = pygame.transform.scale(self.folderImg, (64, 64))
        self.close = pygame.image.load('./Assents/close (2).png')
        self.close = pygame.transform.scale(self.close,(8,8))
        self.visibleOpçoes = 'Console'
        self.red_visible = False
        self.mouse_dragging = False
        self.dragging_start_pos = None
        self.start_size = None
        self.update_size_positions()
    
    def update_size_positions(self):
        if self.visible:
            self.data_objs.update_size_position()
            data_objs_size = self.data_objs.Size

            self.Spacing_UI = 2
            self.Size = [self.Window.get_width() - data_objs_size[0] - self.Spacing_UI, int(self.Window.get_height() * 0.25)]
            self.Vec = [0, self.Window.get_height() - self.Size[1]]
           
            self.Size_Assenst = [int(self.Size[0] * 0.08), int(self.Size[1] * 0.14)]
            self.Vec_text = [self.Vec[0] + 4, self.Vec[1] + 4]
            self.Vec_2 = [self.Vec[0] + self.Size_Assenst[0] + 3, self.Vec[1]]
            self.Vec_text2 = [self.Vec_2[0] + 4, self.Vec[1] + 4]

            # self.VecOutput = [self.Vec[0], self.Vec[1]]
            # self.SizeOutput = [self.Size[0], self.Size[1]]
            
            self.Vec_red = [self.Size[0] / 2, self.Vec[1]]
            
            self.side_bar = [self.Size[0],int(self.Size[1] * 0.13)]
            self.size_assents_bar = [int(self.Size[0] * 0.1),self.side_bar[1]]
            self.size_assents_bar2 = [int(self.Size[0] * 0.13),self.side_bar[1]]
        else:
            self.Size = [0, 0]
    
    def CollisionGUI(self):
        self.update_size_positions()
        console_rect = pygame.Rect(self.Vec[0] + self.size_assents_bar[0],self.Vec[1],self.size_assents_bar2[0],self.size_assents_bar2[1])
        assents_rect = pygame.Rect(self.Vec[0],self.Vec[1],self.size_assents_bar[0],self.size_assents_bar[1])
        close_rect = pygame.Rect(self.Vec[0] + self.Size[0] - 20,self.Vec[1] + 7,self.close.get_width(),self.close.get_height())
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        if mouse_pressed[0] and close_rect.collidepoint(mouse_pos):
            self.visible = False
        
        if mouse_pressed[0] and console_rect.collidepoint(mouse_pos): 
            self.visibleOpçoes = "Folders"
            self.Color_assents = [10,10,10]
            self.Color_console = [26,26,26]
        elif mouse_pressed[0] and assents_rect.collidepoint(mouse_pos): 
            self.visibleOpçoes = "Console"
            self.Color_assents = [26,26,26]
            self.Color_console = [10,10,10]
        
    def renderTopItens(self): 
        pygame.draw.rect(self.Window,(19,19,19),(self.Vec,self.side_bar))
        pygame.draw.rect(self.Window,self.Color_assents,(self.Vec,self.size_assents_bar))
        pygame.draw.rect(self.Window,self.Color_console,(self.Vec[0] + self.size_assents_bar[0],self.Vec[1],self.size_assents_bar2[0],self.size_assents_bar2[1]))
        self.Window.blit(self.icon2, (self.Vec[0] + 10,self.Vec[1] + 4))
        self.Window.blit(self.icon1, (self.Vec[0] + self.size_assents_bar[0] + 10,self.Vec[1] + 4))
        self.Window.blit(self.text_surface2, (self.Vec[0] + 30,self.Vec[1] + 6))
        self.Window.blit(self.text_surface, (self.Vec[0] + self.size_assents_bar[0] + 40,self.Vec[1] + 6))
        self.Window.blit(self.close,(self.Vec[0] + self.Size[0] - 20,self.Vec[1] + 7))

    def renderConsole(self):
        self.console_api.Show()
        
    def renderFolder(self):
        spacing = 0
        spacingH = 0
        max_width = self.Size[0] - 20  
        folder_width = self.folderImg.get_width() + 10  
    
        for folders in range(5):
            if spacing + folder_width > max_width:  
               spacing = 0
               spacingH += self.folderImg.get_height() + 10
        
            self.Window.blit(self.folderImg, (self.Vec[0] + 10 + spacing, self.Vec[1] + 40 + spacingH))
            spacing += folder_width  
    
        # self.Window.blit(self.folderAddImg, (self.Size[0] - self.folderAddImg.get_width() - 10, self.Vec[1] + 10))
    
    def render(self):
        if self.visible:
            self.CollisionGUI()
            pygame.draw.rect(self.Window, self.Color, (self.Vec[0], self.Vec[1], self.Size[0], self.Size[1]))
            if self.visibleOpçoes == 'Folders':
              self.renderFolder()
            else: 
              self.renderConsole()
              
            self.renderTopItens()

class List_OBJS:
    def __init__(self, Window, Assents_OBJS,DATA_OBJ):
        self.config = ConFig()
        config_path = self.config.get_project_path()
        config_name = self.config.get_project_name()
        dentro_do_path = os.path.join(config_path,config_name)
        self.config_project = ProjectConfig(dentro_do_path)
        
        self.Assents_gui = Assents_OBJS
        self.DATA_OBJ = DATA_OBJ
        self.Window = Window
        self.Color = [34, 34, 34]
        self.Color_inspector = [80, 80, 80]
        self.Color_addOBJ = [50,50, 50]
        self.console_api = Console(self.Window,self.DATA_OBJ)
        self.font = pygame.font.SysFont('Arial', 12)
        self.text_surface = self.font.render('Scene Graph', True, (255, 255, 255))
        self.text_surface_Square = self.font.render('Square', True, (255, 255, 255))
        self.text_surface_Circle = self.font.render('Circle', True, (255, 255, 255))
        self.text_surface_triangle = self.font.render('Triangle', True, (255, 255, 255))
        self.text_creating_sceen = self.font.render('Create a Main Sceen',True,(255,255,255))
        self.text_surface_Camera = self.font.render('Camera', True, (255, 255, 255))
        self.addOBJ_img = pygame.image.load('./Assents/plus.png')
        self.view_img = pygame.image.load('./Assents/view.png')
        self.hiden = pygame.image.load('./Assents/hidden.png')
        self.addOBJ_img = pygame.transform.scale(self.addOBJ_img, (14,14))
        self.closeImg = pygame.image.load('./Assents/close.png')
        self.closeImg = pygame.transform.scale(self.closeImg, (9,9))
        self.lixeira = pygame.image.load('./Assents/trash.png')
        self.cube = pygame.image.load('./Assents/BoxMesh.svg')
        self.circle = pygame.image.load('./Assents/CircleShape2D.svg')
        self.cam = pygame.image.load('./Assents/videocam (1).png')
        self.cam = pygame.transform.scale(self.cam,(16,16))
        self.mash_icon_list = pygame.image.load('./Assents/rectangle.png')
        self.mash_icon_list = pygame.transform.scale(self.mash_icon_list, (14,14))
        self.close_2 = pygame.image.load('./Assents/close (2).png')
        self.close_2 = pygame.transform.scale(self.close_2,(8,8))
        self.visible = True
        self.PPD_visible = False
        self.view_img_select = True
        self.visibleSetOBJ = False
        self.Mouse_pressed = False
        self.scroll_offset = 0
        self.visible_objects = []
        self.max_visible_items = 17
        
        self.obj_id_select = None
        self.obj_type_select = None
        self.obj_name_select = None
        self.obj_visible_select = None
        self.obj_size_select = None
        self.obj_position_select = None 
        self.rect_obj_select = 0
        self.clicked = False
        self.create_main_sceen = True
        self.clicked2 = False
        self.update_size_positions()

    def update_size_positions(self):
        self.Assents_gui.update_size_positions()
        self.DATA_OBJ.update_size_position()
        data_objs_size = self.DATA_OBJ.Size
        self.Spacing_UI = 2
        Assents_Size = self.Assents_gui.Size
        DataOBJ_size = self.DATA_OBJ.Size
        if self.visible:
            self.Size = [int(self.Window.get_width() * 0.2), self.Window.get_height() - Assents_Size[1] - self.Spacing_UI - 24]
        else:
            self.Size = [0, 0]
        
        self.Size_console = [self.Window.get_width() - data_objs_size[0] - self.Spacing_UI, int(self.Window.get_height() * 0.25)]
        self.Vec_console = [0, self.Window.get_height() - self.Size[1]]
        
        self.Size_game_sceen = [
            self.Window.get_width() - self.Size[0] - DataOBJ_size[0] - self.Spacing_UI * 2,
            self.Window.get_height() - Assents_Size[1] - self.Spacing_UI - 24
        ]
        self.Vec = [0, 24]

        self.Vec_Inspector = [self.Vec[0], 0]
        self.Size_Inspector = [int(self.Size[0] * 0.55), int(self.Size[1] * 0.1)]
        

        self.Vec_text = [self.Vec_Inspector[0] + 35, self.Vec_Inspector[1] + 6]
        self.Vec_imgADD = [self.Vec_Inspector[0] + self.Size_Inspector[0] - self.addOBJ_img.get_width() - 10, self.Vec_Inspector[1] + 5]
        self.Size_SetOBJ = [int(self.Size[0] * 0.5), int(self.Size[1] * 0.3)]
        self.Vec_SetOBJ = [self.Vec_Inspector[0] + 15, self.Vec_Inspector[1] + self.Size_Inspector[1]]

        self.VecCubeAdd = [self.Vec_SetOBJ[0] + 10,self.Vec_SetOBJ[1]+10]
        self.VecEsferaAdd = [self.Vec_SetOBJ[0] + 10,self.VecCubeAdd[1] + 22]
        self.VecTriangulo = [self.Vec_SetOBJ[0] + 10,self.VecEsferaAdd[1] + 22]
        self.Vec_Cam = [self.Vec_SetOBJ[0] + 10,self.VecTriangulo[1] + 22]

        self.Vec_Square =  [self.VecCubeAdd[0] + self.cube.get_width() + 5,self.VecCubeAdd[1] + 2]
        self.Vec_Circle = [self.VecEsferaAdd[0] + self.cube.get_width() + 5,self.VecEsferaAdd[1] + 2]
        self.Vec_triangulo = [self.VecTriangulo[0] + self.cube.get_width() + 5,self.VecTriangulo[1] + 2]
        self.VecCam = [self.Vec_Cam[0] + self.cam.get_width() + 5,self.Vec_Cam[1] + 2]
        
        self.list_area = pygame.Rect(self.Vec[0], self.Vec[1], self.Size[0], self.Size[1])
        
        self.Vec_icon_mash = [self.Vec_Inspector[0] + 10,self.Vec_Inspector[1] + 4]
        self.Vec_close_2 = [self.Size[0] - 20,7]
        #Vecs for list objs
        # self.cube_list_vec = [10,self.Size_Inspector[1] + self.cube.get_height()]

    def render_top_Data_objs(self):
        if self.visible:
            self.update_size_positions()
            pygame.draw.rect(self.Window,(19,19,19), (0,0,self.Size[0],24))
            pygame.draw.rect(self.Window, self.Color, (*self.Vec_Inspector, *self.Size_Inspector))
            self.Window.blit(self.mash_icon_list, (self.Vec_icon_mash))
            self.Window.blit(self.text_surface, (self.Vec_text))
            self.Window.blit(self.addOBJ_img, (self.Vec_imgADD))
            self.Window.blit(self.close_2, (self.Vec_close_2))
        else: 
           pass

    def renderSetNewOBJ(self):
        pygame.draw.rect(self.Window, self.Color_addOBJ, (*self.Vec_SetOBJ, *self.Size_SetOBJ),border_radius=5)
        self.Window.blit(self.closeImg, (self.Size_SetOBJ[0] - self.closeImg.get_width(),self.Vec_SetOBJ[1]+10))
        
        self.Window.blit(self.text_surface_Square, (self.Vec_Square))
        self.Window.blit(self.text_surface_Circle, (self.Vec_Circle))
        self.Window.blit(self.text_surface_triangle, (self.Vec_triangulo))
        self.Window.blit(self.text_surface_Camera, (self.VecCam))

    def renderDataObjs(self):
        self.update_size_positions()
        objects = self.config_project.get('objects', [])
        spacing = 0

        # Calcular a altura total e visível
        total_height = len(objects) * (self.cube.get_height() + 5)
        visible_height = self.Size[1] - 40

        # Pegar a posição do mouse
        mouse_pos = pygame.mouse.get_pos()

        # Manipular eventos de rolagem do mouse, se o mouse estiver sobre a área da lista
        for event in pygame.event.get():
            if event.type == pygame.MOUSEWHEEL and self.list_area.collidepoint(mouse_pos):
                self.scroll_offset += event.y * 10  # Ajustar a velocidade de rolagem
                # Garantir que o scroll offset esteja dentro do intervalo válido
                max_scroll = visible_height - total_height
                self.scroll_offset = max(self.scroll_offset, max_scroll)
                self.scroll_offset = min(self.scroll_offset, 0)

        # Atualizar a lista de objetos visíveis com base no scroll offset
        start_index = max(0, -self.scroll_offset // (self.cube.get_height() + 5))
        end_index = min(start_index + self.max_visible_items, len(objects))
    
        # Garantir que os índices estejam dentro dos limites válidos
        self.visible_objects = [i for i in range(start_index, end_index) if 0 <= i < len(objects)]

        # Renderizar os objetos com espaçamento e rolagem corretos
        y_position = self.Vec_Inspector[1] + 40 + spacing + self.scroll_offset
        if not objects:
            self.Window.blit(self.text_creating_sceen,(self.Vec_Inspector[0] + 40, y_position + 2))
        else:
            for i in self.visible_objects:
                if i >= len(objects):
                    continue  # Ignorar índices fora do intervalo
        
                obj = objects[i]
                obj_name_p = obj.get('name', 'Unknown')
                obj_type = obj.get('type', 'Unknown')
                obj_id = obj.get('indece', 'Unknown')
                obj_visible = obj.get('visible_in_sceen','Unknown')
                obj_size = obj.get('size','Unknown')
                obj_pos = obj.get('position','Unknown')

                # Apenas renderizar objetos que estão dentro do intervalo visível
                if y_position + self.cube.get_height() > self.Vec_Inspector[1] + 50 and y_position < self.Vec_Inspector[1] + visible_height:
                    obj_name = self.font.render(f'{obj_name_p}', True, (255, 255, 255))
                    
                    match obj_type:
                        case 'Square': 
                            self.Window.blit(self.cube, (self.Vec_Inspector[0] + 20, y_position))
                        case 'Circle':
                            self.Window.blit(self.circle, (self.Vec_Inspector[0] + 20, y_position))
                        case 'Triangle': 
                            pass
                        case _:
                            print('Error (num: 01)')
                        
                    self.Window.blit(obj_name, (self.Vec_Inspector[0] + 40, y_position + 2))
            
                    mouse_clicked = pygame.mouse.get_pressed()
                    object_rect = pygame.Rect(self.Vec_Inspector[0] + 20, y_position, self.Size[0] - 20, self.cube.get_height())
                    object_rect_select = (self.Vec_Inspector[0] + 10, y_position - 5, self.Size[0] - 20, self.cube.get_height() + 10)
                    if mouse_clicked[0] and object_rect.collidepoint(mouse_pos):
                        self.obj_type_select = obj_type
                        self.obj_id_select = obj_id
                        self.obj_name_select = obj_name_p
                        self.obj_visible_select = obj_visible
                        self.obj_size_select = obj_size
                        self.obj_position_select = obj_pos
                        self.PPD_visible = True

                        if self.rect_obj_select != object_rect_select:
                            self.rect_obj_select = object_rect_select
                
                    # elif mouse_clicked[2] and object_rect.collidepoint(mouse_pos):
                    #     pass
            
                y_position += self.cube.get_height() + 10    
    
    def PPD(self): 
        if self.PPD_visible:
            self.DATA_OBJ.render_propieties(self.obj_type_select,self.obj_id_select,self.obj_size_select,self.obj_position_select)
            self.DATA_OBJ.render_input(self.obj_name_select,self.obj_id_select)
        else:
            self.DATA_OBJ.render_not_prop()
            
    def collisionsGUI(self):
        self.update_size_positions()
        mouse = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        close_2_rect = pygame.Rect(self.Size[0] - 20,7,self.close_2.get_width(),self.close_2.get_height())
        
        if mouse_press[0] and close_2_rect.collidepoint(mouse): 
            self.visible = False
    
        # Verifica se o mouse está pressionado
        if not mouse_press[0]:
           self.Mouse_pressed = False

        close_rect = pygame.Rect(self.Vec_imgADD[0], self.Vec_imgADD[1], self.addOBJ_img.get_width(), self.addOBJ_img.get_height())
        list_gui_rect = pygame.Rect(self.Vec[0],self.Vec[1],self.Size[0],self.Size[1])
        area_rect = pygame.Rect(self.Vec_SetOBJ[0],self.Vec_SetOBJ[1] ,self.Size_SetOBJ[0],self.Size_SetOBJ[1])
        if close_rect.collidepoint(mouse) and mouse_press[0]:
           self.visibleSetOBJ = True
           
        if mouse_press[2] and list_gui_rect.collidepoint(mouse): 
            self.visibleSetOBJ = True
            
        if self.visibleSetOBJ:
            sair_rect = pygame.Rect(self.Size_SetOBJ[0] - self.closeImg.get_width(), self.Vec_SetOBJ[1] + 10, self.closeImg.get_width(), self.closeImg.get_height())
            if sair_rect.collidepoint(mouse) and mouse_press[0]:
               self.visibleSetOBJ = False
            
            if not area_rect.collidepoint(mouse) and not close_rect.collidepoint(mouse) and mouse_press[0]:
                self.visibleSetOBJ = False
            
            # Adicionar objeto ao jogo e cena
            cube_text_rect = self.text_surface_Square.get_rect()
            cube_add_button = pygame.Rect(
                self.VecCubeAdd[0],self.VecCubeAdd[1],
                self.cube.get_width() + cube_text_rect.width,
                max(self.cube.get_height(), cube_text_rect.height)
            )
            circle_text_rect = self.text_surface_Circle.get_rect()
            circle_add_button = pygame.Rect( 
                self.VecEsferaAdd[0],self.VecEsferaAdd[1],
                self.cube.get_width() + circle_text_rect.width,
                max(self.cube.get_height(),cube_text_rect.height)
            )
            triangle_text_rect = self.text_surface_triangle.get_rect()
            triangle_add_button = pygame.Rect( 
                self.VecTriangulo[0],self.VecTriangulo[1],
                self.cube.get_width() + triangle_text_rect.width,
                max(self.cube.get_height(),triangle_text_rect.height)
            )
            if mouse_press[0]:
                if cube_add_button.collidepoint(mouse) and not self.Mouse_pressed:
                    posX = randint(0 + self.Size[0] + 50,self.Window.get_width() - self.DATA_OBJ.Size[0] - 50)
                    posY = randint(100,self.Window.get_height() - self.Assents_gui.Size[1] - 50)
                    new_cube = {
                      'type': 'Square',
                      'name': 'Square',
                      'visible_in_sceen': True,
                      'position':[posX,posY],
                      'size': [50, 50],
                      'color': [255, 255, 255],
                      'indece': 0 
                    } 
                    self.config_project.add_object(new_cube)
                    # add conteudo ao console 
                    
                    self.Mouse_pressed = True
                if circle_add_button.collidepoint(mouse) and not self.Mouse_pressed:
                    posX = randint(0 + self.Size[0] + 50,self.Window.get_width() - self.DATA_OBJ.Size[0] - 50)
                    posY = randint(100,self.Window.get_height() - self.Assents_gui.Size[1] - 50)
                    new_circle = { 
                        'type': 'Circle',
                        'name': 'Circle',
                        'visible_in_sceen': True,
                        'position': [posX,posY],
                        'size': [50],
                        'color': [255,255,255], 
                        'indece': 0
                    }
                    self.config_project.add_object(new_circle)
                    self.Mouse_pressed = True
                if triangle_add_button.collidepoint(mouse) and not self.Mouse_pressed and not self.create_main_sceen: 
                    new_triangle = { 
                        'type': 'Triangle',
                        'name': 'Triangle',
                        'visible_in_sceen': True,
                        'position': [500,250], 
                        'size': [50,50],
                        'color': [255,255,255],
                        'indece': 0
                    }
                    self.config_project.add_object(new_triangle)
                    self.Mouse_pressed = True
        
        if self.PPD_visible: 
            x = self.rect_obj_select[0] + self.Size[0] - 5 - self.view_img.get_width() * 4
            y = self.rect_obj_select[1] + self.cube.get_height() / 2 - 2
            lixeira_rect = pygame.Rect(x + self.lixeira.get_width() + 10, y, self.lixeira.get_width(), self.lixeira.get_height())
            view_rect = pygame.Rect(x,y,self.view_img.get_width(),self.view_img.get_height())
            
            if mouse_press[0]:
                if not self.clicked2: 
                    if lixeira_rect.collidepoint(mouse):
                        self.config_project.delete_object(self.obj_id_select)
                        self.PPD_visible = False
                    self.clicked2 = True
            else:
                self.clicked2 = False
            
            if mouse_press[0]:
                if not self.clicked:
                    if view_rect.collidepoint(mouse):
                        self.config_project.change_visible_obj(self.obj_id_select)
                    self.clicked = True
            else: 
                self.clicked = False
                
    def render_backgroundSceen(self):
        #background de cores rgb 
        color_top : tuple[int,int,int] = (20,168,255)
        color_bottom: tuple[int,int,int] = (200,200,200) 
        
        KairosBackgroundSceen(self.Size_game_sceen,self.DATA_OBJ.Size[0],self.Spacing_UI,self.Size[0] + self.Spacing_UI,self.Size_Inspector[1] - self.Spacing_UI,self.Window,color_top,color_bottom) 
    
    def render_sceen(self):
        objs_for_scene =  self.config_project.get('objects', [])

        for obj in objs_for_scene:
            # Modificar os dados do objeto para a cena
            new_data = change_data_for_scene(obj, (800, 500), self.Size_game_sceen)
            # Renderizar o objeto usando Pygame ou OpenGL
            compile_data_for_scene(self.Window, new_data,self.Size_game_sceen,self.DATA_OBJ.Size[0])
    
    def render(self):
        self.render_sceen()
        if self.visible:
            self.update_size_positions()
            self.collisionsGUI()
            pygame.draw.rect(self.Window, self.Color, (*self.Vec, *self.Size))
            self.render_top_Data_objs()
            if self.visibleSetOBJ:
                self.renderSetNewOBJ()
            else:
                if self.PPD_visible:
                    pygame.draw.rect(self.Window,(80,80,80), (self.rect_obj_select))
                    x = self.rect_obj_select[0] + self.Size[0] - 5 -self.view_img.get_width() * 4
                    y = self.rect_obj_select[1] + self.cube.get_height() / 2 - 2
                    self.Window.blit(self.lixeira,(x + self.lixeira.get_width() + 10,y))
                    if  self.obj_visible_select:
                        self.Window.blit(self.view_img,(x,y))
                    else: 
                        self.Window.blit(self.hiden,(x,y))
                    
                self.renderDataObjs()
        self.PPD()        

class Top_bars: 
    def __init__(self, Window, List_OBJ, DATA_OBJ, ASSENTS_OBJ):
        self.LIST_OBJ = List_OBJ
        self.DATA_OBJ = DATA_OBJ
        self.ASSENTS_OBJ = ASSENTS_OBJ
        self.font = pygame.font.SysFont('Arial',12)
        self.text_inspector = self.font.render('2D View',True,(240,240,240))
        self.close = pygame.image.load('./Assents/close (2).png')
        self.tabs_icon = pygame.image.load('./Assents/menu.png')
        self.img_prop = pygame.image.load('./Assents/cube (2).png')
        self.assents_icon = pygame.image.load('./Assents/pasta.png')
        self.assents_icon = pygame.transform.scale(self.assents_icon, (16,16))
        self.view_img = pygame.image.load('./Assents/view.png')
        self.hiden = pygame.image.load('./Assents/hidden.png')
        self.img_prop = pygame.transform.scale(self.img_prop, (16,16))
        self.img_list= pygame.image.load('./Assents/rectangle.png')
        self.img_list = pygame.transform.scale(self.img_list, (16,16))
        self.tabs_icon = pygame.transform.scale(self.tabs_icon, (12,12))
        self.tabs_text = self.font.render('Tabs',True,(255,255,255))
        self.prop_text = self.font.render('Properties',True,(255,255,255))
        self.list_text = self.font.render('Scene Graph',True,(255,255,255))
        self.assents_text = self.font.render('Assents',True,(255,255,255))
        self.close = pygame.transform.scale(self.close,(8,8))
        self.visible = True
        self.cliked = False
        self.cliked2 = False
        self.color_inspector_1 = (0,160,240)
        self.color_inspector_2 = (26,26,26)
        self.Window = Window
        self.tabs_visible = False
        self.update_size_position()
    
    def update_size_position(self):
        self.LIST_OBJ.update_size_positions()
        self.DATA_OBJ.update_size_position()
        self.ASSENTS_OBJ.update_size_positions()
        ListOBJ_size = self.LIST_OBJ.Size
        DataOBJ_size = self.DATA_OBJ.Size
        self.Spacing_UI = 2
        self.Vec = [ListOBJ_size[0] + self.Spacing_UI, 24]
        if self.visible:
            self.Size = [
                self.Window.get_width() - ListOBJ_size[0] - DataOBJ_size[0] - self.Spacing_UI * 2]
        else:
            self.Size = [0]
        self.Vec_bar = [self.Vec[0] - self.Spacing_UI,0]
        self.Size_bar = [self.Size[0] + self.Spacing_UI * 2,24]
        self.Vec_inpector = [self.Vec_bar[0] + self.Spacing_UI,self.Vec_bar[1]]
        self.Size_inspector =[int(self.Window.get_width() * 0.06),self.Size_bar[1]]
        if self.tabs_visible:
            self.Size_inspector2 = [int(self.Window.get_width() * 0.1),150]
        else:
            self.Size_inspector2 = [int(self.Window.get_width() * 0.06),self.Size_bar[1]]
        self.Vec_inpector2 = [self.Vec_inpector[0] + self.Size_inspector[0],self.Vec_inpector[1]]
    
    def collisions(self): 
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        mash_collision_inspector_1 = pygame.Rect(self.Vec_bar[0] + self.Spacing_UI,self.Vec_bar[1],int(self.Window.get_width() * 0.06),self.Size_bar[1])
        mash_collision_inspector_2 = pygame.Rect(self.Vec_inpector[0] + self.Size_inspector[0],self.Vec_bar[1],int(self.Window.get_width() * 0.06),self.Size_bar[1])
        mash_view_1_ = pygame.Rect(self.Vec_inpector2[0] + self.Size_inspector2[0] - 25,self.Vec_inpector2[1] + 24 + 5,self.view_img.get_width(),self.view_img.get_height())
        mash_view_2_ = pygame.Rect(self.Vec_inpector2[0] + self.Size_inspector2[0] - 25,self.Vec_inpector2[1] + 24 + 30,self.view_img.get_width(),self.view_img.get_height())
        mash_view_3_ = pygame.Rect(self.Vec_inpector2[0] + self.Size_inspector2[0] - 25,self.Vec_inpector2[1] + 24 + 55,self.view_img.get_width(),self.view_img.get_height())
        
        if mouse_pressed[0] and mash_collision_inspector_1.collidepoint(mouse_pos):
            self.color_inspector_1 = (0,160,240)
            self.color_inspector_2 = (26,26,26)
            self.tabs_visible = False
        if mouse_pressed[0] and mash_collision_inspector_2.collidepoint(mouse_pos):
            self.color_inspector_2 = (0,160,240)
            self.color_inspector_1 = (26,26,26)
            self.tabs_visible = True
                    
        if self.tabs_visible and mouse_pressed[0]:
            if not self.cliked2:
                if mash_view_1_.collidepoint(mouse_pos):
                    if not self.DATA_OBJ.visible:
                        self.DATA_OBJ.visible = True
                    else:
                        self.DATA_OBJ.visible = False
                self.cliked2 = True
                
            elif not self.cliked:
                if mash_view_3_.collidepoint(mouse_pos): 
                    if self.ASSENTS_OBJ.visible: 
                        self.ASSENTS_OBJ.visible = False
                    else: 
                        self.ASSENTS_OBJ.visible = True
                self.cliked = True
            
            elif  mash_view_2_.collidepoint(mouse_pos):
                if self.LIST_OBJ.visible:
                    self.LIST_OBJ.visible = False
                else: 
                    self.LIST_OBJ.visible = True
        else: 
            self.cliked = False
            self.cliked2 = False
                        
    
    def render(self):
        self.update_size_position()
        self.collisions()
        pygame.draw.rect(self.Window, (19,19,19),(self.Vec_bar,self.Size_bar))
        pygame.draw.rect(self.Window,self.color_inspector_1,(self.Vec_inpector,self.Size_inspector))
        pygame.draw.rect(self.Window,self.color_inspector_2,(self.Vec_inpector2,self.Size_inspector2))
        self.Window.blit(self.text_inspector, (self.Vec_inpector[0] + 10,self.Vec_inpector[1] + self.text_inspector.get_height()/2))
        self.Window.blit(self.tabs_icon, (self.Vec_inpector2[0] + 5,self.Vec_inpector2[1] + 7))
        self.Window.blit(self.tabs_text, (self.Vec_inpector2[0] + 30,self.Vec_inpector2[1] + self.tabs_text.get_height()/2))
        if self.tabs_visible:
            self.Window.blit(self.img_prop,(self.Vec_inpector2[0] + 5,self.Vec_inpector2[1] + 24 + 5))
            self.Window.blit(self.img_list,(self.Vec_inpector2[0] + 5,self.Vec_inpector2[1] + 24 + 30))
            self.Window.blit(self.assents_icon,(self.Vec_inpector2[0] + 5,self.Vec_inpector2[1] + 24 + 55))
            self.Window.blit(self.prop_text,(self.Vec_inpector2[0] + 25,self.Vec_inpector2[1] + 24 + 5))
            self.Window.blit(self.list_text,(self.Vec_inpector2[0] + 25,self.Vec_inpector2[1] + 24 + 30))
            self.Window.blit(self.assents_text,(self.Vec_inpector2[0] + 25,self.Vec_inpector2[1] + 24 + 55))
            
            if self.LIST_OBJ.visible:
                self.Window.blit(self.view_img, (self.Vec_inpector2[0] + self.Size_inspector2[0] - 25,self.Vec_inpector2[1] + 24 + 30))
            else:
                self.Window.blit(self.hiden, (self.Vec_inpector2[0] + self.Size_inspector2[0] - 25,self.Vec_inpector2[1] + 24 + 30))
            if self.DATA_OBJ.visible: 
                self.Window.blit(self.view_img, (self.Vec_inpector2[0] + self.Size_inspector2[0] - 25,self.Vec_inpector2[1] + 24 + 5))         
            else:       
                self.Window.blit(self.hiden, (self.Vec_inpector2[0] + self.Size_inspector2[0] - 25,self.Vec_inpector2[1] + 24 + 5))
            if self.ASSENTS_OBJ.visible: 
                self.Window.blit(self.view_img, (self.Vec_inpector2[0] + self.Size_inspector2[0] - 25,self.Vec_inpector2[1] + 24 + 55))
            else:
                self.Window.blit(self.hiden, (self.Vec_inpector2[0] + self.Size_inspector2[0] - 25,self.Vec_inpector2[1] + 24 + 55))
