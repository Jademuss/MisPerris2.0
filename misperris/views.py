from django.shortcuts import render

def goku_list(request):
    return render(request, 'misperris/goku_list.html', {})