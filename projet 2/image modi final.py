# Créé par barnm_u01082h, le 02/01/2018 en Python 3.2
# Créé par barnm_u01082h, le 02/01/2018 en Python 3.2
from PIL import Image
import pygame
from pygame.locals import *
from tkinter import filedialog
from tkinter import *
import os, subprocess, shutil
from collections import Counter
import PIL.Image
import PIL.ImageTk
from tkinter import *

def parcourir():
    sel_dir=""
    fichier=[]
    sel_dir=filedialog.askopenfilename(title = "veuiller choisir votre fichier",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    fichier=(sel_dir.split("/"))
    print(fichier)
    pic=fichier[len(fichier)-1]
    print(pic)
    return(pic)
#print(sel_dir)


jpg=".jpg"

def menu_cases():
    pygame.draw.rect(screen,BLACK,(100,95,200,100))
    pygame.draw.rect(screen,BLACK,(100,190,200,100))
    pygame.draw.rect(screen,BLACK,(100,285,200,100))

    pygame.draw.rect(screen,WHITE,(105,100,190,90))
    pygame.draw.rect(screen,WHITE,(105,195,190,90))
    pygame.draw.rect(screen,WHITE,(105,290,190,90))

def menu_vignette():
    screen.blit(Negatif, (160, 140))
    screen.blit(Detection_des, (135, 220))
    screen.blit(contours, (160, 240))
    screen.blit(Seuillage, (160, 320))

def select_menu(x):
    if x==1:
        pygame.draw.rect(screen,G,(105,100,190,90))
        pygame.draw.rect(screen,WHITE,(105,195,190,90))
        pygame.draw.rect(screen,WHITE,(105,290,190,90))
        menu_vignette()

    if x==2:
        pygame.draw.rect(screen,G,(105,195,190,90))
        pygame.draw.rect(screen,WHITE,(105,100,190,90))
        pygame.draw.rect(screen,WHITE,(105,290,190,90))
        menu_vignette()

    if x==3:
        pygame.draw.rect(screen,G,(105,290,190,90))
        pygame.draw.rect(screen,WHITE,(105,100,190,90))
        pygame.draw.rect(screen,WHITE,(105,195,190,90))
        menu_vignette()

    return()

def lancement(x,y, pic):
    if x==1 and y==True:
        Image_origine=path#input("Entrer le nom de votre image ( avec son format exemple : image.jpeg")
        ##Image_origine=sel_dir
        #Image_origine=Image_origine + jpg
        Image_modifier=input("Entrer le nom de l'image apres la détection des contours")
        Image_modifier=Image_modifier + jpg

        Image1 = PIL.Image.open(Image_origine) #Ouvre l'image que l'utilisateur a choisit
        Largeur, Hauteur = Image1.size        #Définition de la taille de l'image (exemple 680*560)
        Image2 = PIL.Image.new("RGB",(Largeur,Hauteur))    #Création d'une nouvelle image qui reprend la taille de l'image d'origine

        x=0 #Axe x de l'image
        while x<Largeur-1: #Boucle tant que x est inférieur à la largeur-1 de l image alors...
            y=0 #Axe y de l'image
            while y<Hauteur-1: #Boucle tant que y est inférieur à la largeur-1 de l image alors...

                p = Image1.getpixel((x,y)) #Prend chauqe pixel en fonction de leurs colonne et ligne et donne leur couleur ( 255=blanc, 0=noir)

                p=255-p #Soustraction pour inverser la couleur

                Image2.putpixel((x,y),(p,p,p))#Remplacement des pixels de la nouvelle image par les pixels de l'image d'origine apres traitement

                y+=1 #Ajoute +1 pour passer à une autre ligne
            x+=1    #Ajoute +1 pour passer à une autre colonne

        Image2.save(Image_modifier)    #Sauvegarde de la nouvelle image
        Image2.show()                  #Ouverture de la nouvelle image

    if x==2 and y==True:
        Image_origine=path#input("Entrer le nom de votre image ( avec son format exemple : image.jpeg")
        #Image_origine=Image_origine + jpg
        Image_modifier=input("Entrer le nom de l'image apres la détection des contours")
        Image_modifier=Image_modifier + jpg

        Image1 = PIL.Image.open(Image_origine) #Ouvre l'image que l'utilisateur a choisit
        Largeur, Hauteur = Image1.size        #Définition de la taille de l'image (exemple 680*560)
        Image2 = PIL.Image.new("RGB",(Largeur,Hauteur))    #Création d'une nouvelle image qui reprend la taille de l'image d'origine

        x=1 #Axe x de l'image ( ici x=1 car la 1ere ligne doit sauter)
        while x<Largeur-1: #Boucle tant que x est inférieur à la largeur-1 de l image alors...
            y=1 #Axe y de l'image ( ici y=1 car la 1ere ligne doit sauter)
            while y<Hauteur-1: #Boucle tant que y est inférieur à la largeur-1 de l image alors...

                p1 = Image1.getpixel((x,y))            #Utilisation de la matrice
                p2 = Image1.getpixel((x,y+1))
                p3 = Image1.getpixel((x+1,y))
                p4 = Image1.getpixel((x,y-1))
                p5 = Image1.getpixel((x-1,y))
                p6 = Image1.getpixel((x-1,y+1))
                p7 = Image1.getpixel((x+1,y+1))
                p8 = Image1.getpixel((x+1,y-1))
                p9 = Image1.getpixel((x-1,y-1))

                p=8*p1-p2-p3-p4-p5-p6-p7-p8-p9

                Image2.putpixel((x,y),(p,p,p))#Remplacement des pixels de la nouvelle image par les pixels de l'image d'origine apres traitement

                y+=1 #Ajoute +1 pour passer à une autre ligne
            x+=1    #Ajoute +1 pour passer à une autre colonne

        Image2.save(Image_modifier)    #Sauvegarde de la nouvelle image
        Image2.show()                  #Ouverture de la nouvelle image

    if x==3 and y==True:
        Image_origine=path#input("Entrer le nom de votre image ( avec son format exemple : image.jpeg")
        #Image_origine=Image_origine + jpg
        Image_modifier=input("Entrer le nom de l'image apres la détection des contours")
        Image_modifier=Image_modifier + jpg

        Seuil=int(input("Définir le Seuil :"))

        Image1 = PIL.Image.open(Image_origine) #Ouvre l'image que l'utilisateur a choisit
        Largeur, Hauteur = Image1.size        #Définition de la taille de l'image (exemple 680*560)
        Image2 = PIL.Image.new("RGB",(Largeur,Hauteur))    #Création d'une nouvelle image qui reprend la taille de l'image d'origine

        x=0 #Axe x de l'image
        while x<Largeur-1: #Boucle tant que x est inférieur à la largeur-1 de l image alors...
            y=0 #Axe y de l'image
            while y<Hauteur-1: #Boucle tant que y est inférieur à la largeur-1 de l image alors...

                p = Image1.getpixel((x,y)) #Prend chauqe pixel en fonction de leurs colonne et ligne et donne leur couleur ( 255=blanc, 0=noir)

                if p<Seuil :
                    p=255

                else :
                    p=0

                Image2.putpixel((x,y),(p,p,p))#Remplacement des pixels de la nouvelle image par les pixels de l'image d'origine apres traitement

                y+=1 #Ajoute +1 pour passer à une autre ligne
            x+=1    #Ajoute +1 pour passer à une autre colonne

        Image2.save(Image_modifier)    #Sauvegarde de la nouvelle image
        Image2.show()                  #Ouverture de la nouvelle image



def validation_bouton():
    pygame.draw.rect(screen,BLACK,(100,395,200,100))
    pygame.draw.rect(screen,WHITE,(105,400,190,90))
    screen.blit(validation, (150, 430))


#############################################################################

pygame.init()
pygame.display.set_caption("Mini projet MIJADEC MARTIN & MALANDAIN BARNABE")

#############################################################################
#Variable
GREY=(145,160,255)
WHITE=(145,200,200)
BLACK=(0,0,0)
G=(0,255,0)

font=pygame.font.Font(None, 30)

Negatif = font.render("Negatif",1,BLACK)
Detection_des=font.render("Détection des",1,BLACK)
contours=font.render("contours",1,BLACK)
Seuillage=font.render("Seuillage",1,BLACK)
validation=font.render("Validation",1,BLACK)

select=False
choix=0
condition=False

stop = False

#############################################################################

#Programme princi
screen = pygame.display.set_mode((400 , 500),)
screen.fill(GREY)

path = parcourir()
menu_cases()
menu_vignette()

while stop==False:
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            stop = True

        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 105+190 > mouse[0] > 105 and 100+90 > mouse[1] > 100:
            print("Menu sélection Négatif")
            select=1

        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 105+190 > mouse[0] > 105 and 190+90 > mouse[1] > 190:
            print("Menu sélection Detection des contours")
            select=2

        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 105+190 > mouse[0] > 105 and 290+90 > mouse[1] > 290:
            print("Menu sélection Seuillage")
            select=3

        if select==1 or select==2 or select==3 :
            validation_bouton()

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 105+190 > mouse[0] > 80 and 400+90 > mouse[1] > 400:
                condition=True
                stop=True
                print("Sélection validée")

        select_menu(select)

        lancement(select,condition, path)

        pygame.display.update()


pygame.quit()
