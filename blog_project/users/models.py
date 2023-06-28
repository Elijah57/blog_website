from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=50, blank=True, null=True)
	lastname =  models.CharField(max_length=50,blank=True, null=True)
	image = models.ImageField(default= "img.jpg", upload_to="profilepic")
	bio = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"{self.user.username} profile"

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
