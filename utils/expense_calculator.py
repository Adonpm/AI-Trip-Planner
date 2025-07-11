class Calculator:
    @staticmethod # staticmethod helps to write multiple functions inside a class without __init__ and self
    def multiply(a:int, b:int) -> int:
        '''
        Multiply two integers
        
        Args:
            a (int): First integer
            b (int): Second integer

        Returns:
            int: The product of a and b
        '''
        return a * b
    
    @staticmethod
    def calculate_total(*x: float) -> float:
        '''
        Calculate sum of the given numbers
        
        Args:
            *x (float):  Any number of float values to sum

        Returns:
            float: The sum of numbers in *x
        '''
        return sum(x)
    
    @staticmethod
    def calculate_daiy_budget(total:float, days:int) -> float:
        '''
        Calculate daily budget

        Args:
            total (float): Total cost
            days(int): Total number of days

        Returns:
            float: Expense for a single day
        '''
        return total/days if days > 0 else 0
    