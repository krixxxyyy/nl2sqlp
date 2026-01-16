from schema_utils import load_schema
from normaliser import normalize
from encoder import encode
from planner import build_logical_form
from sql_generator import generate_sql

schema = load_schema("schema.json")

# Holds intent waiting for clarification
pending_intent = None


def nl_to_sql(user_input):
    global pending_intent

    text = user_input.strip().lower()

    # -----------------------------
    # Handle clarification answers
    # -----------------------------
    if pending_intent:
        if text in ("avg", "average"):
            pending_intent.aggregation = "AVG"
            sql = generate_sql(pending_intent)
            pending_intent = None
            return sql

        if text in ("max", "maximum"):
            pending_intent.aggregation = "MAX"
            sql = generate_sql(pending_intent)
            pending_intent = None
            return sql

        return "Please answer with 'max' or 'avg'."

    # -----------------------------
    # Normal NL processing
    # -----------------------------
    norm = normalize(user_input)
    tokens = encode(norm)
    lf = build_logical_form(tokens, schema)

    # -----------------------------
    # FORCE clarification for superlative + department
    # -----------------------------
    if "highest" in text and "department" in text:
        # lock grouping context BEFORE asking
        lf.group_by = ("departments", "name")
        lf.join_required = True
        pending_intent = lf

        return (
            "Do you want the department with the highest "
            "individual salary or the highest average salary? (max/avg)"
        )

    # -----------------------------
    # Generate SQL
    # -----------------------------
    sql = generate_sql(lf)

    if not sql:
        return "I need more information to generate SQL."

    return sql


if __name__ == "__main__":
    while True:
        try:
            q = input("NL Query: ")
            print(nl_to_sql(q))
        except KeyboardInterrupt:
            print("\nExiting.")
            break