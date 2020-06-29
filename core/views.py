from django.shortcuts import render, reverse

from django.views.generic import TemplateView
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = "core/home.html"
