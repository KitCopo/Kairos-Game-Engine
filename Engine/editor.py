import pygame
from Config.config_engine import ConFig
from Gui.gui import Settings
from Gui.guiEngine import Data_OBJS, Assents_OBJS, List_OBJS, Top_bars
from Console.console import *
from objects.objects import VERSION_ENGINE

class Editor:
    def __init__(self, project_data):
        pygame.init()
        self.config = ConFig()

        # Use the passed project data here
        self.project_name = project_data['name']
        self.project_path = project_data['path']

        self.icon = pygame.image.load('./Assents/icon.png')
        self.VERSION = f'{VERSION_ENGINE} (Editor) - {self.project_name}'
        self.WINDOW_SIZE = [1000, 600]
        self.WINDOW = pygame.display.set_mode(self.WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(f' Kairos Engine {self.VERSION}')
        self.data_obj = Data_OBJS(self.WINDOW)
        self.assents_obj = Assents_OBJS(self.WINDOW, self.data_obj)
        self.list_obj = List_OBJS(self.WINDOW, self.assents_obj, self.data_obj)
        self.Top_bars = Top_bars(self.WINDOW, self.list_obj, self.data_obj, self.assents_obj)
        self.INTERFACE_OBJS = [self.data_obj, self.list_obj, self.Top_bars, self.assents_obj]
        self.clock = pygame.time.Clock()

    def render(self):
        self.WINDOW.fill((10, 10, 10))
        self.list_obj.render_backgroundSceen()
        for INTERFACE in self.INTERFACE_OBJS:
            INTERFACE.render()
            
        pygame.display.flip()

    def update(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.config.ClearBuffers()
                    running = False
                    break

                if event.type == pygame.VIDEORESIZE:
                    new_size = (max(event.w, 1000), max(event.h, 600))
                    self.WINDOW = pygame.display.set_mode(new_size, pygame.RESIZABLE)

            self.clock.tick(60)
            self.render()
        pygame.quit()

def run_editor(project_data):
    editor = Editor(project_data)  # Passa o projeto selecionado ao Editor
    editor.update()

if __name__ == '__main__':
    print('run_editor necessita de dados do projeto para abrir')
