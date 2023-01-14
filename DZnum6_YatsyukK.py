class BuyingError(Exception):
    def __str__(self):
        return f"Ми не можемо купити продукти"

def check_money(amount_of_money,limit_value):
    if amount_of_money>limit_value:
        return "Грошей достатньо"
    else:
        raise BuyingError(amount_of_money)

money=123
check_money(money, 300)