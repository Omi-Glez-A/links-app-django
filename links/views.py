from django.shortcuts import render
from django.utils import timezone
from .models import Link

# Create your views here.
def link_list(request):
    links = Link.objects.filter(created_date__lte=timezone.now())
    return render(request, 'links/link_list.html', {'links': links, 'title': 'Home'})