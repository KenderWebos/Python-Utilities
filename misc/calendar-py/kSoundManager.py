import time
import pygame

url = "kSoundManager/"
soundTypes = ["good", "bad", "alert"]
pygame.init()

choise = "alert"

def makeSound(type):
    # sound types can be: good, bad, alert
    soundObj = pygame.mixer.Sound(f'{url}/{type}/1hourAlarm.mp3')
    soundObj.play()
    time.sleep(5)
    soundObj.stop()