from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'game/home.html', context=None)