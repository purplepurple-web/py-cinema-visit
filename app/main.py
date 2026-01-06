from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customer_objects: List[Customer] = []

    for customer in customers:
        customer_obj = Customer(
            name=customer["name"],
            food=customer["food"],
        )
        customer_objects.append(customer_obj)

        CinemaBar.sell_product(
            product=customer_obj.food,
            customer=customer_obj,
        )

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff,
    )
