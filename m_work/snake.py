import turtle
import time
import random

delay = 0.1

# achqo
score = 0

high_score = 0
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)
# Turns off the screen updates

# snake kallasi
head = turtle.Turtle()
head.speed(-10)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake ovqati
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("ball: 0  eng yuqori ball: 0", align="center", font=("Courier", 24, "normal"))


# vazifalari
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# klavyaturalarni belgilash
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# ekrani
while True:
    wn.update()

    # Chegara bilan to'qnashuvni tekshirish
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # segmentlarni yashirish
        for segment in segments:
            segment.goto(1000, 1000)

        # segmentlarni tozalsh
        segments.clear()

        # hisobni qayta tiklash
        score = 0

        # kechiktirishni qayta tiklash
        delay = 0.1

        pen.clear()
        pen.write("ball: {}  eng yuqori ball: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

        # ovqat bn to'qnashuvni tekshirish
    if head.distance(food) < 20:
        # tasodifiy joyga ko'chirish
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # segment qo'shish
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # vaqtni qisqartirish
        delay -= 0.001

        # ballni o'sishi
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("ball: {}  eng yuqori ball: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

        # Avval oxirgi segmentlarni teskari tartibda harakatlantiring
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # 0 segmentni bosh joylashgan joyga ko'chiring
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Tana segmentlari bilan boshning to'qnashuvini tekshiring
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # segmentlarni yashirish
            for segment in segments:
                segment.goto(1000, 1000)

            # segment ro'yhatini tozalash
            segments.clear()
            # hisobni tiklash
            score = 0

            # kechiktirishni tiklash
            delay = 0.1

            # achqoni displayda yanglash
            pen.clear()
            pen.write("ball: {}  eng yuqori ball: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
