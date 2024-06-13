POSITIVE_INTEGER_MESSAGE = "n needs to be a positive integer"

def factorial_recursive(n):
  if (n == 0):
    return 1
  else:
    return n * factorial_recursive(n - 1)

def approx_sin(x, n):
  if (n <= 0):
    print(POSITIVE_INTEGER_MESSAGE)
    return

  sin_x = 0
  for i in range(0, n):
    fraction = (x**(2 * i + 1)) / factorial_recursive((2 * i + 1))
    sin_x += ((-1)**i) * fraction
  return round(sin_x, 4)
def approx_cos(x, n):
  if (n <= 0):
    print(POSITIVE_INTEGER_MESSAGE)
    return

  cos_x = 0
  for i in range(0, n):
    fraction = (x**(2 * i)) / factorial_recursive((2 * i))
    cos_x += ((-1)**i) * fraction
  return round(cos_x, 4)

def approx_sinh(x, n):
  if (n <= 0):
    print(POSITIVE_INTEGER_MESSAGE)
    return

  sinh_x = 0
  for i in range(0, n):
    sinh_x += (x**(2 * i + 1)) / factorial_recursive((2 * i + 1))
  return round(sinh_x, 4)

def approx_cosh(x, n):
  if (n <= 0):
    print(POSITIVE_INTEGER_MESSAGE)
    return

  cosh_x = 0
  for i in range(0, n):
    cosh_x += (x**(2 * i)) / factorial_recursive((2 * i))
  return round(cosh_x, 2)


print(approx_sin(x=3.14, n=10))
print(approx_cos(x=3.14, n=10))
print(approx_sinh(x=3.14, n=10))
print(approx_cosh(x=3.14, n=10))
