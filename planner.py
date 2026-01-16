from logical_form import LogicalForm


def build_logical_form(tokens, schema):
    lf = LogicalForm()
    text = " ".join(tokens)
    words = text.split()

    # -----------------------------
    # Tables
    # -----------------------------
    for table in schema:
        if table in text or table.rstrip("s") in text:
            lf.tables.add(table)

    # -----------------------------
    # Columns
    # -----------------------------
    for table, meta in schema.items():
        for col in meta["columns"]:
            if col.replace("_", " ") in text:
                lf.columns.add((table, col))
                lf.tables.add(table)

    # -----------------------------
    # Aggregation keywords
    # -----------------------------
    AGG_WORDS = {
        "average": "AVG",
        "avg": "AVG",
        "sum": "SUM",
        "total": "SUM",
        "max": "MAX",
        "highest": "MAX",
        "min": "MIN",
        "lowest": "MIN"
    }

    for t in tokens:
        if t in AGG_WORDS:
            lf.aggregation = AGG_WORDS[t]

    # -----------------------------
    # GROUP BY (by department)
    # -----------------------------
    if "by" in tokens:
        idx = tokens.index("by")
        if idx + 1 < len(tokens):
            g = tokens[idx + 1]
            for table, meta in schema.items():
                if g == table or g == table.rstrip("s"):
                    if "name" in meta["columns"]:
                        lf.group_by = (table, "name")
                        lf.tables.add(table)
                        lf.join_required = True

    # -----------------------------
    # FILTER: employees in department hr
    # -----------------------------
    # Pattern: "in <dimension> <value>"
    if "in" in words:
        idx = words.index("in")
        if idx + 2 < len(words):
            dim = words[idx + 1]
            value = words[idx + 2]

            # Handle department explicitly (safe, schema-driven)
            if dim in ("department", "departments"):
                if "departments" in schema:
                    lf.filters.append(("departments", "name", value))
                    lf.tables.add("employees")
                    lf.tables.add("departments")
                    lf.join_required = True

    return lf