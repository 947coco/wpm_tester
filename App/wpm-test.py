import codecs, pygame as codecs, pygame

# définition des couleurs primaires/principales
white, black = (255, 255, 255), (0, 0, 0)
green, blue, red = (0, 255, 0), (0, 0, 255), (255, 0, 0)

# Creation de la fenetre noir en plein ecran
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
window.fill(black) 
pygame.display.set_caption('mpm testeur')

# dimension x et y de l'ecran de l'utilisateur
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h 

# Valeurs x et y en % convertit selon les dimensions de l'écran
def xy_pourcent(X=0, Y=0): return int(screen_width*X*0.01), int(screen_height*Y*0.01)

# Charger une police d'ecriture
def police(nom_police, taille): return pygame.font.SysFont(nom_police, taille)

# L'utilisateur choisi sa langue = selection d'un fichier en consequence

def choisir_langue(langue):
    global mots # pouvoir acceder a la liste mots partout
    fichiertxt = f"Langues/{langue}.txt"
    with codecs.open(fichiertxt, encoding = 'utf-8') as fichier:
        mots = [ligne[:-1] for ligne in fichier.readlines()]

# Création du label meilleur_score
meilleur_score_xy, meilleur_score_wh = xy_pourcent(0.5, 0.85), xy_pourcent(20, 8)
meilleur_score = pygame.Surface(meilleur_score_wh)
meilleur_score.fill(green)
window.blit(meilleur_score, meilleur_score_xy)

# Création du label temps
temps_xy, temps_wh = xy_pourcent(83, 30), xy_pourcent(15, 10)
temps = pygame.Surface((temps_wh))
temps.fill(blue)
window.blit(temps, (temps_xy))

# Création du label mpm_actuel
mpm_actuel_xy, mpm_actuel_wh =  xy_pourcent(40, 87), xy_pourcent(20, 10)
mpm_actuel = pygame.Surface(mpm_actuel_wh)
mpm_actuel.fill(white)
window.blit(mpm_actuel, mpm_actuel_xy)


# Création du bouton exit
exit_xy = xy_pourcent(97, -1)
exit_wh = xy_pourcent(6, 6)
exit = pygame.Surface((exit_wh))
exit.fill(red)
window.blit(exit, (exit_xy))

# Création d'un texte
comic_sans_ms = police('Comic Sans MS', 55)
arial = police('Arial', 55)
impact = police('impact', 55)
texte_meilleur_score = impact.render('Meilleur score', False, white)
window.blit(texte_meilleur_score, (35,30))
"""
# Charger le logo
image_xy, image_wh = xy_pourcent(44, 2), xy_pourcent(12, 22)
image = pygame.image.load('Images/logo.png').convert_alpha()
logo = pygame.transform.scale(image, (image_wh))
window.blit(logo, image_xy)
"""
# Afficher tout : label, texte...
# loop back pour vérifier les évenements clavier
while True:
    pygame.display.update()
    for evenement in pygame.event.get():
        if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
            if exit_xy[0] <= evenement.pos[0] <= exit_xy[0] + exit_wh[0] and exit_xy[1] <= evenement.pos[1] <= exit_xy[1] + exit_wh[1]:
                pygame.quit()
                quit()
        if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
            if temps_xy[0] <= evenement.pos[0] <= temps_xy[0] + temps_wh[0] and temps_xy[1] <= evenement.pos[1] <= temps_xy[1] + temps_wh[1]:
                print("bouton de temps clique ! ") # Mettre la fonction pour changer le temps de test
        
