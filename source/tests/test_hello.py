from src.hello import hello


def test_hello_default(capsys):
    hello()
    out, err = capsys.readouterr()
    assert out == "Hello, world.\n"


def test_hello_with_name(capsys):
    hello("サザエ")
    hello("カツオ")
    out, err = capsys.readouterr()
    assert out == "Hello, サザエ.\n" "Hello, カツオ.\n"
