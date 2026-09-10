from contextlib import contextmanager

@contextmanager
def simple_context():

    print("1. Before yield")

    yield ("here is the main thing ")

    print("3. After yield")


print("=" * 60)
print("Example 1")
print("=" * 60)

with simple_context() as np:
    print(np)
    

