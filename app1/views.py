from django.shortcuts import render, redirect
from .forms import MyForm, MyModelForm

# Create your views here.
## -------------- SIMPLE FORM -------------------- ##
def index(request):
    if request.method == 'POST':
        fm = MyForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            return redirect('app1')
        else:
            return render(request, 'app1/main.html', {'form': fm, 'action' : 'app1'})
    else:
        return render(request, 'app1/main.html', {'form': MyForm(), 'action' : 'app1'})


## --------------- Manual Model Form -------------- ##
def indexTwo(request):
    if request.method == 'POST':
        fm = MyModelForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            fm.save()
            return redirect('modelForm')
        else:
            return render(request, 'app1/main.html', {'form': fm, 'action' : 'app1'})
    else:
        return render(request, 'app1/main.html', {'form': MyModelForm(), 'action' : 'modelForm'})

    