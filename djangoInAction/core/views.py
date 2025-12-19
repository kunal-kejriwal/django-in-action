from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.

def core_home(request):
    list_features = Feature.objects.all()
    # return HttpResponse(
    #     "Welcome to the Core Application of Django-In-Action project. "
    #     "Current List of features is -> " + str(list(list_features))
    # )
    
    # returning a view
    
    return render(request, 'core/home.html')
    
def first_view(request):
    return HttpResponse("This is the first view added, in the CORE app.")


def context_template(request):
    context = {
        'context_placeholder' : 'This is being fetched via a Context variable in HTML Template'
    }
    
    return render(request, 'core/context-template.html', context)