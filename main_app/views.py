from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Finch

from .forms import FeedingForm

import simplejson as json

# Create your views here.
finches_old = [
    {"name": 'Brambling', 'length': 14, 'wingspan': 25, 'weight' : 24, 'habitats': ['Woodland', 'Farmland', 'Urban/Suburban'], 'img': 'https://www.rspb.org.uk/globalassets/images/birds-and-wildlife/bird-species-illustrations/brambling_male_winterplumage_1200x675.jpg?preset=square_desktop'},
    {"name": 'Bullfinch', 'length': 15, 'wingspan': 26, 'weight' : 25, 'habitats': ['Woodland', 'Farmland', 'Urban/Suburban'], 'img': 'https://www.rspb.org.uk/globalassets/images/birds-and-wildlife/bird-species-illustrations/bullfinch_male_1200x675.jpg?preset=square_desktop'},
    {"name": 'Scottish Crossbill', 'length': 17, 'wingspan': 35, 'weight' : 44, 'habitats': ['Woodland'], 'img': 'https://www.rspb.org.uk/globalassets/images/birds-and-wildlife/bird-species-illustrations/scottish-crossbill_male_1200x675.jpg?preset=square_desktop'},
    {"name": 'Golffinch', 'length': 12, 'wingspan': 22, 'weight' : 16, 'habitats': ['Farmland', 'Urban/Suburban'], 'img': 'https://www.rspb.org.uk/globalassets/images/birds-and-wildlife/bird-species-illustrations/goldfinch_adult_1200x675.jpg?preset=square_desktop'},
]


def home(request):
    print('this is logging')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    finches = Finch.objects.all()
    for finch in finches:
        finch.habitats = finch.habitats.replace(' ', '').split(',')

    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    finch.habitats = finch.habitats.replace(' ', '').split(',')
    return render(request, 'finches/show.html', {
        'finch': finch,
        'feeding_form': feeding_form
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id = finch_id)

class FinchesCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchesUpdate(UpdateView):
    model = Finch
    fields = ['wingspan', 'length', 'img']

class FinchesDelete(DeleteView):
    model = Finch
    success_url = '/finches/' 

