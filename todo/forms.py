from django import forms

from .models import(
    TodoModel,
)

class TodoModelForm(forms.ModelForm):
    
    class Meta:
        model = TodoModel
        fields = (
            'title',
            'memo',
            'priority',
            'duedate',
        )
        widgets = {
            'duedate': forms.NumberInput(attrs={
                "type": "date"
            }),
            'memo': forms.Textarea(), 
        }
    memo = forms.CharField(required=False, widget=forms.Textarea())