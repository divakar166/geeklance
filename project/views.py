from django.http import HttpResponse,JsonResponse

# Create your views here.
def projects(request):
  return JsonResponse({"data":"data"})