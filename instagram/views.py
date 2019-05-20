from django.shortcuts import render, redirect, get_object_or_404
from .models import Image,Comment, Profile,Likes,Location
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import NewImageForm, UpdatebioForm
# from .email import send_welcome_email
from .forms import NewsLetterForm

# Views


@login_required(login_url='/accounts/login/')
def home_images(request):
    # Display all images here:

    # images = Image.objects.all()

    locations = Location.objects.all()

    if request.GET.get('location'):
        pictures = Image.filter_by_location(request.GET.get('location'))

    elif request.GET.get('tags'):
        pictures = Image.filter_by_tag(request.GET.get('tags'))

    elif request.GET.get('search_term'):
        pictures = Image.search_image(request.GET.get('search_term'))

    else:
        pictures = Image.objects.all()

    form = NewsLetterForm


    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('home_images')

    return render(request, 'index.html', {'locations':locations,
                                          'pictures':pictures, 'letterForm':form})

def image(request, id):

    try:
        image = Image.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)

    
@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = NewImageForm()
    return render(request, 'registration/new_image.html', {"form": form})

def search_users(request):

    # search for a user by their username
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_users(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "profiles": searched_users})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html', {"message": message})



def search_image(request):

        # search for an image by the description of the image
        if 'image' in request.GET and request.GET["image"]:
            search_term = request.GET.get("image")
            searched_images = Image.search_image(search_term)
            message = f"{search_term}"

            return render(request, 'search.html', {"message": message, "pictures": searched_images})

        else:
            message = "You haven't searched for any image"
            return render(request, 'search.html', {"message": message})


