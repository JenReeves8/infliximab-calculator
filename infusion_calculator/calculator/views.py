from django.shortcuts import render, redirect

def home_page(request):
    if 'user' not in request.session:
        return redirect('/')
    return render(request, "home_page.html")

def new_infusion(request):
    if 'user' not in request.session:
        return redirect('/')
    return render(request,"new_infusion.html")
