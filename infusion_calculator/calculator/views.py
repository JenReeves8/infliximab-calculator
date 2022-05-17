from django.shortcuts import render, redirect

def home_page(request):
    return render(request, "home_page.html")

def new_infusion(request):
    return render(request,"new_infusion.html")
