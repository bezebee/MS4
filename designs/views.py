from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Design, DesignCategory
from .forms import DesignForm


# Create your views here.
def all_designs(request):
    """A view to show all user's designs and searching activities"""

    designs = Design.objects.all()

    context = {
        'designs': designs,
    }

    return render(request, 'designs/designs.html', context)


def design_detail(request, design_id):
    """A view to show user design, including ordering the custom design"""

    design = get_object_or_404(Design, pk=design_id)

    context = {
        'design': design,
    }

    return render(request, 'designs/design_detail.html', context)


def add_design(request):
    """add designs to users profile"""

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only profile owner can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.save()
            messages.success(request, 'Successfully uploaded design')
            return redirect(reverse('design_detail', args=[design.id]))
        else:
            messages.error(request, 'Something went wrong, try again')
    else:
        form = DesignForm()

    template = 'designs/add_design.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_design(request, design_id):
    """Enables user to delete their designs"""
    design = get_object_or_404(Design, pk=design_id)
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES, instance=design)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated design!')
            return redirect(reverse('design_detail', args=[design.id]))
        else:
            messages.error(request, 'Failed to update design. ')
    else:
        form = DesignForm(instance=design)
        messages.info(request, f'You are editing {design.name}')

    template = 'designs/edit_design.html'
    context = {
        'form': form,
        'design': design
    }

    return render(request, template, context)


def delete_design(request, design_id):
    """Delete design from users profile"""
    design = get_object_or_404(Design, pk=design_id)
    design.delete()
    messages.success(request, 'Design deleted!')
    return redirect(reverse('designs'))
