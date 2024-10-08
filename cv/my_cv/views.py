from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    context = {

    }
    return render(request, "home.html", context)

def about(request):
    context = {

    }
    return render(request, "about.html", context)

def resume(request):
    context = {

    }
    return render(request, "resume.html", context)

def services(request):
    context = {

    }
    return render(request, "services.html", context)

def portfolio(request):
    context = {

    }
    return render(request, "portfolio.html", context)

def estate_manage(request):
    return render(request, "portfolio_est_mana_detail.html")

def banking(request):
    return render(request, "portfolio_banking_detail.html")

def calculator(request):
    return render(request, "portfolio_calc_detail.html")

def tic_tac_toe(request):
    return render(request, "portfolio_tic_detail.html")

def contact_me(request):
    form = ContactForm(request.POST if request.method == 'POST' else None)

    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')

        send_mail(from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['chrischidera6@gmail.com', 'chidera.ohanenye-ohiaekpete@stu.cu.edu.ng'],
                    subject=subject,
                    message=f"Sender's Name: {name.title()} \n\nSender's Email: {email.lower()} \n\n" + message,
                    fail_silently=False)

        return JsonResponse({'success': True})
    elif request.method == 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid form submission.'})

    context = {
        'form': form,
    }
    return render(request, "contact_me.html", context)
