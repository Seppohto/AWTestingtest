def fizzbuzz(int):
    lista = int
    if int%3==0 and int%5==0:
        vastaus='FizzBuzz'
    elif int%3==0:
        vastaus='Fizz'
    elif int%5==0:
        vastaus='Buzz'
    else:
        vastaus = int

    return vastaus