import pygame
import sys, random



class caracter(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.width=50
        self.height=50
        self.image=pygame.transform.scale(img,(self.width,self.height))

    
    def checkCollision(self, r):
         return (((self.rect.y <= r.rect.y + r.height and self.rect.y >= r.rect.y) or (self.rect.y+self.height<= r.rect.y + r.height and self.rect.y+self.height >= r.rect.y)) and ((self.rect.x >= r.rect.x and self.rect.x <= r.rect.x + r.width) or (self.rect.x + self.width >= r.rect.x and self.rect.x + self.width <= r.rect.x + r.width)))
    

    def draw(self,window):
         window.blit(self.image,(self.rect.x,self.rect.y))






class enemy_class(caracter):
    def __init__(self,x,y,img):
        super().__init__(x,y,img)




class good_guy(caracter):
    def __init__(self,x,y,img):
        super().__init__(x,y,img)
        self.width=80
        self.height=80
        self.image=pygame.transform.scale(img,(self.width,self.height))
    

class bullet(caracter):
    def __init__(self,x,y,img):
        super().__init__(x,y,img)
        self.speed = 20
        self.width=20
        self.height=20
        self.image = img
        self.image=pygame.transform.scale(img,(self.width,self.height))

    def checkCollision(self, r):
        return self.rect.y+self.height >= r.rect.y and self.rect.y <= r.rect.y + r.height and self.rect.x >= r.rect.x

class steps(caracter):
    def __init__ (self,x,y,img):
        super().__init__(x,y,img)
        self.width=200
        self.height=40
        self.image = img
        self.image=pygame.transform.scale(img,(self.width,self.height))
    
    def checkCollision(self, r):
        return r.rect.y + r.height >= self.rect.y and ((self.rect.x + self.width >= r.rect.x + r.width and r.rect.x + r.width >= self.rect.x) or (self.rect.x + self.width >= r.rect.x and r.rect.x >= self.rect.x))



class heart(caracter):
    def __init__(self,x,y,img):
        super().__init__(x,y,img)
        