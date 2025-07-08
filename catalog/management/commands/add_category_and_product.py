from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add categories and products to the database"

    # def handle(self, *args, **kwargs):
    #     Category.objects.all().delete()
    #     Product.objects.all().delete()
    #
    #     category1, _ = Category.objects.get_or_create(
    #         name="Фрукты", description="Все фрукты, а вы чего хотели?"
    #     )
    #     category2, _ = Category.objects.get_or_create(
    #         name="Овощи", description="Все овощи, и тут так просто, да."
    #     )
    #
    #     products = [
    #         {
    #             "name": "Яблоко",
    #             "description": "Фрукт, растет из земли, желтый",
    #             "category": category1,
    #             "price": 1000,
    #             "created_at": "2009-01-01",
    #             "updated_at": "2010-02-02",
    #         },
    #         {
    #             "name": "Банан",
    #             "description": "Фрукт, растет из земли, зеленый",
    #             "category": category1,
    #             "price": 2000,
    #             "created_at": "2011-01-01",
    #             "updated_at": "2012-02-02",
    #         },
    #         {
    #             "name": "Картофель",
    #             "description": "Овощь, растет на деревьях, голубой",
    #             "category": category2,
    #             "price": 10000,
    #             "created_at": "2014-01-01",
    #             "updated_at": "2016-07-02",
    #         },
    #     ]
    #
    #     for product_data in products:
    #         product, created = Product.objects.get_or_create(**product_data)
    #         if created:
    #             self.stdout.write(
    #                 self.style.SUCCESS(f'Успешно создан продукт "{product.name}".')
    #             )
    #         else:
    #             self.stdout.write(
    #                 self.style.SUCCESS(f'Проудкт "{product.name}" уже существует!')
    #             )

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command("loaddata", "category_fixture.json", "product_fixture.json")
        self.stdout.write(self.style.SUCCESS("Успешно загружены данные с фикстур"))
