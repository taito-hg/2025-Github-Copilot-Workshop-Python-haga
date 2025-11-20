def fibonacci(n):
    """フィボナッチ数列のn番目の数を返す
    
    フィボナッチ数列は、最初の2つの数が0と1で、
    それ以降の数は直前の2つの数の和となる数列です。
    例: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    
    Parameters
    ----------
    n : int
        フィボナッチ数列の位置（0から始まるインデックス）
        - n <= 0 の場合、0を返します
        - n == 1 の場合、1を返します
        - n >= 2 の場合、フィボナッチ数列を計算します
    
    Returns
    -------
    int
        n番目のフィボナッチ数
        - fibonacci(0) -> 0
        - fibonacci(1) -> 1
        - fibonacci(2) -> 1
        - fibonacci(3) -> 2
        - fibonacci(n) -> fibonacci(n-1) + fibonacci(n-2)
    
    Examples
    --------
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    
    Notes
    -----
    この実装は反復的なアプローチを使用しているため、
    再帰的な実装と比較して効率的です。
    
    時間計算量: O(n)
    空間計算量: O(1)
    
    See Also
    --------
    フィボナッチ数列について:
    https://ja.wikipedia.org/wiki/フィボナッチ数
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
