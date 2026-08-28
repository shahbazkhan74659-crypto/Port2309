from projects.models import Tag


def apply_tag_quick_add(post_data):
    """
    If `post_data` (a request.POST QueryDict) contains a `quick_add_field`
    key — the same-page "+ Add tag" submit from partials/tag_picker.html —
    create/reuse that Tag and return a mutated copy of `post_data` with the
    new tag pre-selected in that field's list, so the form can be re-rendered
    unsaved with everything else the user typed still intact.

    Returns None if no quick-add was requested (a normal Save submit).
    """
    field_name = post_data.get("quick_add_field")
    if not field_name:
        return None

    data = post_data.copy()
    new_name = data.get(f"new_tag_for_{field_name}", "").strip()
    if new_name:
        tag, _ = Tag.objects.get_or_create(name=new_name)
        selected = data.getlist(field_name)
        tag_id = str(tag.pk)
        if tag_id not in selected:
            selected.append(tag_id)
        data.setlist(field_name, selected)
    return data
