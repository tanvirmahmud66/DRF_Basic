from rest_framework import serializers
from .models import Books

#create serializers here

#------------------------------------------------------------------- BooksSerializer
# class BooksSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     author = serializers.CharField()
#     pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()

#     def create(self, data):
#         return Books.objects.create(**data)
    
#     def update(self, instance, data):
#         instance.name = data.get('name', instance.name)
#         instance.author = data.get('author', instance.author)
#         instance.pages = data.get('pages', instance.pages)
#         instance.publish_date = data.get('publish_date', instance.publish_date)
#         instance.quantity = data.get('quantity', instance.quantity)
#         instance.save()
#         return instance


#------------------------------------------------------------------- BooksSerializer
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    # def validate(self, data):
    #     if data == True:
    #         return data 