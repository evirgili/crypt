from typing import Tuple


def rsa_encode(public_key: Tuple[int, int], message: int) -> int:
    e, n = public_key
    return (message ** e) % n


def rsa_decode(private_key: Tuple[int, int], encrypted_message: int) -> int:
    d, n = private_key
    return (encrypted_message ** d) % n


p, q = 101, 113
e, d = 3533, 6597

pub_key = e, p * q
pr_key = d, p * q

m1, m2, m3 = 4, 13, 91

encs = rsa_encode(pub_key, m1), rsa_encode(pub_key, m2), rsa_encode(pub_key, m3)
decs = rsa_decode(pr_key, encs[0]), rsa_decode(pr_key, encs[1]), rsa_decode(pr_key, encs[2])
print(f'Сообщения: {m1, m2, m3}')
print(f'Зашифрованные сообщения: {encs}')
print(f'Дешифрованные сообщения: {decs}')
