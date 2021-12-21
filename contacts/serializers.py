from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "country_code",
            "first_name",
            "last_name",
            "phone_number",
            "is_favorited",
            "contact_picture",
        ]
