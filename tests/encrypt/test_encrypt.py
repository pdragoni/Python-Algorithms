from challenges.challenge_encrypt_message import encrypt_message
import pytest

message = "password"
even = 4
odd = 5
negative = -2
zero = 0


def test_encrypt_message():
    assert encrypt_message(message, negative) == "drowssap"
    assert encrypt_message(message, odd) == "wssap_dro"
    assert encrypt_message(message, even) == "drow_ssap"
    with pytest.raises(TypeError, match=r"tipo inválido para key"):
        encrypt_message(message, "a")
    with pytest.raises(TypeError, match=r"tipo inválido para message"):
        encrypt_message(negative, even)


# def f():
#     return 3


# def test_function():
#     assert f() == 4
