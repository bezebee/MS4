from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Sketch
from .forms import SketchForm


def sketches(request):
    """Showing all sketches"""

    sketches = Sketch.objects.all()

    context = {
        'sketches': sketches,
    }

    return render(request, 'sketches/sketches.html', context)


def sketch_detail(request, sketch_id):
    """a view to show individual sketch detail"""

    sketch = get_object_or_404(Sketch, pk=sketch_id)

    context = {
        "sketch": sketch,
    }

    return render(request, 'sketches/sketch_detail.html', context)


def add_sketch(request):
    """ Add sketch to users profile"""
    if request.method == 'POST':
        form = SketchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added design')
            return redirect(reverse('add_sketch'))
        else:
            messages.error(request, 'Failed to add your design. Please ensure the form is valid')
    else:
        form = SketchForm()
    template = 'sketches/add_sketch.html'
    context = {
            'form': form,
    }

    return render(request, template, context)
