#Victoria Ramos
#11/6/22
#Snake Game in Python/Pygame

import pygame
import sys
import random

# initializing pygame
pygame.init()

Colors = {
    "Lavendar": (120, 100, 125),
    "Red": (255, 0, 0),
    "Green": (127, 255, 0),
    "Black": (0, 0, 0),
}

# Setting variables and their values
Config = {
    "ScreenX": 800,
    "ScreenY": 600,
    "ScreenTitle": "Victoria's Snake Game",
    "Background": Colors["Lavendar"],
    "BlockSize": 10,
    "Speed": 15, 
    "Menu": ["Press N for New Game", "Press Q to Quit"],

}

# Dictionary for snake
Snake = {
    # Create the screen 
    # Snake will start at the center of the screen
    "X": Config["ScreenX"] / 2,
    "Y": Config["ScreenY"] / 2,
    "Direction": "none",
    "Color": Colors["Red"],
    "Length": 0,
    "Tail": [],
}
# Function to reset the snake
def ResetSnake():
    Snake["X"] = Config["ScreenX"] / 2
    Snake["X"] = Config["ScreenY"] / 2
    Snake["Direction"] = "none"
    Snake["Length"] = 0
    Snake["Tail"] = []


Food = {
    "X": 0,
    "Y": 0,
    "Color": Colors["Green"],
}

# Randomizing the location of food
def RandomizeFoodlocation():
    Food["X"] = round(random.randrange(0, Config["ScreenX"] - Config["BlockSize"]), -1)
    Food["Y"] = round(random.randrange(0, Config["ScreenY"] - Config["BlockSize"]), -1)

def DrawGame(screen):
    screen.fill(Config["Background"])
    pygame.draw.rect(screen, Snake["Color"], [Snake["X"], Snake["Y"], Config["BlockSize"], Config["BlockSize"]])
    for tail in Snake["Tail"]:
        pygame.draw.rect(screen, Snake["Color"], [tail[0], tail[1], Config["BlockSize"], Config["BlockSize"]])

    pygame.draw.rect(screen, Food["Color"], [Food["X"], Food["Y"], Config["BlockSize"], Config["BlockSize"]])
    pygame.display.update()

def main():
    screen = pygame.display.set_mode([Config["ScreenX"], Config["ScreenY"]])
    clock = pygame.time.Clock()
    pygame.display.set_caption(Config["ScreenTitle"])
    # update the screen
    pygame.display.update()
    # setting game font and size
    menufont = pygame.font.SysFont("micosoftsansserif", 25)
    bGame = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Pressing the 'q' key will exit the game
                if event.key == pygame.K_q:
                    sys.exit()
                # Pressing the 'n' key will start a new game
                if event.key == pygame.K_n:
                    bGame = True
                    ResetSnake()
                    RandomizeFoodlocation()


        screen.fill(Colors["Black"])
        ypos = 30
        for line in Config["Menu"]:
            message = menufont.render(line, True, Colors["Lavendar"])
            screen.blit(message, [30, ypos])
            ypos += ypos
        pygame.display.update()


        # while loop that will keep the screen open
        # ensures we protect ourselves
        while bGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if Snake["Direction"] != "right":
                            Snake["Direction"] = "left"
                    if event.key == pygame.K_RIGHT:
                        if Snake["Direction"] != "left":
                            Snake["Direction"] = "right"
                    if event.key == pygame.K_UP:
                        if Snake["Direction"] != "down":
                            Snake["Direction"] = "up"
                    if event.key == pygame.K_DOWN:
                        if Snake["Direction"] != "up":
                            Snake["Direction"] = "down"

            if Snake["Direction"] == "left":
                Snake["X"] -= Config["BlockSize"]
            if Snake["Direction"] == "right":
                Snake["X"] += Config["BlockSize"]
            if Snake["Direction"] == "up":
                Snake["Y"] -= Config["BlockSize"]
            if Snake["Direction"] == "down":
                Snake["Y"] += Config["BlockSize"]

        #calling the DrawGame function
            DrawGame(screen)

            #Adding a collision so that the snake does not exit boundary of screen
            if Snake["X"] < 0 or Snake["X"] >= Config["ScreenX"] or Snake["Y"] < 0 or Snake ["Y"] >= Config["ScreenY"]:
                bGame = False

            # Creating an evaluation to see if we run into the tail of the snake
            if [Snake["X"], Snake["Y"]] in Snake["Tail"]:
                print("GAME OVER")
                break

            if Snake["X"] == Food["X"] and Snake["Y"] == Food["Y"]:
                Snake["Length"] += 1
                Snake["Tail"].append([Food["X"], Food["Y"]])
                RandomizeFoodlocation()

            Snake["Tail"].append([Snake["X"], Snake["Y"]])
            if len(Snake["Tail"]) > Snake["Length"]:
                del Snake["Tail"][0]

            clock.tick(Config["Speed"])

        print("GAME OVER")

if __name__ == "__main__":
    main()

