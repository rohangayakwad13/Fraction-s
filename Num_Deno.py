import numpy as np

n1 = np.random.randint(1,10)
n2 = np.random.randint(1,10)
d1 = np.random.randint(1,10)
d2 = np.random.randint(1,10)

num = d1 * n2 + d2 * n1
deno = d1 * d2

print(f"""
 {n1}     {n2}
--- + ---
 {d1}     {d2}
""")

n = int(input("Enter Numerator : "))
d = int(input("Enter Denominator : "))

if n == num:
    print("Numerator is right.")
else:
    print("Numerator is wrong.")
if d == deno:
    print("Denominator is right")
    print(f"""
{n1}     {n2}
---  +  ---
{d1}     {d2}
Answer:
{num}
---
{deno}
""")
else:
    print("Denominator is wrong.")