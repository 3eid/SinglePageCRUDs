from django.shortcuts import render,redirect,get_object_or_404
from .models import Branch
from .forms import BranchForm
from django.urls import reverse

# Create your views here.
def index(request):
    id = request.GET.get('id')
    data = {}

    # Get all branches ordered by id
    branches = Branch.objects.order_by('id')

    if branches:
        # Fetch the first and last branches
        first_branch = branches.first()
        last_branch = branches.last()
        
        # Fetch the current branch based on the provided id or default to the first branch
        branch = get_object_or_404(Branch, pk=id) if id else first_branch
        
        # Generate the form for the current branch
        form = BranchForm(instance=branch)
        
        # Determine the index of the current branch in the ordered queryset
        current_index = list(branches).index(branch)
        
        # Fetch the previous and next branches if they exist
        previous_branch = branches[current_index - 1] if current_index > 0 else branch
        next_branch = branches[current_index + 1] if current_index + 1 < len(branches) else branch
                
        # Populate data dictionary with relevant information
        data['id'] = branch.id
        data['cur'] = current_index + 1
        data['branch'] = branch
        data['length'] = len(branches)
        data['form'] = form
        data['last'] = last_branch.id
        data['first'] = first_branch.id
        data['prev'] = previous_branch.id
        data['next'] = next_branch.id
    else:
        # If no branches exist, create a new one
        branch = Branch.objects.create()
        form = BranchForm(instance=branch)
        
        # Populate data dictionary with relevant information for the newly created branch
        data['id'] = branch.id
        data['cur'] = 1
        data['length'] = 1
        data['branch'] = branch
        data['form'] = form
        data['last'] = branch.id
        data['first'] = branch.id
        data['prev'] = branch.id
        data['next'] = branch.id
        
    # Render the template with the data
    return render(request, 'index.html', data)

def create(request):
    #Create a new Branch record
    branch = Branch()
    branch.save()
    #retriving the url of home page
    url = reverse('home')
    # Append the branch ID as a query parameter to the URL
    url_with_query_param = f"{url}?id={branch.id}"
    # Redirect to the URL with the query parameter
    return redirect(url_with_query_param)

def update(request, id):
    # Retrieve the branch object based on the provided id
    branch = get_object_or_404(Branch, pk=id)
    
    if request.method == 'POST':
        # If the request method is POST, process the form submission
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            # Save the form data if it's valid
            form.save()
            # Redirect to the home page with the updated branch's id as a query parameter
            return redirect(reverse('home') + f"?id={id}")
    else:
        # If the request method is not POST, render the form with the branch data
        form = BranchForm(instance=branch)
    
    # Render the update form template with the form data and the current branch
    return render(request, 'update.html', {'form': form, 'branch': branch})

def delete(request, id):
    # Retrieve the branch object based on the provided id
    branch = get_object_or_404(Branch, pk=id)
    
    # Delete the branch object
    branch.delete()
    
    # Redirect to the home page
    return redirect("home")