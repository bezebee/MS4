from django.shortcuts import render,redirect, reverse, get_object_or_404
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

    return render(request,'designs/designs.html', context)


def design_detail(request, design_id):
    """A view to show user design, including ordering the custom design"""

    design = get_object_or_404(Design, pk=design_id)

    context = {
        'design': design,
    }

    return render(request,'designs/design_detail.html', context)

@login_required
def add_design(request):
    """add designs to users profile"""
    if request.method == "POST":
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully uploaded design')
            return redirect(reverse('designs'))
        else:
            messages.error(request, 'Something went wrong, try again')
    else:
        form = DesignForm()

    template = 'designs/add_design.html'
    context = {
        'form': form,
    }

    return render(request, template, context)