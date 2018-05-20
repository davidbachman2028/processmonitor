#! /usr/bin/python3

#imports
from gpiozero import LED, PWMLED
import psutil
from time import sleep

#declarations
r = LED(17)
y = LED(27)
g = LED(22)
b = LED(23)
#wt = PWMLED(24)
#wb = PWMLED(25)
#white LEDs have been commented out as they have no use in this version. 


monitoringinterval = 1

#cpu percentages for status lights
gf = 5
gs = 20
ys = 50
rs = 70
rf = 95
flatout = 100





def main():
    # my code here
    print("Running code")
    ledtest()
    
    monitoring()
    
    
    
    print("End of code")
    
    
def monitoring():
	while True:
		useage = psutil.cpu_percent(interval = monitoringinterval)
		ledupdater(useage)
		b.blink(0.1,0,1)
		sleep(monitoringinterval)
		    
def ledupdater(useage):
	if useage <= gf:
		g.blink(0.1,monitoringinterval - 0.1)
		y.off()
		r.off()
	elif useage <= gs:
		g.on()
		y.off()
		r.off()
	elif useage <= ys:
		g.on()
		y.on()
		r.off()
	elif useage <= rs:
		g.on()
		y.on()
		r.on()
	elif useage <= rf:
		g.on()
		y.on()
		r.blink(0.5,0.5)
	elif useage < flatout:
		g.blink(0.5,0.5)
		y.blink(0.5,0.5)
		r.blink(0.5,0.5)	
	elif useage >=flatout:
		g.blink(0.1,0.1)
		y.blink(0.1,0.1)
		r.blink(0.1,0.1)

def ledtest():
	#turn all leds on, and a bit of fancy stuff...
	
	#everything on for one second.
	r.blink(0.5,0.5)
	y.blink(0.5,0.5)
	g.blink(0.5,0.5)
	b.blink(0.5,0.5)
	#wt.pulse()
	#wb.pulse()
	sleep(1.9)
	r.off()
	y.off()
	g.off()
	b.off()
	#wt.off()
	#wb.off()
	sleep(0.5)
	

	
	
	
	


if __name__ == "__main__":
    main()
