from gamestart import *

fill('black')
paddle = box(20, 20, 50, 300, 'white')
ball = box(70, 190, 50, 50, 'white')
ball.angle = 45

def loop():
    ball.forward(10)
    ball.bounce() # the ball bounces at the screen
    if ball.hits(paddle):
        ball.angle = 180 - ball.angle
        ball.x = paddle.x + paddle.width + 1
    if key.up:
        paddle.y -= 10
        paddle.bounce()
    elif key.down:
        paddle.y += 10
        paddle.bounce()
    

start()