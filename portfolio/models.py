from django.db import models
from django.db.models.fields import URLField, FilePathField, CharField, TextField
# Create your models here.

class Portfolio_Model_Home(models.Model):
    home_url = URLField(max_length=500)
    home_html = TextField(max_length=1000000)
    home_css = TextField(max_length=1000000)
    home_js = TextField(max_length=1000000)


