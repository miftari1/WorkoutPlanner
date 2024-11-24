from django import forms


class NavSearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search...',
                'width': '20%',
                'class': 'search-bar',
            }
        ),
        required=False,
        label='',
    )