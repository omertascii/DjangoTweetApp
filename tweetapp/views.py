from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required



def tweets(request):
    tweets_data = models.User.objects.all()
    tweets_context = {"tweets": tweets_data}
    return render(request, 'tweetapp/tweets.html',context=tweets_context)


@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        message = request.POST["message"]
        models.User.objects.create(username=request.user , message=message)
        return redirect(reverse('tweetapp:tweets'))
    else:
        return render(request,'tweetapp/addtweet.html')
    
@login_required
def deletetweet(request,id):
    tweet = models.User.objects.get(pk=id)
    if request.user == tweet.username:
        models.User.objects.filter(id=id).delete()
        return redirect('tweetapp:tweets')



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


