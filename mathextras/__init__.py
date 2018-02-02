"""__init__.py
Calls other files in the package.
"""


def fac(num):
    # Gets list of factors of variable num
    output = []
    # Creates list for output
    for x in range(1, num + 1):
    # Loop with variable x
        if num % x == 0 and not num % x in output:
            # Tests if x goes into num and if x is already in output
            output.append(x)
    return output

def lcm(num1, num2, limit=10):
  num1ls = [num1]
  num2ls = [num2]
  mult = list(range(2, limit + 1))
  for x in mult:
    num1ls.append(num1 * x)
    num2ls.append(num2 * x)
    if num1ls[-1] in num2ls:
      return num1ls[-1]
    elif num2ls[-1] in num1ls:
      return num2ls[-1]
    else:
      continue
  return


def prime (num):
    """prime(num)
    Returns true or false depending on whether or not a number is prime.
    num is and int to process.  
    """
    import time
    strnum = str(num)
    count = num - 1
    def remain (div):
        quotient = num / div
        strdiv = str(div)
        foo = num % div
        if foo == 0:
            return True
        else:
            return False
    while count > 1:
        if remain (count):
            return False
            count = 1
        else:
            count = count - 1
    return True
    return

def prime_out(num):
    """prime_out(num)
    User-friendly version of prime().
    Prints output and has timing functionality.
    Usage:
    prime_out(num)
    num is an int that to be evaluated as prime.  
    """
    import time
    t1_start = time.perf_counter()
    t2_start = time.process_time()
    strnum = str(num)
    count = num - 1
    print("Calculating whether " + strnum + " is prime...")
    def remain (div):
        quotient = num / div
        strdiv = str(div)
        foo = num % div
        if foo == 0:
            print (strnum +" is divisible by " + strdiv)
            return True
        else:
            return False
    while count > 1:
        if remain (count):
            t1_stop = time.perf_counter()
            t2_stop = time.process_time()
            print(strnum + " isn't Prime.  Done! ")
            print("--------------------------------------------------")
            print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
            print("or %.1f [min]" % ((t1_stop-t1_start)/60))
            print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))
            print("or %.1f [min]" % ((t1_stop-t1_start)/60))
            print("--------------------------------------------------") 
            return
            count = 1
        else:
            count = count - 1
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print (strnum + " is prime! Done! ")
    print("--------------------------------------------------")
    print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
    print("or %.1f [min]" % ((t1_stop-t1_start)/60))
    print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))
    print("or %.1f [min]" % ((t1_stop-t1_start)/60))
    print("--------------------------------------------------") 

    return
def mode(nums):
    output = {}
    lsnum = None
    lock = 0
    amount = 0
    for x in range(len(nums)):
        if lock == 0:
            lock = 1
            lsnum = nums[x]
        if nums[x] != lsnum:
            output[lsnum] = amount
            lsnum = nums[x]
            amount = 0
            continue
        else:
            amount += 1
            continue
    return output


def mean(nums):
  output = 0
  for x in range(len(nums)):
    output += nums[x]
  return output / len(nums)
    
