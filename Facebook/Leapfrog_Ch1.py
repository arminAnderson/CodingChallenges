cases = int(input())
for i in range(cases):
    sequence = input()
    if sequence.count(".") == 0 or sequence.count("B") < sequence.count("."):
        print("Case #{}: {}".format(i + 1, "N"))
    else:
        print("Case #{}: {}".format(i + 1, "Y"))