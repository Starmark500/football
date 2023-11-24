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
speed_x=2
speed_y=2
right_ball=sprite.get_right(ball)


@wrap.always(10)
def fly_ball():
    global speed_x,speed_y
    sprite.move(ball, speed_x, speed_y)
    right_ball = sprite.get_right(ball)
    left_ball = sprite.get_left(ball)
    top_ball = sprite.get_top(ball)
    bottom_ball = sprite.get_bottom(ball)
    print(bottom_ball)
    if right_ball > 1000:
        speed_x=-speed_x
    if left_ball < 0:
        speed_x=-speed_x
    if bottom_ball > 500:
        speed_y=-speed_y
    if top_ball < 0:
        speed_y=-speed_y
    otbivka_platform()
@wrap.on_key_always(wrap.K_DOWN,wrap.K_UP)
def move_platform(keys):
    if wrap.K_DOWN in keys:
        sprite.move(platform1,0,10)
    else:
        sprite.move(platform1,0,-10)
@wrap.on_key_always(wrap.K_w,wrap.K_s)
def move_platform(keys):
    if wrap.K_s in keys:
        sprite.move(platform2,0,10)
    else:
        sprite.move(platform2,0,-10)

def otbivka_platform():
    global speed_x
    left_platform=sprite.get_left(platform1)
    if sprite.is_collide_sprite(ball,platform1):
        sprite.move_right_to(ball,left_platform)
        speed_x=-speed_x
































import wrap_py

wrap_py.app.start()
