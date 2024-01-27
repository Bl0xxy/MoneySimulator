# Imports
from File import File

class SaveFile(File):
    def __init__(self, filename, default="No Value", nameUpdates={}):
        super().__init__(filename, default)

        self.nameUpdates = nameUpdates

        self.item_check()
    
    def item_check(self):

        save = self.get()

        for item in self.nameUpdates: # Name Change Check
            if item in save:
                save[self.nameUpdates[item]] = save[item]
                save.__delitem__(item) 
        for item in self.default: # Item Exists Check
            if not item in save:
                save[item] = self.default[item]
        
        self.save(save) # Saves Data After Check
        
