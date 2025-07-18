from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def profile(request):
    context = {
        'name': 'Tasneem Mohamed',
        'bio': 'Aspiring web developer who loves creating beautiful and functional websites.',
        'skills': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django']
    }
    return render(request, 'profile.html', context)
