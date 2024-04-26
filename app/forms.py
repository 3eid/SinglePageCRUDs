from django.forms import ModelForm,IntegerField,TextInput,Textarea
from .models import Branch

class BranchForm(ModelForm):
    id = IntegerField(disabled=True,label='Branch')
    
    def __init__(self, *args, **kwargs):
        super(BranchForm, self).__init__(*args, **kwargs)
        # Add form-control class to all fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Branch
        fields = ["id", "customer_no", "arabic_name", "arabic_description", "english_name", "english_description", 'note', "address"]
        # You can also define widgets specific to certain fields if needed
        widgets = {
            'id': TextInput(attrs={'disabled': 'disabled'}),
            'note': Textarea(attrs={'cols': 30, 'rows': 3}),
            'address': Textarea(attrs={'cols': 30, 'rows': 3}),
        }