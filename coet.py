import pygame

class Coet:
    
    def __init__(self):
        pygame.init
        self.screen = pygame.display.set_mode((1000, 666))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Coet")

        self.image = pygame.image.load("coet.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.moure_dreta = False
        self.moure_esquerra = False
        self.moure_dalt = False
        self.moure_baix =False


    def _mira_events(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moure_dreta = True

                elif event.key == pygame.K_LEFT:
                    self.moure_esquerra = True

                elif event.key == pygame.K_UP:
                    self.moure_dalt = True

                elif event.key == pygame.K_DOWN:
                    self.moure_baix = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moure_dreta = False
 
                elif event.key == pygame.K_LEFT:
                    self.moure_esquerra = False
 
                elif event.key == pygame.K_UP:
                    self.moure_dalt = False
 
                elif event.key == pygame.K_DOWN:
                    self.moure_baix = False

    def _actualitza_moviments(self):
        self.x = self.rect.x
        self.y = self.rect.y
        if self.moure_dreta and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moure_esquerra and self.rect.left > self.screen_rect.left:
            self.x -= 1
        if self.moure_dalt and self.rect.top > self.screen_rect.top:
            self.y -= 1
        if self.moure_baix and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        self.rect.x =self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def _actualitza_pantalla(self):
        self.screen.fill((255, 255, 255))
        self.blitme()
        pygame.display.flip()

    def jugar(self):
        while True:
            self._mira_events()
            self._actualitza_moviments()
            self._actualitza_pantalla()


def main():
    coet = Coet()
    coet.jugar()

if __name__ == "__main__":
    main()
