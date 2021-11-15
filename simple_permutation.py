from math import ceil


def simple_permutation_encode(s: str, n_rows: int) -> str:
    permutation_matrix = [s[i::n_rows] for i in range(n_rows)]
    return ''.join(permutation_matrix)


def simple_permutation_decode(s: str, n_rows: int) -> str:
    n_cols, n_last = ceil(len(s) / n_rows), len(s) % n_rows
    permutation_matrix = ['' for i in range(n_cols)]
    s1, s2 = s[:n_cols * n_last], s[n_cols * n_last:]
    for i, ch in enumerate(s1):
        permutation_matrix[i % n_cols] += ch
    for i, ch in enumerate(s2):
        permutation_matrix[i % (n_cols - 1)] += ch
    return ''.join(permutation_matrix)


crypt_key = 5
name = 'Медведева Мария Максимовна'
print(f'Имя: {name}')

encrypted = simple_permutation_encode(name, crypt_key)
print(f'Зашифрованное имя: {encrypted}')

decrypted = simple_permutation_decode(encrypted, crypt_key)
print(f'Дешифрованное имя: {decrypted}')
