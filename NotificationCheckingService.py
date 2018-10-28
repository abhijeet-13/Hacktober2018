# Script forever keeps visiting API endpoint from rep's perspective
# if a question was detected, fire up the question in a new tab

import webbrowser
import time
import requests

while True:
	# wait for 1 second before checking again
	time.sleep(1)
	
	# Access API endpoint from rep's side and obtain response
	r = requests.get('https://dw86fwjspk.execute-api.us-west-2.amazonaws.com/dev/t16etx2rro-dev/tmobilexa/tmobilexa')
	body = r.content.decode("utf-8") 
	
	# Check if the response contains current state and if it is set or reset
	if  '"curr_state":"RESET"' in body:
		#print('RESET')
		pass
	elif '"curr_state":"SET"' in body:
		print('SET')

		# Open the question in the rep's window 
		webbrowser.open_new('127.0.0.1:8000/app/?action=quesreceived')
	else:
		#print('UNKNOWN')
		pass

