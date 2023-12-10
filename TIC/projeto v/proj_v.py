def aritmetico_encode(symbol_probabilities, symbol):
    # Calculate cumulative probabilities
    cumulative_probs = [0] + list(itertools.accumulate(symbol_probabilities))
    
    # Find the subinterval that corresponds to the symbol
    symbol_index = symbol_probabilities.index(symbol)
    subinterval_start = cumulative_probs[symbol_index]
    subinterval_end = cumulative_probs[symbol_index + 1]
    
    # Update the interval
    interval_width = subinterval_end - subinterval_start
    interval_start += subinterval_start * interval_width
    interval_end = interval_start + symbol * interval_width
    
    return interval_start, interval_end

def aritmetico_decode(symbol_probabilities, encoded_value):
    # Calculate cumulative probabilities
    cumulative_probs = [0] + list(itertools.accumulate(symbol_probabilities))
    
    # Find the symbol that corresponds to the subinterval containing the encoded value
    for i in range(len(symbol_probabilities)):
        subinterval_start = cumulative_probs[i]
        subinterval_end = cumulative_probs[i + 1]
        if subinterval_start <= encoded_value < subinterval_end:
            symbol = symbol_probabilities[i]
            break
    
    return symbol

def ans_encode(symbol_probabilities, symbol):
    # Calculate subinterval size
    subinterval_size = 1 / len(symbol_probabilities)
    
    # Find the subinterval that corresponds to the symbol
    symbol_index = symbol_probabilities.index(symbol)
    subinterval_start = symbol_index * subinterval_size
    subinterval_end = (symbol_index + 1) * subinterval_size
    
    # Update the interval
    interval_start += subinterval_start * interval_width
    interval_end = interval_start + symbol * interval_width
    
    return interval_start, interval_end

def ans_decode(symbol_probabilities, encoded_value):
    # Calculate subinterval size
    subinterval_size = 1 / len(symbol_probabilities)
    
    # Find the symbol that corresponds to the subinterval containing the encoded value
    symbol_index = int(encoded_value / subinterval_size)
    symbol = symbol_probabilities[symbol_index]
    
    return symbol
