from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    bid = serializers.IntegerField()
    day = serializers.ListField(child = serializers.CharField(max_length=50))

    def create(self, validated_data):
        result = []
        for d in validated_data['day']:
            book = Book.objects.create(
                validated_data['bid'],
                d
            )

            book.save()
            result.append(book)
            

        return result

    def update(self, instance, validated_data):
        instance.bid = validated_data.get('bid', instance.bid)
        instance.day = validated_data.get("day", instance.day)

        instance.save()
        return instance
