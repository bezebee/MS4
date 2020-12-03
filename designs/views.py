from django.shortcuts import render, get_object_or_404
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


def add_design(request):
    """add designs to users profile"""
    form = DesignForm()
    template = 'designs/add_design.html'
    context = {
        'form': form,
    }

    return render(request, template, context)