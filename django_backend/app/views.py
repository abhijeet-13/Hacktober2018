from django.shortcuts import render
from twilio.rest import Client


# Create your views here.

from django.http import HttpResponse

def index(request):
	params = request.GET
	if 'quesresponse' in params:
		text = params['quesresponse']
		print(text)
		
		# Send a text message to the customer
		client = Client('AC33d6e631bf9b652d14a6e742f34a84d2', '9c063b571769f028cd1837bb7d9c703e')
		client.messages.create(to='+14692580330', from_='+18176637305' , body=text)
		
		return HttpResponse('The customer has been responded to.')
	if 'action' in params:
		# Customer rep interface
		if params['action'] == 'quesreceived':
			#return HttpResponse('Qustion for the rep')
			return HttpResponse('''
			<html>
			<body>
			<h1 style="text-align: center; padding-left: 30px;"><strong>T-Mobile Customer Engagement Portal</strong></h1>
<p>&nbsp;</p>
<p style="padding-left: 30px;">1 new question received.</p>
<p style="padding-left: 30px;">&nbsp;</p>
<p style="padding-left: 30px;"><em><strong>Question:</strong></em></p>
<table style="margin-left: 30px; background-color: #ff009f; width: 500px;" cellspacing="10" cellpadding="20">
<tbody>
<tr>
<td><strong>Can I get seven lines on T-Mobile One?</strong></td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p style="padding-left: 30px;"><em><strong>Respond:</strong></em></p>
<form style="padding-left: 30px;"><input id="quesresponse" style="background-color: #ffd2fa; width: 500px; height: 200px;" name="quesresponse" type="text" />
<p style="text-align: left;"><input type="submit" value="Submit" /></p>
</form>
			</body>
			</html>''')
	else:
		return HttpResponse("You have 0 messages to respond.")
