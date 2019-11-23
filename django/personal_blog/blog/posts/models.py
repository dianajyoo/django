from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=250)
  pub_date = models.DateTimeField()
  image = models.ImageField(upload_to='media/', null=True)
  body = models.TextField()

  # edit title of each post in admin
  def __str__(self):
    return self.title

  def prettify_pub_date(self):
    return self.pub_date.strftime('%b %e %Y')

  def summary(self):
    return self.body[:100] # return first 100 char

