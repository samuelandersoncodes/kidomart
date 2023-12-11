from .models import Category


def menu_links(request):
    """
    This function gets all categories
    stores them into various category links
    and returns it in dictionary context
    """
    links = Category.objects.all()
    return dict(links=links)
