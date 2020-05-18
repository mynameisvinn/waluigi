# waluigi
waluigi is a bare bones implementation of luigi, the workflow scheduler developed by spotify.

## example
every task is defined as a `WaluigiTask`.

```python
class FinalRecipe(WaluigiTask):
    def requires(self):
        return [AddGrapes()]

    def run(self):
        with open("words.txt", "r") as f:
            print(f.read()) 
            
    def output(self):
        return 'letter_counts.txt'
```

when we execute, we call:
```python
F = FinalRecipe()
F()
```
this kicks off `WaluigiTask`s call method, which looks like this:
```python
def __call__(self):
    if len(self.requires()) > 0:
        for parent in self.requires():
            parent()
    self.run()
``` 
it will call any `WaluigiTask` that's required. once it's done executing its parent, it will `run()` itself, which was previously defined by the user.
```python
class FinalRecipe(WaluigiTask):
    # def requires(self):
        # return [AddGrapes()]

    def run(self):
        with open("words.txt", "r") as f:
            print(f.read()) 
            
    # def output(self):
        # return 'letter_counts.txt'
```