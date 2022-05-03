from django.shortcuts import render

# Create your views here
def showindex(request):
    return render(request, 'main/index.html')

def showintroduction(request):
    return render(request, 'main/introduction.html')