"""
Lite experiment med heltalsoperationer
"""

def divisionsexempel(x, y):
    """Tar x, y skriver ut x/y, x//y, x%y"""
    print("---------------")
    print(f"{x} // {y} = {x//y}")
    print(f"{x} % {y} = {x%y}")
    print(f"{x} / {y} = {x/y}")

def farenheit(celsius):
    """tar grader Celsius, returnererar Farenheit"""
    return 9/5 * celsius + 32

divisionsexempel(5, 2)
divisionsexempel(4, 2)
divisionsexempel(3, 2)
divisionsexempel(2, 2)
divisionsexempel(1, 2)

print(f"20 celsius = {farenheit(20)} farenheit")
