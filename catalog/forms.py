from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Category

Forbidden_Words = [
    "казино",
    "биржа",
    "обман",
    "криптовалюта",
    "дешево",
    "полиция",
    "крипта",
    "бесплатно",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "image",
            "category",
            "price",
        ]

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Цена не может быть ниже нуля")
        return price

    def clean_name(self):
        name = self.cleaned_data["name"]
        name_list = name.split(" ")
        for el in name_list:
            if el.strip().lower() in Forbidden_Words:
                self.add_error("name", "Нельзя использовать данные слова")
        for word in Forbidden_Words:
            if word in name:
                self.add_error("name", "Нельзя использовать данные слова")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        description_list = description.split(" ")
        for el in description_list:
            if el.strip().lower() in Forbidden_Words:
                self.add_error("description", "Нельзя использовать данные слова")
        for word in Forbidden_Words:
            if word in description:
                self.add_error("description", "Нельзя использовать данные слова")
        return description

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите название",
            }
        )

        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите описание",
            }
        )

        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите цену",
            }
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if Category.objects.filter(name=name).exists():
            raise ValidationError("Такая категория уже существует")

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Название категории",
            }
        )

        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Описание",
            }
        )


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, validators=[MaxLengthValidator(100)])
#     email = forms.EmailField(validators=[EmailValidator()])
#     # message = forms.
#
#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         if not email.endswith("@example.com"):
#             raise ValidationError("Email должен оканчиваться на")
#         return email
#
#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get("name")
#         email = cleaned_data.get("email")
#         message = cleaned_data.get("message")
#
#     def __init__(self, *args, **kwargs):
#         super(ContactForm, self).__init__(*args, **kwargs)
#
#         self.fields["name"].widget.attrs.update(
#             {
#                 "class": "form-control",
#                 "placeholder": "Ваше имя",
#             }
#         )
#
#         self.fields["email"].widget.attrs.update(
#             {
#                 "class": "form-control",
#                 "placeholder": "Ваша почта",
#             }
#         )
#
#         self.fields["message"].widget.attrs.update(
#             {
#                 "class": "form-control",
#                 "placeholder": "Ваше сообщение",
#             }
#         )
