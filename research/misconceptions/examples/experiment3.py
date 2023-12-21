class TraceClass:
  def __init__(self):
    print(f"{self} created")

def test_function(obj=TraceClass()):
  print(f"test_function called with obj = {obj}")

print("Test code begins")
test_function()
