#MIJADEC / MALANDAIN
# Interface Pygame
# Tout fonctionne
# Reste des choses a améliorer, ( je pourrais le réecrire en beaucoup plus court )
# Il reste à intégrer le crypatge et decryptage, mais je le ferais plus tard car il faut déja pourvoir s'envoyer et recvevoir les clés
# Pour changer le message recu c'est ligne 35 si tu veux faire des tests

import pygame as pg  # ca permet de gagner du temps en ecriture


def reception_cle():
    h = 1


def cryptage_decryptage():
    h = 1


def main():

    # Variable

    # Box
    box = pg.Rect(10, 10, 580, 100)
    box2 = pg.Rect(150, 125, 300, 60)
    box3 = pg.Rect(150, 300, 290, 60)
    input_box = pg.Rect(10, 380, 580, 100)
    box = pg.Rect(10, 10, 580, 100)

    # Couleur
    red = (235, 0, 0)
    blue = (0, 255, 255)
    color_inactif = pg.Color(10, 120, 255)
    color_actif = pg.Color(0, 255, 255)
    color = color_inactif

    # Message
    """Variable pour l'ecriture de nos message"""
    text1 = ("Pas plus de 126 caracteres")  # 1 ere ligne d'affichage du message
    text2 = ""  # 2 eme ligne d'affichage du message
    text3 = ""  # 3 eme ligne d'affichage du message
    text_final = ""  # Le texte qui sera cryptée puis envoyé

    """Variable pour l'affichage de nos message"""
    message_recpu_crypte = ("")  # Ce sera le message recu
    message_recu_decrypte = (
        "1234567891235656789123456789123456789123565678912345678912345678912356567891234567891234567891235656789123456789")  # 126 caractere

    message_recu_1 = message_recu_decrypte[0:42]
    message_recu_2 = message_recu_decrypte[42:84]
    message_recu_3 = message_recu_decrypte[84:126]

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    # Varaible Pygame + condition
    done = False
    screen = pg.display.set_mode((600, 500))
    screen = pg.display.set_mode((600, 500))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    condition = False
    active = False
    test = 0

    while not done:  # Boucle d'evenement
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:

                # Cadre de l'input box, change sa couleur
                if input_box.collidepoint(event.pos):
                    if condition == False:
                        text1 = ""
                        condition = True
                    actif = not active
                else:
                    actif = False
                color = color_actif if actif else color_inactif

            if event.type == pg.KEYDOWN:
                if actif:
                    test = 0
                    if event.key == pg.K_RETURN:  # reset apres l'envoie
                        if text_final != '':
                            print(text_final)
                            text1 = ('')
                            text2 = ('')
                            text3 = ('')
                            text_final = ("")

                    elif event.key == pg.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text_final += event.unicode  # Le texte qui sera cryptée puis envoyé
                        """event.unicode permet de retranscrire le caractere taper au clavier"""
                        if len(text_final) <= 42:
                            text1 += event.unicode
                        if len(text_final) > 42 and len(text_final) < 84:
                            text2 += event.unicode
                        if len(text_final) >= 84 and len(text_final) <= 126:
                            text3 += event.unicode

                        if len(text_final) >= 126:
                            text3 = text3[:-1]  # Retire le dernier caractere
                            # Retire le dernier caractere
                            text_final = text_final[:-1]

        # Affichage

        screen.fill((30, 40, 30))

        """Ici c'est pour l'input box, la boite ou l'on ecrit notre message"""
        txt_surface1 = font.render(
            text1, True, color)  # font.render fait le rendu, tout simplement, on entre le texte, l'activation de l'aliasing, et sa couleur
        txt_surface2 = font.render(text2, True, color)
        txt_surface3 = font.render(text3, True, color)

        # Affiche le Text dans l'input box, Les 3 lignes ici represente les 3 lignes d'ecriture
        screen.blit(txt_surface1, (input_box.x + 5, input_box.y + 10))
        screen.blit(txt_surface2, (input_box.x + 5, input_box.y + 40))
        screen.blit(txt_surface3, (input_box.x + 5, input_box.y + 70))
        pg.draw.rect(screen, color, input_box, 4)  # Cadrre de l'input box

        """Ici c'est pour afficher le message recu """
        message_surface1 = font.render(
            message_recu_1, True, red)  # font.render fait le rendu, tout simplement, on entre le texte, l'activation de l'aliasing, et sa couleur
        message_surface2 = font.render(message_recu_2, True, red)
        message_surface3 = font.render(message_recu_3, True, red)

        # Les 3 lignes ici represente les 3 lignes d'ecriture dans la boite de reception
        screen.blit(message_surface1, (box.x + 5, box.y + 10))
        screen.blit(message_surface2, (box.x + 5, box.y + 40))
        screen.blit(message_surface3, (box.x + 5, box.y + 70))
        pg.draw.rect(screen, red, box, 4)  # Cadre de la box de reception

        # Box Message recu + Message à envoyé

        txt_reception = font.render("Message Reçu", True, red)
        screen.blit(txt_reception, (225, 145))
        pg.draw.rect(screen, red, box2, 3)

        txt_reception = font.render("Message à Envoyé", True, blue)
        screen.blit(txt_reception, (200, 320))
        pg.draw.rect(screen, blue, box3, 3)

        pg.display.flip()
        clock.tick(60)


pg.init()
main()
pg.quit()
