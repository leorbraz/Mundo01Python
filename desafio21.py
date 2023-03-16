import pygame

pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('LetsGo3.mp3.mp3')
pygame.mixer.music.pause(loops=0, start=0.0)
pygame.event.wait()
