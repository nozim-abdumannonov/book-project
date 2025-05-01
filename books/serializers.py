from turtle import title
from docs.conf import author
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title','content', 'subtitle', 'author', 'isbn', 'price')







    def validate(self, data):
        title = data.get('title', None)
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "massage": "kitobni sarlovhasi harflardan tashkil topishi kerak"
                }
            )

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "massage": "kitobni sarlovhasi va mualifi birhil bulgan kitobni yuklay olmaysiz"

                }
            )

        return data

    def validate_price(self, price):
        if price < 0 or price > 99999999999:
            raise ValidationError(
                {
                    "status": False,
                    "massage": "kitobni narhi tug`ri kiritilmagan"

                }
            )
