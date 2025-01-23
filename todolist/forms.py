from django import forms

class TodoList(forms.Form):
    text = forms.CharField(
        max_length=45,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter a todo',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn'  # Corrected typo here
            }
        )
    )
