import pygame
from Config.config_engine import ConFig
from Gui.gui import Settings, SetNewObj

class ProjectManager:
    def __init__(self):
        pygame.init()
        self.run = True
        self.config = ConFig()
        self.state = self.config.get_project_data()  # Dados dos projetos
        self.icon = pygame.image.load('./Assents/icon.png')  # Ícone do engine
        self.VERSION = 'v0.0.0 Beta (Project Manager)'
        self.WINDOW_SIZE = [800, 500]
        self.WINDOW = pygame.display.set_mode(self.WINDOW_SIZE)
        self.WINDOW_COLOR = (31, 31, 31)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(f' Kairos Engine {self.VERSION}')
        self.settings = Settings(self.WINDOW)
        self.SetNewObj = SetNewObj(self.WINDOW)  # GUI que lida com os projetos
        self.GUI = [self.SetNewObj, self.settings]
        self.clock = pygame.time.Clock()

    def render(self):
        self.WINDOW.fill(self.WINDOW_COLOR)
        for INTERFACE in self.GUI:
            INTERFACE.render()  # Renderiza cada interface
        pygame.display.flip()

    def update(self):
        while self.run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.run = False
                    break

                if event.type == pygame.VIDEORESIZE:
                    new_size = (max(event.w, 800), max(event.h, 500))
                    self.WINDOW = pygame.display.set_mode(new_size, pygame.RESIZABLE)

            # Eventos são tratados dentro do SetNewObj
            self.SetNewObj.handle_events(events)

            self.clock.tick(60)
            self.render()

def run_project_manager():
    manager = ProjectManager()
    manager.update()
    pygame.quit()

if __name__ == '__main__':
    run_project_manager()
