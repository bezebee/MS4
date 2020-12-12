from django.shortcuts import render

# Create your views here.

def view_orders(request):
    """ A view that renders the orders contents page """

    return render(request, 'orders/orders.html')