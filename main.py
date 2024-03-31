def read_words(filename):
    words_freq = []
    with open(filename, 'r') as file:
        for line in file:
            freq, word = line.strip().split()
            if int(freq) > 50000:  # Filtrujeme slova s frekvencí větší než 50000
                words_freq.append((word, int(freq)))
            else:
                break
    words_freq.sort(key=lambda x: x[0])  # Lexikografické řazení

    with open("./data/output.txt", "w") as file:
        for word, freq in words_freq:
            file.write(f"{freq} {word}\n")

    return words_freq

def calculate_probabilities(words_freq):
    total_freq = sum(freq for _, freq in words_freq)
    p = [0] + [freq / total_freq for _, freq in words_freq]  # pravděpodobnosti p_i
    q = [words_freq[0][1] / total_freq] + [(words_freq[i][1] - words_freq[i-1][1]) / total_freq for i in range(1, len(words_freq))] + [1 / total_freq]  # pravděpodobnosti q_i
    return p, q

def construct_optimal_bst(p, q, n):
    e = [[0] * (n+2) for _ in range(n+2)]
    w = [[0] * (n+2) for _ in range(n+2)]
    root = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]

    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            e[i][j] = float('inf')
            w[i][j] = w[i][j-1] + p[j] + q[j]

            for r in range(i, j+1):
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root

def count_comparisons(root, words, key, i, j, comparisons=0, compared_words=[]):
    if i > j:
        return comparisons, compared_words
    r = root[i][j]
    compared_words.append(words[r-1])
    if words[r-1] == key:
        return comparisons + 1, compared_words
    elif key < words[r-1]:
        return count_comparisons(root, words, key, i, r-1, comparisons + 1, compared_words)
    else:
        return count_comparisons(root, words, key, r+1, j, comparisons + 1, compared_words)

def main():
    filename = './data/dictionary.txt'
    words_freq = read_words(filename)
    words, freqs = zip(*words_freq)
    p, q = calculate_probabilities(words_freq)
    n = len(words)
    e, root = construct_optimal_bst(p, q, n)

    # Příklad hledání slova "must" a výpis počtu porovnání a porovnávaných slov
    key = 'must'
    comparisons, compared_words = count_comparisons(root, words, key, 1, n)
    print("Number of words in dictionary:", n)
    print(f"Number of comparisons to find '{key}': {comparisons}")
    print("Compared words:", compared_words)

if __name__ == "__main__":
    main()
