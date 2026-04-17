from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # You can save this to database or send mail later
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()  # clear form after success
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
