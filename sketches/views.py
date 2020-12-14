from django.shortcuts import render
from .models import Sketch


def sketches(request):
    """Showing all sketches"""

    sketches = Sketches.objects.all()

    context = {
        'sketches': sketches,
    }

    return render(request, 'sketches/sketch.html', context)
