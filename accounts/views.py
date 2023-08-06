from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, ProfileForm, LoginForm
from .models import CustomUser, Profile


# views.py


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])  # Set the password
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('complete_profile')
        else:
            error_massage = form.errors
            print(type(error_massage))

            return render(request, 'signup.html', {'form': form, 'error': error_massage})
            # return HttpResponse(form.errors)  # Handle the error case
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def complete_profile(request):
    user_id = request.user.id
    # (get_object_or_404(CustomUser, id=user_id))
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST' and user:
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            if request.FILES:
                uploaded_picture = request.FILES.get('picture')  # Assign the uploaded picture
                new_picture_name = f"profile_{user.profile.id}.{uploaded_picture.name.split('.')[-1]}"
                form.instance.picture.save(new_picture_name, uploaded_picture, save=False)  # Assign the renamed picture

            form.save()
            user.completed_profile = True
            user.save()
            login(request, user)
            return redirect('user_info')
        else:

            return render(request, 'complete_profile.html', {'form': form, 'user': user})
    elif user:
        form = ProfileForm(instance=user.profile)
        return render(request, 'complete_profile.html', {'form': form, 'user': user})
    else:
        redirect('signup')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['email'].strip()
            password = form.cleaned_data['password'].strip()
            print(username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user_info')
            else:
                errorStr = "Invalid username or password."
                if form.errors:
                    for field in form:
                        for error in field.errors:
                            if field.label == 'Captcha':
                                errorStr = 'pleas verify that you are human'
                form = LoginForm()
                return render(request, 'login.html', {'form': form, 'error_message': errorStr})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, })


@login_required
def user_info(request):
    user_id = request.user.id
    user = CustomUser.objects.get(id=user_id)
    if user.completed_profile:
        return render(request, 'user_info.html', {'user': request.user})
    else:
        return redirect('complete_profile')


def logout_view(request):
    logout(request)
    return redirect('login')


# def login_signup(request):
@login_required
def index(request):
    return redirect('user_info')

# @login_required
# def edit_profile(request):
#     user = CustomUser.objects.get(request.user.id)
#     profile = Profile.objects.get(user=user)
#     if request.method == 'POST':
#
#     else:
#
