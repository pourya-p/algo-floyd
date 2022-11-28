from django.shortcuts import render

import numpy as np
import json

from .algo import Floyd
# Create your views here.
def compute(request):
    if request.method == 'GET' and 'matrix' in request.GET:
        matrix = request.GET.get('matrix')
        list_matrix = []
        for row in matrix.split('\n'):
            list_matrix.append(json.loads(row))
        array = np.array(list_matrix)
        com = Floyd(array)
        if request.GET.get('option') == 'compute':
            com.compute()
            context = {'result_d':com.D, 'result_p':com.P}
            return render(request, 'result.html', context)
        if request.GET.get('option') == 'route':
            f = int(request.GET.get('from'))
            to = int(request.GET.get('to'))
            route = com.router(f, to)
            lenght = len(route)-2
            context = {'result_d': com.D, 'result_p': com.P, 'route':route, 'lenght':lenght}
            return render(request, 'result.html', context)
    return render(request, 'home.html')