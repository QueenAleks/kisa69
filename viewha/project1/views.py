from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .models import DataPiece

def form_view(request):
  return render(request, 'form.html')

def data_view(request):
  all_records = DataPiece.objects.all()
  return render(request, 'data.html', {'all_records': all_records})

@require_POST
def add_data(request):
  try:
    data = {f'field{i}': value for i, value in enumerate(request.POST.getlist('field[]'))}
    record = DataPiece(data = data)
    record.save()
  except Exception as ex:
    return HttpResponse(ex.args[0])
  
  return redirect('/success.html')

def success_view(request):
  return render(request, 'success.html')
