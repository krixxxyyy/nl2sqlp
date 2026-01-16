def generate_sql(lf):
    if not lf.is_complete():
        return None

    base = "employees"

    # -----------------------------
    # WHERE clause (filters)
    # -----------------------------
    where = ""
    if lf.filters:
        t, c, v = lf.filters[0]
        where = f" WHERE {t}.{c} = '{v}'"

    # -----------------------------
    # Aggregation + Group By
    # -----------------------------
    if lf.aggregation and lf.group_by:
        gt, gc = lf.group_by
        return (
            f"SELECT {gt}.{gc}, {lf.aggregation}({base}.salary) "
            f"FROM {base} "
            f"JOIN {gt} ON {base}.department_id = {gt}.id"
            f"{where} "
            f"GROUP BY {gt}.{gc};"
        )

    # -----------------------------
    # Aggregation only
    # -----------------------------
    if lf.aggregation:
        return f"SELECT {lf.aggregation}(salary) FROM {base};"

    # -----------------------------
    # Filters ALWAYS force join
    # -----------------------------
    if lf.filters:
        return (
            f"SELECT * FROM {base} "
            f"JOIN departments ON {base}.department_id = departments.id"
            f"{where};"
        )

    # -----------------------------
    # Default
    # -----------------------------
    return f"SELECT * FROM {base};"
