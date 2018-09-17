import pygame
from random import *
from pygame.locals import *
import fonction

# Initialiser les modules de Pygame
pygame.init()

#OUvrir une fenetre
hauteur_fenetre=800
largeur_fenetre=1000
fenetre=pygame.display.set_mode((largeur_fenetre,hauteur_fenetre), RESIZABLE)

#Charger un fond d'ecran dans la fenetre
#Affichage du fond d'ecran
fond = pygame.image.load("fond_r.png").convert()
fenetre.blit(fond, (0,0))


#deplacement point bleu
taille_sprite=24
position_point_bleu_x=taille_sprite
position_point_bleu_y=taille_sprite

point_bleu = pygame.image.load("perso_redim.png").convert_alpha()
mur=pygame.image.load("carre-noir_redim.png").convert()

#on ouvre le fichier text et on place dans une liste_maison chaque info sur le txt. 
with open("n1.txt", "r") as fichier:
            liste_maison = []
            #On parcourt les lignes du fichier
            for ligne in fichier:
                liste_maison_ligne = []
                #On parcourt les sprites (lettres) contenus dans le fichier. On aurait pu dire i plutot que sprite.
                for sprite in ligne:
                    #On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        #On ajoute le sprite a la liste de la ligne
                        liste_maison_ligne.append(sprite)
                #On ajoute la ligne a la liste du niveau
                liste_maison.append(liste_maison_ligne)
            #On sauvegarde cette structure
            structure = liste_maison

num_ligne = 0

#cette boucle permet d'afficher sur la fenetre les points rouges en fonction de la taille des sprites (des points rouges).
for ligne in structure:
    #On parcourt les listes de lignes
    num_case = 0

    for sprite in ligne:
        #On calcule la position reelle en pixels
        x = num_case * taille_sprite
        y = num_ligne * taille_sprite
        #si info ligne = m alors i y a un mur
        if sprite == 'm':          #m = Mur
            fenetre.blit(mur, (x,y))
        num_case += 1
    num_ligne += 1

#fonction qui reprend la boucle precedente
def afficher(fenetre):
    """Methode permettant d'afficher le niveau en fonction 
    de la liste de structure renvoyee par generer()"""
    #Chargement des images (seule celle d'arrivee contient de la transparence)

    mur = pygame.image.load("carre-noir_redim.png").convert()
    #On parcourt la liste du niveau
    num_ligne = 0

    for ligne in structure:
        #On parcourt les listes de lignes
        num_case = 0
        for sprite in ligne:

            #On calcule la position reelle en pixels

            x = num_case * taille_sprite

            y = num_ligne * taille_sprite

            if sprite == 'm':          #m = Mur
                fenetre.blit(mur, (x,y))
            num_case += 1
        num_ligne += 1    


image_gagne = pygame.image.load("gagne.jpeg").convert()

#On enpile le fond sur la fenetre pour l'afficher
#la fonction blit prend en argument 1) l'image a coller et 2) les coordonnees pour coller l'image

#ajout du son
#son=pygame.mixer.Sound("442.wav")
#joue =0 si pas de son
joue=0

#Definition de l'onde sonore, qui est une distance en px (10px=1m dans la maison)
onde_sonore=100

#Position de l'onde sonore	
position_cercle_x=250
position_cercle_y=250

#Affiche de perdu
nb_victoire=0
nb_defaite=0
image_perdu=pygame.image.load("perdu.png").convert_alpha()

#Creation de la jauge + fct de mise a jour de la jauge et de son affichage
score=100
myfont=pygame.font.SysFont("monospace",25)
score_display=myfont.render(str(score),1, (0,0,0))
position_jauge_x=700
position_jauge_y=100
fenetre.blit(score_display, (position_jauge_x,position_jauge_y))
fenetre.blit(point_bleu, (position_point_bleu_x, position_point_bleu_y))


#mise a jour de la fenetre
pygame.display.flip()

pygame.key.set_repeat(400, 30)

case_x=1
case_y=1
#deplacement du personnage
#evenement clavier
continuer_menu = 1
continuer_jeu=1

#BOUCLE JEU
while continuer_menu:

	#appuyer sur espace pour jouer
	fonction.draw_text(fenetre, "Appuyez sur espace pour jouer", 30, 300, 300)
	pygame.display.flip()

	
	for event in pygame.event.get():
			
			if event.type==QUIT:

				continuer_menu=0
				continuer_jeu=0

			if event.type==KEYDOWN:
				if event.key==K_SPACE:
					
					continuer_jeu=1
					
					position_point_bleu_x=24
					position_point_bleu_y=24
					
					score=100
					case_x=1
					case_y=1

					#mise a jour de l'image
					#recollage du fond
					fenetre.blit(fond, (0,0))
					#remerttre perso avec nouvelles coordonees
					#fenetre.blit(perso, position_perso)
					fenetre.blit(point_bleu, (position_point_bleu_x,position_point_bleu_y))
					#reafficher avec flip
					pygame.display.flip()

	while continuer_jeu:

		#deplacement aleatoire du point rouge
		#position_point_bleu_x, position_point_bleu_x=fonction.deplacement_aleatoire_point_rouge(position_point_bleu_x, position_point_bleu_y, largeur_fenetre, hauteur_fenetre)
		nombre_alea=randint(1,4)

		if nombre_alea==1:
		#if event.key==K_DOWN:
		#en bas
			if case_y<14:
				if liste_maison[case_y+1][case_x]=='0':
					position_point_bleu_y += taille_sprite
					case_y+=1
					print(position_point_bleu_x)


		if nombre_alea==2:
		#if event.key == K_UP:
		#en haut
			if case_y>0:
				if liste_maison[case_y-1][case_x]=='0':
					position_point_bleu_y -= taille_sprite
					case_y-=1
					print(position_point_bleu_x)
					#print(case_y)


		if nombre_alea==3:
		#if event.key == K_RIGHT:
		#droite
			if case_x<14:
				if liste_maison[case_y][case_x+1]=='0':
					position_point_bleu_x += taille_sprite
					case_x+=1
					print(position_point_bleu_x)

		if nombre_alea==4:
		#if event.key == K_LEFT:
		#gauche 
			if case_x>0:
				if liste_maison[case_y][case_x-1]=='0':
					position_point_bleu_x -= taille_sprite
					case_x-=1
					print(position_point_bleu_x)

		for event in pygame.event.get():
			
			if event.type==QUIT:

				continuer_menu=0
				continuer_jeu=0

			if event.type == KEYDOWN:

				if event.key==K_SPACE:
					continuer_jeu=0

			#bruit quand clic gauche
			if event.type==MOUSEBUTTONDOWN and event.button == 1:
				
				#Initialisation des variables
				onde_sonore=20
				nbr_alea=randint(1, 3)
				
				#Choix du caca + du son
				son=fonction.caca(nbr_alea)
				son.play()
				#recuperation de l'onde sonore en fonction du caca
				onde_sonore=fonction.cercle_onde_sonore(fenetre,position_cercle_x, position_cercle_y,onde_sonore, nbr_alea)

				#Affichage du cercle sonore
				fonction.cercle_onde_sonore(fenetre,position_cercle_x, position_cercle_y,onde_sonore, nbr_alea)
				#Mise a jour du score
				score=fonction.maj_score(nbr_alea, score)
				#print(score)
				if score==0:
					print("gagne")
					fenetre.blit(image_gagne, (200,200))
					continuer_jeu=0
					nb_victoire+=1
			
				entendu = fonction.habitant(position_point_bleu_x, position_point_bleu_y, position_cercle_x,position_cercle_y,onde_sonore)				
				if entendu==True:
					print("entendu, perdu")
					fenetre.blit(image_perdu, (200,200))
					continuer_jeu=0
					nb_defaite+=1
				
				#fonction.cercle_onde_sonore(fenetre,position_cercle_x, position_cercle_y,onde_sonore, nbr_alea)
				pygame.display.flip()
				pygame.time.delay(500)

		#mise a jour de l'image
		fenetre.blit(fond, (0,0))
		fonction.draw_text(fenetre, str(score), 18, 500, 100)
		fonction.draw_text(fenetre, str(nb_victoire), 18, 600, 50)
		fonction.draw_text(fenetre, str(nb_defaite), 18, 600, 100)

		fenetre.blit(point_bleu, (position_point_bleu_x,position_point_bleu_y))
		#pygame.display.flip()
		#pygame.time.delay(100)
		afficher(fenetre)
		pygame.display.flip()
		pygame.time.delay(500)