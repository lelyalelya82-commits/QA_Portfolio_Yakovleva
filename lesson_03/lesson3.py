
from user import User
from lesson_04.card import Card

marta = User("Marta")


marta.sayName()
marta.sayAge()
marta.setAge(33)
marta.sayAge()

card = Card("1234 5678 9876 5432", "11/28", "Marta A")
card.pay(1000)