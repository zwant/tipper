from django.db import models
from django.db.models import F

class Team(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=1)

    def __str__(self):
        return self.name

class Game(models.Model):
    time = models.DateTimeField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')

    def __str__(self):
        return '{} vs {}'.format(self.home_team, self.away_team)


class Result(models.Model):
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    game = models.OneToOneField(Game, on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.home_score, self.away_score)
