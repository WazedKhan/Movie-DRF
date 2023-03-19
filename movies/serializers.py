from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

        def validate_rating(self, value):
            if value < 1 and value > 10:
                raise serializers.ValidationError("Rating has to be between 1 to 10")
            return value
