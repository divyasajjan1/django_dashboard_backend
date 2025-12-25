from django.db import models

# Create your models here.
# class TeamDC(models.Model):
#     player_name = models.CharField(max_length=100)
#     player_height = models.FloatField(default=0.0)
#     player_weight = models.FloatField(default=0.0)
#     player_matches_played = models.IntegerField(default=0)


# class TeamMarvel(models.Model):
#     player_name = models.CharField(max_length=100)
#     player_height = models.FloatField(default=0.0)
#     player_weight = models.FloatField(default=0.0)
#     player_matches_played = models.IntegerField(default=0)

class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.CharField(max_length=20)
    player_name = models.CharField(max_length=100, db_column="name")
    player_height = models.FloatField(db_column="height")
    player_weight = models.FloatField(db_column="weight")
    player_matches_played = models.IntegerField(db_column="games")

    class Meta:
        db_table = "players"   # <-- must match existing table name
        managed = False        # <-- Don’t try to create or modify this table.
