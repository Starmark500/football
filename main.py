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
speed_y=0
right_ball=sprite.get_right(ball)

top_ball=sprite.get_top(ball)
bottom_ball=sprite.get_bottom(ball)
@wrap.always(10)
def fly_ball():
    global speed_x
    sprite.move(ball, speed_x, speed_y)
    right_ball = sprite.get_right(ball)
    left_ball = sprite.get_left(ball)
    print(right_ball)
    if right_ball > 1000:
        speed_x=-2
































import wrap_py

wrap_py.app.start()
