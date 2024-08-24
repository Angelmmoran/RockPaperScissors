import random
import pygame

pygame.init()

#Configuracion de la ventana
ancho = 640
alto = 480

ventana = pygame.display.set_mode((ancho , alto))
pygame.display.set_caption("Piedra, papel o tijera")

#Definicion de los colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

#fuente 
fuente = pygame.font.SysFont(None, 50)

#funcion para texto en pantalla

def mostrar_mensaje (texto):
    texto_render = fuente.render(texto, True, negro)
    texto_rect = texto_render.get_rect(center=(ancho//2, alto//2 + 50))  # Ajusta el valor 50 para cambiar la posición vertical
    ventana.blit(texto_render, texto_rect)



#botones

piedra_rect = pygame.Rect(50,100,150,150)
papel_rect = pygame.Rect(250,100,150,150)
tijera_rect = pygame.Rect(450,100,150,150)

#ejecutar juego

ejecutando = True

while ejecutando:
    ventana.fill(blanco)

    pygame.draw.rect(ventana, negro, piedra_rect, 2)
    pygame.draw.rect(ventana, negro, papel_rect, 2)
    pygame.draw.rect(ventana, negro, tijera_rect, 2)

    ventana.blit(fuente.render("Piedra", True, negro), (piedra_rect.x + 20, piedra_rect.y + 50))
    ventana.blit(fuente.render("Papel", True, negro), (papel_rect.x + 30, piedra_rect.y + 50))
    ventana.blit(fuente.render("Tijera", True, negro), (tijera_rect.x + 30, piedra_rect.y + 50))

    #funcion para determinar ganador
    def ganador (jugador, odernador):
          if jugador == ordenador:
            return "Empate"
          elif (jugador == "Piedra" and ordenador == "Tijera") or \
               (jugador == "Papel" and ordenador == "Piedra") or \
               (jugador == "Tijera" and ordenador == "Papel"):
            return "Ganaste"
          else:
            return "Perdiste"

#juego


    ordenador = random.choice (["Piedra", "Papel", "Tijera"])
    jugador = ""
    resultado = ""

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if 50 < x < 200 and 100 < y < 250:
                    jugador = "Piedra"
            elif 250 < x < 400 and 100 < y < 250:
                    jugador = "Papel"
            elif 450 < x < 600 and 100 < y < 250:
                    jugador = "Tijera"
            else:
                  jugador = None

        if jugador :
         resultado = ganador (jugador, ordenador)

         if resultado:
            mostrar_mensaje(resultado)
            pygame.display.update()



MAX_ROUNDS = 10  # Número máximo de rondas a jugar
round_count = 0
if round_count == MAX_ROUNDS:
    pygame.quit()

while ejecutando:
    
    if resultado:
        mostrar_mensaje(resultado)

    pygame.display.update()

    # Reiniciar el juego después de cada ronda o si se alcanza el máximo
    if resultado or round_count >= MAX_ROUNDS:
        mostrar_mensaje("Presiona una tecla para jugar de nuevo")
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ejecutando = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    resultado = ""
                    round_count = 0
                    waiting = False

    round_count += 1

pygame.quit()


                  