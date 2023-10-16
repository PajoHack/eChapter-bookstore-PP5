from django.shortcuts import render
from django.core.exceptions import PermissionDenied

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def custom_404(request, exception):
    return render(request, 'home/404.html', {}, status=404)


def custom_500(request):
    return render(request, 'home/500.html', {}, status=500)


def custom_403(request, exception):
    return render(request, 'home/403.html', {}, status=403)


def trigger_403_error(request):
    raise PermissionDenied
