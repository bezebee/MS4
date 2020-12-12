from django.shortcuts import render, redirect

# Create your views here.

def view_orders(request):
    """ A view that renders the orders contents page """

    return render(request, 'orders/orders.html')


def order(request, order_id):
    """Add quantity of the specified design to the order"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    orders = request.session.get('orders', {})

    if order_id in list(orders.keys()):
        orders[order_id] += quantity
    else:
        orders[order_id] = quantity

    request.session['orders'] = orders
    print(request.session['orders'])
    return redirect(redirect_url)
