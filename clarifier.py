def needs_clarification(logical_form):
    # Superlative + grouping entity but no explicit grouping intent
    if (
        logical_form.aggregation in ("MAX", "MIN")
        and logical_form.group_by is not None
    ):
        return True
    return False


def generate_clarification(logical_form):
    return (
        "Do you want the department with the highest "
        "individual salary or the highest average salary? "
        "(max/avg)"
    )
