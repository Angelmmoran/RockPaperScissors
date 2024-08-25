

import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Piedra, Papel o Tijera")

# Colores
fondo = (128, 128, 128)
negro = (0, 0, 0)

# Fuente
fuente = pygame.font.Font(None, 36)

# Función para dibujar un botón
def dibujar_boton(texto, x, y, ancho, alto, color):
    pygame.draw.rect(ventana, color, (x, y, ancho, alto))
    texto_renderizado = fuente.render(texto, True, negro)
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    ventana.blit(texto_renderizado, texto_rect)


# Función para comprobar si se ha hecho clic en un botón
def comprobar_clic(x, y, ancho, alto, pos):
    if x < pos[0] < x + ancho and y < pos[1] < y + alto:
        return True
    else:
        return False

# Posiciones y dimensiones de los botones
boton1_x = 75
boton1_y = 100
boton2_x = 300
boton2_y = 100
boton3_x = 550
boton3_y = 100
ancho_boton = 150
alto_boton = 50
ancho_resultado = 200
alto_resultado = 50
x = 280
y = 300
color = negro

#lista de opciones para escoger por el ordenador
opciones = ["Piedra", "Papel", "Tijera"]

#resultado
RESULTADO = ""


# Bucle principal del juego
ejecutando = True
while ejecutando:

     # Dibujar la ventana y los botones
    ventana.fill(fondo)
    dibujar_boton("Piedra", boton1_x, boton1_y, ancho_boton, alto_boton, (93, 247, 102))
    dibujar_boton("Papel", boton2_x, boton2_y, ancho_boton, alto_boton, (93, 247, 102))
    dibujar_boton("Tijera", boton3_x, boton3_y, ancho_boton, alto_boton, (93, 247, 102))
    dibujar_boton(RESULTADO, x, y, ancho_resultado, alto_resultado, fondo)
    pygame.display.flip()

   
#elegir opcion y el resultado
    for evento in pygame.event.get():
        jugador = ""
        ordenador = ""
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if comprobar_clic(boton1_x, boton1_y, ancho_boton, alto_boton, pos):
                jugador = "Piedra"
                ordenador = random.choice (opciones)
            elif comprobar_clic(boton2_x, boton2_y, ancho_boton, alto_boton, pos):
                jugador = "Papel"
                ordenador = random.choice (opciones)
            elif comprobar_clic(boton3_x, boton3_y, ancho_boton, alto_boton, pos):
                jugador = "Tijera"
                ordenador = random.choice (opciones)
            
            if jugador == ordenador:
             RESULTADO = "EMPATE"
            elif jugador == "Piedra" and ordenador == "Tijera" or jugador ==  "Papel" and ordenador == "Piedra" or jugador == "Tijera" and ordenador == "Papel":
                RESULTADO = "HAS GANADO"
            else:
                RESULTADO = "HAS PERDIDO"
                








       


  


                  