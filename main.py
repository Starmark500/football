import time

import wrap
from wrap import sprite, sprite_text, world

world.create_world(1000, 500)
world.set_back_color(110, 200, 150)

ball = sprite.add("mario-enemies", 500, 250, "armadillo_egg")
sprite.set_size(ball, 50, 50)
platform1 = sprite.add("mario-items", 900, 250, "moving_platform3")
platform2 = sprite.add("mario-items", 150, 250, "moving_platform3")
goal1 = 0
goal2 = 0

timer = sprite.add_text(str(goal1), 900, 100, text_color=[200, 170, 40], font_size=100)
timer1 = sprite.add_text(str(goal2), 100, 100, text_color=[139, 150, 108], font_size=100)
timer_start = sprite.add_text("0", 500, 180, font_size=50)
sprite.set_angle(platform2, 180)
sprite.set_angle(platform1, 180)
sprite.set_height(platform1, 100)
sprite.set_height(platform2, 100)
speed_x = 2
speed_y = 2
right_ball = sprite.get_right(ball)
speed_plat = 10
speed_plat2 = 10
time1=time.time()
mode="game"





@wrap.always(100)
def t_timer():
    global time1
    if mode != "timer":

        return

    time2=time1-time.time()
    time2=time2+4
    if int(time2) <= 0:
        time1=time.time()
        change_mode("game")
    time2=int(time2)
    sprite_text.set_text(timer_start,str(time2))



def start_timerball():

    sprite_text.set_text(timer_start,str(3-1))
    time.time()

def goal(id, g):
    sprite_text.set_text(id, str(g + 1))


@wrap.on_key_always(wrap.K_DOWN, wrap.K_UP)
def move_platform(keys):
    global speed_plat, speed_y
    if wrap.K_DOWN in keys:
        speed_plat = abs(speed_plat)
        sprite.move(platform1, 0, speed_plat)
    else:
        speed_plat = -abs(speed_plat)
        sprite.move(platform1, 0, speed_plat)
    if sprite.is_collide_sprite(platform1, ball):
        if speed_plat < 0:
            sprite.move_bottom_to(ball, sprite.get_top(platform1))
        if speed_plat > 0:
            sprite.move_top_to(ball, sprite.get_bottom(platform1))


@wrap.on_key_always(wrap.K_w, wrap.K_s)
def move_platform(keys):
    global speed_plat2
    if wrap.K_s in keys:
        speed_plat2 = abs(speed_plat2)
        sprite.move(platform2, 0, speed_plat2)
    else:
        speed_plat2 = -abs(speed_plat2)
        sprite.move(platform2, 0, speed_plat2)
    if sprite.is_collide_sprite(platform2, ball):
        if speed_plat2 < 0:
            sprite.move_bottom_to(ball, sprite.get_top(platform2))
        if speed_plat2 > 0:
            sprite.move_top_to(ball, sprite.get_bottom(platform2))


def otbivka_x(id):
    global speed_x
    if sprite.is_collide_sprite(ball, id):
        if speed_x > 0:
            sprite.move_right_to(ball, sprite.get_left(id))
        elif speed_x < 0:
            sprite.move_left_to(ball, sprite.get_right(id))
        speed_x = -speed_x


def otbivka_y(id):
    global speed_y
    if sprite.is_collide_sprite(ball, id):
        if speed_y > 0:
            sprite.move_bottom_to(ball, sprite.get_top(id))
        elif speed_y < 0:
            sprite.move_top_to(ball, sprite.get_bottom(id))
        speed_y = -speed_y


@wrap.always(10)
def otbivka_ball():
    global speed_x, speed_y, goal2, goal1
    if mode != "game":
        return

    sprite.move(ball, speed_x, 0)

    otbivka_x(platform2)
    otbivka_x(platform1)

    if sprite.get_right(ball) > 1000:
        speed_x = -abs(speed_x)
        goal(timer, goal1)
        goal1 += 1
        sprite.move_to(ball, 500, 250)
        change_mode("timer")
    if sprite.get_left(ball) < 0:
        speed_x = abs(speed_x)
        goal(timer1, goal2)
        goal2 += 1
        sprite.move_to(ball, 500, 250)
        change_mode("timer")

    sprite.move(ball, 0, speed_y)
    otbivka_y(platform1)
    otbivka_y(platform2)
    if sprite.get_bottom(ball) > 500:
        speed_y = -abs(speed_y)
    if sprite.get_top(ball) < 0:
        speed_y = abs(speed_y)

def change_mode(m):
    global mode,time1
    mode = m
    if mode =="timer":
        sprite.show(timer_start)
        time1 = time.time()
    if mode == "game":
        sprite.hide(timer_start)
change_mode("timer")
import wrap_py

wrap_py.app.start()
