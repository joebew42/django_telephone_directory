from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q

from address_book.models import AddressbookEntry
from address_book.forms import AddressbookEntryForm

def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('address_book/index.html', c)

def search(request):
    c = {}
    c.update(csrf(request))
    
    c['keyword'] = request.POST.get('keyword', False)
    if c['keyword'] is not False:
        c['search_result'] = AddressbookEntry.objects.filter(
            Q(name__icontains=c['keyword'])
            | Q(surname__icontains=c['keyword'])
            | Q(telephone__contains=c['keyword']))
    
    return render_to_response('address_book/search.html', c)

def detail(request, entry_id=None):
    c = {'error' : False}
    try:
        c['entry'] = AddressbookEntry.objects.get(pk=entry_id)
    except ObjectDoesNotExist:
        c['error'] = u'Address entry not exists'
    
    return render_to_response('address_book/detail.html', c)

def edit(request, entry_id=None):
    c = {}
    c.update(csrf(request))
    
    if request.method == 'POST':
        # Form validation
        c['form'] = AddressbookEntryForm(request.POST)
        if c['form'].is_valid():
            cd = c['form'].cleaned_data
            # Check whether to add or modify the address entry
            c['entry'] = None
            try:
                c['entry'] = AddressbookEntry.objects.get(pk=int(cd['pk']))
            except:
                # pk is null or object does not exist
                c['entry'] = AddressbookEntry()

            # Fill data
            c['entry'].name = cd['name']
            c['entry'].surname = cd['surname']
            c['entry'].telephone = cd['telephone']
            c['entry'].save()
            
            c['message'] = "Address book entry saved."
            
            return render_to_response('address_book/detail.html', c)
    else:
        # Showing the form to add or update
        # an address entry
        try:
            entry = AddressbookEntry.objects.get(pk=entry_id)
        except:
            c['form'] = AddressbookEntryForm()
        else:
            # Fill the form with database information
            c['form'] = AddressbookEntryForm(initial={
                    'pk' : entry_id,
                    'name' : entry.name,
                    'surname' : entry.surname,
                    'telephone' : entry.telephone,
                    })

    return render_to_response('address_book/edit.html', c)
