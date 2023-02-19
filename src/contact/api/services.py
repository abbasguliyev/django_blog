from contact.models import Contact
from contact.api.selectors import contact_list
def create_contact(
    *, name: str,
    email: str,
    subject: str,
    message: str
) -> Contact:
    obj = Contact.objects.create(name=name, email=email, subject=subject, message=message)
    obj.full_clean()
    obj.save()
    
    return obj

def update_contact(instance, **data) -> Contact:
    obj = contact_list().filter(pk=instance.id).update(**data)
    return obj