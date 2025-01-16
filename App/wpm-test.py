import codecs, pygame

# définition des couleurs primaires/principales
white, black = (255, 255, 255), (0, 0, 0)
green, blue, red = (0, 255, 0), (0, 0, 255), (255, 0, 0)

# Creation de la fenetre noir en plein ecran
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window.fill(black) 
pygame.display.set_caption('MPM testeur')

# dimension x et y de l'ecran de l'utilisateur
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h 

def xy_pourcent(X=0, Y=0): return int(screen_width*X*0.01), int(screen_height*Y*0.01)# x, y convertit selon de l'écran

def police(nom_police, taille): return pygame.font.SysFont(nom_police, taille) # Police d'ecriture

# L'utilisateur choisi sa langue = selection d'un fichier en consequence
def choisir_langue(langue):
    global mots # pouvoir acceder a la liste mots partout
    fichiertxt = f"Langues/{langue}.txt"
    with codecs.open(fichiertxt, encoding = 'utf-8') as fichier:
        mots = [ligne[:-1] for ligne in fichier.readlines()]

def charger_formes():
    # Afficher tout : label, texte...
    window.fill((0, 0, 0))
    window.blit(score, score_xy)
    window.blit(temps, temps_xy)
    window.blit(mpm_actuel, mpm_actuel_xy)
    window.blit(exit, (exit_xy))
    window.blit(texte_score, texte_score_xy)
    
    
# Création du label score
score_xy, score_wh = xy_pourcent(0.5, 0.85), xy_pourcent(21.5, 8) # Position et taille
score = pygame.Surface(score_wh) # Creer le label
score.fill(green) # Remplir de couleur   

# Création du label temps
temps_xy, temps_wh = xy_pourcent(83, 30), xy_pourcent(15, 10)
temps = pygame.Surface((temps_wh)) # Pareille que label score
temps.fill(blue)

# Création du label mpm_actuel
mpm_actuel_xy, mpm_actuel_wh =  xy_pourcent(40, 87), xy_pourcent(20, 10)
mpm_actuel = pygame.Surface(mpm_actuel_wh) # Pareille que label score
mpm_actuel.fill(white)

# Création du label exit
exit_xy, exit_wh = xy_pourcent(96, 0), xy_pourcent(4, 6)
exit = pygame.Surface((exit_wh)) # Pareille que label score
exit.fill(red)

# Polices d'ecriture
taille_police = 70
comic_sans_ms = police('Comic Sans MS', taille_police)
arial = police('Arial', taille_police)
impact = police('impact', taille_police)

# Création d'un texte
texte_score_xy = xy_pourcent(1, 1.4)
texte_score = impact.render('Meilleur score', False, white)

# loop back pour vérifier les évenements clavier
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
        print("touche z cliqué")
    if keys[pygame.K_s]:
        print("touche s cliqué")
        

    # Your game logic here
    
    # Afficher tout : label, texte...
    charger_formes()
    pygame.display.flip()

pygame.quit()
quit()