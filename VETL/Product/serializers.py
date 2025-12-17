from .models import TeamDC, TeamMarvel
from rest_framework import serializers

class TeamDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamDC
        fields=['id', 'player_name', 'player_height', 'player_weight', 'player_matches_played']

class TeamMarvelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMarvel
        fields=['id', 'player_name', 'player_height', 'player_weight', 'player_matches_played']