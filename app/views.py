from django.shortcuts import render,get_object_or_404,redirect
from .models import Project
from django.views.generic import ListView,DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

# def home(request):
#     context = {
#         'projects':Project.objects.all()
#     }
#     return render(request,'index.html',context)

# def detail(request,id):
#     context = {
#         'project':get_object_or_404(Project,pk=id)
#     }
#     return render(request,'detail.html',context)

class HomePageView(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = Project
    context_object_name ='projects'
    
class ProjectDetailView(LoginRequiredMixin,DetailView):
    template_name = 'detail.html'
    model = Project
    context_object_name = 'project'
    
@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Project.objects.filter(
            Q(name__icontains=search_term)|
            Q(email__icontains=search_term)|
            Q(info__icontains=search_term)
            )
        context = {
             'search_term': search_term,
             'projects':search_results
    }
        return render(request,'search.html',context)
    else:
        return redirect('home')

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = 'create.html'
    fields = ['name','email','info','image']
    success_url = '/'
    
class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = 'update.html'
    fields = ['name','email','info','image']
    
    def form_valid(self,form):
        instance = form.save()
        return redirect('detail',instance.pk) 
        
class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    template_name = 'delete.html'
    success_url = '/'
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'