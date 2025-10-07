MAX = 10001

# To count digits in n (Required to rotate)
def length(n):
    return len(str(n))

# Function to rotate the digits of the number
def rotate(n):
    
    str_n = str(n)
    rotated = str_n[-1] + str_n[:-1]
    return int(rotated)


# Function to print circular primes up to n

def circular_primes(n):
    if n < 2:
        return

    # Build prime list using Sieve of Eratosthenes
    prime = [True] * MAX
    prime[0] = prime[1] = False

    for i in range(2, int(MAX**0.5) + 1):
        if prime[i]:
            for j in range(i * i, MAX, i):
                prime[j] = False

    # Check each number from 2 to n for circular prime
    for i in range(2, n):
        str_i = str(i)
        len_ = len(str_i)
        j, x = 0, i
        is_circular_prime = True
        for j in range(len_):
            if not prime[x]:
                is_circular_prime = False
                break
            x = rotate(x)
        
        # If all rotations are prime
        if is_circular_prime:
            print(i, end=" ")

# Main function to test the above functions
if __name__ == "__main__":
    n = 900
    circular_primes(n)
