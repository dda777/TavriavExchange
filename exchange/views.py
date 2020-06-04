from django.shortcuts import render
from .models import Enterprise


def data_info(request):
    return render(request, 'exchange/index.html')


def enterprise_list(request):
    title = Enterprise
    column = Enterprise.column_name
    data = Enterprise.objects.all()
    return render(request, 'exchange/enterprise.html', context={'column': column, 'data': data, 'title': title})
