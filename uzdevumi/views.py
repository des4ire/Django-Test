from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import VisitForm, VisitorNameForm
from .forms import VisitForm
from .models import Visit
from .forms import reportform
from .forms import UploadCsvForm
import csv
from .csv_handler import read_and_decode_csv  
from .csv_handler import visit_csv_rows_to_db
def get_all_visits(request):

    visits = Visit.objects.all()

    context = {
        'visits': visits,
    }

    return render(
        request,
        template_name='visits.html',
        context=context,
    )


def get_visit(request, visit_id):

    visit = Visit.objects.get(id=visit_id)

    context = {
        'visit': visit,
    }

    return render(
        request,
        template_name='visit.html',
        context=context,
    )


def add_visit(request):

    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visit = Visit(
                visitor=form.cleaned_data['visitor'],
                reason=form.cleaned_data['reason'],
                date_time=form.cleaned_data['date_time'],
                email=form.cleaned_data['email']
            )

            visit.save()

            context = {
                'visit': visit,
            }

            return render(
                request,
                template_name='visit.html',
                context=context,
            )

    return render(
        request,
        template_name='visit_form.html',
        context={'form': form}
)

def filter_visits_by_visitor(request):

    form = VisitorNameForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visitor_name = form.cleaned_data['visitor_name']
            visits = Visit.objects.filter(visitor=visitor_name)

            context = {
                'visits': visits,
            }

            return render(
                request,
                template_name='visits.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='visit_form.html',
        context=context,
    )

def del_visit(request, visit_id):
   # form = reportform(request.POST or None)
   # if request.method == 'POST':
        record = Visit.objects.get(id=visit_id) 
        record.delete()
        #record.save()
        response_data = 'successful!'
       # context = {
        #    'visits': record,
        #}
        return HttpResponseRedirect('visits.html', content='True')
            #    return HttpResponseRedirect(redirect_to=reverse('url_name'))
   # return render(
    #        request,
     #       template_name='visit.html',
      #      context={
       #         "visit":record,
        #        }
        #)
           

       
def upload_csv_row_to_db(request):

    form = UploadCsvForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':

        if form.is_valid():
          
            decoded_csv=read_and_decode_csv(request.FILES["csv_file"])
            visit_csv_rows_to_db(decoded_csv)
            return HttpResponse('OK')

    return render(
        request,
        template_name='visit_form.html',
        context={'form': form}
)
    
