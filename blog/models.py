from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image 
from django.urls import reverse

# Create your models here.

class Posts(models.Model):
	title = models.CharField(max_length=200, blank=False)
	date_posted = models.DateTimeField(default=timezone.now)
	thumbnail = models.ImageField(default="holder.jpg", upload_to="post_images", blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()



	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post-detail", kwargs={"pk": self.pk})


	def save(self):
		super().save()

		img = Image.open(self.thumbnail.path)

		if img.height > 300 or img.width > 300:
			resize = (640, 320)
			img.thumbnail(resize)
			img.save(self.thumbnail.path)




