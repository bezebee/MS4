from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import OrderForm


# function to render the order form returning order confirmation
# upon submitting


@login_required
def order(request):
    template = "order/order.html"

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "contact/confirmation.html")

    else:
        form = OrderForm()

    context = {
        'form': form,
    }
    return render(request, template, context)
