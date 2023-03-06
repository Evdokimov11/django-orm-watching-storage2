from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from scripts import get_duration
from scripts import format_duration
from scripts import is_visit_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    
    passcard = get_object_or_404(Passcard, passcode=passcode)
 
    visits_owner = Visit.objects.filter(passcard=passcard)
    
    filtered_visits_owner=[]

    for visit in visits_owner:

        duration = get_duration(visit)

        formated_duration_time = format_duration(duration)

        is_strange = is_visit_long(visit)

        this_passcard_visits = {
                'entered_at': visit.created_at,
                'duration': formated_duration_time,
                'is_strange': is_strange
            }
        
         
        filtered_visits_owner.append(this_passcard_visits)
      
    context = {
        'passcard': passcard,
        'this_passcard_visits': filtered_visits_owner
    }
    return render(request, 'passcard_info.html', context)
