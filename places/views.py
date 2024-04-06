from django.shortcuts import render, get_object_or_404,redirect
from .models import Places,Comment
from .forms import PlaceCommentForm
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


def places_page(request):
    places = Places.objects.all()  
    search_query = request.GET.get('q', '')
    if search_query:
        places = places.filter(name__icontains=search_query)
    return render(request, 'places.html', {"places": places, "search_query": search_query})


def about(request, id):
    place = get_object_or_404(Places, pk=id)
    form = PlaceCommentForm()
    return render(request, 'about.html', {'place': place, 'form':form})



def landing(request):
    all_reviews = Comment.objects.all()
    return render(request, 'landing.html', {'all_reviews': all_reviews})


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, id):
        place = Places.objects.get(id=id)
        form = PlaceCommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user = request.user,
                place = place,
                comment_text = form.cleaned_data['comment_text'],
                stars_given = form.cleaned_data['stars_given'],
            )
            return redirect(reverse("places:about-page", kwargs={"id":place.id}))
        
        return render(request, 'about.html', {'place': place, 'form':form})
