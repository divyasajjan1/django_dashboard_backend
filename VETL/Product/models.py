from django.db import models

# Create your models here.
class TeamDC(models.Model):
    player_name = models.CharField(max_length=100)
    player_height = models.FloatField(default=0.0)
    player_weight = models.FloatField(default=0.0)
    player_matches_played = models.IntegerField(default=0)


class TeamMarvel(models.Model):
    player_name = models.CharField(max_length=100)
    player_height = models.FloatField(default=0.0)
    player_weight = models.FloatField(default=0.0)
    player_matches_played = models.IntegerField(default=0)