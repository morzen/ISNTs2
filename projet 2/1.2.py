#Mini Pojet ISN 09/01/2018
#MIJADEC Martin & MALANDAIN BARNABE


from PIL import Image
import pygame
from pygame.locals import *

def menu_cases():
    pygame.draw.rect(screen,BLACK,(100,95,200,290))
    pygame.draw.rect(screen,BLACK,(100,395,200,100))
    pygame.draw.rect(screen,BLACK,(30,15,160,60))
    pygame.draw.rect(screen,BLACK,(210,15,160,60))

    pygame.draw.rect(screen,WHITE,(105,100,190,90))
    pygame.draw.rect(screen,WHITE,(105,195,190,90))
    pygame.draw.rect(screen,WHITE,(105,290,190,90))
    pygame.draw.rect(screen,WHITE,(105,400,190,90))


    pygame.draw.rect(screen,RED,(35,20,150,50))
    pygame.draw.rect(screen,RED,(215,20,150,50))



def menu_vignette():
    screen.blit(Negatif, (160, 140))
    screen.blit(Detection_des, (135, 220))
    screen.blit(contours, (160, 240))
    screen.blit(Seuillage, (160, 320))
    screen.blit(validation, (150, 430))
    screen.blit(Importer,(65,35))
    screen.blit(Sauve,(225,35))

def select_fichier(y,z):
    if y==True:
        pygame.draw.rect(screen,G,(35,20,150,50))


    if z==True:
        pygame.draw.rect(screen,G,(215,20,150,50))

    menu_vignette()


def select_menu(x):
    menu_cases()
    if x==1:
        pygame.draw.rect(screen,G,(105,100,190,90))

    if x==2:
        pygame.draw.rect(screen,G,(105,195,190,90))

    if x==3:
        pygame.draw.rect(screen,G,(105,290,190,90))

    menu_vignette()



def lancement(x,y,z):

    if x==1 and y==True and z==True:
        print("Sélection validée!")

        Image1 = Image.open(Image_origine) #Ouvre l'image que l'utilisateur a choisit
        Largeur, Hauteur = Image1.size        #Définition de la taille de l'image (exemple 680*560)
        Image2 = Image.new("RGB",(Largeur,Hauteur))    #Création d'une nouvelle image qui reprend la taille de l'image d'origine

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


    if x==2 and y==True and z==True:
        print("Sélection validée!")


        Image1 = Image.open(Image_origine) #Ouvre l'image que l'utilisateur a choisit
        Largeur, Hauteur = Image1.size        #Définition de la taille de l'image (exemple 680*560)
        Image2 = Image.new("RGB",(Largeur,Hauteur))    #Création d'une nouvelle image qui reprend la taille de l'image d'origine

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


    if x==3 and y==True and z==True:
        print("Sélection validée!")


        Image1 = Image.open(Image_origine) #Ouvre l'image que l'utilisateur a choisit
        Largeur, Hauteur = Image1.size        #Définition de la taille de l'image (exemple 680*560)
        Image2 = Image.new("RGB",(Largeur,Hauteur))    #Création d'une nouvelle image qui reprend la taille de l'image d'origine
        Seuil=int(input("Définir le seuil (Entre 0 et 255 )"))
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




#############################################################################

pygame.init()
pygame.display.set_caption("Mini projet MIJADEC MARTIN & MALANDAIN BARNABE")

#############################################################################
#Variable
GREY=(145,160,255)
WHITE=(145,200,200)
BLACK=(0,0,0)
RED=(255,0,0)
G=(0,255,0)

font=pygame.font.Font(None, 30)

Negatif = font.render("Negatif",1,BLACK)
Detection_des=font.render("Détection des",1,BLACK)
contours=font.render("contours",1,BLACK)
Seuillage=font.render("Seuillage",1,BLACK)
validation=font.render("Validation",1,BLACK)
Importer=font.render("Importer",1,BLACK)
Sauve=font.render("Sauvegarder",1,BLACK)

condi1=False
condi2=False
select=False
choix=0
validation_boutton=False

stop = False

#############################################################################

#Programme princi
screen = pygame.display.set_mode((400 , 500),)
screen.fill(GREY)

menu_cases()
select_fichier(condi1,condi2)
menu_vignette()
jpg=".jpg"


while stop==False:
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            print("Fermeture!")
            stop=True

        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 105+190 > mouse[0] > 105 and 100+90 > mouse[1] > 100:
            print("Menu sélection Négatif!")
            select=1


        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 105+190 > mouse[0] > 105 and 190+90 > mouse[1] > 190:
            print("Menu sélection Detection des contours!")
            select=2


        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 105+190 > mouse[0] > 105 and 290+90 > mouse[1] > 290:
            print("Menu sélection Seuillage!")
            select=3

        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 35+150 > mouse[0] > 35 and 20+50 > mouse[1] > 20:
            Image_origine=input(("Entrer le nom de votre image ( avec son format exemple : image.jpeg ) : "))+jpg
            print(Image_origine,"sélectionné!")
            condi1=True



        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 215+150 > mouse[0] > 215 and 20+50 > mouse[1] > 20:
            Image_modifier=input("Entrer le nom de l'image après traitement ( avec son format exemple : image.jpeg ) :")+jpg
            print(Image_modifier,"déterminé!")
            condi2=True



        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 105+190 > mouse[0] > 80 and 400+90 > mouse[1] > 400 :
            lancement(select,condi1,condi2)
            condi2=False


        select_menu(select)
        select_fichier(condi1,condi2)


        pygame.display.update()


pygame.quit()



