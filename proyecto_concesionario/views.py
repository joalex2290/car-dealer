from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):

    def get_template_names(self):
        """
        Returns a different template depending
        on whether the user is logged in or not
        """
        if self.request.user.is_active:
            return 'manager/index.html'
        else:
            return 'guest_homepage.html'
