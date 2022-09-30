import pygame

# def getArray(text):
#     output = text.split(" ")

#     return output

# command = "add 12 11 1998 crear la plicacion nueva"

# print(len(command))

# print( getArray(command) )

# input("")

pygame.init()

# Get the list of events
events = pygame.event.get()
# Check to see if the event is a pressed or released key
if events[0].type == pygame.KEYDOWN:
    print("A key was pressed!")
elif events[0].type == pygame.KEYUP:
    print("A key was released!")
# Check to see which key was pressed
if events[0].key == pygame.K_UP:
    print("The up arrow key was pressed!")
elif events[0].key == pygame.K_DOWN:
    print("The down arrow key was pressed!")
elif events[0].key == pygame.K_q:
    print("The letter q was pressed!")