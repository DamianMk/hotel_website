from django.shortcuts import render

from django.views import View

from reservations.models import RoomStandard




class RoomStandardView(View):
    def get(self, request):
        standards = []
        for standard in RoomStandard.objects.all():
            data = [standard.standard_name, standard.price]
            standards.append(data)

        html = 'room_standard.html'

        return render(request, html, context={'standards': standards})
















