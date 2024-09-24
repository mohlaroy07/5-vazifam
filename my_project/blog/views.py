from django.shortcuts import render

def Bags_page(request):
    return render(request, 'bag.html')

def Phones_page(request):
    return render(request, 'phone.html')

def Animals_page(request):
    return render(request, 'animal.html')

def Cars_page(request):
    return render(request, 'car.html')

def Books_page(request):
    return render(request, 'book.html')