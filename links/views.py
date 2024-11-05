from django.shortcuts import render

# Create your views here.
def link_list(request):
    return render(request, 'links/link_list.html', {})