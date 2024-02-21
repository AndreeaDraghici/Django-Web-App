from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q


# Create your views here.
def members(request) :
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id) :
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request) :
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request) :
    """ Return records where firstname is Andreea-Maria or firstname is Tobias (meaning: returning records that matches either query,
    not necessarily both) is not as easy as the AND example above."""
    # mydata = Member.objects.filter(Q(firstname='Andreea-Maria') | Q(firstname='Tobias')).values()
    mydata = Member.objects.all().order_by('firstname').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers' : mydata,
    }
    return HttpResponse(template.render(context, request))
