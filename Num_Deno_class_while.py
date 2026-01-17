import numpy as np

class Fractions:
    class calculate:
        def plus():
            while True:
                try:
                    n1 = np.random.randint(1,10)
                    n2 = np.random.randint(1,10)
                    d1 = np.random.randint(1,10)
                    d2 = np.random.randint(1,10)
                    print(f"""
        {n1}     {n2}
        --- + ---
        {d1}     {d2}
        """)
                    num = d1 * n2 + d2 * n1
                    deno = d1 * d2
                    n = int(input("Enter Numerator : "))
                    d = int(input("Enter Denominator : "))
                    if n == num:
                        print("Numerator is right.")
                    else:
                        print("Numerator is wrong.")
                        break
                    if d == deno:
                        print("Denominator is right.")
                        print(f"""
        {n1}     {n2}
        --- + ---
        {d1}     {d2} 
        Answer:
        {num}
        --
        {deno}
        """)    
                        cob = input("Do you wan't to countinue this? (yes/no) : ")
                        if cob == "Yes" or cob == "yes":
                            continue
                        elif cob == "No" or cob == "no":
                            break
                        else:
                            print("Condition is not match!.\nPlease enter only yes or no.")
                    else:
                        print("Denominator is wrong.")
                        break
                except Exception:
                    print("Please Enter a value.")
                    break
        
Fractions.calculate.plus()