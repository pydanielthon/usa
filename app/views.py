from django.shortcuts import render
from .forms import NewForm
# Create your views here.
from django.http import HttpResponseRedirect

def home(request):
    context = {

    }


    return render(request, "websites/home.html", context)




def site2(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = NewForm()
    return render(request, 'websites/site2.html', {'form': form})

