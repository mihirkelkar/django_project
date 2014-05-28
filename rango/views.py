# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World from the Amazing Bistro !. Learn More about us <a href='/rango/about'>here</a>")

def about(request):
	return HttpResponse("Here is the about Page for the Bistro. <a href = '/rango/'>Go Back</a>")
