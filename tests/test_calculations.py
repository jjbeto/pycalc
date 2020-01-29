import pytest

import main


def test_evaluate_simple_values():
    expressions = {
        ' + 1 ': 1,
        '-1': -1,
    }
    for expr, result in expressions.items():
        assert result == main.evaluate(expr)


def test_evaluate_simple_expressions():
    expressions = {
        ' 1 + 1 ': 2,
        '100 / 4': 25,
        '9 * 9': 81,
        '15 - 5': 10
    }
    for expr, result in expressions.items():
        assert result == main.evaluate(expr)


def test_evaluate_sequence_expressions():
    expressions = {
        ' 2 x 2 / 2 ': 2,
        ' 2 / 2 * 2 ': 2,
        ' 2 + 2 / 2 ': 3,
        ' 2 / 2 + 1 ': 2,
    }
    for expr, result in expressions.items():
        assert result == main.evaluate(expr)


def test_evaluate_expressions_with_sublevel():
    expressions = {
        '(4+4) * 10': 80,
        '(10/10) * (-5+1)': -4,
    }
    for expr, result in expressions.items():
        assert result == main.evaluate(expr)


def test_evaluate_expressions_with_two_sublevels():
    expressions = {
        '(4+(16/4)) * 10': 80,
        '((4x2+2)/(5x2)) * ((5-10)+(10-9))': -4,
    }
    for expr, result in expressions.items():
        assert result == main.evaluate(expr)


def test_evaluate_expressions_more_complex():
    "all expressions from https://teresachiacchio.wixsite.com/matemagica/expressoes"
    expressions = {
        '4 – [– (6 + 4) + (3 – 2 – 1)]': 14,
        '15 x 2 – 30 ÷ 3 + 7': 27,
        '10 x [30 ÷ (2 x 3 + 4) + 15]': 180,
        '25 + {14 – [25 x 4 + 40 – (20 ÷ 2 + 10)]}': -81,
        '37 – 14 + 35 – 10': 48,
        '32 ÷ 2 . 3 ÷ 4 . 5': 3.091787439613527,
        '32 ÷ 2 x 3 ÷ 4 x 5': 60,
        '180 ÷ 4 * {9 ÷ [3 * (3 * 1)]}': 45,
        '16 : (-4) x 2': -8,
        '16 x(-4): 2': -32,
        '10 + 2² x 3': 22,
        '5² – 4 x 2 + 3': 20,
        '20 – [4² + ( 2³ – 7 )]': 3,
        '10 –{ 10 + [ 8² : ( 10 – 2 ) + 3 x 2 ] }': -14,
        '27 + {14 + 3 x [100 : (18 – 4 x 2) + 7] } : 13': 32,
        '{100 – 413 x (20 – 5 x 4) + 25} : 5': 25,
        '25 + { 12 + [ 2 – ( 8 – 6 ) + 2 ]}': 39,
        '38 – { 20 – [ 22 – ( 5 + 3) + ( 7 – 4 +1)]}': 36,
        '26 + { 12 – [ ( 30 – 18) + ( 4 – 1) – 6 ] – 1 }': 28,
        '(90+10)*2 / (90+(1000/    (   50+25*2)))': 2,
    }
    for expr, result in expressions.items():
        assert result == main.evaluate(expr)


def test_evaluate_multiple_evaluations():
    assert 42 == main.evaluate(main.evaluate('5² – 4 x 2 + 3'), '+', main.evaluate('10 + 2² x 3'))


def test_evaluate_with_wrong_parentheses():
    with pytest.raises(SyntaxError):
        main.evaluate('(1+1')


def test_evaluate_with_wrong_text():
    with pytest.raises(SyntaxError):
        main.evaluate('ABC')


def test_evaluate_with_wrong_text():
    with pytest.raises(SyntaxError):
        main.evaluate('')
