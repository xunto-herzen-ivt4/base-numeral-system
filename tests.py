import base_ns

for base in range(2, 20, 5):
    for number in range(1, 100, 15):
        number /= 10
        converted = base_ns.convert(number, base)
        print(number, "in", base,  "==", converted)
        print(converted, "=>", base_ns.convert_to_dec(converted))
        print("\n")