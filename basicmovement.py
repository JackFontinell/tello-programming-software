from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_forward(304.8)
tello.rotate_counter_clockwise(90)

tello.rotate.counter_clockwise(180)
tello.move_left(304.8)

tello.rotate_clockwise(90)

tello.move_backward(304.8)
tello.rotate_clockwise(90)

tello.move_right(304.8)

tello.flip_forward(304.8)

tello.land()
