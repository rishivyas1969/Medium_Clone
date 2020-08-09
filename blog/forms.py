from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widget = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['text'].widget.attrs.update({'class' : 'editable medium-editor-textarea postcontent'})

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

    widget = {
        'author': forms.TextInput(attrs={'class': 'textinput'}),
        'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea'}),
    }