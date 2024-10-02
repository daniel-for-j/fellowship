from django.shortcuts import render
from django.http import HttpResponse
from .models import picture, Event, Executive, Testimony, audioMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    bg = picture.objects.filter(isWallpaper=True).order_by('-date').first()
    messagepic = picture.objects.filter(isMessagesThumbnail=True).order_by('-date').first()
    execs = Executive.objects.all()
    event1 = Event.objects.filter(isFeatured=True).first
    event2 = Event.objects.filter(isFeatured=True).last
    events = []
    tests= Testimony.objects.all()[:5] 
    audios = []


    #making sure featured images aren't more than six
    # for p in range(6):
        # audios.append(audioMessage.objects.all()[p])
        # tests.append(Testimony.objects.all()[p])
    for t in range(3):
        events.append(Event.objects.all()[t])
    #end of that
    
    


    
    context={
        'bg': bg,
        'messagepic': messagepic,
        'events':events,
        'execs': execs,
        'event1': event1,
        'event2': event2,
        'tests': tests,
        'audios': audios,
        
    }
    return render(request, 'base/index.html', context)

def testimonies(request):
    alltestimonies = Testimony.objects.all()
    context = {'testimonies': alltestimonies}

    page = request.GET.get('page')

    paginator = Paginator(testimonies, 6)

    try:
        testimonies = paginator.page(page)
    except PageNotAnInteger:
        testimonies = paginator.page(1)
    except EmptyPage:
        testimonies = paginator.page(paginator.num_pages)


    return render(request, 'base/testimonies.html', context)

def about(request):
    return render(request, 'base/aboutUs.html')

def messages(request):
    allmessages = audioMessage.objects.all()
    context = {'messages': allmessages}
    return render(request, 'base/messages.html', context)

def events(request):
    events = Event.objects.all()

    page = request.GET.get('page')

    paginator = Paginator(events, 6)

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    context = {'events': events}
    return render(request, 'base/events.html', context)

    

def eventDetails(request, slug):
    event = Event.objects.get(slug=slug)
    context = {'event': event}
    return render(request, 'base/event-details.html',context)


def testimonyDetails(request, slug):
    testimony = Testimony.objects.get(slug=slug)
    context = {'testimony': testimony}
    return render(request, 'base/testimony-details.html',context)
