from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=10, max_length=150)
    description = forms.CharField(widget=forms.Textarea)
    characteristics = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=8, max_length=150)
    grade = forms.ChoiceField(choices=(
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    ))
