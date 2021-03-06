from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .services import get_characters

class GetInfo(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'characters' : get_characters(),
        }
        return context
