class WaluigiTask():
    """represent all tasks as WaluigiTask.
    """
    def __init__(self):
        pass
    
    @classmethod
    def get_classname(cls):
        return cls.__name__
    
    def __call__(self):
        print(">> executing ", self.get_classname())
    
        # execute parents... self.requires is a list of class instances
        if len(self.requires()) > 0:
            for parent in self.requires():
                parent()

        # step 2 - once parents have been executed, run itslef
        self.run()

        
    def requires(self):
        return []