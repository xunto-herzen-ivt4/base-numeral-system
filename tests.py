import base_ns

for i in range(2, 16):
    print("=== ns " + str(i) + "===")
    for j in range(0, 20):
        tmp = base_ns.convert(j, i)
        print(j, "=>", tmp)
        print(tmp, "=>", base_ns.convert_to_dec(tmp, i))
        print("\n")

