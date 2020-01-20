from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class SignUp(generic.CreateView):
    """
        Function that handles signup
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('Index')
    template_name = 'registration/register.html'
    
class HomePageView(LoginRequiredMixin, ListView):
    """
        Function to display home page
    """
    template_name = "home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


@login_required()
def profile(request):
    """
        Function for creating profile
    """
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
        return render(request,'profile.html',{"form":form})
    

class UpdateProfileView(UpdateView):
    """
        Function for updating profile
    """
    model = Post
    form_class = PostForm
    template_name = "profile.html"
    success_url = reverse_lazy("home")


class BlogPageView(LoginRequiredMixin, ListView):
    """
        Function to display blog page
    """
    model = BlogPost
    template_name = "posts/blogs.html"
    context_object_name = "blogposts"
    ordering = ["-date_posted"]


class EducationView(LoginRequiredMixin, ListView):
    """
        Function for displaying education page
    """
    model = Education
    template_name = "posts/education.html"
    context_object_name = "educations"
    ordering = ["-date_posted"]



class BusinessView(LoginRequiredMixin, ListView):
    """
        Function for displaying business page
    """
    model = Business
    template_name = "posts/businesses.html"
    context_object_name = "businesses"
    ordering = ["-date_posted"]




class AuthorityView(LoginRequiredMixin, ListView):
    """
        Function for displaying security issues
    """
    model = Authorities
    template_name = "posts/authority.html"
    context_object_name = "authorities"
    ordering = ["-date_posted"]


@login_required()

def search_results(request):
    """
        Search function
    """
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_business(search_term)
        message=f"{search_term}"

        print(searched_businesses)

        return render(request,'posts/search.html',{"message":message,"businesses":searched_businesses,"profile":profile})

    else:
        message="You haven't searched for any term"
        return render(request,'posts/search.html',{"message":message})

@login_required()
def user_dashboard(request):
    """
        function for displaying dashboard
    """
    return render(request, 'dashboard.html')
