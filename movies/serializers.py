from rest_framework import serializers
from .models import Movie


def is_rating(value):
    if value < 1:
        raise serializers.ValidationError("Value cannot be lower than 1")
    elif value > 10:
        raise serializers.ValidationError("Value cannot be higher than 10")


class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(validators=[is_rating])
    class Meta:
        model = Movie
        fields = "__all__"

        def validate_rating(self, value):
            if value < 1 and value > 10:
                raise serializers.ValidationError("Rating has to be between 1 to 10")
            return value

        def validate(self, data):
            if data["us_gross"] > data["worldwide_gross"]:
                raise serializers.ValidationError(
                    "us_gross can't be bigger then worldwide gross"
                )
            return data
