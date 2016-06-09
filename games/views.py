from django.http import HttpResponse
from django.views.generic import View

class GameView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
