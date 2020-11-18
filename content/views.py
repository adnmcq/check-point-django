from django.shortcuts import render

# Create your views here.



def index(request):
    context = { 'a': 0}
    return render(request, 'content/index.html', context)

def about(request):
    context = { 'a': 0}
    return render(request, 'content/about.html', context)


def contact(request):
    context = { 'a': 0}
    return render(request, 'content/contact.html', context)