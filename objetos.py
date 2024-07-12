import pygame,random
pygame.init()
pygame.mixer.init()

tiempo_juego = pygame.time.get_ticks()

#AUDIO-----------------------------------------------------
perdiste = pygame.mixer.Sound('recursos/audio/perdiste.wav')
musica = pygame.mixer.music.load('recursos/audio/musica.wav')
pygame.mixer.music.play(-1)
#AUDIO-----------------------------------------------------
texto = pygame.font.SysFont('Engravers MT',30)
pygame.display.set_caption('Urb@nSpace')
#ajustes pantalla---------------------------
resol=(900,500)
pantalla= pygame.display.set_mode(resol)
fondo = pygame.image.load('recursos/fondo.png')
urban = pygame.image.load('recursos/urban.png')
escala= pygame.transform.scale(fondo,(resol))
reloj= pygame.time.Clock()

#ajustes pantalla---------------------------

#colores------------------
verde =(19, 255, 4)
rojo = (255,0,0)
blanco=(255,255,255)
negro =(0,0,0)
#-------------------------
#explosion de asteroides-----------
asteroide_exp= []

explosion= pygame.image.load(f'recursos/asteroides/explosion.PNG')
       

#texto------------------------------------------
perdiste_texto = texto.render('PERDISTE',1,rojo)

#cosas juego----------------------------------
asteroide_sprite = pygame.sprite.Group()
num_asteroid = 7
#puntaje--------------
puntaje = 0

#-----------------
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('recursos/jugador.png')
        self.rect= self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.velx = 5
        self.vely = 5
        
    def generar(self):
        pantalla.blit(self.image,self.rect)

   
    def teclado(self,tecla):
        if tecla[pygame.K_a]:
            self.rect.x -= self.velx
        if tecla[pygame.K_s]:
            self.rect.y += self.vely
        if tecla[pygame.K_d]:
            self.rect.x += self.velx
        if tecla[pygame.K_w]:
            self.rect.y -= self.velx
  
    def colision_pant(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 900:
            self.rect.x = 900
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 450:
            self.rect.y = 450
                
jugador = Jugador()

class Estrella():
    def __init__(self):
        self.radio=2
        self.posx= random.randint(0,900)
        self.posy= random.randint(0,500)
        self.color = (171, 247, 215)
        self.velx= 3

    def generar(self):
        pygame.draw.circle(pantalla,self.color,(self.posx,self.posy),self.radio)
    def movimiento(self):
        self.posx -= self.velx
        if self.posx < 0:
            self.posx = 900
            self.posy= random.randint(0,500)


class Asteroides_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('recursos/asteroides/asteroide1.PNG')
        self.rect = self.image.get_rect()
        self.image.set_colorkey(negro)
        self.velx= 3
        

    def generar(self):
        asteroide_sprite.draw(pantalla)
    def movimiento(self):
        self.rect.x -= self.velx
        if self.rect.x <= 0:
            self.rect.x = 900
            self.rect.y= random.randint(0,500)
            
            
    def explosion(self):
        pantalla.blit(explosion,(self.rect.x,self.rect.y))

class Asteroides_2(Asteroides_1):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('recursos/asteroides/asteroide2.png')
        self.image.set_colorkey(negro)


for i in range(num_asteroid):
    asteroide = Asteroides_1()
            
    asteroide.rect.x= random.randint(500,900)
    asteroide.rect.y= random.randint(0,500)
   

    asteroide2= Asteroides_2()
    asteroide2.rect.x= random.randint(500,900)
    asteroide2.rect.y= random.randint(0,500)
    asteroide_sprite.add(asteroide)
    asteroide_sprite.add(asteroide2)
        


#juego corriendo
    


estrellas_lista=[]
for i in range(75):
    estrella= Estrella()
    estrellas_lista.append(estrella)

class Proyectil():
    def __init__(self):
        self.proyect_velx= 5
        self.proyect_coordx = jugador.rect.x +69
        self.proyect_coordy=jugador.rect.y + 25
        self.largo = 40
        self.ancho = 5
        self.color= (193, 39, 177)
       
    def generar(self):
        dibujo= pygame.draw.rect(pantalla,self.color,(self.proyect_coordx,self.proyect_coordy,self.largo,self.ancho))
        return dibujo
    def disparar(self):
        self.proyect_coordx += self.proyect_velx


#objetos de interfaz----------------------------------------------------------------------------------------------------
class Boton():
    def __init__(self):
        self.imagen= pygame.image.load('recursos/boton.png')
        self.imagen.set_colorkey(blanco)
        self.imagen2= pygame.image.load('recursos/boton2.png')
        self.imagen2.set_colorkey(blanco)
        self.posx=450
        self.posy= 0
        self.mute = False
    def crear(self):
        if not self.mute:
            pantalla.blit(self.imagen,(self.posx,self.posy))
        else:
            pantalla.blit(self.imagen2,(self.posx,self.posy))

    def click(self,evento):
        rectangulo = pygame.Rect(self.posx,self.posy,50,50)
        
        if rectangulo.collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.MOUSEBUTTONDOWN and not self.mute:
            self.mute = True
      
        elif rectangulo.collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.MOUSEBUTTONDOWN and self.mute:
            self.mute = False
            
        if self.mute:
           
            pygame.mixer.music.pause()

        else:
            pygame.mixer.music.unpause()
            
boton= Boton()