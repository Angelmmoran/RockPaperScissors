

import pygame
import random

imagen_piedra = pygame.image.load("C:\\Users\\Ángel\\Desktop\\Workspace\\Ejercicios Python\\Juegos\\PiedraPapelTijera\\piedra.png")
imagen_papel = pygame.image.load("C:\\Users\\Ángel\\Desktop\\Workspace\\Ejercicios Python\\Juegos\\PiedraPapelTijera\\papel.png")
imagen_tijera = pygame.image.load("C:\\Users\\Ángel\\Desktop\\Workspace\\Ejercicios Python\\Juegos\\PiedraPapelTijera\\tijera.png")

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
def dibujar_boton(imagen, x, y, ancho_boton, alto_boton):
    ventana.blit(imagen, (x, y))


# Función para comprobar si se ha hecho clic en un botón
def comprobar_clic(x, y, ancho, alto, pos):
    if x < pos[0] < x + ancho and y < pos[1] < y + alto:
        return True
    else:
        return False
    
def dibujar_resultado(texto, x, y, ancho, alto, color): 
    pygame.draw.rect(ventana, color, (x, y, ancho, alto))
    texto_renderizado = fuente.render(texto, True, negro)
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    ventana.blit(texto_renderizado, texto_rect)


def dibujar_rondas(texto, x, y, ancho, alto, color): 
    pygame.draw.rect(ventana, color, (x, y, ancho, alto))
    texto_renderizado = fuente.render("Rondas:  " + texto, True, negro)
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    ventana.blit(texto_renderizado, texto_rect)

def dibujar_victorias_jugador(texto, x, y, ancho, alto, color): 
    pygame.draw.rect(ventana, color, (x, y, ancho, alto))
    texto_renderizado = fuente.render("Victorias jugador:  " +texto, True, negro)
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    ventana.blit(texto_renderizado, texto_rect)

def dibujar_victorias_ordenador(texto, x, y, ancho, alto, color): 
    pygame.draw.rect(ventana, color, (x, y, ancho, alto))
    texto_renderizado = fuente.render("Victorias ordenador:  " + texto, True, negro)
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    ventana.blit(texto_renderizado, texto_rect)

# Posiciones y dimensiones de los botones
boton1_x = 75
boton1_y = 100
boton2_x = 300
boton2_y = 100
boton3_x = 550
boton3_y = 100
ancho_boton = 150
alto_boton = 155
ancho_resultado = 200
alto_resultado = 50
x = 280
y = 300
color = negro
rondas_x = 200
rondas_y = 400
jugador_x = 200
jugador_y = 450
ordenador_x = 200
ordenador_y = 500

#lista de opciones para escoger por el ordenador
opciones = ["Piedra", "Papel", "Tijera"]

#resultado
RESULTADO = ""

#Rondas
RONDAS =  0

#Victorias ordenador
VICTORIAS_ORDENADOR =  0

    #Victorias jugador
VICTORIAS_JUGADOR =  0


# Bucle principal del juego
ejecutando = True
while ejecutando:

    


     # Dibujar la ventana y los botones
    ventana.fill(fondo)
    dibujar_boton(imagen_piedra, boton1_x, boton1_y, ancho_boton, alto_boton)
    dibujar_boton(imagen_papel, boton2_x, boton2_y, ancho_boton, alto_boton)
    dibujar_boton(imagen_tijera, boton3_x, boton3_y, ancho_boton, alto_boton)
    dibujar_resultado(RESULTADO, x, y, ancho_resultado, alto_resultado, fondo)
    dibujar_rondas(str(RONDAS), rondas_x, rondas_y, ancho_resultado, alto_resultado, fondo)
    dibujar_victorias_jugador(str(VICTORIAS_JUGADOR), jugador_x, jugador_y, ancho_resultado, alto_resultado, fondo)
    dibujar_victorias_ordenador(str(VICTORIAS_ORDENADOR), ordenador_x, ordenador_y, ancho_resultado, alto_resultado, fondo)


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
                VICTORIAS_JUGADOR += 1
            else:
                RESULTADO = "HAS PERDIDO"
                VICTORIAS_ORDENADOR += 1
            RONDAS += 1
  
            if VICTORIAS_JUGADOR == 5 or VICTORIAS_ORDENADOR == 5 :
                ejecutando = False
