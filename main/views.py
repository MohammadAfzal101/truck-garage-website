from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')
def contact(request):
    return render(request, 'main/contact.html')
def about(request):
    return render(request, 'main/about.html')
def gallery(request):
    return render(request, 'main/gallery.html')
def services(request):
    return render(request, 'main/services.html')

# def services(request):
#     return render(request, 'services.html')