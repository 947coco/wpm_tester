import codecs, pygame

# definition des couleurs primaires/principales
white, black          = (255, 255, 255), (0, 0, 0)
red, green, blue      = (255, 0, 0), (0, 255, 0), (0, 0, 255)
yellow, cyan, magenta = (255, 255, 0), (0, 255, 255), (255, 0, 255)
orange, purple, pink  = (255, 165, 0), (128, 0, 128), (233, 40, 99)

# Creation de la fenetre noir en plein ecran
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window.fill(black) 
pygame.display.set_caption('MPM testeur')

######## Fonctions pour alleger le code ########
elements = {}
def creer_label(nom, couleur, x, y, w, h):
    nom_xy, nom_wh = nom+"_xy", nom+"_wh"
    globals()[nom_xy] = xy_pourcent(x, y)
    globals()[nom_wh] = xy_pourcent(w, h)
    globals()[nom] = pygame.Surface(globals()[nom_wh])
    globals()[nom].fill(couleur)
    window.blit(globals()[nom], globals()[nom_xy])
    elements[nom] = nom_xy
"""
A CORRIGER
def creer_texte(nom, string, couleur, x, y, car_invisible=False):
    nom_xy = nom+"_xy"
    globals()[nom_xy] = xy_pourcent(x, y)
    globals()[nom] = impact.render(string, car_invisible, couleur)
    window.blit(globals()[nom], globals()[nom_xy])
    elements[nom] = nom_xy
# Creation des textes
creer_texte("texte_score", "meilleur score = 0 mpm", white, 1, 1.4)
creer_texte("texte_temps", "30sec", white, 83, 30)
"""
def charger_formes():
    # Afficher tout : label, texte...
    window.fill((0, 0, 0))
    window.blit(ecriture, ecriture_xy)
    window.blit(score, score_xy)
    window.blit(temps, temps_xy)
    window.blit(mpm_actuel, mpm_actuel_xy)
    window.blit(exit, (exit_xy))
    #window.blit(texte_score, texte_score_xy)

def xy_pourcent(X, Y): # x, y convertit selon taille de l'ecran en pourcent
    return int(pygame.display.Info().current_w*X*0.01), int(pygame.display.Info().current_h *Y*0.01)

def choisir_langue(langue): # L'utilisateur choisi sa langue = selection d'un fichier en consequence
    global mots
    fichiertxt = f"Langues/{langue}.txt"
    with codecs.open(fichiertxt, encoding = 'utf-8') as fichier:
        mots = [ligne[:-1] for ligne in fichier.readlines()]
    
# Creation des labels
creer_label("ecriture",cyan ,15, 13, 65, 65)
creer_label("score", green , 0.5, 0.85, 21.5, 8)
creer_label("temps", blue , 83, 30, 15, 10)
creer_label("mpm_actuel", white , 39.6, 87, 20, 10)
creer_label("exit", red , 96, 0, 4, 6)



# Creation des polices d'ecriture
taille_police = 70
comic_sans_ms = pygame.font.SysFont('Comic Sans MS', taille_police)
arial = pygame.font.SysFont('Arial', taille_police)
impact = pygame.font.SysFont('impact', taille_police)





# L'utilisateur choisi une langue
langue_choisie = False
while not langue_choisie:
    langue_choisie = True


# loop back pour verifier les evenements clavier
continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
            # Bouton exit
            if exit_xy[0] <= evenement.pos[0] <= exit_xy[0] + exit_wh[0] and exit_xy[1] <= evenement.pos[1] <= exit_xy[1] + exit_wh[1]:
                continuer = False
            # Bouton temps 
            elif temps_xy[0] <= evenement.pos[0] <= temps_xy[0] + temps_wh[0] and temps_xy[1] <= evenement.pos[1] <= temps_xy[1] + temps_wh[1]:
                print("bouton de temps clique ! ") # Mettre la fonction pour changer le temps de test
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        print("touche z clique")
    if keys[pygame.K_s]:
        print("touche s clique")
        

    # Your game logic here
    
    # Probleme du alt+tab
    charger_formes(), pygame.display.flip()

pygame.quit(), quit()