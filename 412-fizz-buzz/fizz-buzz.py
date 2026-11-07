class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        arr = []
        for i in range(0,n):
            if (i+1)%3 == 0 and (i+1)%5 == 0:
                value = "FizzBuzz"
            elif (i+1)%3 == 0:
                value = "Fizz"
            elif (i+1)%5 == 0:
                value = "Buzz"
            else:
                value = str(i+1)
            arr.append(value)
        return arr
