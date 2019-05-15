class Sol:
    def fizz_buzz(self,n):
        list=[]
        for i in range(n):
            if (i+1)%15==0:
                list.append("FizzBuzz")
            elif (i+1)%5==0:
                list.append("Buzz")
            elif (i+1)%3==0:
                list.append("Fizz")
            else:
                list.append(str(i+1))
        return list


if __name__ == '__main__':
    p1=Sol()
    print(p1.fizz_buzz(15))
