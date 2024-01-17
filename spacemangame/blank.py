import random
screenX, screenY = 1280,720

for i in range(5):
    if random.randint(1,2) == 1:
        birdX = random.randint(-100, 0)
    else:
        birdX = random.randint(screenX,screenX + 100)
    if random.randint(1,2) == 1:
        birdY = random.randint(-100, 0)
    else:
        birdY = random.randint(screenY, screenY + 100)
    print(f"Bird {i+1}: {birdX}, {birdY}")
