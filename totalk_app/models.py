from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	image = models.ImageField(upload_to="static/profile_pic")
	city = models.CharField(max_length=100)	
	Bio = models.TextField()
	ocupation = models.CharField(max_length=150)
	insta = models.URLField(null=True, blank=True)
	linkedin = models.URLField(null=True, blank=True)
	verify = models.BooleanField(null=True, blank=True, default=False)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	user = models.ForeignKey(
		User, 
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return self.user.username

class Invitation(models.Model):
	raising_request_for = models.TextField()
	location = models.CharField(max_length=300)
	dateandtime = models.DateTimeField(null=True, blank=True)
	going_out_for = models.CharField(max_length=12, null=True, choices=(('Coffee', 'Coffee'),('Lunch', 'Lunch'), ('Dinner', 'Dinner')))
	interested = models.ManyToManyField(
		User,
		related_name='accept',
		blank=True
		)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	profile = models.ForeignKey(
		Profile, 
		on_delete=models.CASCADE,
		blank=True
		)

	def __str__(self):
		return self.going_out_for

