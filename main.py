import wrap
from wrap import sprite, sprite_text, world

world.create_world(1000, 500)
world.set_back_color(110, 200, 150)

ball = sprite.add("mario-enemies", 500, 250, "armadillo_egg")
sprite.set_size(ball, 50, 50)
platform1 = sprite.add("mario-items", 900, 250, "moving_platform3")
platform2 = sprite.add("mario-items", 150, 250, "moving_platform3")

sprite.set_angle(platform2, 180)
sprite.set_angle(platform1, 180)
sprite.set_height(platform1, 100)
sprite.set_height(platform2, 100)
speed_x = 2
speed_y = 2
right_ball = sprite.get_right(ball)
speed_plat=10


@wrap.on_key_always(wrap.K_DOWN, wrap.K_UP)
def move_platform(keys):
    global speed_plat,speed_y
    if wrap.K_DOWN in keys:
        sprite.move(platform1, 0, speed_plat)
    else:
        sprite.move(platform1, 0, -speed_plat)
    if sprite.is_collide_sprite(platform1,ball):
        if speed_plat > 0:
            speed_y=-speed_y
        if speed_plat < 0:
            speed_y = -speed_y



@wrap.on_key_always(wrap.K_w, wrap.K_s)
def move_platform(keys):
    if wrap.K_s in keys:
        sprite.move(platform2, 0, 10)
    else:
        sprite.move(platform2, 0, -10)


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
def otbivka_platform():
    global speed_x, speed_y

    sprite.move(ball, speed_x, 0)

    otbivka_x(platform2)
    otbivka_x(platform1)

    if sprite.get_right(ball) > 1000:
        speed_x = -speed_x
    if sprite.get_left(ball) < 0:
        speed_x = -speed_x

    sprite.move(ball, 0, speed_y)
    otbivka_y(platform1)
    otbivka_y(platform2)
    if sprite.get_bottom(ball) > 500:
        speed_y = -speed_y
    if sprite.get_top(ball) < 0:
        speed_y = -speed_y


import wrap_py

wrap_py.app.start()
