from django.shortcuts import render,redirect,get_object_or_404
from .models import Branch
from .forms import BranchForm
from django.urls import reverse

# Create your views here.

def index(request):
    id = request.GET.get('id')
    data = {}
    branches = Branch.objects.all()
    if branches:
        last = branches.last()
        if id:
            branch = branches.get(pk=id)
            form = BranchForm( instance=branch)
            data['id'] = branch.id
            data['branch'] = branch
            data['length'] = len(branches)
            data['form'] = form
            data['last'] = last.id
        else:
            branch = branches.first()
            form = BranchForm( instance=branch)
            data['id'] = branch.id
            data['branch'] = branch
            data['length'] = len(branches)
            data['form'] = form
            data['last'] = last.id
    else:
        data['id'] = None
        data['length'] = 0
        data['branch'] = None
    print(data)
    return render(request, 'index.html', data)

def create(request):
    # Create an instance of the Branch model
    branch = Branch()
    branch.save()

    # Get the ID of the newly created branch
    branch_id = branch.id

    # Construct the URL with the query parameter using the reverse function
    url = reverse('home')

    # Append the branch ID as a query parameter to the URL
    url_with_query_param = f"{url}?id={branch_id}"

    # Redirect to the URL with the query parameter
    return redirect(url_with_query_param)

def update(request,id):
    branch = get_object_or_404(Branch,pk=id)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            url = reverse('home')
            url_with_query_param = f"{url}?id={id}"
            return redirect(url_with_query_param)
        
