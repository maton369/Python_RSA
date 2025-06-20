# ===== 小さなRSA公開鍵（各nは互いに素） =====
m = 65
e = 3

n1 = 7 * 11  # n1 = 77
n2 = 13 * 17  # n2 = 221
n3 = 19 * 23  # n3 = 437

# ===== 各モジュロで暗号化（RSA暗号） =====
c1 = pow(m, e, n1)
c2 = pow(m, e, n2)
c3 = pow(m, e, n3)


# ===== 中国剰余定理で復号（m^e を合成） =====
def chinese_remainder_theorem(c, n):
    # N = n1 * n2 * n3
    N = 1
    for ni in n:
        N *= ni

    result = 0
    for ci, ni in zip(c, n):
        Ni = N // ni
        xi = pow(Ni, -1, ni)  # modinv(Ni, ni)
        result += ci * Ni * xi

    return result % N  # m^e を復元


# ===== 合成値を求める（m^e） =====
c = chinese_remainder_theorem([c1, c2, c3], [n1, n2, n3])

# ===== 整数e乗根（実質的なRSA復号） =====
m_recovered = int(round(c ** (1 / e)))

# ===== 結果表示 =====
print(f"復元された平文 m = {m_recovered}")
assert m_recovered == m
