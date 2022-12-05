from rest_framework import serializers
from books.models import Books


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user

        book = Books.objects.create(owner=user, **validated_data)
        return book
