# Standalone Calculator
A Python calculator project to enable to do any simple math express calculation.

## Motivation
I decided to research a bit more complex scenario for my Python studies and I found this peculiar script, the script
looks interesting but had some pitfalls, which is interesting for learning 😃 So I decided to take it as an exercise
and also produce some interesting ideas for further scenarios to come.

## Source
The code was originally developed in conjunction by `internet_user` and `Gareth Rees` on [StackExchange](https://codereview.stackexchange.com/questions/160524/evaluating-arithmetic-expressions).

This code has fixed some pitfalls:
- can execute consecutive different operations in the same level (ex. `2 * 2 / 2 = 2`)
- can execute operations starting with `+` and `-` and also deal with small operations like `(-10)`.

And also has some improvements:
- accepts inputs with spaces and special characters `[`, `]`, `{`, `}`, `–`, `:`, `÷`, `x`, `²` and `³`.
- some code reviews

## How to Use
1. Clone this repository.
2. Execute `main.py` with an expression as arguments:
```bash
$ ./main.py 1 + 1
```
or
```bash
$ python main.py 1 + 1
```
3. Follow the instructions: input the complete expression as arguments for the script. The result is displayed. (See [Supported Operations](#supported-operations))

## Supported Operations
| operator    |    function                             |
|:-----------:|-----------------------------------------|
| `+`         | addition                                |
| `-` `–`     | subtraction                             |
| `*` `x`     | multiplication                          |
| `/` `:` `÷` | division                                |
| `^`NUM      | exponentiation                          |
| `²` `³`     | shortcuts for exponentiation to 2 and 3 |  

## Requirements
```bash
pip3 install -r requirements.txt
```
or
```bash
pip install -r requirements.txt
```

## License
Apache 2.0 license. See more details [here](https://github.com/jjbeto/pycalc/blob/master/LICENSE).
