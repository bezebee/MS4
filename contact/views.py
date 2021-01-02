from django.shortcuts import render

from .forms import ContactForm


def contact(request):
    template = "contact/contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "contact/confirmation.html")

    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, template, context)
