import json

def load_schema(path="schema.json"):
    with open(path, "r") as f:
        return json.load(f)

def get_tables(schema):
    return list(schema.keys())

def get_columns(schema):
    cols = []
    for table, meta in schema.items():
        for col, dtype in meta["columns"].items():
            cols.append((table, col, dtype))
    return cols
