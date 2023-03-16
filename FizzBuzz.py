# FizzBuzz
# To proste zadanie wygląda następująco:
# Wypisz liczby od 1 do 100, przy czym liczby podzielne przez 3 zastąp słowem ‘Fizz’, liczby podzielne przez 5,
# zastąp słowem ‘Buzz’,
# natomiast liczby podzielne i przez 3 i przez 5 zastąp słowem ‘FizzBuzz’.
# A w rezultacie, powinniśmy otrzymać – 1, 2, Fizz, 4, Buzz, 6, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16 itd
def fizzbuzz(start , stop):
    poczatek_zakresu = start
    koniec_zakresu = stop
    for i in range(poczatek_zakresu,koniec_zakresu+1):
      if i%3 ==0 and i%5 == 0:
         print("FizzBuzz")
      elif i%5 ==0:
         print("Buzz")
      elif i%3 ==0:
         print("Fizz")
      else:
         print(i)
print("FizzBuzz")
print("15 => FizzBuzz")
print("5 => Buzz")
print("3 => Fizz")
a= int(input("Podaj poczatek zakresu: "))
b=int(input("Podaj koniec zakresu: "))
fizzbuzz(a,b)