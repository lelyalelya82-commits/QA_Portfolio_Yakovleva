from lesson_03.address import Address
from mailing import Mailing

to_address = Address("385214", "Иркутск", "Желябова", "15", "37")
from_address = Address("664528", "Ангарск", "Лапина", "2", "5")

mailing = Mailing(to_address, from_address, 350, "TRACK123456789")

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} -"
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)