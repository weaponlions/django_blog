from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.


###     =====================    CLASS BASED TEMPLATE VIEWS ==================== ###

class UserView(TemplateView): 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'APP @ 2'
        return context
    
class UserRedirectView(RedirectView):
    # url = '/app2'
    pattern_name='app2'

    # def get_redirect_url(self, *args, **kwargs):
    #     kwargs['pk'] = 12
    #     return super().get_redirect_url(*args, **kwargs)

###     =====================    CLASS BASED GENERIC VIEWS ==================== ###
### =================== USERCREATION FORM with FORMVIEW =======================####


from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import MyModels

##### ++++++++++++++++++++++++ FORMVIEW +++++++++++++++++ #####
class MyFormView(FormView):
    template_name = 'app2/form.html'
    form_class = UserCreationForm
    success_url = '/app2/Userlist'

    
    def form_valid(self, form):
        fm = UserCreationForm(request.POST)
        fm.save()
        return redirect('userlist')


##### ++++++++++++++++++++++++ LISTVIEW +++++++++++++++++ #####


class UserList(ListView):
    model = MyModels
    template_name='app2/list.html'
    ordering = ['name']
    context_object_name = 'my'

      ###====== Data Filter =======###
    # def get_queryset(self):
    #     return MyModels.objects.filter(name='Harsh')


##### ++++++++++++++++++++++++ CREATEVIEW +++++++++++++++++ #####

class MyModelsCreateView(CreateView):
    model = MyModels
    fields = ['name', 'age']
    template_name = "app2/form.html"
    success_url = '/app2/Userlist'

##### ++++++++++++++++++++++++ DETAILVIEW +++++++++++++++++ #####

class MyModelsDetail(DetailView):
    model = MyModels
    template_name='app2/detail.html'
    context_object_name = 'my'
    

##### ++++++++++++++++++++++++ UPDATEVIEW +++++++++++++++++ #####
class MyModelsUpdateView(UpdateView):
    model = MyModels
    fields = ['name','age']
    template_name = "app2/form.html"
    success_url = '/app2/Userlist/'


##### ++++++++++++++++++++++++ DELETEVIEW +++++++++++++++++ #####

class MyModelsDeleteView(DeleteView):
    model = MyModels
    template_name = "app2/delete.html"
    success_url = '/app2/Userlist/'
