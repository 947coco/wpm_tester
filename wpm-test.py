import pygame as pygame

# définition des couleurs primaires/principales
white, black = (255, 255, 255), (0, 0, 0)
green, blue, red = (0, 255, 0), (0, 0, 255), (255, 0, 0)

pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE) # fenetre en plein ecran
window.fill(black) # couleur de l'arriere plan
pygame.display.set_caption('mpm testeur') # Titre de la fenetre

# dimension x et y de l'ecran de l'utilisateur
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h 

# Valeurs x et y en % convertit selon les dimensions de l'écran
def xy_pourcent(X=0, Y=0): 
    return int(screen_width*X*0.01), int(screen_height*Y*0.01)

# L'utilisateur choisi sa langue = selection d'un fichier en consequence
def choisir_langue(langue):
    global mots # pouvoir acceder a la liste mots partout
    fichiertxt = {"fr": "Langue/francais.txt", "en": "Langue/english.txt"}
    mots = [mot for ligne in open(fichiertxt[langue], "r") for mot in ligne.split()]




# Création du label meilleur_score
meilleur_score = pygame.Surface(xy_pourcent(14, 8))
meilleur_score.fill(green)
window.blit(meilleur_score, xy_pourcent(1, 1))

# Création du label temps
btn_temps_x, btn_temps_y = xy_pourcent(83, 30)
btn_temps_w, btn_temps_h = xy_pourcent(15, 10)
temps = pygame.Surface((btn_temps_w, btn_temps_h))
temps.fill(blue)
window.blit(temps, (btn_temps_x, btn_temps_y))

# Création du label mpm_actuel
mpm_actuel = pygame.Surface(xy_pourcent(20, 10))
mpm_actuel.fill(white)
window.blit(mpm_actuel, xy_pourcent(40, 87))

# Création du bouton exit
btn_exit_x, btn_exit_y = xy_pourcent(97, -1)
btn_exit_w, btn_exit_h = xy_pourcent(6, 6)
mpm_actuel = pygame.Surface((btn_exit_w, btn_exit_h))
mpm_actuel.fill(red)
window.blit(mpm_actuel, (btn_exit_x, btn_exit_y))

# Création d'un texte
texte_meilleur_score = 0
font = pygame.font.SysFont('Comic Sans MS', 55)
texte_meilleur_score = font.render('Meilleur score', False, white)
window.blit(texte_meilleur_score, (35,30))

# Chargement de l'image (chemin absolu vers votre fichier d'image)
img = pygame.image.load('Images/logo.png')
fenetre = img.get_rect()
fenetre.size = (640, 480)


# loop back pour vérifier les évenements clavier
while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
            if btn_exit_x <= evenement.pos[0] <= btn_exit_x + btn_exit_w and btn_exit_y <= evenement.pos[1] <= btn_exit_y + btn_exit_h:
                pygame.quit()
                quit()
        if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
            if btn_temps_x <= evenement.pos[0] <= btn_temps_x + btn_temps_w and btn_temps_y <= evenement.pos[1] <= btn_temps_y + btn_temps_h:
                pygame.quit()
                quit()
        pygame.display.update()
        

