from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
from django.views.generic import FormView,ListView,UpdateView,CreateView,DetailView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from . import forms
from .import models
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from taggit.models import Tag
from django.contrib.auth.mixins import LoginRequiredMixin
def BaseView(request):
    return render(request,"marketapp/base.html")

def HomePageView(request):
    return render(request,"marketapp/homepage.html")

class ProjectListView(ListView):
    template_name='marketapp/projectlist.html'
    model=models.Project
    def get_queryset(self, *args, **kwargs): 
        qs = super(ProjectListView, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("-id") 
        return qs
    
    
class HostorCollab(TemplateView):
    template_name='marketapp/hostorcollab.html'
    
class RegisterView(FormView):
    template_name='marketapp/register.html'
    form_class=forms.CustomUserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('hostorcollab')
        
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterView,self).form_valid(form)
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterView,self).get(*args,**kwargs)
    
class UserLogin(LoginView):
    models=User
    template_name='marketapp/login.html'
    redirect_authenticated_user=True
    
    def get_success_url(self) :
        return reverse_lazy('home')
    
    
    
class DataCollection(LoginRequiredMixin,UpdateView):
    model=models.Collaborator
    fields=['description','tags']
    template_name='marketapp/survey.html'
    success_url=reverse_lazy("home")

class CreateProject(LoginRequiredMixin,CreateView):
    model=models.Project
    fields=['name','description','tags']
    #form_class=forms.ProjectForn
    template_name='marketapp/addproject.html'
    success_url=reverse_lazy("home")
    def form_valid(self, form):
        project=form.save(commit=False)
        project.User=self.request.user
        if project is not None:
            login(self.request,project)
    
class ProjDetail(DetailView):
    model=models.Project
    template_name='marketapp/projectdetail.html'
    context_object_name='product'
    
    
''''def DataCollection(request):
    form =forms.DataForm (request.POST)
    form.is_valid():
        try:
            form.instance.created_by = request.user
                form.save()
                return redirect('order_management:table_allotment_home')
            except IntegrityError as err:
                print('err => ', err)
                context['unique_error'] = 'User has already assigned table for today'
    context = {
        'form':form,
    }
    return render(request, 'marketapp/survey.html', context)

def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'detail.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)'''
    
    
    
