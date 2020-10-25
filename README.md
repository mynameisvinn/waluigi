# waluigi
waluigi is a simple <100 loc re-implementation of [luigi](https://github.com/spotify/luigi), the popular workflow scheduler developed by spotify. 

## a working example
we have the following seqeuential pipeline: (1) add cereal, (2) add milk, (3) eat.

each task is represented as a `WaluigiTask` object:
```python
class AddCereal(WaluigiTask):
    def requires(self):
        return [AddMilk()]

    def run(self):
        # do something
            
    def output(self):
        # do something


class AddMilk(WaluigiTask):
    def requires(self):
        return [AddMilk()]

    def run(self):
        # do something
            
    def output(self):
        # do something


class Eat(WaluigiTask):
    def requires(self):
        return [AddMilk()]

    def run(self):
        # do something
            
    def output(self):
        # do something
```

to execute, we call:
```python
breakfast = Eat()
breakfast()
```