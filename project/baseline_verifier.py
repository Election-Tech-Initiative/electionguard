import number
from generator import ParameterGenerator
from interfaces import IVerifier


class BaselineVerifier(IVerifier):
    """
    This class tests that whether the given parameters p, q, r, g equal to expected values. (box 1)
    """

    def __init__(self, param_g: ParameterGenerator):
        super().__init__(param_g)

        # constants
        self.DICT_KEYS = {'cofactor', 'generator', 'large_prime', 'small_prime'}
        self.LARGE_PRIME_EXPECTED = (int(('''104438888141315250669175271071662438257996424904738378038423348328
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
        self.SMALL_PRIME_EXPECTED = pow(2, 256) - 189

    def verify_all_params(self) -> bool:
        """
        verify all parameters including p, q, r, g, inverse g
        :return: True if all parameters are verified to fit in designated equations or have specific values,
                False otherwise
        """
        error = self.initialize_error()

        # check if p and q are the expected values
        if not number.equals(self.large_prime, self.LARGE_PRIME_EXPECTED):
            # if not, use Miller-Rabin algorithm to check the primality of p and q, 5 iterations by default
            if not number.is_prime(self.large_prime):
                error = self.set_error()
                print("Large prime value error. ")

        if not number.equals(self.small_prime, self.SMALL_PRIME_EXPECTED):
            if not number.is_prime(self.small_prime):
                error = self.set_error()
                print("Small prime value error. ")

        # get basic parameters
        cofactor = self.param_g.get_cofactor()

        # check equation p - 1 = qr
        if not number.equals(self.large_prime - 1, self.small_prime * cofactor):
            error = self.set_error()
            print("p - 1 does not equals to r * q.")

        # check q is not a divisor of r
        if number.is_divisor(self.small_prime, cofactor):
            error = self.set_error()
            print("q is a divisor of r.")

        # check 1 < g < p
        if not number.is_within_range(self.generator, 1, self.large_prime):
            error = self.set_error()
            print("g is not in the range of 1 to p. ")

        # check g^q mod p = 1
        if not number.equals(pow(self.generator, self.small_prime, self.large_prime), 1):
            error = self.set_error()
            print("g^q mod p does not equal to 1. ")

        # print out message
        output = "Baseline parameter check"
        if error:
            output += " failure. "
        else:
            output += " success. "
        print(output)

        return not error
