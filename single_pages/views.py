from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'

    )
def mai_profile(request):
    return render(
        request,
        'single_pages/mai_profile.html'

    )
# Create your views here.
