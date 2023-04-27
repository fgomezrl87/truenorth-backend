class Utils:
    def check_user_balance(self, user_balance: int, operation_cost: int) -> bool:
        return user_balance >= operation_cost
