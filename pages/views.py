from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Header



class HomeView(ListView):
    def get(self, request, *args, **kwargs):
        headers = list(Header.objects.filter(status=True).order_by('position')[:3])

        carousel_image1 = headers[0]
        carousel_image2 = headers[1]
        carousel_image3 = headers[2]

        ctx = {
            'carousel_image1': carousel_image1,
            'carousel_image2': carousel_image2,
            'carousel_image3': carousel_image3,
        }
        return render(request, 'pages/index.html', ctx) 