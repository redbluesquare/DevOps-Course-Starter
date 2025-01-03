class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def open_items(self):
        output = []
        for item in self._items:
            if item.status == 'open':
                output.append(item)
        return output
    
    @property
    def done_items(self):
        output = []
        for item in self._items:
            if item.status == 'closed':
                output.append(item)
        return output