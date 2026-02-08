def normalize_username(name: str) -> str:
    """
    ユーザー名を正規化する:
    - 前後の空白を除去
    - 連続スペースを1つに
    - 小文字化
    """
    parts = name.strip().split()
    return " ".join(parts).lower()
