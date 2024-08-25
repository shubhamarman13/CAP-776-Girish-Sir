try:
    x = 10
    y = "Shubham"
    print(x + y)
except (TypeError, ValueError, ZeroDivisionError) as e:
    print(f"The Error is {e}")
