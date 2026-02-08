from app.utils import normalize_username


def test_normalize_username():
    assert normalize_username("  Alice   Bob ") == "alice bob"
    assert normalize_username("Alice") == "alice"
