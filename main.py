import turtle
import random

class Circuito():
    corredores = [] # lista vacía
    __posStartY = (-30, -10, 10, 30) # tupla con la posicion inicial de cada tortuga
    __colorTurtle = ('red', 'blue', 'purple','orange')
    
    def __init__(self, width, height): # CONSTRUCTOR!
        self.width = width # esta variable la dejamos pública. Para ser privada self.__width
        self.height = height
        
        self.__screen = turtle.Screen() # usamos funcion pantalla de turtle como privada
        self.__screen.setup(width, height) # crea la pantalla con las variables que hemos entrado
        self.__screen.bgcolor('lightgray') # color de la pantalla por defecto
        self.__startLine = -width/2 + 20 # linea de salida
        self.__finishLine = width/2 - 20 # linea de llegada
        
        self.__createRunners() # inicializo la creación de corredores con la función de abajo.
        
    def __createRunners(self):
        for i in range(4): # como habra 4 corredores usamos "for"
            new_turtle = turtle.Turtle() # crea una tortuga
            new_turtle.color(self.__colorTurtle[i]) # ponle el primer color de la tupla de colores
            new_turtle.shape('turtle') # ponle forma de tortuga
            new_turtle.penup() # funcion de turtle que levanta el lapiz y ya no se dibuja el recorrido de la tortuga
            new_turtle.setpos(self.__startLine, self.__posStartY[i]) # posicion X,Y de la tortuga en donde la corresponda usando las posiciones iniciales de la tupla de posiciones
            
            self.corredores.append(new_turtle) # añade cada nueva tortuga a la lista de corredores vacía
            # esto loo harás 4 veces, y así tendremos 4 corredoras.
            
    def competir(self): # hacer que avancen como si lanzaran un dado...
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1, 6) # lanzar un dado virtual del paquete random
                tortuga.forward(avance) # funcion de avance del paquete turtle
                
                if tortuga.position()[0] >= self.__finishLine:
                    hayGanador = True
                    
                    if tortuga.color()[0] == 'red':
                        print('¡Ha ganado Rafael!')
                    elif tortuga.color()[0] == 'blue':
                        print('¡Ha ganado Leonardo!')
                    elif tortuga.color()[0] == 'orange':
                        print('¡Ha ganado Michelangelo!')
                    elif tortuga.color()[0] == 'purple':
                        print('¡Ha ganado Donatello!')
                    break # con esto el FOR se para en cuanto una tortuga cumple la condicion (llegar a linea de final)


if __name__ == '__main__':
    circuito = Circuito(640, 200) # invoco la pantalla de juego
    circuito.competir() # invoco la competicion
        
# circuito.corredores[0].position()[0] # esto es la coordenada x de la tortuga cero        
        