import pygame,random,objetos
import time,os
proyectiles =[]


#juego corriendo
def jugando():
    
    tiempo_juego = time.time()

    cooldown = 0.25
    juego = True
    while juego:
        
        try:
        #pantalla-------------------------------------------------------------------------------------------------------------------------------
            
            objetos.pantalla.blit(objetos.escala,(0,0))
           
            teclas= pygame.key.get_pressed()

            for estrellas in objetos.estrellas_lista:
                estrellas.generar()
                estrellas.movimiento()

            #jugador-----------------------
            objetos.jugador.generar()
            objetos.jugador.teclado(teclas)
            objetos.jugador.colision_pant()
            #------------------------------    
            objetos.asteroide.generar()
            for asteroides in objetos.asteroide_sprite:
                asteroides.movimiento()
                
            
            for proyectil in proyectiles:
                proyectil.generar()
                proyectil.disparar()
                if proyectil.proyect_coordx > 900:
                    proyectiles.remove(proyectil)

        #pantalla--------------------------------------------------------------------------------------------------------------------------------
        #colisiones------------------------------------------------------------------------------------------------------------------------------
                
                for asteroide in objetos.asteroide_sprite:
        
                    if asteroide.rect.colliderect(proyectil.generar()):
                        asteroide.explosion()
                        asteroide.rect.x = 900
                        asteroide.rect.y = random.randint(0,500)
                        objetos.puntaje += 1
                        proyectiles.remove(proyectil)
                        if objetos.puntaje % 5 == 0:
                            for asteroide in objetos.asteroide_sprite:
                                asteroide.velx += 1
                        
                           
                            
                        
            if pygame.sprite.spritecollide(objetos.jugador,objetos.asteroide_sprite,False):
                perdida = True
        #colisiones--------------------------------------------------------------------------------------------------------------------------------

        #perdiste----------------------------------------------------------------------------------------------------------------------------------
                
                if perdida == True:
                    objetos.perdiste.play()
                    while perdida:
                        
                        objetos.pantalla.fill((0,0,0))
                        objetos.boton.crear()
                        objetos.pantalla.blit(objetos.perdiste_texto,(395,250))
                        objetos.pantalla.blit(objetos.texto.render(f'tu puntuacion fue: {objetos.puntaje}',1,objetos.blanco),(350,300))
                        objetos.pantalla.blit(objetos.urban,(800,400))
                        objetos.pantalla.blit(objetos.texto.render(f'ESPACIO para reiniciar',1,objetos.blanco),(345,450))
                        teclas = pygame.key.get_pressed()
                        pygame.display.flip()
                        for evento in pygame.event.get():
                            if evento.type == pygame.QUIT:
                                    pygame.quit()
                            objetos.boton.click(evento)
                        if teclas[pygame.K_SPACE]:
                            objetos.puntaje = 0
                            
                            for proyectil in proyectiles:
                                proyectiles.clear()

                            for asteroide in objetos.asteroide_sprite:
                                asteroide.velx = 3
                            objetos.jugador.rect.x= 0
                            objetos.jugador.rect.y = 0
                            for asteroide in objetos.asteroide_sprite:
                                if asteroide.rect.x < 500:
                                    asteroide.rect.x = random.randint(499,899)


                            jugando()
        #perdiste----------------------------------------------------------------------------------------------------------------------------------
        #eventos-----------------------------------------------------------------------------------------------------------------------------------
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                
                objetos.boton.click(evento)
                
            tiempo = time.time() 
            if tiempo - tiempo_juego > cooldown:
                    
                proyectil = objetos.Proyectil()
                proyectiles.append(proyectil)
                tiempo_juego = tiempo
                        

                   
                    
                    
        #eventos-----------------------------------------------------------------------------------------------------------------------------------
         
           
            puntuacion = objetos.texto.render(f'puntaje:{objetos.puntaje}',1,objetos.blanco)
     

            objetos.pantalla.blit(puntuacion,(0,450))
            objetos.reloj.tick(45)  
            objetos.boton.crear()
            pygame.display.flip()    
        except pygame.error:
            pass
        except ValueError:
            pass
        

    
jugando()