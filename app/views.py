from django.shortcuts import render
from .models import Branch
from .forms import BranchForm
# Create your views here.

def index(request):
    id = request.GET.get('id')
    data = {}
    branches = Branch.objects.all()
    if branches:
        if id:
            branch = branches.get(pk=id)
            form = BranchForm( instance=branch)
            data['id'] = branch.id
            data['branch'] = branch
            data['length'] = len(branches)
            data['form'] = form
        else:
            branch = branches.first()
            form = BranchForm( instance=branch)
            data['id'] = branch.id
            data['branch'] = branch
            data['length'] = len(branches)
            data['form'] = form
    else:
        data['id'] = None
        data['length'] = 0
        data['branch'] = None
    print(data)
    return render(request, 'index.html', data)