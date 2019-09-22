from django import forms


class QRCodeForm(forms.Form):
    image = forms.FileField(label="QRコード", widget=forms.FileInput())
