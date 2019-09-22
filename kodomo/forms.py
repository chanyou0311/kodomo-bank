from django import forms


class AnalyticsForm(forms.Form):
    price = forms.IntegerField(label="csvファイル")
    column = forms.CharField(label="解析するカラム名", widget=forms.TextInput())
