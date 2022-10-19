from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    bid = serializers.IntegerField()
    day = serializers.ListField(child = serializers.CharField(max_length=50))

    def validate(self, data):
        return data



    def create(self, validated_data):
        print("=============================================", validated_data)
        print(validated_data['day'])
        for d in validated_data['day']:
            book = Book.objects.create(
                bid = validated_data['bid'],
                day = d
            )

            book.save()
        
            

        return book

    def update(self, instance, validated_data):

        
        instance.bid = validated_data.get('bid', instance.bid)
        instance.day = validated_data.get("day", instance.day)

        instance.save()
        return instance
