class List:
    def __init__(self, input_list):
        try:
            input_list = list(input_list)
        except Exception as e:
            raise ValueError("\n\nInput must be convertible to a list.\n") from e
            
        self.item_list = input_list
        
    def __str__(self):
        return str(self.item_list)
        
    def __getitem__(self, index):
        return self.item_list[index]
        
    def __setitem__(self, index, value):
        self.item_list[index] = value
        
    @staticmethod
    def get_info():
        return "Python lists but better"
        
    def setlist(self, new_list):
        try:
            new_list = list(new_list)
        except Exception as e:
            raise ValueError("Input must be convertible to a list.") from e
            
        self.item_list = new_list

    def append(self, *args):
        # Args is a list ([])
        for i in args:
            self.item_list.append(i)
            
    def remove(self, *args):
        # Args is a list ([])
        for item in args:
            try:
                self.item_list.remove(item)
            except ValueError:
                pass
            
    def pop(self, *args):
        sorted_indices = sorted(args, reverse=True)  # Sort indices in reverse order to avoid shifting
        
        for index in sorted_indices:
            try:
                self.item_list.pop(index)
            except IndexError:
                pass