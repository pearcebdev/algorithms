def is_palindrome1(w):
  """Create slice with negative step and confirm equality with w."""
  return w[::-1] == w

def is_palindrome2(w):
  """Strip outermost characters if same, return false when mismatch."""
  while len(w) > 1:
    if w[0] != w[-1]:
      return False
    w = w[1:-1]           # strip characters on either end; repeat

  return True