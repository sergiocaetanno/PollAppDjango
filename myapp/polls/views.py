from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello,wold. You're at the polls index.")