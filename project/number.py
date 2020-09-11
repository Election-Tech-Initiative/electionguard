import random
import hashlib
from typing import (
    Sequence
)

LARGE_PRIME = (int(('''104438888141315250669175271071662438257996424904738378038423348328
3953907971553643537729993126875883902173634017777416360502926082946377942955704498
5420976148418252467735806893983863204397479111608977315510749039672438834271329188
1374801626975452234350528589881677721176191239277291448552115552164104927344620757
8961939840619466145806859275053476560973295158703823395710210329314709715239251736
5523840808458360487786673189314183384224438910259118847234330847012077719019445932
8662497991739135056466263272370300796422984915475619689061525228653308964318490270
6926081744149289517418249153634178342075381874131646013444796894582106870531535803
6662545796026324531037414525697939055519015418561732513850474148403927535855819099
5015804625681054267836812127850996052095762473794291460031064660979266501285839738
1435755902851312071248102599442308951327039250818892493767423329663783709190716162
0235296692173009397831714158082331468230007669177892861540060422814237337064629052
4377485454312723950024587358201266366643058386277816736954760301634424272959224454
4608279405999759391099775667746401633668308698186721172238255007962658564443858927
6348504157753488390520266757856948263869301753031434500465754608438799417919463132
99322976993405829119''').replace('\n', '')))
SMALL_PRIME = pow(2, 256) - 189


def is_prime(num: int, k=5) -> bool:
    """
    implements Miller-Rabin algorithm to test the primality of a number
    :param num: a positive integer
    :param k: the number of iterations, impacting accuracy; the larger the number, the higher accuracy will be.
              set default as 5
    :return: True if it's a prime, False otherwise
    """
    # Corner cases
    if num <= 1 or num == 4:
        return False
    if num <= 3:
        return True

    # Find r such that n = 2^d * r + 1 for some r >= 1
    d = num - 1
    while d % 2 == 0:
        d //= 2

    # Iterate given number of 'k' times
    for i in range(k):
        if not __miller_test(d, num):
            return False

    return True


def __miller_test(d: int, num: int) -> bool:
    """
    find a odd number of d such that num - 1 = d * 2^r
    :param d: an odd number that num - 1 = d * 2^r for r >= 1
    :param num: the number needs to be check against
    :return: True if num is prime, False if it's a composite
    """

    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, num - 4)

    # Compute a^d % n
    x = pow(a, d, num)

    if x == 1 or x == num - 1:
        return True

    # Keep squaring x while one of the following doesn't happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while d != num - 1:
        x = (x * x) % num
        d *= 2

        if x == 1:
            return False
        if x == num - 1:
            return True

    # Return composite
    return False


def equals(a, b) -> bool:
    """
    compares two values and check if their values are equal
    @input: two integers a, b
    @output: True if a, b have same values, False otherwise
    """
    a, b = int(a), int(b)

    return a == b


def is_divisor(a, b) -> bool:
    """
    check if a is a divisor of b
    :param a: a positive integer
    :param b: b positive integer
    :return: True if a is a divisor of b, False otherwise
    """
    a, b = int(a), int(b)

    return a % b == 0


def is_within_range(num, lower_bound: int, upper_bound: int) -> bool:
    """
    check if a number is within a range bounded by upper and lower bound
    :param num: target number needs to be checked against
    :param lower_bound: exclusive lower bound
    :param upper_bound: exclusive upper bound
    :return:  True if number is within this range, False otherwise
    """
    num = int(num)

    if upper_bound < lower_bound:
        raise ValueError("bounds are incorrect")

    return lower_bound < num < upper_bound


def is_within_set_zq(num) -> bool:
    """
    check if a number is within set Zq,
    :param num: target number needs to be checked against
    :return:  True if  0 <= num < q , False otherwise
    """
    num = int(num)

    # exclusive bounds, set lower bound to -1
    return is_within_range(num, 0 - 1, SMALL_PRIME)


def is_within_set_zrp(num) -> bool:
    """
    check if a number is within set Zrp, 0 < num < p and num ^ q mod p = 1
    :param num: target number needs to be checked against
    :return: True if  0 < num < p and num ^ q mod p = 1 , False otherwise
    """
    num = int(num)

    return is_within_range(num, 0, LARGE_PRIME) and equals(
        pow(num, SMALL_PRIME, LARGE_PRIME), 1)


def mod_p(dividend) -> int:
    """
    compute the modulus number by calculating dividend mod p
    :param dividend: dividend, the number in front
    :return: dividend mod p
    """
    dividend = int(dividend)

    return dividend % int(LARGE_PRIME)


def mod_q(dividend) -> int:
    """

    :param dividend:
    :return:
    """
    dividend = int(dividend)

    return dividend % int(SMALL_PRIME)


def multiply(*args, mod_num=1) -> int:
    """

    :param mod_num:
    :return:
    """
    product = 1
    for arg in args:
        if arg >= mod_num:
            arg = arg % mod_num
        if product >= mod_num:
            product = product % mod_num
        product *= arg

    return product % mod_num


def hash_elems(*a):
    """
    main hash function using SHA-256, used in generating data, reference:
    :param a: elements being fed into the hash function
    :return: a hash number of 256 bit
    """
    h = hashlib.sha256()
    h.update("|".encode("utf-8"))

    for x in a:

        if not x:
            # This case captures empty lists and None, nicely guaranteeing that we don't
            # need to do a recursive call if the list is empty. So we need a string to
            # feed in for both of these cases. "None" would be a Python-specific thing,
            # so we'll go with the more JSON-ish "null".
            hash_me = "null"

        elif isinstance(x, str):
            # strings are iterable, so it's important to handle them before the following check
            hash_me = x
        elif isinstance(x, Sequence):
            # The simplest way to deal with lists, tuples, and such are to crunch them recursively.
            hash_me = str(hash_elems(*x))
        else:
            hash_me = str(x)
        h.update((hash_me + "|").encode("utf-8"))

    # Note: the returned value will range from [1,Q), because zeros are bad
    # for some of the nonces. (g^0 == 1, which would be an unhelpful thing
    # to multiply something with, if you were trying to encrypt it.)

    # Also, we don't need the checked version of int_to_q, because the
    # modulo operation here guarantees that we're in bounds.
    # return int_to_q_unchecked(
    #     1 + (int.from_bytes(h.digest(), byteorder="big") % Q_MINUS_ONE)
    # )

    return int.from_bytes(h.digest(), byteorder="big") % (SMALL_PRIME - 1)