import pyautogui as pagui

x=1360
y=766

pagui.click(x, y)
pagui.alert("bomba de mensajes! ")

'''
moveTo(x, y): Mueve el cursor del mouse a las coordenadas (x, y) de la pantalla.
moveRel(xOffset, yOffset): Mueve el cursor del mouse en relación a su posición actual, desplazándolo en los ejes x e y.
click(x, y): Simula un clic del mouse en las coordenadas (x, y).
rightClick(x, y): Simula un clic derecho del mouse en las coordenadas (x, y).
doubleClick(x, y): Simula un doble clic del mouse en las coordenadas (x, y).
scroll(units): Realiza un desplazamiento de scroll en la dirección especificada por units.
typewrite(message): Escribe el texto message en el teclado virtual.
press(key): Simula la presión de una tecla específica.
hotkey(key1, key2, ..., keyN): Simula la combinación de teclas, presionando varias teclas al mismo tiempo.
screenshot(): Captura una captura de pantalla de la pantalla actual.
locateOnScreen(image): Busca una imagen específica en la pantalla y devuelve su ubicación.
pixel(x, y): Obtiene el color de un píxel en las coordenadas (x, y) de la pantalla.
size(): Devuelve el tamaño actual de la pantalla.
alert(text): Muestra una alerta en la pantalla con el texto especificado.
'''