"""Experiment with Python's default arguments."""

def expand(x):
    """Append 1 to the list x and return it."""
    x += [2]
    # x.append(1)
    # x.expand([1])
    return x


print(
  f"[1] -> {expand([1])}\n"
  f"[2] -> {expand([2])}\n"
  f"()  -> {expand([])}\n"
  f"()  -> {expand([])}\n"
)
