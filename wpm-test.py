import pygame as pygame


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h # dimension x et y de l'ecran
pygame.display.set_caption('mpm testeur') # Titre de la fenetre

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)


print(f"Screen resolution: {screen_width}x{screen_height}")

def choisir_langue(langue):
    fichiertxt = {"fr": "Langue/francais.txt", "en": "Langue/english.txt"}
    mots = [mot for ligne in open(fichiertxt[langue], "r") for mot in ligne.split()]

class Button:
    def __init__(self, x, y, width, height, color, text=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.text:
            font = pygame.font.Font(None, 36)
            text_surf = font.render(self.text, True, black)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

button = Button(100, 100, 200, 200, green, "Click me")

# loop back (boucle afin de garder la fenetre)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()