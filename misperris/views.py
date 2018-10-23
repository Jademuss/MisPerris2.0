from django.shortcuts import render
from .models import Goku

def goku_list(request):
    return render(request, 'misperris/goku_list.html', {})

def goku_formulario(request):
    return render(request, 'misperris/goku_formulario.html', {})

def goku_notfound(request):
    return render(request, 'misperris/goku_notfound.html', {})
    

   # def goku_notfound(request, pk):
   #goku = get_object_or_404(Goku, pk=pk)
   # return render(request, 'misperris/goku_notfound.html', {'goku': goku})

    #def goku_formulario(request):
    #if request.method == "GOKU":
     #   form = GokuForm(request.GOKU)
     #   if form.is_valid():
     #       goku = form.save(commit=False)
     #       goku.author = request.user
     #       goku.published_date = timezone.now()
     #       goku.save()
     #       return redirect('misperris.views.goku_notfound', pk=goku.pk)
    #else:
     #   form = GokuForm()
   # return render(request, 'misperris/goku_formulario.html', {'form': form})