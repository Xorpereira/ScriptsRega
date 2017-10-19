import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

GPIO.setup([5,6,13,19],GPIO.IN, pull_up_down=GPIO.PUD_DOWN);


prevstate = [0, 0, 0, 0];
input =[0, 0, 0, 0]; 
var = 1;


while var == 1 :
	
	input[0] = GPIO.input(5);
	input[1] = GPIO.input(6);
	input[2] = GPIO.input(13);
	input[3] = GPIO.input(19);

	if ( prevstate[0] != input[0] ) :
		print "Button 1 Pressed"
		if ( input[0] == 1 ) :
                        r=requests.get("http://esteirense:8080/bin/manual?zone=zc&state=on")
		else :
                        r=requests.get("http://esteirense:8080/bin/manual?zone=zc&state=off")
                        r=requests.get("http://esteirense:8080/bin/run?system=on")
                prevstate[0] = input[0];
		print "prevstate1 alterado: ", prevstate[0]
	if ( prevstate[1] != input[1] ) :
		print "Button 2 Pressed"
		if ( input[1] == 1 ) :
                        r=requests.get("http://esteirense:8080/bin/manual?zone=zd&state=on")
		else :
                        r=requests.get("http://esteirense:8080/bin/manual?zone=zd&state=off")
                        r=requests.get("http://esteirense:8080/bin/run?system=on")
                prevstate[1] = input[1];
		print "prevstate2 alterado: ", prevstate[1]
	if ( prevstate[2] != input[2] ) :
		print "Button 3 Pressed"
		if ( input[2] == 1 ) :
                        r=requests.get("http://esteirense:8080/bin/manual?zone=zh&state=on")
		else :
                        r=requests.get("http://esteirense:8080/bin/manual?zone=zh&state=off")
                        r=requests.get("http://esteirense:8080/bin/run?system=on")
                prevstate[2] = input[2];
		print "prevstate3 alterado: ", prevstate[2]
	if ( prevstate[3] != input[3] ) :
		print "Button 4 Pressed"
		if ( input[3] == 1 ) :
                        r=requests.get("http://esteirense:8080/bin/manual?zone=zm&state=on")
		else :
                        r=requests.get("http://esteirense:8080/bin/manual?zone=zm&state=off")
                        r=requests.get("http://esteirense:8080/bin/run?system=on")
                prevstate[3] = input[3];
		print "prevstate4 alterado: ", prevstate[3]
	time.sleep (1)
