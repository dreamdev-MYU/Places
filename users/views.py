from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm,LoginForm,ProfileUpdateview, ResetPasswordForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, FriendRequest


class RegisterView(View):
    def get(self,request):
        form=RegisterForm()
        return render(request,'users/register.html',context={"form":form})
    
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,"Siz muvaffaqiyatli registratsiya qildingiz ")
            return redirect('landing')

        return render(request,'users/register.html',context={"form":form})

class Loginview(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'users/login-page.html',context={"form":form})
    
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
             username=form.cleaned_data['username']
             password=form.cleaned_data['password']
             user=authenticate(username=username,password=password)
             if user is not None:
                 login(request,user)
                 messages.success(request,"Siz muvaffaqiyatli login qildingiz ")
                 return redirect('landing')
        return render(request,'users/login-page.html',context={"form":form})
    

class Logoutview(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,"Siz muvaffaqiyatli logout qildingiz ")
        return redirect('landing')
    

class Profileview(View):
    def get(self,request):
        form=ProfileUpdateview(instance=request.user)
        return render(request,'users/profile.html',context={"form":form})

    def post(self,request):
        form=ProfileUpdateview(instance=request.user,data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request,"Siz muvaffaqiyatli yangilanish qildingiz ")
            return redirect('landing')
        return render(request,'users/profile.html',context={"form":form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile-view.html')
    

class ResetPasswordView(LoginRequiredMixin, View):
    def get(self,request):
        form = ResetPasswordForm()
        
        return render(request, 'users/reset-password.html', {"form":form}) 
    
    def post(self,request):
        form = ResetPasswordForm(request.POST)
        user = request.user
        if form.is_valid():
            if checkpassword(user, form.cleaned_data['old_password']):
                user.set_password(form.cleaned_data['confirm_password'])
                user.save()
                return redirect("users:profile-view")

            else:
                return render(request, 'users/reset-password.html', {"form":form})
       
        return render(request, 'users/reset-password.html', {"form":form})
        

def checkpassword(user, password):
    return user.check_password(password)


class UserView(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.exclude(username = request.user.username).exclude(friends = request.user)
        friend_requests = User.objects.filter(id__in=FriendRequest.objects.filter(from_user=request.user).values_list('to_user'))
        
        return render(request, 'users/users-list.html', {"users":users, "friend_requests":friend_requests})
    

class MyNetworksView(LoginRequiredMixin, View):
    def get(self, request):
        networks = FriendRequest.objects.filter(to_user=request.user, is_accepted=False)

        
        suggested_friends = User.objects.exclude(id=request.user.id).exclude(friends=request.user).filter(friends__in=request.user.friends.all())

        return render(request, 'users/networks.html', {"networks": networks, "suggested_friends": suggested_friends})
    

class AcceptFriendRequestView(LoginRequiredMixin, View):
    def get(self, request, id):
        friend_request = FriendRequest.objects.get(id=id)
        from_user = friend_request.from_user

        main_user = request.user
        main_user.friends.add(from_user)
        from_user.friends.add(main_user)

        friend_request.is_accepted = True
        friend_request.save()
    
        FriendRequest.objects.get_or_create(from_user=from_user, to_user=main_user)

        return redirect("users:networks")

    
class IgnoreFriendRequestView(LoginRequiredMixin, View):
    def get(self, request, id):
        friend_request = FriendRequest.objects.get(id=id)
        user = request.user
        friend_request.delete()
        
        return redirect("users:networks")


class DeleteFromFriendsView(LoginRequiredMixin, View):
    def get(self, request, id):
        friend = User.objects.get(id=id)
        user = request.user
        user.friends.remove(friend)
        friend.friends.remove(user)
        return redirect("users:list")


class SendFriendRequestView(LoginRequiredMixin, View):
    def get(self, request, id):
        to_user = User.objects.get(id=id)
        from_user = request.user
     
        if to_user in from_user.friends.all() or FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
           
            return redirect("users:list")
        
        FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
       
        return redirect("users:list")


