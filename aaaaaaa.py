def bitwise_circuit(a: int, b: int) -> dict:
    result = {
        'AND': a & b,
        'OR': a | b,
        'XOR': a ^ b,
        'NOT A': ~a,
        'NOT B': ~b,
        'A << 1': a << 1,
        'B >> 1': b >> 1
    }
    return result

# Example usage:
a = 6  # 0b0110
b = 3  # 0b0011

output = bitwise_circuit(a, b)
for op, res in output.items():
    print(f'{op}: {res}')

