# 小さい素数を使った簡易RSAテスト
p = 61
q = 53
e = 17

n = p * q  # n = 3233
phi_n = (p - 1) * (q - 1)  # φ(n) = 3120
d = pow(e, -1, phi_n)  # d = 2753（eの逆元）

# 平文（m）を適切に小さく設定
m = 65  # m < n である必要がある


def rsa_encrypt(m, e, n):
    return pow(m, e, n)


def rsa_decrypt(c, d, n):
    return pow(c, d, n)


# 暗号化
cipher_text = rsa_encrypt(m, e, n)
print(f"c={hex(cipher_text)}")  # 0x79f

# 復号
plain_text = rsa_decrypt(cipher_text, d, n)
print(f"m={hex(plain_text)}")  # 0x41

# 検証
assert plain_text == m
