from django.shortcuts import render
from .models import Design

# Create your views here.
def all_designs(request):
    """A view to show all user's designs and searching activities"""

    designs = Design.objects.all()

    context = {
        'designs': designs,
    }

    return render(request,'designs/designs.html', context)
