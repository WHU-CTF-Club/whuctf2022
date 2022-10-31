from typing import Tuple, Iterator, Iterable, Optional


def isqrt(n: int) -> int:
    if n == 0:
        return 0
    x = 2 ** ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def is_perfect_square(n: int) -> bool:
    sq_mod256 = (
    1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
    if sq_mod256[n & 0xff] == 0:
        return False

    mt = (
        (9, (1, 1, 0, 0, 1, 0, 0, 1, 0)),
        (5, (1, 1, 0, 0, 1)),
        (7, (1, 1, 1, 0, 1, 0, 0)),
        (13, (1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1)),
        (17, (1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1))
    )
    a = n % (9 * 5 * 7 * 13 * 17)
    if any(t[a % m] == 0 for m, t in mt):
        return False

    return isqrt(n) ** 2 == n


def rational_to_contfrac(x: int, y: int) -> Iterator[int]:
    while y:
        a = x // y
        yield a
        x, y = y, x - a * y


def contfrac_to_rational_iter(contfrac: Iterable[int]) -> Iterator[Tuple[int, int]]:
    n0, d0 = 0, 1
    n1, d1 = 1, 0
    for q in contfrac:
        n = q * n1 + n0
        d = q * d1 + d0
        yield n, d
        n0, d0 = n1, d1
        n1, d1 = n, d


def convergents_from_contfrac(contfrac: Iterable[int]) -> Iterator[Tuple[int, int]]:
    n_, d_ = 1, 0
    for i, (n, d) in enumerate(contfrac_to_rational_iter(contfrac)):
        if i % 2 == 0:
            yield n + n_, d + d_
        else:
            yield n, d
        n_, d_ = n, d


def attack(e: int, n: int) -> Optional[int]:
    f_ = rational_to_contfrac(e, n)
    for k, dg in convergents_from_contfrac(f_):
        edg = e * dg
        phi = edg // k

        x = n - phi + 1
        if x % 2 == 0 and is_perfect_square((x // 2) ** 2 - n):
            g = edg - phi * k
            return dg // g
    return None


n = 12159891771013595814091861874421237585413006358206424082455634832926323194345835046235391486976184552133143329591437178662345730209888807650947037014314586234738789951967938911343052092814756499927753883248059955719123797775174845540111932407799514279901643394655797001273023118185654706240750668406507075848502103921454045082847250889333760714185157556161149008265548298639622072127150613477361173938771419295716135315250527713627525487340817084800006139324924120633
e = 213430058491778540960760024438695043602478507503440169434257192452982713126550143463211986560696072631461520765079924616978705534621300264297689001753491674154760883840909846609800795144777305651106426279144796744740429593882387137111622972666648062225161733733882949499069602323754776638192717411131975351015616681736934546665843369748279104215149629133967947618281790436189006910280067044972668152130796424077182216525946728252724509629272536239924932370930844607
c = 8541318851645545344930243969429110208254565388085191517872761876900839076065069888858514228262306414747946717710205279245215034198965473107281872193488118230733863861616328150112085500328432358109659088247825927281412808489490707737075292549138659022487851598377867926699203115994343831215533955081300618602617070303389413096018280325725402247611090721635884411321425677611344588261611431947370799546061778334598026059784862108006128306767927154553941313401810412831

d = attack(e, n)
print(d)
print(hex(d))

c = 8541318851645545344930243969429110208254565388085191517872761876900839076065069888858514228262306414747946717710205279245215034198965473107281872193488118230733863861616328150112085500328432358109659088247825927281412808489490707737075292549138659022487851598377867926699203115994343831215533955081300618602617070303389413096018280325725402247611090721635884411321425677611344588261611431947370799546061778334598026059784862108006128306767927154553941313401810412831
# m = pow(c, d, n)
plain = bytearray.fromhex(hex(pow(c, d, n))[2:]).decode()
print(plain)

# https://github.com/orisano/owiener/blob/master/owiener.py#L7

