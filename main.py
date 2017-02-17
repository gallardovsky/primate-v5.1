import pygame, random, sys
from pygame.locals import *
from nodos import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Primate v5.1")
screen.fill((44,0,30))
pygame.font.init

nodosDesconectados = []
nodosConectados = []
bordes = []
bordesConectados = []
numNodos = 0
distCorta = 1000

welcomeScreen = True
stay = True

def ran():
	for i in range(5):
		nodosDesconectados.append(Node(random.randint(0,800), random.randint(0,600)))

	for cadaNodo in nodosDesconectados:
		pygame.draw.circle(screen, (255,255,255), (cadaNodo.xPos,cadaNodo.yPos), 5, 5)
		pygame.display.update()
		clock.tick(24)

	numNodos = len(nodosDesconectados)
	print 'Creados'
	return nodosDesconectados, numNodos

def draw(nodosDesconectados):
	pos = pygame.mouse.get_pos()
	x = int(pos[0])
	y = int(pos[1])
	nodosDesconectados.append(Node(x,y))
	pygame.draw.circle(screen, (255,255,255), pygame.mouse.get_pos(), 5, 5)
	pygame.display.update()
	clock.tick(24)

	print 'Creado'

	return nodosDesconectados

def unir(nodosDesconectados, numNodos):
	numNodos = numNodos
	distCorta = 1000.0
	cadaNodo = 0

	for i in range(numNodos):
		for j in range(i + 1, numNodos):
			if nodosDesconectados[i] != nodosDesconectados[j]:
				bordes.append(Aristas(nodosDesconectados[i], nodosDesconectados[j]))
				distActual = (((nodosDesconectados[i].xPos - nodosDesconectados[j].xPos) ** 2) + ((nodosDesconectados[i].yPos - nodosDesconectados[j].yPos) ** 2)) ** 0.5

			if distActual < distCorta:
				bordesCortos = Aristas(nodosDesconectados[i], nodosDesconectados[j])
				nodoCorto1 = nodosDesconectados[i]
				nodoCorto2 = nodosDesconectados[j]
#				print distActual, distCorta
				distCorta = distActual

# Une los puntos con una linea y muestra la distancia mas corta en otro color
	for line in bordes:
		pygame.draw.line(screen, (119,33,111), (line.xPos1,line.yPos1), (line.xPos2,line.yPos2), 1)
		for cadaNodo in nodosDesconectados:
			pygame.draw.circle(screen, (255,255,255), (cadaNodo.xPos,cadaNodo.yPos), 5, 0)

		pygame.display.update()
		clock.tick(24)

	pygame.draw.line(screen, (255,255,255), (bordesCortos.xPos1, bordesCortos.yPos1),(bordesCortos.xPos2,bordesCortos.yPos2), 1)

	pygame.display.update()
	clock.tick(24)

	nodosConectados.append(nodoCorto1)
	nodosConectados.append(nodoCorto2)
	nodosDesconectados.remove(nodoCorto1)
	nodosDesconectados.remove(nodoCorto2)
	bordesConectados.append(bordesCortos)

	numNodos = len(nodosDesconectados)

	print 'Conectados'
		
	return nodosDesconectados, nodosConectados, bordesConectados, numNodos, distCorta

def Prim(nodosDesconectados, nodosConectados, bordesConectados, numNodos):
	print '''
	Comienza el Algoritmo Prim
	'''
	print numNodos
	while len(nodosDesconectados) > 0:
		distCorta = 1000.0
		#print 'hola'
		for nodoInicial in nodosConectados:
			for nodoFinal in nodosDesconectados:
				distActual = (((nodoInicial.xPos - nodoFinal.xPos) ** 2) + ((nodoInicial.yPos - nodoFinal.yPos) ** 2)) ** 0.5

				if distActual < distCorta:
					distCorta = distActual
					nodoCorto1 = nodoInicial
					nodoCorto2 = nodoFinal

				for aristaConectada in bordesConectados:
					pygame.draw.line(screen,(233,84,32),(aristaConectada.xPos1,aristaConectada.yPos1),(aristaConectada.xPos2,aristaConectada.yPos2),3)
				pygame.draw.line(screen,(174,167,159),(nodoInicial.xPos,nodoInicial.yPos),(nodoFinal.xPos,nodoFinal.yPos),1)

				for cadaNodo in nodosConectados:
					pygame.draw.circle(screen,(255,255,255),(cadaNodo.xPos,cadaNodo.yPos),5,0)
				pygame.display.update()
				clock.tick(24)

		bordesConectados.append(Aristas(nodoCorto1, nodoCorto2))
		nodosConectados.append(nodoCorto2)
		nodosDesconectados.remove(nodoCorto2)

		print 'Arista encontrada'

		for line in bordes:
			pygame.draw.line(screen,(119,33,111),(line.xPos1,line.yPos1),(line.xPos2,line.yPos2),1)

        for aristaConectada in bordesConectados:
            pygame.draw.line(screen,(233,84,32),(aristaConectada.xPos1,aristaConectada.yPos1),(aristaConectada.xPos2,aristaConectada.yPos2),4)

        for cadaNodo in nodosConectados:
            pygame.draw.circle(screen,(255,255,255),(cadaNodo.xPos,cadaNodo.yPos),5,0)
        pygame.display.update()
        clock.tick(24)

	bordesConectados = []
	#bordes = []
	nodosDesconectados = []
	nodosConectados = []


	print 'Nos Alegramos, encontramos el arbol de expasion :D'
	print '''
	puede crear otro grafo ahora
	'''
	return bordesConectados, nodosDesconectados, nodosConectados

def main(nodosDesconectados, nodosConectados, bordes, bordesConectados):
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((1200, 600))
	pygame.display.set_caption("Primate v5.1")
	screen.fill((44,0,30))
	pygame.font.init

	menuFont = pygame.font.SysFont('courier',30, bold = True)
	menuFont1 = pygame.font.SysFont('courier',24)
	optionFont = pygame.font.SysFont('courier',18)
	notasFont = pygame.font.SysFont('courier',14)

	numNodos = 0
	distCorta = 1000

	welcomeScreen = True
	pygame.draw.line(screen, (255,255,255), (800,0),(800,600),3)

	screen.blit(menuFont.render('Algoritmo Prim',True,(174,167,159)),(880,20))
	screen.blit(menuFont1.render('Opciones',True,(174,167,159)),(810,70))
	screen.blit(optionFont.render('R - Crear 5 nodos aleatorios',True,(174,167,159)),(830,110))
	screen.blit(optionFont.render('C - Conectar nodos',True,(174,167,159)),(830,130))
	screen.blit(optionFont.render('N - Nuevo grafo',True,(174,167,159)),(830,150))
	screen.blit(optionFont.render('P - Usar Prim',True,(174,167,159)),(830,170))
	screen.blit(optionFont.render('Q - Salir',True,(174,167,159)),(830,200))
	screen.blit(notasFont.render('Tambien se pueden poner los nodos',True,(174,167,159)),(830,250))
	screen.blit(notasFont.render('dando click sobre la pantalla izquierda',True,(174,167,159)),(830,270))
	
	pygame.display.flip()
	pygame.display.update()

	while welcomeScreen:
		for evento in pygame.event.get():
			menu = pygame.key.get_pressed()

			if evento.type == QUIT or menu[K_q]:
				print 'Gracias por Usar "Primate v5.1"'
				exit()
		
			if menu[K_r]:
				nodosDesconectados, numNodos = ran()

			elif menu[K_c]:
				if len(nodosDesconectados) == 0:
					print 'Crear Nodos Primero'
				else:
					nodosDesconectados, nodosConectados, bordesConectados, numNodos, distCorta = unir(nodosDesconectados, numNodos)
			
			elif menu[K_n]:
				#nodosDesconectados, nodosConectados, bordes, bordesConectados = clean(nodosDesconectados, nodosConectados, bordes, bordesConectados)				
				welcomeScreen = False
				screen.fill((44,0,30))
				pygame.display.update()

				pygame.draw.line(screen, (255,255,255), (800,0),(800,600),3)
				screen.blit(menuFont.render('Algoritmo Prim',True,(174,167,159)),(880,20))
				screen.blit(menuFont1.render('Opciones',True,(174,167,159)),(810,70))
				screen.blit(optionFont.render('R - Crear 5 nodos aleatorios',True,(174,167,159)),(830,110))
				screen.blit(optionFont.render('C - Conectar nodos',True,(174,167,159)),(830,130))
				screen.blit(optionFont.render('N - Nuevo grafo',True,(174,167,159)),(830,150))
				screen.blit(optionFont.render('P - Usar Prim',True,(174,167,159)),(830,170))
				screen.blit(optionFont.render('Q - Salir',True,(174,167,159)),(830,200))
				screen.blit(notasFont.render('Tambien se pueden poner los nodos',True,(174,167,159)),(830,250))
				screen.blit(notasFont.render('dando click sobre la pantalla izquierda',True,(174,167,159)),(830,270))

				pygame.display.flip()
				pygame.display.update()
#				main1(nodosDesconectados, nodosConectados, bordes, bordesConectados)

			elif menu[K_p]:
				if len(nodosConectados) == 0:
					print 'Conectar Nodos Primero'
				else:
					Prim(nodosDesconectados, nodosConectados, bordesConectados, numNodos)
			
			elif pygame.mouse.get_pressed() == (1,0,0):
				nodosDesconectados = draw(nodosDesconectados)
				numNodos = len(nodosDesconectados)

while stay:
	main(nodosDesconectados, nodosConectados, bordes, bordesConectados)
	nodosDesconectados = []
	nodosConectados = []
	bordes = []
	bordesConectados = []