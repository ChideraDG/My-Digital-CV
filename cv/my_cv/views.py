from django.shortcuts import render

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
