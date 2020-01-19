from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
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

def index(request):
    """
        Home view on login
    """
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')
    return render(request,'index.html')



@login_required(login_url='/accounts/login/')
    
def my_profile(request):
    """
        Admin's profile view function
    """
    current_user=request.user
    profile =Profile.objects.get(username=current_user)
    return render(request,'profile/user_profile.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    """
        Profile view function
    """
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)

@login_required(login_url='/accounts/login/')
def create_profile(request):
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
        return render(request,'profile/profile_form.html',{"form":form})
    

@login_required(login_url='/accounts/login/')
def update_profile(request):
    """
        Function for updating profile
    """
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =UpdateprofileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = UpdateprofileForm(instance=profile)
    else:
        form = UpdateprofileForm()

    return render(request,'profile/update_profile.html',{"form":form})

class BlogPageView(LoginRequiredMixin, ListView):
    """
        Function to display blog page
    """
    model = BlogPost
    template_name = "posts/blogs.html"
    context_object_name = "blogposts"
    ordering = ["-date_posted"]


@login_required(login_url='/accounts/login/')
def new_blogpost(request):
    """
        Function for creating new blog
    """
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            blogpost = form.save(commit = False)
            blogpost.username = current_user
            blogpost.neighbourhood = profile.neighbourhood
            blogpost.profpic = profile.profpic
            blogpost.save()

        return HttpResponseRedirect('/blog')

    else:
        form = BlogPostForm()

    return render(request,'posts/blogpost_form.html',{"form":form})



class EducationView(LoginRequiredMixin, ListView):
    """
        Function for displaying education page
    """
    model = Education
    template_name = "posts/education.html"
    context_object_name = "educations"
    ordering = ["-date_posted"]

@login_required(login_url='/accounts/login/')
def new_education(request):
    """
        Function for creating new education post
    """
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =EducationForm(request.POST,request.FILES)
        if form.is_valid():
            education = form.save(commit = False)
            education.owner = current_user
            education.neighbourhood = profile.neighbourhood
            education.save()
        return HttpResponseRedirect('/education')

    else:
        form = EducationForm()
    return render(request,'posts/education_form.html',{"form":form})

class BusinessView(LoginRequiredMixin, ListView):
    """
        Function for displaying business page
    """
    model = Business
    template_name = "posts/businesses.html"
    context_object_name = "businesses"
    ordering = ["-date_posted"]
    
@login_required(login_url='/accounts/login/')
def new_business(request):
    """
        Function for creating business post
    """
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.owner = current_user
            business.neighbourhood = profile.neighbourhood
            business.save()

        return HttpResponseRedirect('/businesses')

    else:
        form = BusinessForm()

    return render(request,'posts/business_form.html',{"form":form})




class AuthorityView(LoginRequiredMixin, ListView):
    """
        Function for displaying security issues
    """
    model = Authorities
    template_name = "posts/authority.html"
    context_object_name = "authorities"
    ordering = ["-date_posted"]


@login_required(login_url='/accounts/login/')
def new_authority(request):
    """
        Function for creating security
    """
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =AuthorityForm(request.POST,request.FILES)
        if form.is_valid():
            authority = form.save(commit = False)
            authority.username = current_user
            authority.neighbourhood = profile.neighbourhood
            authority.profpic = profile.profpic
            authority.save()

        return HttpResponseRedirect('/')

    else:
        form = AuthorityForm()

    return render(request,'posts/authority_form.html',{"form":form})


@login_required(login_url='/accounts/login/')

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

@login_required()
def registered_users(request):
    """
        Function for displaying registerd users
    """
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users.html', context)

@login_required()
def user_deactivate(request, user_id):
    """
        Function for deactivating users 
    """
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    messages.success(request, "User account has been successfully deactivated!")
    return redirect('system_users')
@login_required()
def user_activate(request, user_id):
    """
        Function for activating users 
    """
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()
    messages.success(request, "User account has been successfully activated!")
    return redirect('system_users')