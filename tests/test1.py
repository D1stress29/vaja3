# tests/my_custom_tests.py

def test_arithmetic():
    """Preprost test za preverjanje osnovne matematike."""
    niz_stevil = [1, 2, 3, 4, 5]
    assert sum(niz_stevil) == 15
    assert max(niz_stevil) == 5

def test_string_logic():
    """Test za preverjanje logike nizov."""
    ime = "Gemini"
    assert ime.upper() == "GEMINI"
    assert "mi" in ime

def test_environment_check():
    """Ta test vedno uspe in služi kot dokaz, da se okolje postavi pravilno."""
    is_ready = True
    assert is_ready is True