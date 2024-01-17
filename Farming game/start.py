import pygame
 
 
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
        self.points = 0
 
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()
                    self.points += 1
            else:
                sprite.image.fill("blue")
 
 
def on_click():
    color = (255, 0, 0) 
    sprite.image.fill(color)

w = 1200
h = 800 
pygame.init()
screen = pygame.display.set_mode((1200, 800))

 
sprite = ClickableSprite(pygame.Surface((100, 100)), w//2, h//2, on_click)
group = pygame.sprite.GroupSingle(sprite)
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
 
    group.update(events)
    screen.fill((0,0,0))
    group.draw(screen)
    text = font.render(f'Points {sprite.points}', False, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (75, h-50)
    screen.blit(text, textRect)

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60
 
pygame.quit()