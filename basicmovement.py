from djitellopy import Tello
from time import sleep
tello = Tello()

tello.connect()
tello.takeoff()

sleep(1.5)
tello.move_forward(304.8)
tello.rotate_counter_counter_clcokwise(90)

sleep(1.5)
tello.move_forward(304.8)
tello.rotate_counter_clockwise(90)

sleep(1.5)
tello.move_forward(304.8)
tello.rotate_counter_clockwise(90)

sleep(1.5)
tello.move_forward(304.8)

sleep(2)
tello.flip_forward(1)
tello.flip_backward(1)

tello.land()

