import pygame

def change_data_for_scene(obj_data: dict, original_scene_size: tuple, current_scene_size: tuple):
    # Tamanho original e atual da cena
    original_width, original_height = original_scene_size
    current_width, current_height = current_scene_size

    # Fatores de escala para ajuste da posição e tamanho
    scale_x = current_width / original_width
    scale_y = current_height / original_height

    # Ajustar posição e tamanho do objeto com base na escala
    obj_pos = obj_data.get('position', [0, 0])
    obj_size = obj_data.get('size', [0, 0])

    # Ajustar o novo tamanho com base na quantidade de valores presentes
    if len(obj_size) == 2:
        new_size = [int(obj_size[0] * scale_x), int(obj_size[1] * scale_y)]
    elif len(obj_size) == 1:
        new_size = [int(obj_size[0] * scale_x)]
    else:
        new_size = obj_size  # Caso não haja tamanho definido ou a estrutura seja inesperada

    new_pos = [int(obj_pos[0] * scale_x), int(obj_pos[1] * scale_y)]

    # Retornar os dados atualizados para o objeto
    return {
        'type': obj_data['type'],
        'position': new_pos,
        'size': new_size,
        'color': obj_data['color'],
        'visible_in_sceen': obj_data['visible_in_sceen']
    }
    
def is_within_viewport(obj_pos, obj_size, viewport_size, size_data):
    obj_x, obj_y = obj_pos
    viewport_w, viewport_h = viewport_size

    # Verificar se o tamanho do objeto tem 2 valores (largura e altura) ou apenas 1 (raio)
    if len(obj_size) == 2:
        obj_w, obj_h = obj_size
    elif len(obj_size) == 1:
        obj_w = obj_h = obj_size[0]
    else:
        return False  # Caso não haja um tamanho definido ou a estrutura seja inesperada

    # Verificar se qualquer parte do objeto está dentro da área visível
    return (obj_x + obj_w > 0 and obj_x < viewport_w + size_data and
            obj_y + obj_h > 0 and obj_y < viewport_h)

def draw_visible_rect(surface, obj_pos, obj_size, obj_color, viewport_size,size_data):
    x, y = obj_pos
    w, h = obj_size
    viewport_w, viewport_h = viewport_size

    # Calcula a parte visível do retângulo
    visible_rect = pygame.Rect(x, y, w, h).clip(pygame.Rect(0, 0, viewport_w + size_data, viewport_h))

    # Se houver uma parte visível, desenhe o retângulo
    if visible_rect.width > 0 and visible_rect.height > 0:
        pygame.draw.rect(surface, obj_color, visible_rect)

def draw_visible_circle(surface, obj_pos, obj_size, obj_color, viewport_size,size_data):
    x, y = obj_pos
    radius = obj_size[0] // 2
    viewport_w, viewport_h = viewport_size

    # Verificar se o círculo está dentro da área visível
    if (x - radius < viewport_w + size_data and x + radius > 0 and
        y - radius < viewport_h and y + radius > 0):
        # Desenhar o círculo completo
        pygame.draw.circle(surface, obj_color, (x, y), radius)

def compile_data_for_scene(window, obj_data, viewport_size,size_data):
    obj_type = obj_data['type']
    obj_pos = obj_data['position']
    obj_size = obj_data['size']
    obj_color = obj_data['color']
    obj_visible = obj_data['visible_in_sceen']

    # Verificar se o objeto está dentro da área visível
    if not is_within_viewport(obj_pos, obj_size, viewport_size,size_data):
        return  # Não renderizar se estiver fora do campo de visão

    # Renderizar o objeto com base no tipo
    if obj_type == 'Square' and obj_visible:
        draw_visible_rect(window, obj_pos, obj_size, obj_color, viewport_size,size_data)
    elif obj_type == 'Circle' and obj_visible:
        draw_visible_circle(window, obj_pos, obj_size, obj_color, viewport_size,size_data)
    elif obj_type == 'Triangle' and obj_visible:
        # Implementar o desenho do triângulo conforme necessário
        pass