from django import forms
from article.models import Article



class ArticleForm(forms.Form):
    title=forms.CharField(max_length=400)
    text=forms.CharField()
    image=forms.ImageField()


    def save(self,**cleaned_data):
        data=self.cleaned_data
        return Article.objects.create(
            title=data.get('title'),
            text=data.get('text'),
            image=data.get('image'),
        )

    def clean_title(self):
        title=self.cleaned_data.get('title')
        title=title.title().strip(' *&^$#@')
        return title

