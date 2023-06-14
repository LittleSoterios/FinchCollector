from django.shortcuts import render

# Create your views here.
finches = [
    {"name": 'Brambling', 'length': 14, 'wingspan': 25, 'weight' : 24, 'habitats': ['Woodland', 'Farmland', 'Urban/Suburban'], 'img': 'https://www.rspb.org.uk/globalassets/images/birds-and-wildlife/bird-species-illustrations/brambling_male_winterplumage_1200x675.jpg?preset=square_desktop'},
    {"name": 'Bullfinch', 'length': 15, 'wingspan': 26, 'weight' : 25, 'habitats': ['Woodland', 'Farmland', 'Urban/Suburban'], 'img': 'https://www.rspb.org.uk/globalassets/images/birds-and-wildlife/bird-species-illustrations/bullfinch_male_1200x675.jpg?preset=square_desktop'},
    {"name": 'Scottish Crossbill', 'length': 17, 'wingspan': 35, 'weight' : 44, 'habitats': ['Woodland'], 'img': 'https://www.rspb.org.uk/globalassets/images/birds-and-wildlife/bird-species-illustrations/scottish-crossbill_male_1200x675.jpg?preset=square_desktop'},
    {"name": 'Golffinch', 'length': 12, 'wingspan': 22, 'weight' : 16, 'habitats': ['Farmland', 'Urban/Suburban'], 'img': 'https://www.rspb.org.uk/globalassets/images/birds-and-wildlife/bird-species-illustrations/goldfinch_adult_1200x675.jpg?preset=square_desktop'},
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })

