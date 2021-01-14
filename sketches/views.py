from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Sketch
from .forms import SketchForm


@login_required
def sketches(request):
    """Showing all sketches"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only profile owners can do that.')
        return redirect(reverse('home'))

    sketches = Sketch.objects.all()

    context = {
        'sketches': sketches,
    }

    return render(request, 'sketches/sketches.html', context)


@login_required
def sketch_detail(request, sketch_id):
    """a view to show individual sketch detail"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only profile owners can do that.')
        return redirect(reverse('home'))

    sketch = get_object_or_404(Sketch, pk=sketch_id)

    context = {
        "sketch": sketch,
    }

    return render(request, 'sketches/sketch_detail.html', context)


@login_required
def add_sketch(request):
    """ Add sketch to users profile"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only profile owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def delete(request, sketch_id):
    """Delete sketch of the system"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    sketch = get_object_or_404(Sketch, pk=sketch_id)
    sketch.delete()
    messages.success(request, 'Design deleted!')
    return redirect(reverse('sketches'))
