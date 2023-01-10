from django.db.models.query import QuerySet
from contact.models import Contact

def contact_list() -> QuerySet[Contact]:
    qs = Contact.objects.all()
    return qs
