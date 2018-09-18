import pygame
from random import *
from pygame.locals import *


#fonction habitant
def habitant(position_point_rouge_x, position_point_rouge_y, position_cercle_x,position_cercle_y, onde_sonore):
	entendu=False
	if position_point_rouge_x<position_cercle_x + onde_sonore and position_point_rouge_x>position_cercle_x - onde_sonore and position_point_rouge_y<position_cercle_y + onde_sonore and position_point_rouge_y>position_cercle_y-onde_sonore:
		print(onde_sonore)
		entendu=True
	return entendu

#fonction affichage du cercle
def cercle_onde_sonore (fenetre, position_cercle_x, position_cercle_y, onde_sonore, nbr_alea):
	RED = (255,0,0)
	epaisseur=1

	#Taille de l'onde sonore
	if nbr_alea==1:
		onde_sonore=40
	if nbr_alea==2:
		onde_sonore=80
	if nbr_alea==3:
		onde_sonore=140

	pygame.draw.circle(fenetre, RED,(position_cercle_x, position_cercle_y), onde_sonore, epaisseur)
	return onde_sonore

#fonction maj_jauge
def maj_score(nbr_alea, score):
#le score depend du caca qui est sortie. Si caca de type 1, alors jauge = -10. Si caca =2, alors jauge = -20, si caca =3, alors jauge =-30.
	score_fct=score
	if nbr_alea==1:
		score_fct=score_fct-10
	if nbr_alea==2:
		score_fct=score_fct-20
	if nbr_alea==3:
		score_fct=score_fct-30
	if score_fct<0:
		score_fct=0
	return score_fct


font_name = pygame.font.match_font('arial')
#fonction dessiner un rectangle avec du text
def draw_text(surf, text, size, x, y):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, (255,255,255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)


#fonction deplacement aleatoire point rouge
def deplacement_aleatoire_point_rouge(position_point_rouge_x, position_point_rouge_y, largeur_fenetre, hauteur_fenetre):
	nombre_aleatoire=randint(1,4)

	if nombre_aleatoire==1:
		position_point_rouge_x+=5
	if nombre_aleatoire==2:
		position_point_rouge_y+=5
	if nombre_aleatoire==3:
		position_point_rouge_x-=5
	if nombre_aleatoire==4:
		position_point_rouge_y-=5

	if position_point_rouge_x >= largeur_fenetre:
		position_point_rouge_x=0
	elif position_point_rouge_x<=0:
		position_point_rouge_x=largeur_fenetre
	elif position_point_rouge_y>= hauteur_fenetre: 
		position_point_rouge_y=0
	elif position_point_rouge_y<=0:
		position_point_rouge_y=hauteur_fenetre

	return position_point_rouge_x, position_point_rouge_y
	#return position_point_rouge_x, position_point_rouge_y

#fonction choix du caca
def caca(nbr_alea):
	#son=pygame.mixer.Sound("resources/sounds/pet_chiasseux.wav")
	if nbr_alea==1:
		#prout 1
		son=pygame.mixer.Sound("resources/sounds/pet_normal.wav")
		#prout 2
	if nbr_alea==2:	
		son=pygame.mixer.Sound("resources/sounds/pet_chiasseux.wav")
		#prout3
	if nbr_alea==3:	
		son=pygame.mixer.Sound("resources/sounds/pet_immonde.wav")
	return son

