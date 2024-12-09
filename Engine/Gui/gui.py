import pygame
import os
import shutil
from Config.config import *
from Config.config_engine import *
import tkinter as tk
from tkinter import filedialog
from Gui.forms_gui import *

class Settings: 
    def __init__(self,WINDOW):
        self.WINDOW = WINDOW
        
        self.Size = [self.WINDOW.get_width(),120]
        self.Vecs = [0,0]

        #imgs
        self.Background_img = pygame.image.load('./Assents/Cave.png')
        self.Background_img = pygame.transform.scale(self.Background_img,(self.Size))
        self.Engine_img = pygame.image.load('./Assents/Engine2.png')
        
        #font
        self.font = pygame.font.SysFont('Arial',22,bold=True)
        self.Engine_name = self.font.render('KAIROS',True, (255,255,255))

    def render(self): 
        self.WINDOW.blit(self.Background_img, (self.Vecs))

class SetNewObj:
    def __init__(self, WINDOW):
        self.config = Config()
        self.Config = ConFig()
        self.WINDOW = WINDOW
        self.Color = (10, 10, 10)
        self.Color_input = (21, 21, 21)
        self.Color2 = (71, 71, 71)
        self.input_color_text = (230,230,230)
        self.Size = [120, 120]
        self.Size2 = [470, 250]
        self.Size3 = [230, 25]
        self.Vecs = [10, 140]

        # Fonte
        self.font = pygame.font.SysFont('Arial', 14, bold=True)
        self.font_2_ = pygame.font.SysFont('Arial', 12, bold=True)
        self.add_text = self.font.render('New Project', True, (255, 255, 255))
        self.text = self.font_2_.render('Create a New Project', True, (230, 230, 230))
        self.text2 = self.font_2_.render('Project Name', True, (230, 230, 230))
        self.text3 = self.font_2_.render('Project Path', True, (230, 230, 230))
        self.text5 = self.font.render('Cancel', True, (230, 230, 230))
        self.text6 = self.font.render('Create Project', True, (230,230,230))
        self.text_open = self.font_2_.render('Open Project: Mouse[0]',True,(230,230,230))
        self.text_rename = self.font_2_.render('Change Project Mouse[2]',True, (230,230,230))
        self.text_delete = self.font_2_.render('Delete Project Key[D]',True,(230,230,230))
        self.delete_text= self.font.render('DELETE',True,(230,230,230))
        self.text7 = self.font_2_.render('Change Your Project Data',True,(230,230,230))
        self.text8 = self.font.render('Change Project',True,(230,230,230))

        # Imagens
        self.plus = pygame.image.load('./Assents/mais.png')
        self.plus_h2 = pygame.transform.scale(self.plus, (26, 26))
        self.folder = pygame.image.load('./Assents/pasta.png')
        self.folder_2_ = pygame.transform.scale(self.folder, (22, 22))
        self.verificado = pygame.image.load('./Assents/ok.png')
        self.verificado = pygame.transform.scale(self.verificado, (18,18))
        self.close = pygame.image.load('./Assents/close (2).png')
        self.close = pygame.transform.scale(self.close, (12,12))
        self.change = pygame.image.load('./Assents/refresh.png')
        
        #config
        self.scroll_offset = 0
        self.max_visible_items = 5
        self.visible = False
        self.active = False
        self.input = ''
        self.user_direct = os.path.expanduser("~")
        self.local_padrao = os.path.join(self.user_direct, "desktop")
        self.folder_caminho = self.local_padrao
        self.path_change_data = None

        #config avançadas
        self.config_visible = False
        self.config_2_visible = False
        self.delete_visible = False
        self.charge_visible = False
        self.name_delet = None
        self.project_name = None
        self.open_project_data_name = None
        self.open_project_data_path = None
        self.path_change = None
        self.old_path = None
        self.Vecs_config = [None,None]
        self.Size_config = [50,150]
        self.Size_config_two = [170,100]
        self.Size_Triangle = 2.5
        self.Gui_Forms = Gui_Forms()
        self.state = False
        self.dragging = False
        self.rect_width, self.rect_height = 200, 100
        self.rect_x = self.WINDOW.get_width() / 2 - self.rect_width / 2
        self.rect_y = self.WINDOW.get_height() / 2 - self.rect_height / 2
        self.error_box = False
        self.error_mensage = None
        self.pressed = False
        self.name_project_mouse_passed = ''
        self.path_project_mouse_passed = ''
        self.active3 = False

    def inputs(self):
        text_surface = self.font_2_.render(self.input, True, self.input_color_text)
        pygame.draw.rect(self.WINDOW, self.Color_input, (self.WINDOW.get_width()/2, self.Vecs[1] + self.Size3[1] + 10, self.Size3[0], self.Size3[1]), border_radius=10)
        self.WINDOW.blit(text_surface, (self.WINDOW.get_width()/2 + 10, self.Vecs[1] + self.Size3[1] + 16))
        pygame.draw.rect(self.WINDOW, (200, 200, 200), (self.WINDOW.get_width()/2, self.Vecs[1] + self.Size3[1] + 45, self.Size3[0], self.Size3[1]), border_radius=6)
        self.Gui_Forms.draw_Form1(self.WINDOW,(0,0,0),self.Size_Triangle,self.WINDOW.get_width()/2 + self.Size3[0]- 6 * 2,self.Vecs[1] + self.Size3[1] + 45 + self.Size_Triangle*5,self.state)
        
        if len(self.folder_caminho) > 28:
            display_text = self.folder_caminho[:28] + '...'

        else:
            if self.folder_caminho == '':
                display_text = self.local_padrao
            else:
                display_text = self.folder_caminho
        
        self.text4 = self.font_2_.render(display_text, True, (20, 20, 20))
        self.WINDOW.blit(self.text4, (self.WINDOW.get_width()/2 + self.Size3[0]/2 - self.text4.get_width()/2, self.Vecs[1] + self.Size3[1] + 45 + self.text4.get_height()/2))

    def inputs_change(self): 
        pygame.draw.rect(self.WINDOW, self.Color_input, (self.WINDOW.get_width()/2, self.Vecs[1] + self.Size3[1] + 10, self.Size3[0], self.Size3[1]), border_radius=10)
        pygame.draw.rect(self.WINDOW, (200, 200, 200), (self.WINDOW.get_width()/2, self.Vecs[1] + self.Size3[1] + 45, self.Size3[0], self.Size3[1]), border_radius=6)
        self.Gui_Forms.draw_Form1(self.WINDOW,(0,0,0),self.Size_Triangle,self.WINDOW.get_width()/2 + self.Size3[0]- 6 * 2,self.Vecs[1] + self.Size3[1] + 45 + self.Size_Triangle*5,self.state)
        
        pygame.draw.rect(self.WINDOW, (21, 21, 21), (self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10, self.Vecs[1] + self.Size2[1] - 130, self.Size2[0] - 20, 50), border_radius=5)
        self.WINDOW.blit(self.text8, (self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10 + self.Size2[0]/2 - self.text6.get_width()/2, self.Vecs[1] + self.Size2[1] - 130 + self.text6.get_height()))
        self.WINDOW.blit(self.verificado, (self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10 + self.Size2[0]/2 - self.text6.get_width()/2 - self.verificado.get_width(), self.Vecs[1] + self.Size2[1] - 130 + self.text6.get_height()-2))

    def set_new_boj(self):
        if self.visible:
            project_names = [project['name'] for project in self.config.get()]
            pygame.draw.rect(self.WINDOW, self.Color2, (self.WINDOW.get_width()/2 - self.Size2[0]/2, self.Vecs[1], self.Size2[0], self.Size2[1]), border_radius=10)
            pygame.draw.rect(self.WINDOW, (21, 21, 21), (self.WINDOW.get_width()/2 - self.Size2[0]/2, self.Vecs[1], self.Size2[0], 25), border_top_left_radius=10, border_top_right_radius=10)
            self.WINDOW.blit(self.plus_h2, (self.WINDOW.get_width()/2 - self.Size2[0]/2, self.Vecs[1]))
            self.WINDOW.blit(self.text, (self.WINDOW.get_width()/2 - self.Size2[0]/2 + self.plus_h2.get_width(), self.Vecs[1] + self.text.get_height()/2))
            self.WINDOW.blit(self.text2, (self.WINDOW.get_width()/2 - self.Size2[0]/2 + self.plus_h2.get_width(), self.Vecs[1] + 35))
            self.WINDOW.blit(self.folder_2_, (self.WINDOW.get_width()/2 - self.Size2[0]/2 + self.plus_h2.get_width(), self.Vecs[1] + 65))
            self.WINDOW.blit(self.text3, (self.WINDOW.get_width()/2 - self.Size2[0]/2 + self.plus_h2.get_width() + self.folder_2_.get_width() + 10, self.Vecs[1] + 65 + self.text3.get_height()/2))
            self.inputs()

            pygame.draw.rect(self.WINDOW, (21, 21, 21), (self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10, self.Vecs[1] + self.Size2[1] - 70, self.Size2[0] - 20, 50), border_radius=5)
            self.WINDOW.blit(self.text5, (self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10 + self.Size2[0]/2 - self.text5.get_width()/2, self.Vecs[1] + self.Size2[1] - 70 + self.text5.get_height()))

            if self.input != '': 
                pygame.draw.rect(self.WINDOW, (21, 21, 21), (self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10, self.Vecs[1] + self.Size2[1] - 130, self.Size2[0] - 20, 50), border_radius=5)
                self.WINDOW.blit(self.text6, (self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10 + self.Size2[0]/2 - self.text6.get_width()/2, self.Vecs[1] + self.Size2[1] - 130 + self.text6.get_height()))
                self.WINDOW.blit(self.verificado, (self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10 + self.Size2[0]/2 - self.text6.get_width()/2 - self.verificado.get_width(), self.Vecs[1] + self.Size2[1] - 130 + self.text6.get_height()-2))
            
            if self.input in project_names:
                self.input_color_text = (255,0,0)
            else: 
                self.input_color_text = (230,230,230)
            

    def handle_events(self, events):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        add_rect = pygame.Rect(self.Vecs[0], self.Vecs[1], self.Size[0], self.Size[1])
        input_rect = pygame.Rect(self.WINDOW.get_width()/2, self.Vecs[1] + self.Size3[1] + 10, self.Size3[0], self.Size3[1])
        cancel_rect = pygame.Rect(self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10, self.Vecs[1] + self.Size2[1] - 70, self.Size2[0] - 20, 50)
        create_rect = pygame.Rect(self.WINDOW.get_width()/2 - self.Size2[0]/2 + 10, self.Vecs[1] + self.Size2[1] - 130, self.Size2[0] - 20, 50)
        add_local_folder_rect = pygame.Rect(self.WINDOW.get_width()/2, self.Vecs[1] + self.Size3[1] + 45, self.Size3[0], self.Size3[1])

        if add_rect.collidepoint(mouse_pos) and mouse_pressed[0] and not self.delete_visible and not self.charge_visible:
            self.visible = True
            self.state = False
        
        if self.charge_visible:
            name_rect = pygame.Rect(self.WINDOW.get_width()/2, self.Vecs[1] + self.Size3[1] + 10, self.Size3[0], self.Size3[1])
            
            if self.active:   
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.project_name = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.project_name = self.project_name[:-1]
                        else:
                            if len(self.project_name) < 15:
                               self.project_name += event.unicode
                            else:
                               return
            
            if mouse_pressed[0] and name_rect.collidepoint(mouse_pos):
                self.active = not self.active
                self.Color_input = (28, 28, 28) 
                
            if mouse_pressed[0] and not name_rect.collidepoint(mouse_pos): 
                self.active = False
                self.Color_input = (21, 21, 21)

        if self.visible:
            if cancel_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
                self.visible = False
                self.state = False
                self.input = ''
                self.folder_caminho = self.local_padrao
            
            if create_rect.collidepoint(mouse_pos) and mouse_pressed[0] and self.input != '':
                    project_names = [project['name'] for project in self.config.get()]
                    if self.input in project_names: 
                        return
                    else:
                       if self.folder_caminho == '':
                           new_folder = os.path.join(self.local_padrao, self.input)
                           self.folder_caminho = self.local_padrao
                       else:
                           #cria o caminho do projeto
                           new_folder = os.path.join(self.folder_caminho,self.input)
                           
                           #cria a pasta do projeto
                           os.makedirs(new_folder, exist_ok=True)
                           
                           #cria caminho da pasta data dentro da pasta do projeto
                           data_folder = os.path.join(new_folder,'configs')
                           #cria a pasta data dentro do projeto
                           os.makedirs(data_folder,exist_ok=True)
                           
                           #cria arquivo config.json dentro a pasta do projeto
                           config_path = os.path.join(data_folder,'config.json')
                           #cria um json vazio inicialmente
                           with open(config_path, 'w') as config_file:
                                json.dump({}, config_file)  # Adiciona um JSON vazio inicialmente
                            
                           #cria arquivo nota do motor 
                           nota = os.path.join(new_folder,'nota.txt')
                           with open(nota,'w') as file: 
                               file.write('Kairos Version: 0.0.0 Beta. \n')
                               file.write('using Libarys: Pygame and Box2D. \n')
                               file.write('creating with Python. \n')
                               file.write(f'Pygame {pygame.__version__} \n')
                               file.write('Credits Marcos Antônio Higino Figueiredo De Lima. Brasil')

                           #dados do projeto como nome e caminho
                           new_project = { 
                              'name': self.input,
                              'path': self.folder_caminho
                           }
                           #adiciona ao json project.json
                           self.config.add_object(new_project)

                           #configs finish
                           self.input = ''
                           self.visible = False

            if input_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
                self.active = not self.active
                self.Color_input = (28, 28, 28)

            if add_local_folder_rect.collidepoint(mouse_pos) and mouse_pressed[0]:
                self.state = True 
                root = tk.Tk()
                root.withdraw()
                folder_select = filedialog.askdirectory()
                self.folder_caminho = folder_select

            for event in events:
                if event.type == pygame.KEYDOWN and self.active:
                    if event.key == pygame.K_RETURN:
                        self.input = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.input = self.input[:-1]
                    else:
                        if len(self.input) < 15:
                            self.input += event.unicode
                        else:
                            return
                    
            if mouse_pressed[0] and not input_rect.collidepoint(mouse_pos):
                self.Color_input = (21, 21, 21)
                self.active = False
        else: 
            if self.delete_visible:
                close_rect = pygame.Rect(self.rect_x + self.rect_width - 20, self.rect_y + 10, 12, 12)

                if close_rect.collidepoint(mouse_pos) and mouse_pressed[0]: 
                    self.delete_visible = False
                    self.error_box = False
            else: 
                self.rect_x = self.WINDOW.get_width() / 2 - self.rect_width / 2
                self.rect_y = self.WINDOW.get_height() / 2 - self.rect_height / 2
       
        projects = self.config.get()
        for event in events:
            if event.type == pygame.MOUSEWHEEL and len(projects) > 12:
                if self._is_mouse_over_list(mouse_pos):
                    self.scroll_offset += event.y * 20
                    self._clamp_scroll_offset()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect_x < event.pos[0] < self.rect_x + self.rect_width and self.rect_y < event.pos[1] < self.rect_y + self.rect_height:
                    self.dragging = True
                    self.mouse_x, self.mouse_y = event.pos
                    self.offset_x = self.rect_x - self.mouse_x
                    self.offset_y = self.rect_y - self.mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False

        if self.dragging:
            self.mouse_x, self.mouse_y = mouse_pos
            new_rect_x = self.mouse_x + self.offset_x
            new_rect_y = self.mouse_y + self.offset_y

            if 0 <= new_rect_x <= self.WINDOW.get_width() - self.rect_width:
                self.rect_x = new_rect_x
            if 120 <= new_rect_y <= self.WINDOW.get_height() - self.rect_height:
                self.rect_y = new_rect_y
                
    def render(self):
        pygame.draw.rect(self.WINDOW, self.Color, (self.Vecs[0], self.Vecs[1] + self.scroll_offset, self.Size[0], self.Size[1]), border_radius=10)
        self.WINDOW.blit(self.plus, (self.Vecs[0] + self.Size[0] // 2 - self.plus.get_width() // 2, self.Vecs[1] + self.Size[1] // 2 - self.plus.get_height() // 2 - 10 + self.scroll_offset))
        self.WINDOW.blit(self.add_text, (self.Vecs[0] + self.Size[0] // 2 - self.add_text.get_width() // 2, self.Vecs[1] + self.Size[1] // 2 + self.plus.get_height() // 2 + self.scroll_offset))
        spacing_x = 10
        spacing_y = 0
        projects = self.config.get()
        for project in projects:
            rect_x = self.Vecs[0] + self.Size[0] + spacing_x
            rect_y = self.Vecs[1] + spacing_y + self.scroll_offset
            project_rect = pygame.Rect(rect_x, rect_y, self.Size[0], self.Size[1])
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()
            if rect_y + self.Size[1] > 0 and rect_y < self.WINDOW.get_height():
                pygame.draw.rect(self.WINDOW, self.Color, (rect_x, rect_y, self.Size[0], self.Size[1]), border_radius=10)
                self.WINDOW.blit(self.folder, (rect_x + self.folder.get_width() / 2 - 5, rect_y + self.folder.get_height() / 2 - 10))
                if len(project['name']) < 13:
                    project_name = self.font.render(project['name'], True, (255, 255, 255))
                    self.WINDOW.blit(project_name, (rect_x + self.Size[0] / 2 - project_name.get_width() / 2, rect_y + self.Size[1] // 2 + self.plus.get_height() // 2))
                else:
                    display_text = project['name'][:12] + '...'
                    project_name = self.font.render(display_text, True, (255, 255, 255))
                    self.WINDOW.blit(project_name, (rect_x + self.Size[0] / 2 - project_name.get_width() / 2, rect_y + self.Size[1] // 2 + self.plus.get_height() // 2))
            
            spacing_x += self.Size[0] + 10
            if spacing_x > 5 * (self.Size[0] + 10):
                spacing_x = -self.Size[0]
                spacing_y += self.Size[1] + 10
            if project_rect.collidepoint(mouse_pos):
                if rect_x + self.Size[0] > self.WINDOW.get_width() - self.Size[0]:
                    self.Vecs_config = [rect_x - 50, rect_y + self.Size[1] - self.Size_config_two[1] / 2]
                else:
                    self.Vecs_config = [rect_x + self.Size[0], rect_y + self.Size[1] - self.Size_config_two[1] / 2]
                
                self.config_2_visible = True
                self.name_project_mouse_passed = project['name']
                self.path_project_mouse_passed = project['path']
                
                if mouse_pressed[0]:
                    if os.path.exists(project['path']):
                        self.Config.add_project_data(False)
                        new_data = { 
                           'name': project['name'],
                          'path': project['path']     
                        }
                        self.Config.set_project_name(new_data)
                        from editor import run_editor
                        run_editor(new_data)
                    else: 
                        self.error_mensage = f"Erro: O caminho '{project['path']}' não existe no seu computador"
                        self.error_box = True
                    
                if mouse_pressed[2] and not self.delete_visible and not self.charge_visible:
                    self.charge_visible = True
                    self.project_name = project['name']
                    self.path_change = project['path']
                    self.current_project_id = project['id']
                    
                elif keys[pygame.K_d] and not self.delete_visible and not self.charge_visible:
                    self.name_delet = project['name']
                    self.current_project_id = project['id']
                    self.delete_visible = True
            
            if self.charge_visible and not self.visible and not self.delete_visible:
                events = pygame.event.get()
                pygame.draw.rect(self.WINDOW, self.Color2, (self.WINDOW.get_width() / 2 - self.Size2[0] / 2, self.Vecs[1], self.Size2[0], self.Size2[1]), border_radius=10)
                pygame.draw.rect(self.WINDOW, (21, 21, 21), (self.WINDOW.get_width() / 2 - self.Size2[0] / 2, self.Vecs[1], self.Size2[0], 25), border_top_left_radius=10, border_top_right_radius=10)
                self.WINDOW.blit(self.change, (self.WINDOW.get_width() / 2 - self.Size2[0] / 2 + 5, self.Vecs[1] + 5))
                self.WINDOW.blit(self.text7, (self.WINDOW.get_width() / 2 - self.Size2[0] / 2 + self.plus_h2.get_width() + 3, self.Vecs[1] + self.text.get_height() / 2))
                self.WINDOW.blit(self.text2, (self.WINDOW.get_width() / 2 - self.Size2[0] / 2 + self.plus_h2.get_width(), self.Vecs[1] + 35))
                self.WINDOW.blit(self.folder_2_, (self.WINDOW.get_width() / 2 - self.Size2[0] / 2 + self.plus_h2.get_width(), self.Vecs[1] + 65))
                self.WINDOW.blit(self.text3, (self.WINDOW.get_width() / 2 - self.Size2[0] / 2 + self.plus_h2.get_width() + self.folder_2_.get_width() + 10, self.Vecs[1] + 65 + self.text3.get_height() / 2))
                self.inputs_change()
                pygame.draw.rect(self.WINDOW, (21, 21, 21), (self.WINDOW.get_width() / 2 - self.Size2[0] / 2 + 10, self.Vecs[1] + self.Size2[1] - 70, self.Size2[0] - 20, 50), border_radius=5)
                self.WINDOW.blit(self.text5, (self.WINDOW.get_width() / 2 - self.Size2[0] / 2 + 10 + self.Size2[0] / 2 - self.text5.get_width() / 2, self.Vecs[1] + self.Size2[1] - 70 + self.text5.get_height()))
                cancel_rect = pygame.Rect(self.WINDOW.get_width() / 2 - self.Size2[0] / 2 + 10, self.Vecs[1] + self.Size2[1] - 70, self.Size2[0] - 20, 50)
                path_rect = pygame.Rect(self.WINDOW.get_width() / 2, self.Vecs[1] + self.Size3[1] + 45, self.Size3[0], self.Size3[1])
                text_name = self.font_2_.render(self.project_name, True, (230, 230, 230))
                if self.path_change == '':
                    self.path_change = self.local_padrao
                    
                if len(self.path_change) < 28:
                    path = self.font_2_.render(self.path_change, True, (20, 20, 20))
                else:
                    path = self.font_2_.render(self.path_change[:28] + '...', True, (20, 20, 20))
                
                self.WINDOW.blit(text_name, (self.WINDOW.get_width() / 2 + 10, self.Vecs[1] + self.Size3[1] + 16))
                self.WINDOW.blit(path, (self.WINDOW.get_width() / 2 + self.Size3[0] / 2 - path.get_width() / 2, self.Vecs[1] + self.Size3[1] + 45 + path.get_height() / 2))
                change_rect = pygame.Rect(self.WINDOW.get_width() / 2 - self.Size2[0] / 2 + 10, self.Vecs[1] + self.Size2[1] - 130, self.Size2[0] - 20, 50)
                if mouse_pressed[0] and change_rect.collidepoint(mouse_pos):
                    self.old_path = project['path']
                    if self.path_change_data == None: 
                        self.path_change_data = self.old_path
                    new_path = self.path_change_data
                    new_name = self.project_name
                    self.old_name = project['name']
                    self.config.update_project_path(self.current_project_id, new_path)
                    self.config.update_project_name(self.current_project_id, new_name)
                    self.charge_visible = False
                    
                if mouse_pressed[0] and cancel_rect.collidepoint(mouse_pos):
                    self.charge_visible = False
                    self.state = False
                    
                if mouse_pressed[0] and path_rect.collidepoint(mouse_pos):
                    self.state = True
                    root = tk.Tk()
                    root.withdraw()
                    self.path_change_data = filedialog.askdirectory()
                    self.path_change = self.path_change_data
            
            if self.delete_visible and not self.visible:
                text = self.font_2_.render(f'Project Name: {self.name_delet}', True, (230, 230, 230))
                pygame.draw.rect(self.WINDOW, self.Color2, (self.rect_x, self.rect_y, self.rect_width, self.rect_height), border_radius=5)
                pygame.draw.rect(self.WINDOW, (200, 0, 0), (self.rect_x + 10, self.rect_y + self.rect_height - 35, 180, 30), border_radius=5)
                self.WINDOW.blit(self.delete_text, (self.rect_x + 90 / 2 + self.delete_text.get_width() / 2, self.rect_y + 55 + self.delete_text.get_height()))
                self.WINDOW.blit(text, (self.rect_x + 4, self.rect_y + self.rect_height / 2 - 12))
                self.WINDOW.blit(self.close, (self.rect_x + self.rect_width - 20, self.rect_y + 14))
                delete_rect = pygame.Rect(self.rect_x + 10, self.rect_y + self.rect_height - 35, 180, 30)
                if mouse_pressed[0]:
                    if delete_rect.collidepoint(mouse_pos) and not self.active3:
                        project_path = None
                        for p in projects:
                            if p['id'] == self.current_project_id:
                                project_path = os.path.join(p['path'], p['name'])
                                break
                            
                        if project_path:
                            try:
                               shutil.rmtree(project_path)
                               projects = [p for p in projects if p['id'] != self.current_project_id]
                               self.config.set('projects', projects)
                               self.delete_visible = False
                            except Exception as e:
                               self.error_mensage = f'Erro ao deletar o projeto: {str(e)}'
                               self.error_box = True
                        else:
                            self.error_mensage = 'Projeto não encontrado'
                            self.error_box = True
                    self.active3 = True
                else: 
                    self.active3 = False
            
            if self.error_box:
                text = self.font.render(self.error_mensage,True,(230,100,100))
                pygame.draw.rect(self.WINDOW,(50,50,50),(self.WINDOW.get_width() / 2 - text.get_width()/2,130,text.get_width() + 20,40),border_radius=5)
                self.WINDOW.blit(text, (self.WINDOW.get_width() / 2 - 100 + 110 - text.get_width()/2,130 + text.get_height()/2 + 3))
            
            if self.config_2_visible and not self.visible and not self.delete_visible and not self.charge_visible:
                pygame.draw.rect(self.WINDOW, (101, 101, 101), (self.Vecs_config, self.Size_config_two), border_radius=0)
                name_text = self.font_2_.render(f'Name Project: {self.name_project_mouse_passed}',True,(230,230,230))
                if  len(self.path_project_mouse_passed) < 12:
                    self.Size_config_two[1] = 105
                    path_text = self.font_2_.render(f'Path Project: {self.path_project_mouse_passed}',True,(230,230,230))
                    self.WINDOW.blit(path_text, (self.Vecs_config[0] + 10,self.Vecs_config[1] + 25))
                    self.WINDOW.blit(name_text, (self.Vecs_config[0] + 10, self.Vecs_config[1] + 5))
                    self.WINDOW.blit(self.text_open, (self.Vecs_config[0] + 10, self.Vecs_config[1] + 45))
                    self.WINDOW.blit(self.text_rename, (self.Vecs_config[0] + 10, self.Vecs_config[1] + 65))
                    self.WINDOW.blit(self.text_delete, (self.Vecs_config[0] + 10, self.Vecs_config[1] + 85))
                else:
                    self.Size_config_two[1] = 125
                    path1 = self.path_project_mouse_passed[:12]
                    path2 = self.path_project_mouse_passed[12:]
                    path_text1 = self.font_2_.render(f'Path Project: {path1}',True,(230,230,230))
                    path_text2 = self.font_2_.render(f'{path2}',True,(230,230,230))
                    self.WINDOW.blit(path_text1, (self.Vecs_config[0] + 10,self.Vecs_config[1] + 25))
                    self.WINDOW.blit(path_text2, (self.Vecs_config[0] + 10,self.Vecs_config[1] + 45))
                    self.WINDOW.blit(name_text, (self.Vecs_config[0] + 10, self.Vecs_config[1] + 5))
                    self.WINDOW.blit(self.text_open, (self.Vecs_config[0] + 10, self.Vecs_config[1] + 65))
                    self.WINDOW.blit(self.text_rename, (self.Vecs_config[0] + 10, self.Vecs_config[1] + 85))
                    self.WINDOW.blit(self.text_delete, (self.Vecs_config[0] + 10, self.Vecs_config[1] + 105))
            
            if not project_rect.collidepoint(mouse_pos) and self.config_2_visible:
                self.config_2_visible = False
        
        self.set_new_boj()

    def _is_mouse_over_list(self, mouse_pos):
        rect_list_area = pygame.Rect(self.Vecs[0] + self.Size[0] + 10, self.Vecs[1], 14 * (self.Size[0] + 10), 14 * (self.Size[1] + 10))
        return rect_list_area.collidepoint(mouse_pos)

    def _clamp_scroll_offset(self):
        max_scroll = 14 * (self.Size[1] + 10) - self.max_visible_items * (self.Size[1] + 10)
        self.scroll_offset = max(self.scroll_offset, -max_scroll)
        self.scroll_offset = min(self.scroll_offset, 0)