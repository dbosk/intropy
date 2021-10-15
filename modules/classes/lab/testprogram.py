import my_sequence_library as myseq
# Ladda hem modulen input_type från:
# https://github.com/dbosk/intropy/raw/master/modules/classes/lab/input_type.py
import input_type as it

def test_arithmetic_seq():
    """Function testing the arithmetic sequence"""
    a1 = myseq.ArithmeticSequence(1, 1)
    for i in range(20):
        print(f"a1[{i}] = {a1[i]}")
        if a1[i] != i:
            raise Exception(f"a1[{i}] = {a1[i]} != {i}")

    a2 = myseq.ArithmeticSequence(2, 2)
    for i in range(20):
        print(f"a2[{i}] = {a2[i]}")
        if a2[i] != 2*i:
            raise Exception(f"a1[{i}] = {a1[i]} != {2*i}")

    try:
        a2[-1]
    except IndexError as err:
        print(f"Förväntat IndexError fångat: {err}")
    else:
        raise Exception(f"a2[-1] = {a2[-1]}, förväntades IndexError")

def test_geometric_seq():
    """Function testing the arithmetic sequence"""
    g1 = myseq.GeometricSequence(1, 1)
    for i in range(20):
        print(f"g1[{i}] = {g1[i]}")
        if g1[i] != 1:
            raise Exception(f"g1[{i}] = {g1[i]} != 1")

    g2 = myseq.GeometricSequence(2, 2)
    for i in range(10):
        print(f"g2[{i}] = {g2[i]}")
        if g2[i] != 2**(i+1):
            raise Exception(f"g1[{i}] = {g1[i]} != {2**(i+1)}")

    try:
        g2[-1]
    except IndexError as err:
        print(f"Förväntat IndexError fångat: {err}")
    else:
        raise Exception(f"g2[-1] = {g2[-1]}, förväntades IndexError")

def test_file_seq():
    """Function testing the MultiplicativeSequenceFromFile class"""
    # använd sequence.csv som exempelinmatning:
    # https://github.com/dbosk/intropy/raw/master/modules/classes/lab/sequence.csv
    filename = "sequence.csv"
    gf = myseq.MultiplicativeSequenceFromFile(filename)

    print(f"gf[7] = {gf[7]}")
    if gf[7] != 1.217251414:
        raise Exception(f"gf[7] = {gf[7]} != 1.217251414")

    # sequence.csv har färre än 1000 element, så detta ska generera ett
    # IndexError
    try:
        print(f"gf[1000] = {gf[1000]}")
    except IndexError:
        print("Förväntat IndexError fångat.")
    else:
        raise Exception(f"Förväntade ett IndexError: gf[1000] = {gf[1000]}")


def run_tests():
    """Function containing tests for the my_sequence_library module"""
    test_arithmetic_seq()
    test_geometric_seq()
    test_file_seq()

if __name__ == "__main__":
    run_tests()
