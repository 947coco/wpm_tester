import pygame as pygame


pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h # dimension x et y de l'ecran
pygame.display.set_caption('mpm testeur') # Titre de la fenetre

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)


def generate_variable(name):
    return "Variable {}".format(name)


print(generate_variable("co"))  # Output: Variable 0
print(generate_variable("ar"))  # Output: Variable 1
print(generate_variable("ta"))  # Output: Variable 2
def choisir_langue(langue):
    fichiertxt = {"fr": "Langue/francais.txt", "en": "Langue/english.txt"}
    mots = [mot for ligne in open(fichiertxt[langue], "r") for mot in ligne.split()]

def taille_en_pourcent(X=0, Y=0):
    return int(screen_width*X*0.01), int(screen_height*Y*0.01)

def créer_label(largeur, hauteur, x, y, couleur):
    pass
# Création du label meilleur_score
meilleur_score = pygame.Surface(taille_en_pourcent(14, 8))
meilleur_score.fill(green)
window.blit(meilleur_score, taille_en_pourcent(1, 1))

# Création du label temps
temps = pygame.Surface(taille_en_pourcent(15, 10))
temps.fill(blue)
window.blit(temps, taille_en_pourcent(83, 30))

# Création du label mpm_actuel
mpm_actuel = pygame.Surface(taille_en_pourcent(20, 10))
mpm_actuel.fill(white)
window.blit(mpm_actuel, taille_en_pourcent(40, 87))

# Création du bouton exit
btn_exit_x, btn_exit_y = taille_en_pourcent(97, -1)
btn_exit_largeur, btn_exit_hauteur = taille_en_pourcent(6, 6)
mpm_actuel = pygame.Surface((btn_exit_largeur, btn_exit_hauteur))
mpm_actuel.fill(red)
window.blit(mpm_actuel, (btn_exit_x, btn_exit_y))



# loop back pour vérifier les évenements clavier
while True:
    pygame.display.flip()
    for evenement in pygame.event.get():
        if evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
            if btn_exit_x <= evenement.pos[0] <= btn_exit_x + btn_exit_largeur and btn_exit_y <= evenement.pos[1] <= btn_exit_y + btn_exit_hauteur:
                pygame.quit()
                quit()
        pygame.display.update()
        

