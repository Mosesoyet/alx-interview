#!/usr/bin/python3
"""Prime game module
"""


def isPrime(n):
    """Checks if a number is prime
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def delete(n, nums):
    """ delete numbers and assign 0
    """
    for i in range(len(nums)):
        if nums[i] % n == 0:
            nums[i] == 0


def isWinner(x, nums):
    """ Where x is the number of rounds and nums is an array of of n
    return name of the player that won the most rounds
    """
    nums.sort()
    winner = False
    Maria = 0
    Ben = 0
    for game in range(x):
        #print(gane#, game+1
        num2 = list(range(1, num[game] + 1))
        turn = 0
        while True:
            change = False
            for i, n in enumerate(num2):
                if n > 1 and isPrime(n):
                    delete(n, num2)
                    change = True
                    turn += 1
                    break
                # print('movement: ', num2)
            if change is False:
                break
        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria == Ben:
        return None
    if Maria > Ben:
        return 'Maria'
    return 'Ben'
