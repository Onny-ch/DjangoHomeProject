from django import forms

from blogs.models import Blogs


class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = [
            "title",
            "content",
            "preview",
        ]

    def __init__(self, *args, **kwargs):
        super(BlogsForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите заголовок",
            }
        )

        self.fields["content"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Добавьте содержание записи",
            }
        )

        self.fields["preview"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
