import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22

Motor2A = 19
Motor2B = 21
Motor2E = 23

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

print "Move forward"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)
time.sleep(2)

print  "Move backward"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)
time.sleep(2)

print "Turn left"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)
time.sleep(2)

print "Turn right"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)
time.sleep(2)

print "Stop"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)

GPIO.cleanup()

min distance = 70
 
def autonomy():
	no_problem = True
	while no_problem
	servo(70)
	time.sleep(1)
	dist = us_dist(15)

	if dist > min_distance:
		print('Move forward', dist)
		fwd()
		time.sleep(1)
	else:
		print('Obstacle ahead' , dist)
		stop()
		servo(28)
		time.sleep(1)
		left_dir = us_dist(15)
		servo(112)
		right_dir = us_dist(15)
		time.sleep(1)
		
		if 	left_dir > right_dir and left_dir > min_disatnce
			print ('turn left')
			left()
			time.sleep(1)
		elif leftt_dir < right_dir and right_dir > min_distance:
			print ('turn Right')
			right()
			time.sleep(1)
			
		else: 
			print('Move backward')
			bwd()
			time.sleep(2)
			rot_decision = [right_rot, left_rot]
			rotation = rot_decision [random.randrange(0,1)]
			rotation()
			time.sleep(1)
		
	stop()
	
	
	stop()
	enavle_servo()
	servo(70)
	time.sleep(3)
	autonomy()
	
	
	
	