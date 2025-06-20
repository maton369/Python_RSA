# 🔐 小さな素数（CTFや概念検証用）
p = 61
q = 53
e = 17

n = p * q  # n = 3233
phi_n = (p - 1) * (q - 1)  # φ(n) = 3120
d = pow(e, -1, phi_n)  # 秘密指数 d = e⁻¹ mod φ(n)

# 🧾 平文（署名対象のメッセージ） → m < n が必要
m = 65  # 例: 'A' のASCIIコードでもある


def rsa_encrypt(m, e, n):
    """署名検証（公開鍵）"""
    return pow(m, e, n)


def rsa_decrypt(c, d, n):
    """署名生成（秘密鍵）"""
    return pow(c, d, n)


# 🖊️ 署名：秘密鍵でメッセージに署名する
signature = rsa_decrypt(m, d, n)
print(f"s = {signature}")  # ex: 2790

# ✅ 検証：公開鍵で署名を検証し、元のメッセージと一致するか確認
verification = rsa_encrypt(signature, e, n)
print(f"v = {verification}")  # ex: 65

# ✅ 一致検証
assert verification == m
