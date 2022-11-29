
from django.http import HttpResponse

# Create your views here.
def logueado(request):
    return HttpResponse(request,'index/index.html')
