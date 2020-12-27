def hello(name: str = "world") -> None:
    """
    `Hello, xxx.` のメッセージを出力する。

    Parameters
    ----------
    name : str
        対象の文字列。
    """
    print(f"Hello, {name}.")
