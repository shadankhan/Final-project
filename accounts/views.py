from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import smtplib
from email.message import EmailMessage
# from accounts.email_cred import *  # import the email creadential to send the mail

# Create your views here.
def register(request):
	if request.method == "POST":
		username = request.POST["username"]
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		email = request.POST["email"]
		password1 = request.POST["password1"]
		password2 = request.POST["password2"]

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, "Username Exists")
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email Exists")
				return redirect('register')
			else:
				user = User.objects.create_user(
					username=username,
					first_name=first_name,
					last_name=last_name,
					email= email,
					password=password1
					)
				user.save()
				# email = EmailMessage()
				# email['from'] = 'Your Name'
				# email['to'] = 'shadankhan.an@gmail.com'
				# email['subject'] = 'Welcome to Our Website!'

				# email.set_content("Yay you're proud user of totalk!")

				# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
				# 	smtp.ehlo()
				# 	smtp.starttls()
				# 	smtp.login(email_1, password_1) 
				# 	smtp.send_message(email)
				# 	print("Done")
				return redirect('create_profile')
		else:
			messages.info(request,"Password Not Matching")
			return redirect('register')

	return render(request, 'register.html')

def login(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/totalk/going_out')
		else:
			messages.info(request, "Invalid Username and Password")
			return redirect('login')

	return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')
