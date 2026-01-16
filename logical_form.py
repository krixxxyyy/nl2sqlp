class LogicalForm:
    def __init__(self):
        self.tables = set()
        self.columns = set()
        self.filters = []
        self.aggregation = None
        self.group_by = None
        self.join_required = False

    def is_complete(self):
        if self.aggregation and not self.columns and not self.group_by:
            return False
        return True
