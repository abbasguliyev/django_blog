from blog.models import Blog, Category, Questions
from blog.api.selectors import blog_list, category_list, questions_list

def create_blog(
    *, user, title: str, description: str, body: str,
    category = None, image = None, author = None 
) -> Blog:
    obj = Blog.objects.create(
        title = title, description = description, body=body,
        category=category, image=image, author=user
    )
    obj.full_clean()
    obj.save()

    return obj

def update_blog(instance, **data) -> Blog:
    obj = blog_list().filter(pk=instance.id).update(**data)
    return obj

def create_category(
    *, category_name: str
) -> Category:
    obj = Category.objects.create(category_name=category_name)
    obj.full_clean()
    obj.save()

    return obj

def update_category(instance, **data) -> Category:
    obj = category_list().filter(pk=instance.id).update(**data)
    return obj

def create_question(
    *, user, title: str, subject: str, owner = None
) -> Questions:
    obj = Questions.objects.create(title = title, subject = subject, owner = user)
    obj.full_clean()
    obj.save()

    return obj

def update_question(instance, **data) -> Questions:
    obj = questions_list().filter(pk=instance.id).update(**data)
    return obj
