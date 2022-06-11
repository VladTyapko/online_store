from django.template import Library

register = Library()


@register.inclusion_tag("includes/_sorting_header.html", takes_context=True)
def sorting_header(context, field, label):
    """Render a table sorting header."""
    request = context["request"]
    request_get = request.GET.copy()
    sort_by = request_get.get("sort_by")

    # path to icon indicating applied sorting
    sorting_icon = ""

    # flag which determines if active sorting is on field
    is_active = False

    if sort_by:
        if field == sort_by:
            is_active = True
            # enable ascending sort
            # new_sort_by is used to construct a link with already toggled
            # sort_by value
            new_sort_by = "-%s" % field
            sorting_icon = "fas fa-arrow-up"
        else:
            # enable descending sort
            new_sort_by = field
            if field == sort_by.strip("-"):
                is_active = True
                sorting_icon = "fas fa-arrow-down"
    else:
        new_sort_by = field

    request_get["sort_by"] = new_sort_by
    return {
        "url": "%s?%s" % (request.path, request_get.urlencode()),
        "is_active": is_active,
        "sorting_icon": sorting_icon,
        "label": label,
    }