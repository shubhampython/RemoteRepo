from  django import forms
class ProductInsertForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enetr Your Product Id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    product_name = forms.CharField(
        label="Enetr Your Product Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Name'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enetr Your Product cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )
    product_color = forms.CharField(
        label="Enetr Your Product Color",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Color'
            }
        )
    )
    product_class = forms.CharField(
        label="Enetr Your Product Class",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Class'
            }
        )
    )
class ProductUpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enetr Your Product Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product ID'
          }
        )
    )
    product_cost = forms.IntegerField(
        label="Enetr Your Product cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )
class ProductDeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enetr Your Product Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product ID'
            }
        )
    )


