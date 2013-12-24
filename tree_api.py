#!/usr/bin/python

from bottle import route, run,  static_file, response
import sys



try:
	import RPi.GPIO as GPIO ## Import GPIO library
	GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
	GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
	ON_RPI = True
	PORT = 80
except:
	print 'not running on Rpi'
	ON_RPI = False
	PORT = 8080


@route('/on')
def turn_on():
    try:
    	print 'tree is on now'
    	if ON_RPI:
    		  GPIO.output(7,False)
    	return 'OK'
    except:
    	traceback.print_exc()
    	return 'BAD'

@route('/off')
def turn_off():
	try:
		print 'tree is now off'
		if ON_RPI:
			GPIO.output(7,True)

		return 'OK'
	except:
		traceback.print_exc()
    	return 'BAD'

@route('/log')
def getlog():
	response.set_header('Content-Type', 'text/plain')
	return open('tree.log').read()

if __name__ == '__main__':
	run(host='', port=PORT, debug=True, reloader=True)

