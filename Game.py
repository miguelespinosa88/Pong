import turtle # Modelo a utilizar
import winsound

wn = turtle.Screen() # Se crea la pantalla
wn.title("PONG") # Title
wn.bgcolor("black") # Background color
wn.setup(width=800,height=600) # Medidas el 0,0 se encuentra en el centro
wn.tracer(0)

#Marcadores de puntos
marcador_a=0;
marcador_b=0;

# Linea div
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Speed of animation it is the maximum
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(50,0.1) # Por default el cuadrado es de 20 px de lado, el 5 es factoe multiplicativo
paddle_a.penup()
paddle_a.goto(0,0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Speed of animation it is the maximum
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(5,1) # Por default el cuadrado es de 20 px de lado, el 5 es factoe multiplicativo
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0) # Speed of animation it is the maximum
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(5,1) # Por default el cuadrado es de 20 px de lado, el 5 es factoe multiplicativo
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # Speed of animation it is the maximum
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
#Everytime de ball moves, it will do it by 0.4 pixels
ball.dx = 0.4
ball.dy = 0.4

# Marcador A
score_a = turtle.Turtle()
score_a.speed(0)
score_a.color("white")
score_a.penup()
score_a.hideturtle()
score_a.goto(-80,230)
score_a.write(marcador_a, font=("Courier",35,"normal"))

# Marcador B
score_b = turtle.Turtle()
score_b.speed(0)
score_b.color("white")
score_b.penup()
score_b.hideturtle()
score_b.goto(40,230)
score_b.write(marcador_b, font=("Courier",35,"normal"))

# Resultado
message = turtle.Turtle()
message.speed(0)
message.color("white")
message.penup()
message.hideturtle()
message.goto(0,150)
message.write("", font=("Courier",35,"normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if (y > 235):
        paddle_a.sety(y)
    else:
        y = y + 20
        paddle_a.sety(y)

def paddle_a_down():
   y = paddle_a.ycor()
   if (y < -220):
       paddle_a.sety(y)
   else :
        y = y-20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if (y > 235):
        paddle_b.sety(y)
    else:
        y = y + 20
        paddle_b.sety(y)

def paddle_b_down():
   y = paddle_b.ycor()
   if (y < -220):
       paddle_b.sety(y)
   else :
        y = y-20
        paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop
while True:
    wn.update()

    # Checar si ganó el jugador B
    if (marcador_a == 5):
        #Escribir mensaje
        message.write("Ganó el jugador A",align="center",font=("Courier", 30, "normal"))
        #Bola en el centro
        ball.setx(0)
        ball.sety(0)

    #Checar si ganó el gujador B
    if (marcador_b == 5):
        #Escribir mensaje
        message.write("Ganó el jugador B",align="center",font=("Courier", 30, "normal"))
        #Bola en el centro
        ball.setx(0)
        ball.sety(0)

    #Move de ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #LIMITES CON LA PANTALLA

    #Check de upper limits
    if (ball.ycor()>290):
        ball.dy=-ball.dy
        #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if (ball.ycor()< -280):
        ball.dy=-ball.dy
        #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


    #Check right and left borders

    if (ball.xcor()>390):
        ball.goto(0,0)
        # Punto para jugador A
        marcador_a=marcador_a+1;
        score_a.clear()
        score_a.write(marcador_a, font=("Courier", 35, "normal"))
        score_b.clear()
        score_b.write(marcador_b, font=("Courier", 35, "normal"))

        #print("Jugador A " + str(marcador_a) + " puntos")
        #print("Jugador B " + str(marcador_b) + " puntos")
        #ball.dx=-ball.dx

    if (ball.xcor()< -390):
        ball.goto(0,0)
        #Punto para jugador B
        marcador_b=marcador_b+1;
        score_a.clear()
        score_a.write(marcador_a, font=("Courier", 35, "normal"))
        score_b.clear()
        score_b.write(marcador_b, font=("Courier", 35, "normal"))

        #print("Jugador A " + str(marcador_a) + " puntos")
        #print("Jugador B " + str(marcador_b) + " puntos")
        #ball.dx=-ball.dx

    #LIMITES CON BARRAS
    # Right paddle
    if (ball.xcor()>340) and (ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() +50) and (ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx=-ball.dx
        #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


    if (ball.xcor()<-340) and (ball.xcor()>-350) and (ball.ycor() > paddle_a.ycor() -50) and (ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx=-ball.dx
        #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

