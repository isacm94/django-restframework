from rest_framework import serializers

from tutorial.quickstart.models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'type', 'author', 'creation_date', 'number_of_pages', 'user', 'borrow_date']
