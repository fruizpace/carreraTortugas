import turtle

class Circuito():
    corredores = [] # lista vacía
    __posStartY = (-30, -10, 10, 30) # tupla con la posicion inicial de cada tortuga
    __colorTurtle = ('red', 'blue', 'green','orange')
    
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
            new_turtle.penup() # funcion de turtle que levanta el lapiz y ya no se dibuja el rrecorrido de la tortuga
            new_turtle.setpos(self.__startLine, self.__posStartY[i]) # posicionala en donde la corresponda usando las posiciones iniciales de la tupla de posiciones
            
            self.corredores.append(new_turtle) # añade cada nueva tortuga a la lista de corredores vacía
            # esto loo harás 4 veces, y así tendremos 4 corredoras.
            
        def Competir



if __name__ == '__main__':
    circuito = Circuito(640, 480)
        
        
        