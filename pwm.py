import RPi.GPIO as GPIO
from time import sleep
import sys

ledpin = 12				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,20000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 
pi_pwm.ChangeDutyCycle(0)

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    val = sys.argv[1]
    print(val)
    pi_pwm.ChangeDutyCycle(int(val))
    sleep(10.0)
