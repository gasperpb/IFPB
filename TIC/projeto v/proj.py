class ANS:
    def __init__(self, probabilities):
        self.probabilities = probabilities
        self.max_val = 2 ** 16
        self.state = self.max_val

    def encode_symbol(self, symbol):
        target_row = int(self.probabilities[symbol] * self.max_val)
        while self.state > target_row:
            self.state >>= 1
            print("1", end="")
        self.state = target_row
        print("0", end="")

    def decode_symbol(self, stream):
        bit = stream.read(1)
        while bit == "1":
            self.state <<= 1
            bit = stream.read(1)
        self.state += 1
        print(f"Decoded symbol: {self.get_decoded_symbol()}")

    def get_decoded_symbol(self):
        for symbol, prob in self.probabilities.items():
            if int(prob * self.max_val) == self.state:
                return symbol

# Exemplo de uso
symbol_probabilities = {'A': 0.4, 'B': 0.5, 'C': 0.1}
ans_encoder = ANS(symbol_probabilities)

# Codificação
user_input = input("Digite uma sequência de símbolos (por exemplo, 'IFPB'): ")
for symbol in user_input:
    ans_encoder.encode_symbol(symbol)

# Decodificação (a partir da sequência de bits gerada)

user_input_decoding = input("\nDigite a sequência de bits para decodificar: ")
ans_encoder.decode_symbol(user_input_decoding)
