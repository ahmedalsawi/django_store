from django import forms


class AddToCart(forms.Form):
    quantity = forms.IntegerField(label='Qty')


class CheckoutForm(forms.Form):
    pass
