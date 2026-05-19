from scripts.thematic_analysis import identify_theme


def test_authentication_theme():

    text = "OTP code not working"

    result = identify_theme(text)

    assert result == "Authentication Issues"


def test_transaction_theme():

    text = "Money transfer failed"

    result = identify_theme(text)

    assert result == "Transaction Issues"


def test_performance_theme():

    text = "The app crashes frequently"

    result = identify_theme(text)

    assert result == "Performance Issues"