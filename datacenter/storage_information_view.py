from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from scripts import get_duration
from scripts import format_duration


def storage_information_view(request):

    non_closed_visits=[]
  
    active_visitors = Visit.objects.filter(leaved_at__isnull=True)

    for visit in active_visitors:

        visit_owner_name = visit.passcard.owner_name

        duration = get_duration(visit)

        formated_duration_time = format_duration(duration)
        
        dict_visitor = {
            'who_entered': visit_owner_name,
            'entered_at': visit.created_at,
            'duration': formated_duration_time,
        }
      
        non_closed_visits.append(dict_visitor)

    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
