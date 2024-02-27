from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('user', 'poster')

    def __init__(self, *args, **kwargs):
        """
        Fetch the user's full name
        Add placeholders and classes
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['user_displayed_name'].widget.attrs = (
            {
              'class': 'border-black rounded-0',
              'placeholder': 'Blank to post review anonymously'}
        )

        self.fields['title'].widget.attrs = (
            {
              'class': 'border-black rounded-0',
              'placeholder': 'Title of your review'}
        )
        self.fields['content'].widget.attrs = (
            {
              'class': 'border-black rounded-0',
              'placeholder': 'Your review'}
        )
        self.fields['rating'].widget.attrs = (
            {
              'class': 'border-black rounded-0',
              'placeholder': 'Your overall rating (0-5)'}
        )
        self.fields['user_displayed_name'].widget.attrs['autofocus'] = True
