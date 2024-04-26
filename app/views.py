from django.shortcuts import render
from .models import Branch
# Create your views here.

def index(request):
    id = request.GET.get('id')
    data = {}
    branches = Branch.objects.all()
    if branches:
        if id:
            data['id'] = id
            branch = branches.get(id)
            data['branch'] = branch
            data['length'] = len(branches)
        
        else:
            branch = branches.first()
            data['id'] = branch.id
            data['branch'] = branch
            data['length'] = len(branches)
    else:
        data['id'] = None
        data['length'] = 0
        data['branch'] = None
    print(data)
    return render(request, 'index.html', data)