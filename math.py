import math
number = float(input("Enter a number: "))
square_root = math.sqrt(number)
if number > 0:
    natural_log = math.log(number)
else:
    natural_log = "undefined (log is not defined for non-positive numbers)"
sine_value = math.sin(number)
print(f"\nResults for number {number}:")
print(f"Square root: {square_root}")
print(f"Natural logarithm: {natural_log}")
print(f"Sine (radians): {sine_value}")
