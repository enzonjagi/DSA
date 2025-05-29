def multiply(n):
    result = 1
    
    result *= int(n)
        
    return result
        

def persistence(n):
    result = 1
    count = 0
    
    if len(str(n)) == 1:
        # value is already one digit
        return count
    else:
        while len(str(n)) > 1:
            for i in str(n):
                result *= int(i)
            
            n = result
            persistence(n)
            count += 1
        
        return count
                
