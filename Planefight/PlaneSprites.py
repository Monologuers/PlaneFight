import pygame
from pygame import  Surface


class GameSprite(pygame.sprite.Sprite):
    """新飞机大战"""
    def __init__(self,image_name:str,speed:float=1):
        #调用父类的初始化
        super().__init__()
        #定义对象的属性
        self.image:Surface = (
            pygame.image.load(image_name))
        self.rect = self.image.get_rect()
        self.speed:float = speed

        pass
    def update(self):
        self.rect.y += self.speed
        pass