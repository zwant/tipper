from django.contrib import admin
from .models import Game, Team, Result

class GameAdmin(admin.ModelAdmin):
    model = Game
    ordering = ('time',)
    list_display = ('time', 'home_team', 'away_team', 'result')

class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ('name', 'group')


admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Result)
