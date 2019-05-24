from microbit import *
ball1 = Image(
    "00000:"
    "00900:"
    "09990:"
    "00900:"
    "00000")
ball2 = Image(
    "00000:"
    "09000:"
    "99900:"
    "09000:"
    "00000")
ball3 = Image(
    "00000:"
    "90000:"
    "99009:"
    "90000:"
    "00000")
ball4 = Image(
    "00000:"
    "00009:"
    "90099:"
    "00009:"
    "00000")
ball5 = Image(
    "00000:"
    "00090:"
    "00999:"
    "00090:"
    "00000")

ball_left = [ball1, ball2, ball3, ball4, ball5]
ball_right = [ball1, ball5, ball4, ball3, ball2]

while True:
    if button_a.is_pressed():
        display.show(ball_left, delay=200)
    elif button_b.is_pressed():
        display.show(ball_right, delay=200)
    else:
        display.show(Image.HEART)