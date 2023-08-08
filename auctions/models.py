from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Aucton_listing(models.Model):
    item_list = models.CharField(max_length=64)

# auction listing 
# bids
# comments_auction


# i will need to add additional models to this file to represent details about auction listings,
# bids, comments, and auction categories.  
# 1;34 many to many 