from django.shortcuts import render

# Create your views here.
from .models import Poll, Response,  Option



#from .models import Poll, Response, Option
#from django.db.models import Count

def polls_list(request):
  polls1 = Poll.objects.filter(status=1)
  options_ = polls1.option_set.all()
  responses_ = options_.response_set.all().count()
  data = {}
  data["list_poll"] = polls1
  data["options_list1"] = options_
  data["responses_list1"] = responses_

  return render(request, 'poll.html', context=data)


def polls_list_u(request):
  polls2 = Poll.objects.filter(status=0)
  options_2 = polls2.option_set.all()
  responses_2 = options_2.response_set.all().count()
  data = {}
  data["list_poll_u"] = polls2
  data["options_list2"] = options_2
  data["responses_list2"] = responses_2

  return render(request, 'poll.html', context=data)


def poll_details(request, p_title):
  poll_d = Poll.objects.filter(title=p_title)
  n_responses = Response.objects.all().count()
  data = {}
  data["details"] = poll_d
  data["number_responses"] = n_responses
  return render(request, 'poll.html', context=data)


def names_list(request):
  names_re = Response.objects.all()
  data = {}
  data["names"] = names_re
  return render(request, 'responses.html', context=data)


def form_list(request):
  return render(request, 'form.html')

