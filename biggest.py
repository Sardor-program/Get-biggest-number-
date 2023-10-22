
def getBiggest(numbers):
    if len(numbers) == 0:
        return None
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            
            biggest = number
           
    return biggest        
      