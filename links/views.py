from django.shortcuts import render
from django.utils import timezone
from .models import Link, Video

# Create your views here.
def link_list(request):
    links = Link.objects.filter(created_date__lte=timezone.now())
    video = Video.objects.all()
    return render(request, 'links/link_list.html', {'links': links, 'title': 'Home', video: video})