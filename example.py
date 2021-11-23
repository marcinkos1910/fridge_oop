from datetime import datetime, timedelta


class FilteringByExpirationDate:

    def __init__(self, expiration_date, product):
        self.products = []
        self.product = product
        self.expiration_date = expiration_date
        self.date_with_warning = datetime.today() + timedelta(days=5)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx <= len(self.product):
            raise StopIteration("No more products")

        # products_to_expire = []
        # if self.date_with_warning >= self.expiration_date:

