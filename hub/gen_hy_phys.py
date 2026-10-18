"""High-yield NEET Physics, Classes 11-12: original questions on the problem types NEET (and AIPMT before it) asks again and again.

Every numerical answer is computed and wrong options are typical slips. Nothing is copied from past papers.
"""
import math

from .core import table, facts, groups, gen, num_q, Q, fmt, sig, sci, tag

tag("hy")
G = 10


def R(rng, *xs):
    return rng.choice(xs)


def ints(x):
    return str(int(round(x)))


# ---------------------------------------------------------------- p11-01 Units and Measurement
@gen("p11-01", weight=2)
def _rel_err(rng):
    l, dl = R(rng, 10, 20, 25, 50), R(rng, 0.1, 0.2, 0.5)
    t, dt = R(rng, 2, 4, 5), R(rng, 0.01, 0.02, 0.05)
    # g = 4π²L/T²
    e = 100 * (dl / l + 2 * dt / t)
    return num_q(rng, f"In a pendulum experiment L = {l} ± {dl} cm and T = {t} ± {dt} s. The maximum % error in g = 4π²L/T² is:", e, "%",
                 "%g = %L + 2 × %T.", wrongs=[100 * (dl / l + dt / t), 100 * (dl / l - 2 * dt / t), 100 * 2 * (dl / l + dt / t)])


table("p11-01", [
    ("Light year", "Distance"), ("Parsec", "Distance", ["Distance"]), ("Electron volt", "Energy"), ("Kilowatt hour", "Energy", ["Energy"]),
    ("Pascal", "Pressure"), ("Tesla", "Magnetic field"), ("Weber", "Magnetic flux"), ("Henry", "Inductance"), ("Farad", "Capacitance"),
    ("Becquerel", "Activity of a radioactive sample"), ("Dioptre", "Power of a lens"),
], "{} is a unit of:", None, weight=2)
facts("p11-01", [
    "Plane angle and solid angle are dimensionless",
    "Strain has no dimensions",
    "Work and torque have the same dimensions",
    "Impulse and momentum have the same dimensions",
    "The SI unit of luminous intensity is the candela",
    "Planck's constant and angular momentum have the same dimensions",
    "Dimensional analysis cannot find dimensionless constants",
    "The maximum relative error in a product is the sum of the relative errors of the factors",
], [
    "Work and power have the same dimensions",
    "Strain has the dimensions of pressure",
    "The SI unit of temperature is the degree Celsius",
    "Dimensional analysis gives the value of 2π in T = 2π√(l/g)",
    "Force and energy have the same dimensions",
    "Light year is a unit of time",
    "Planck's constant has the dimensions of energy",
    "Stress and strain have the same dimensions",
], "units and dimensions")

# ---------------------------------------------------------------- p11-02 Motion in a Straight Line
@gen("p11-02", weight=2)
def _nth_second(rng):
    u, a, n = R(rng, 0, 2, 4, 10), R(rng, 2, 4, 6, 10), R(rng, 3, 4, 5, 10)
    s = u + a * (2 * n - 1) / 2
    return num_q(rng, f"A body starts with {u} m/s and accelerates uniformly at {a} m/s². The distance covered in the {n}th second is:",
                 s, " m", "sₙ = u + a(2n - 1)/2.", wrongs=[u * n + a * n * n / 2, u + a * n / 2, u + a * (2 * n + 1) / 2])


@gen("p11-02", weight=2)
def _ratio_galileo(rng):
    n = R(rng, 3, 4, 5)
    seq = ":".join(str(2 * k - 1) for k in range(1, n + 1))
    return Q(f"A body falls freely from rest. The distances covered in the first {n} equal successive seconds are in the ratio:", seq,
             [":".join(str(k) for k in range(1, n + 1)), ":".join(str(k * k) for k in range(1, n + 1)), ":".join(str(2 * k) for k in range(1, n + 1))],
             "Galileo's law of odd numbers.")


@gen("p11-02", weight=2)
def _up_down(rng):
    u = R(rng, 10, 20, 30, 40, 50)
    kind = rng.choice(["h", "t"])
    if kind == "h":
        return num_q(rng, f"A ball is thrown vertically up at {u} m/s (g = 10 m/s²). The maximum height reached is:", u * u / 20, " m", "H = u²/2g.",
                     wrongs=[u * u / 10, u / 10, u * u / 40])
    return num_q(rng, f"A ball is thrown vertically up at {u} m/s (g = 10 m/s²). It returns to the thrower after:", 2 * u / 10, " s", "T = 2u/g.",
                 wrongs=[u / 10, 4 * u / 10, u * u / 20])


@gen("p11-02")
def _relative(rng):
    a, b = R(rng, 36, 54, 72, 90), R(rng, 18, 36, 54)
    same = rng.random() < 0.5
    rel = abs(a - b) if same else a + b
    if same and a == b:
        return None
    return num_q(rng, f"Two trains move {'in the same direction' if same else 'towards each other'} at {a} km/h and {b} km/h. Their relative speed is:",
                 rel, " km/h", "Same direction: subtract; opposite: add.", wrongs=[a + b if same else abs(a - b) or 1, (a + b) / 2, a * b / (a + b)])


# ---------------------------------------------------------------- p11-03 Motion in a Plane
@gen("p11-03", weight=3)
def _projectile(rng):
    u = R(rng, 10, 20, 30, 40, 50)
    th = R(rng, 30, 45, 60)
    s, c = math.sin(math.radians(th)), math.cos(math.radians(th))
    kind = rng.choice(["R", "H", "T"])
    if kind == "R":
        return num_q(rng, f"A projectile is fired at {u} m/s at {th}° to the horizontal (g = 10 m/s²). Its range is:", u * u * 2 * s * c / G, " m",
                     "R = u² sin2θ/g.", wrongs=[u * u * s / G, u * u / G, u * u * s * s / (2 * G)])
    if kind == "H":
        return num_q(rng, f"A projectile is fired at {u} m/s at {th}° to the horizontal (g = 10 m/s²). Its maximum height is:", u * u * s * s / (2 * G), " m",
                     "H = u² sin²θ/2g.", wrongs=[u * u * s / (2 * G), u * u * s * s / G, u * u * 2 * s * c / G])
    return num_q(rng, f"A projectile is fired at {u} m/s at {th}° to the horizontal (g = 10 m/s²). Its time of flight is:", 2 * u * s / G, " s",
                 "T = 2u sinθ/g.", wrongs=[u * s / G, 2 * u * c / G, 2 * u / G])


@gen("p11-03", weight=2)
def _river(rng):
    w, vb, vr = R(rng, 100, 200, 300, 400), R(rng, 3, 4, 5), R(rng, 1, 2, 3)
    if vr >= vb:
        return None
    kind = rng.choice(["short time", "drift"])
    t = w / vb
    if kind == "short time":
        return num_q(rng, f"A swimmer crosses a {w} m wide river at {vb} m/s relative to water, heading straight across. The river flows at {vr} m/s. Time to cross is:",
                     t, " s", "t = width / speed across.", wrongs=[w / math.sqrt(vb * vb - vr * vr), w / (vb + vr), w / vr])
    return num_q(rng, f"A swimmer crosses a {w} m wide river at {vb} m/s relative to water, heading straight across. The river flows at {vr} m/s. Drift downstream is:",
                 vr * t, " m", "drift = river speed × crossing time.", wrongs=[vb * t, vr * w / (vb + vr), w])


@gen("p11-03")
def _vec(rng):
    a, b = R(rng, 3, 5, 6, 8), R(rng, 4, 12, 8, 6)
    th = R(rng, 0, 60, 90, 120, 180)
    r = math.sqrt(a * a + b * b + 2 * a * b * math.cos(math.radians(th)))
    return num_q(rng, f"Two forces of {a} N and {b} N act at an angle of {th}°. The magnitude of the resultant is:", r, " N",
                 "R = √(A² + B² + 2AB cosθ).", wrongs=[a + b, abs(a - b) or 1, math.sqrt(a * a + b * b) if th != 90 else a + b - 1])


# ---------------------------------------------------------------- p11-04 Laws of Motion
@gen("p11-04", weight=3)
def _atwood(rng):
    m1, m2 = R(rng, 2, 3, 4, 5, 6), R(rng, 1, 2, 3)
    if m1 <= m2:
        return None
    kind = rng.choice(["a", "T"])
    a = (m1 - m2) * G / (m1 + m2)
    if kind == "a":
        return num_q(rng, f"Masses {m1} kg and {m2} kg hang over a light frictionless pulley (g = 10 m/s²). Their acceleration is:", a, " m/s²",
                     "a = (m1 - m2)g/(m1 + m2).", wrongs=[(m1 - m2) * G / m1, (m1 + m2) * G / (m1 - m2), G])
    T = 2 * m1 * m2 * G / (m1 + m2)
    return num_q(rng, f"Masses {m1} kg and {m2} kg hang over a light frictionless pulley (g = 10 m/s²). The tension in the string is:", T, " N",
                 "T = 2m1m2g/(m1 + m2).", wrongs=[m1 * m2 * G / (m1 + m2), m1 * G, (m1 - m2) * G])


@gen("p11-04", weight=2)
def _lift(rng):
    m, a = R(rng, 40, 50, 60, 70), R(rng, 1, 2, 2.5, 5)
    up = rng.random() < 0.5
    w = m * (G + a) if up else m * (G - a)
    return num_q(rng, f"A {m} kg person stands on a scale in a lift accelerating {'upward' if up else 'downward'} at {fmt(a)} m/s² (g = 10 m/s²). The scale reads:",
                 w, " N", "N = m(g ± a).", wrongs=[m * (G - a) if up else m * (G + a), m * G, m * a])


@gen("p11-04", weight=2)
def _friction(rng):
    m, mu, f = R(rng, 2, 4, 5, 10), R(rng, 0.1, 0.2, 0.25, 0.4, 0.5), R(rng, 20, 30, 40, 50)
    fr = mu * m * G
    if f <= fr:
        return Q(f"A {m} kg block rests on a floor (μs = μk = {mu}, g = 10 m/s²). A horizontal force of {f} N acts on it. The friction force is:",
                 f"{fmt(f)} N", [f"{fmt(fr)} N", "0 N", f"{fmt(f + fr)} N"], "Static friction equals the applied force until it reaches its limit.")
    return num_q(rng, f"A {m} kg block on a floor (μk = {mu}, g = 10 m/s²) is pulled horizontally with {f} N. Its acceleration is:", (f - fr) / m, " m/s²",
                 "a = (F - μmg)/m.", wrongs=[f / m, (f + fr) / m, fr / m])


@gen("p11-04", weight=2)
def _banking(rng):
    r, v = R(rng, 20, 40, 50, 90, 100), R(rng, 10, 15, 20, 30)
    tan = v * v / (r * G)
    return num_q(rng, f"A road of radius {r} m is banked for a speed of {v} m/s with no friction needed (g = 10 m/s²). tanθ equals:", tan, "",
                 "tanθ = v²/(rg).", wrongs=[v / (r * G), r * G / (v * v), v * v / r])


@gen("p11-04")
def _impulse(rng):
    m, v = R(rng, 0.1, 0.15, 0.2, 0.5), R(rng, 10, 20, 30)
    back = rng.random() < 0.5
    j = m * v * (2 if back else 1)
    return num_q(rng, f"A {fmt(m)} kg ball moving at {v} m/s {'rebounds with the same speed from a wall' if back else 'is stopped by a wall'}. The impulse on it is:",
                 j, " N s", "Impulse = change in momentum.", wrongs=[m * v * (1 if back else 2), 0.5 * m * v * v, m * v * 4])


# ---------------------------------------------------------------- p11-05 Work, Energy and Power
@gen("p11-05", weight=2)
def _ke_mom(rng):
    f = R(rng, 2, 3, 4, 9, 16)
    kind = rng.choice(["p_from_k", "k_from_p"])
    if kind == "p_from_k":
        return num_q(rng, f"The kinetic energy of a body is made {f} times. Its momentum becomes how many times?", math.sqrt(f), " times",
                     "p = √(2mK).", wrongs=[f, f * f, f / 2])
    return num_q(rng, f"The momentum of a body is made {f} times. Its kinetic energy becomes how many times?", f * f, " times",
                 "K = p²/2m.", wrongs=[f, math.sqrt(f), 2 * f])


@gen("p11-05", weight=2)
def _spring(rng):
    k, x = R(rng, 100, 200, 400, 800), R(rng, 0.05, 0.1, 0.2)
    return num_q(rng, f"A spring of constant {k} N/m is compressed by {fmt(x)} m. The energy stored is:", 0.5 * k * x * x, " J", "U = ½kx².",
                 wrongs=[k * x * x, k * x, 0.5 * k * x])


@gen("p11-05", weight=2)
def _collision(rng):
    m1, m2, u = R(rng, 1, 2, 3, 4), R(rng, 1, 2, 3, 6), R(rng, 4, 6, 10, 12)
    kind = rng.choice(["inelastic", "elastic"])
    if kind == "inelastic":
        v = m1 * u / (m1 + m2)
        return num_q(rng, f"A {m1} kg body moving at {u} m/s sticks to a {m2} kg body at rest. Their common speed is:", v, " m/s", "Momentum conservation.",
                     wrongs=[u * m2 / (m1 + m2), u / 2, m1 * u / m2])
    v1 = (m1 - m2) * u / (m1 + m2)
    return num_q(rng, f"A {m1} kg ball at {u} m/s hits a {m2} kg ball at rest head-on, elastically. The second ball moves off at:", 2 * m1 * u / (m1 + m2), " m/s",
                 "v2 = 2m1u/(m1 + m2).", wrongs=[m1 * u / (m1 + m2), u, abs(v1) or u / 2])


@gen("p11-05")
def _power(rng):
    m, h, t = R(rng, 50, 60, 100, 200), R(rng, 5, 10, 20), R(rng, 10, 20, 40)
    return num_q(rng, f"A pump lifts {m} kg of water through {h} m in {t} s (g = 10 m/s²). The power needed is:", m * G * h / t, " W", "P = mgh/t.",
                 wrongs=[m * h / t, m * G * h * t, m * G * h])


@gen("p11-05")
def _vcircle(rng):
    r = R(rng, 0.5, 1, 1.6, 2.5, 4.9)
    return num_q(rng, f"The minimum speed at the lowest point for a bob on a string of length {fmt(r)} m to complete a vertical circle (g = 10 m/s²) is:",
                 math.sqrt(5 * G * r), " m/s", "v = √(5gr).", wrongs=[math.sqrt(G * r), math.sqrt(2 * G * r), math.sqrt(3 * G * r)])


# ---------------------------------------------------------------- p11-06 System of Particles and Rotational Motion
table("p11-06", [
    ("ring about its central axis", "MR²"), ("disc about its central axis", "MR²/2"), ("solid sphere about a diameter", "2MR²/5"),
    ("hollow sphere about a diameter", "2MR²/3"), ("thin rod about its centre, perpendicular to length", "ML²/12"),
    ("thin rod about one end, perpendicular to length", "ML²/3"), ("ring about a diameter", "MR²/2"),
], "The moment of inertia of a {} is:", None, weight=3)


@gen("p11-06", weight=2)
def _rolling(rng):
    body, k2 = rng.choice([("ring", 1), ("disc", 0.5), ("solid sphere", 0.4), ("hollow sphere", 2 / 3), ("solid cylinder", 0.5)])
    kind = rng.choice(["frac", "acc"])
    if kind == "frac":
        f = k2 / (1 + k2)
        return num_q(rng, f"For a {body} rolling without slipping, the fraction of its kinetic energy that is rotational is:", f, "",
                     f"K_rot/K = (k²/R²)/(1 + k²/R²), k²/R² = {fmt(k2)}.", wrongs=[1 / (1 + k2), k2, 0.5 if f != 0.5 else 0.25], form=lambda x: fmt(x, 3))
    th = 30
    a = G * 0.5 / (1 + k2)
    return num_q(rng, f"A {body} rolls without slipping down a {th}° incline (g = 10 m/s²). Its acceleration is:", a, " m/s²",
                 "a = g sinθ/(1 + k²/R²).", wrongs=[G * 0.5, G * 0.5 / (1 + 1 / k2) if k2 else 1, G / (1 + k2)])


@gen("p11-06", weight=2)
def _ang_mom(rng):
    i1, w1, f = R(rng, 2, 4, 5, 10), R(rng, 10, 20, 30), R(rng, 2, 4, 0.5)
    return num_q(rng, f"A skater spinning at {w1} rad/s pulls in her arms so that her moment of inertia becomes {fmt(f)} times. Her new angular speed is:",
                 w1 / f, " rad/s", "Iω is conserved.", wrongs=[w1 * f, w1 / (f * f), w1])


@gen("p11-06")
def _com(rng):
    m1, m2, d = R(rng, 1, 2, 3, 4), R(rng, 1, 2, 3, 6), R(rng, 1, 2, 3, 4)
    if m1 == m2:
        return None
    return num_q(rng, f"Masses {m1} kg and {m2} kg are {d} m apart. The centre of mass is how far from the {m1} kg mass?", m2 * d / (m1 + m2), " m",
                 "x = m2 d/(m1 + m2).", wrongs=[m1 * d / (m1 + m2), d / 2, m2 * d / m1])


# ---------------------------------------------------------------- p11-07 Gravitation
@gen("p11-07", weight=3)
def _g_var(rng):
    kind = rng.choice(["height", "depth", "radius"])
    if kind == "height":
        k = R(rng, 1, 2, 3)
        return Q(f"At a height h = {'R' if k == 1 else f'{k}R'} above Earth's surface (R = Earth's radius), g becomes:", f"g/{(k + 1) ** 2}",
                 [f"g/{k + 1}", f"g/{(k + 1) ** 2 * 2}", f"g/{(k + 1) ** 3}", f"g/{k + 2}"], "g' = g R²/(R + h)².")
    if kind == "depth":
        f = R(rng, 3, 4, 5)
        return Q(f"At a depth of R/{f} below Earth's surface, g becomes:", f"{f - 1}g/{f}", [f"g/{f}", f"g/{f * f}", f"{f}g/{f + 1}", "g"],
                 "g' = g(1 - d/R).")
    f = R(rng, 2, 3, 4)
    return Q(f"If Earth's radius shrinks to 1/{f} of its value with the same mass, g at the surface becomes:", f"{f * f}g",
             [f"{f}g", f"g/{f * f}", f"g/{f}"], "g = GM/R².")


@gen("p11-07", weight=2)
def _escape(rng):
    f = R(rng, 2, 3, 4, 9)
    kind = rng.choice(["mass", "radius"])
    if kind == "mass":
        return num_q(rng, f"A planet has {f} times Earth's mass and the same radius. Its escape speed is how many times Earth's?", math.sqrt(f), " times",
                     "vₑ = √(2GM/R).", wrongs=[f, f * f, f / 2])
    return num_q(rng, f"A planet has the same mass as Earth but {f} times its radius. Its escape speed is how many times Earth's?", 1 / math.sqrt(f), " times",
                 "vₑ ∝ 1/√R.", wrongs=[math.sqrt(f), 1 / f, f], form=lambda x: fmt(x, 3))


@gen("p11-07", weight=2)
def _kepler(rng):
    f = R(rng, 4, 9, 16)
    return num_q(rng, f"A satellite's orbital radius is made {f} times. Its period becomes how many times?", f ** 1.5, " times", "T² ∝ r³.",
                 wrongs=[f, f * f, math.sqrt(f)])


facts("p11-07", [
    "Escape speed from Earth is about 11.2 km/s",
    "Orbital speed close to Earth's surface is about 7.9 km/s",
    "A geostationary satellite has a period of 24 hours",
    "Kepler's second law follows from conservation of angular momentum",
    "The total energy of a satellite in orbit is negative",
    "g is zero at the centre of the Earth",
    "Weight of a body is zero in a freely falling lift",
    "Escape speed does not depend on the mass of the escaping body",
], [
    "Escape speed depends on the mass of the escaping body",
    "g is maximum at the centre of the Earth",
    "A geostationary satellite has a period of 12 hours",
    "The total energy of a bound satellite is positive",
    "Kepler's second law follows from conservation of energy only",
    "Orbital speed is √2 times the escape speed",
    "Value of g is greater at the equator than at the poles",
    "Gravitational force can be shielded by a lead plate",
], "gravitation")

# ---------------------------------------------------------------- p11-08 Mechanical Properties of Solids
@gen("p11-08", weight=3)
def _young(rng):
    f = R(rng, 100, 200, 500, 1000)
    a_mm2 = R(rng, 1, 2, 4, 5)
    l = R(rng, 1, 2, 4)
    y = R(rng, 1, 2) * 1e11
    dl = f * l / (a_mm2 * 1e-6 * y)
    return num_q(rng, f"A wire of length {l} m and area {a_mm2} mm² (Y = {sci(y)} N/m²) carries a load of {f} N. Its extension is:", dl * 1000, " mm",
                 "ΔL = FL/(AY).", wrongs=[dl * 100, dl * 1e4, dl * 1000 * 2])


@gen("p11-08", weight=2)
def _wire_scale(rng):
    lf, rf = R(rng, 2, 3, 0.5), R(rng, 2, 0.5, 3)
    ext = lf / (rf * rf)
    return num_q(rng, f"A wire is replaced by one of the same material with {fmt(lf)} times the length and {fmt(rf)} times the radius. Under the same load, the extension becomes how many times?",
                 ext, " times", "ΔL ∝ L/r².", wrongs=[lf / rf, lf * rf * rf, lf * rf])


@gen("p11-08")
def _energy_density(rng):
    stress, y = R(rng, 1e7, 2e7, 5e7, 1e8), R(rng, 1e11, 2e11)
    return num_q(rng, f"A wire under a stress of {sci(stress)} N/m² has Y = {sci(y)} N/m². Elastic energy per unit volume is:", stress ** 2 / (2 * y), " J/m³",
                 "u = stress²/(2Y).", wrongs=[stress ** 2 / y, stress / (2 * y), stress * y], form=lambda x: sci(x))


facts("p11-08", [
    "Steel is more elastic than rubber",
    "Bulk modulus of an ideal gas at constant temperature equals its pressure",
    "Poisson's ratio has no units",
    "Young's modulus of a perfectly rigid body is infinite",
    "Compressibility is the reciprocal of bulk modulus",
    "Beyond the yield point the wire does not return to its original length",
], [
    "Rubber is more elastic than steel",
    "Poisson's ratio has the unit N/m²",
    "Young's modulus depends on the length of the wire",
    "Liquids have a shear modulus",
    "Bulk modulus of an ideal gas at constant temperature is zero",
    "Stress has the same unit as strain",
], "elasticity")

# ---------------------------------------------------------------- p11-09 Mechanical Properties of Fluids
@gen("p11-09", weight=2)
def _terminal(rng):
    f = R(rng, 2, 3, 4, 0.5)
    return num_q(rng, f"The radius of a small sphere falling through a viscous liquid is made {fmt(f)} times. Its terminal speed becomes how many times?",
                 f * f, " times", "vₜ ∝ r².", wrongs=[f, f ** 3, math.sqrt(f)])


@gen("p11-09", weight=2)
def _drops(rng):
    n = R(rng, 8, 27, 64, 125)
    k = round(n ** (1 / 3))
    return Q(f"{n} identical small drops coalesce into one big drop. The ratio of the big drop's radius to a small drop's radius is:", str(k),
             [str(x) for x in (n, k * k, n // 2, k + 1)], f"Volume conserved: R = {n}^(1/3) r = {k}r.")


@gen("p11-09", weight=2)
def _cont(rng):
    a1, a2, v1 = R(rng, 4, 8, 10, 20), R(rng, 1, 2, 5), R(rng, 1, 2, 3)
    if a2 >= a1:
        return None
    return num_q(rng, f"Water flows at {v1} m/s through a pipe of area {a1} cm² that narrows to {a2} cm². The speed in the narrow part is:", v1 * a1 / a2, " m/s",
                 "A1v1 = A2v2.", wrongs=[v1 * a2 / a1, v1 * (a1 / a2) ** 2, v1 + a1 - a2])


@gen("p11-09")
def _capillary(rng):
    f = R(rng, 2, 3, 4, 0.5)
    return num_q(rng, f"The radius of a capillary tube is made {fmt(f)} times. The height of water rise becomes how many times?", 1 / f, " times",
                 "h ∝ 1/r.", wrongs=[f, 1 / (f * f), f * f], form=lambda x: fmt(x, 3))


@gen("p11-09")
def _excess_pressure(rng):
    t, r = R(rng, 0.03, 0.05, 0.07), R(rng, 1, 2, 5)
    bubble = rng.random() < 0.5
    p = (4 if bubble else 2) * t / (r * 1e-3)
    return num_q(rng, f"The excess pressure inside a {'soap bubble' if bubble else 'liquid drop'} of radius {r} mm with surface tension {t} N/m is:", p, " Pa",
                 "Drop: 2T/r; soap bubble (two surfaces): 4T/r.", wrongs=[(2 if bubble else 4) * t / (r * 1e-3), t / (r * 1e-3), p * 1000])


facts("p11-09", [
    "Bernoulli's principle is a statement of conservation of energy for a flowing fluid",
    "Viscosity of liquids decreases with rise in temperature",
    "Viscosity of gases increases with rise in temperature",
    "Surface tension decreases with rise in temperature",
    "Pascal's law is the basis of the hydraulic lift",
    "Flow is streamlined when the Reynolds number is low",
    "Angle of contact for water on clean glass is acute",
    "Mercury shows a depression in a glass capillary",
], [
    "Viscosity of liquids increases with rise in temperature",
    "Surface tension increases with rise in temperature",
    "Bernoulli's principle is a statement of conservation of momentum",
    "Turbulence sets in at low Reynolds number",
    "Mercury rises in a glass capillary",
    "Angle of contact of mercury with glass is acute",
    "Detergents increase the surface tension of water",
    "Terminal velocity is proportional to the radius of the sphere",
], "fluids")

# ---------------------------------------------------------------- p11-10 Thermal Properties of Matter
@gen("p11-10", weight=2)
def _mix(rng):
    m1, t1, m2, t2 = R(rng, 100, 200, 300), R(rng, 80, 90, 60), R(rng, 100, 200, 400), R(rng, 10, 20, 30)
    t = (m1 * t1 + m2 * t2) / (m1 + m2)
    return num_q(rng, f"{m1} g of water at {t1} °C is mixed with {m2} g of water at {t2} °C. The final temperature is:", t, " °C",
                 "Heat lost = heat gained.", wrongs=[(t1 + t2) / 2, (m1 * t2 + m2 * t1) / (m1 + m2), t1 - t2])


@gen("p11-10", weight=2)
def _ice(rng):
    m = R(rng, 10, 20, 50, 100)
    t = R(rng, 0, 20, 50)
    q = m * 80 + m * t
    return num_q(rng, f"The heat needed to turn {m} g of ice at 0 °C into water at {t} °C is (L = 80 cal/g, c = 1 cal/g °C):", q, " cal",
                 "Q = mL + mcΔT.", wrongs=[m * t, m * 80, m * 540 + m * t] if t else [m * 540, m * 40, m * 160])


@gen("p11-10", weight=2)
def _expansion(rng):
    kind = rng.choice(["area", "volume"])
    return Q(f"For an isotropic solid with linear expansivity α, the {kind} expansivity is:", "2α" if kind == "area" else "3α",
             ["α", "2α", "3α", "α/3", "α²"], "β = 2α, γ = 3α.")


@gen("p11-10")
def _wien(rng):
    t = R(rng, 2000, 3000, 5000, 6000)
    return num_q(rng, f"A black body is at {t} K. Using Wien's constant b = 2.9 × 10^-3 m K, λmax is:", 2.9e-3 / t * 1e9, " nm", "λmax = b/T.",
                 wrongs=[2.9e-3 * t, 2.9e-3 / t * 1e6, 2.9e-3 / t * 1e10])


@gen("p11-10")
def _stefan(rng):
    f = R(rng, 2, 3, 4)
    return num_q(rng, f"The absolute temperature of a black body is made {f} times. The power it radiates becomes how many times?", f ** 4, " times",
                 "P ∝ T⁴.", wrongs=[f * f, f ** 3, f], form=ints)


facts("p11-10", [
    "Water has its maximum density at 4 °C",
    "Newton's law of cooling holds for small temperature differences",
    "Good absorbers of radiation are good emitters",
    "The latent heat of vaporisation of water is larger than its latent heat of fusion",
    "Convection is not possible in a vacuum",
    "Thermal conductivity of a metal is high because of free electrons",
], [
    "Water has its maximum density at 0 °C",
    "Good absorbers are poor emitters",
    "Heat transfer by radiation needs a medium",
    "Latent heat of fusion of ice is more than latent heat of vaporisation of water",
    "Stefan's law says power is proportional to T²",
    "Wien's law says λmax is proportional to T",
], "thermal properties")

# ---------------------------------------------------------------- p11-11 Thermodynamics
@gen("p11-11", weight=3)
def _carnot(rng):
    th, tc = R(rng, 400, 500, 600, 800, 1000), R(rng, 300, 250, 200)
    if tc >= th:
        return None
    kind = rng.choice(["eff", "cop"])
    if kind == "eff":
        return num_q(rng, f"A Carnot engine works between {th} K and {tc} K. Its efficiency is:", 100 * (1 - tc / th), "%", "η = 1 - T₂/T₁.",
                     wrongs=[100 * tc / th, 100 * (th - tc) / tc, 100 * (1 - th / (th + tc))])
    return num_q(rng, f"A Carnot refrigerator works between {th} K (outside) and {tc} K (inside). Its coefficient of performance is:", tc / (th - tc), "",
                 "β = T₂/(T₁ - T₂).", wrongs=[th / (th - tc), (th - tc) / tc, tc / th])


@gen("p11-11", weight=2)
def _first_law(rng):
    q, w = R(rng, 100, 200, 300, 500), R(rng, 40, 50, 75, 150)
    return num_q(rng, f"A gas absorbs {q} J of heat and does {w} J of work. The change in its internal energy is:", q - w, " J", "ΔU = Q - W.",
                 wrongs=[q + w, w - q, q])


@gen("p11-11", weight=2)
def _process_work(rng):
    kind = rng.choice(["isochoric", "isobaric", "cyclic"])
    if kind == "isochoric":
        return Q("In an isochoric process the work done by the gas is:", "Zero", ["PΔV", "nRT ln(V2/V1)", "Equal to the heat supplied"],
                 "Volume does not change, so W = 0 and Q = ΔU.")
    if kind == "cyclic":
        return Q("In a cyclic process the change in internal energy is:", "Zero", ["Equal to the work done", "Equal to the heat absorbed", "Always positive"],
                 "Internal energy is a state function; it returns to its initial value.")
    p, v1, v2 = R(rng, 1e5, 2e5), R(rng, 1, 2), R(rng, 3, 4, 5)
    return num_q(rng, f"A gas expands at a constant pressure of {sci(p)} Pa from {v1} L to {v2} L. The work done by it is:", p * (v2 - v1) * 1e-3, " J",
                 "W = PΔV.", wrongs=[p * (v2 - v1), p * v2 * 1e-3, p * (v2 - v1) * 1e-6])


facts("p11-11", [
    "In an adiabatic process no heat is exchanged",
    "In an isothermal process for an ideal gas ΔU = 0",
    "PV^γ is constant in a reversible adiabatic process",
    "The slope of an adiabatic curve is γ times that of an isothermal curve at the same point",
    "No engine working between two temperatures can be more efficient than a Carnot engine",
    "Cp - Cv = R for one mole of an ideal gas",
], [
    "In an isothermal process no heat is exchanged",
    "A Carnot engine can have 100% efficiency at finite temperatures",
    "Cp - Cv = 2R for one mole of an ideal gas",
    "In an adiabatic process the temperature stays constant",
    "The slope of an isothermal curve is steeper than an adiabatic one",
    "Heat flows on its own from a colder to a hotter body",
], "thermodynamics")

# ---------------------------------------------------------------- p11-12 Kinetic Theory
@gen("p11-12", weight=3)
def _vrms(rng):
    kind = rng.choice(["temp", "mass"])
    if kind == "temp":
        t1, f = R(rng, 300, 200, 400), R(rng, 4, 9, 2)
        return num_q(rng, f"The absolute temperature of a gas is made {f} times. Its rms speed becomes how many times?", math.sqrt(f), " times",
                     "vrms ∝ √T.", wrongs=[f, f * f, f / 2])
    g1, m1, g2, m2 = rng.choice([("H2", 2, "O2", 32), ("He", 4, "CH4", 16), ("H2", 2, "He", 4), ("O2", 32, "H2", 2)])
    return num_q(rng, f"At the same temperature, the ratio of rms speeds of {g1} to {g2} is:", math.sqrt(m2 / m1), "", "vrms ∝ 1/√M.",
                 wrongs=[m2 / m1, math.sqrt(m1 / m2), m1 / m2])


@gen("p11-12", weight=2)
def _gamma(rng):
    gas, f = rng.choice([("monatomic", 3), ("rigid diatomic", 5), ("rigid non-linear polyatomic", 6)])
    ask = rng.choice(["γ", "Cv", "Cp"])
    val = {"γ": f"{f + 2}/{f}", "Cv": f"{f}R/2", "Cp": f"{f + 2}R/2"}[ask]
    pool = {"γ": ["5/3", "7/5", "8/6", "4/3", "9/7"], "Cv": ["3R/2", "5R/2", "6R/2", "7R/2"], "Cp": ["5R/2", "7R/2", "8R/2", "3R/2"]}[ask]
    tidy = {"8/6": "4/3", "6R/2": "3R", "8R/2": "4R"}
    val = tidy.get(val, val)
    pool = list(dict.fromkeys(tidy.get(p, p) for p in pool))
    return Q(f"For a {gas} ideal gas ({f} degrees of freedom), {ask} is:", val, [p for p in pool if p != val],
             "Cv = fR/2, Cp = Cv + R, γ = Cp/Cv = 1 + 2/f.")


@gen("p11-12", weight=2)
def _mixture_cv(rng):
    n1, n2 = R(rng, 1, 2, 3), R(rng, 1, 2, 3)
    cv = (n1 * 1.5 + n2 * 2.5) / (n1 + n2)
    return Q(f"{n1} mol of a monatomic gas is mixed with {n2} mol of a diatomic gas. The Cv of the mixture is:", f"{fmt(cv, 3)}R",
             [f"{fmt(x, 3)}R" for x in (2, 1.5, 2.5, (n1 * 2.5 + n2 * 1.5) / (n1 + n2), 4)], "Cv = (n1Cv1 + n2Cv2)/(n1 + n2).")


facts("p11-12", [
    "The average kinetic energy of a gas molecule depends only on temperature",
    "Each degree of freedom has energy ½kT on average",
    "Mean free path decreases as the gas density increases",
    "A diatomic molecule has 5 degrees of freedom at room temperature",
    "Pressure of an ideal gas is (1/3)ρv²rms",
    "At absolute zero the molecular motion of an ideal gas would stop",
], [
    "The average kinetic energy of a gas molecule depends on its mass",
    "A monatomic gas has 5 degrees of freedom",
    "Mean free path increases with gas density",
    "Each degree of freedom has energy kT on average",
    "Real gases follow the ideal gas law at high pressure and low temperature",
    "The rms speed is independent of temperature",
], "kinetic theory")

# ---------------------------------------------------------------- p11-13 Oscillations
@gen("p11-13", weight=3)
def _shm(rng):
    a, w = R(rng, 2, 4, 5, 10), R(rng, 2, 3, 5, 10)
    kind = rng.choice(["vmax", "amax", "vx"])
    if kind == "vmax":
        return num_q(rng, f"A particle in SHM has amplitude {a} cm and angular frequency {w} rad/s. Its maximum speed is:", a * w, " cm/s", "vmax = Aω.",
                     wrongs=[a * w * w, a / w, a + w])
    if kind == "amax":
        return num_q(rng, f"A particle in SHM has amplitude {a} cm and angular frequency {w} rad/s. Its maximum acceleration is:", a * w * w, " cm/s²",
                     "amax = Aω².", wrongs=[a * w, a * a * w, a / (w * w)])
    x = a / 2
    return num_q(rng, f"A particle in SHM has amplitude {a} cm and angular frequency {w} rad/s. Its speed at x = {fmt(x)} cm is:", w * math.sqrt(a * a - x * x),
                 " cm/s", "v = ω√(A² - x²).", wrongs=[w * x, w * a, w * math.sqrt(a * a + x * x)])


@gen("p11-13", weight=2)
def _period_scale(rng):
    kind = rng.choice(["pend", "spring", "series"])
    f = R(rng, 4, 9, 16, 2)
    if kind == "pend":
        return num_q(rng, f"The length of a simple pendulum is made {f} times. Its period becomes how many times?", math.sqrt(f), " times", "T ∝ √L.",
                     wrongs=[f, f * f, 1 / math.sqrt(f)])
    if kind == "spring":
        return num_q(rng, f"The mass on a spring is made {f} times. Its period becomes how many times?", math.sqrt(f), " times", "T = 2π√(m/k).",
                     wrongs=[f, 1 / math.sqrt(f), f * f])
    return Q("A spring is cut into two equal halves and one half is used. Its spring constant becomes:", "2k", ["k/2", "4k", "k"],
             "k ∝ 1/length.")


@gen("p11-13")
def _energy_frac(rng):
    frac, name = rng.choice([(0.5, "half"), (1 / 3, "one-third"), (0.25, "one-quarter")])
    ke = 1 - frac ** 2
    return num_q(rng, f"In SHM, at a displacement of {name} of the amplitude, the fraction of the total energy that is kinetic is:", ke, "",
                 "K/E = 1 - x²/A².", wrongs=[frac ** 2, frac, 1 - frac], form=lambda x: fmt(x, 3))


facts("p11-13", [
    "In SHM acceleration is proportional to displacement and opposite to it",
    "The period of a simple pendulum does not depend on the mass of the bob",
    "In SHM the total mechanical energy stays constant",
    "Speed is maximum at the mean position",
    "Resonance happens when the driving frequency equals the natural frequency",
    "A seconds pendulum has a period of 2 s",
], [
    "In SHM acceleration is maximum at the mean position",
    "A seconds pendulum has a period of 1 s",
    "The period of a pendulum depends on the mass of the bob",
    "Speed is maximum at the extreme positions",
    "Kinetic energy in SHM is constant",
    "Damping increases the amplitude of oscillation",
], "oscillations")

# ---------------------------------------------------------------- p11-14 Waves
@gen("p11-14", weight=3)
def _pipes(rng):
    l = R(rng, 0.25, 0.5, 0.85, 1, 1.7)
    v = 340
    kind = rng.choice(["open", "closed"])
    if kind == "open":
        return num_q(rng, f"The fundamental frequency of an open pipe of length {fmt(l)} m (speed of sound 340 m/s) is:", v / (2 * l), " Hz", "f = v/2L.",
                     wrongs=[v / (4 * l), v / l, 3 * v / (4 * l)])
    return num_q(rng, f"The fundamental frequency of a pipe closed at one end of length {fmt(l)} m (speed of sound 340 m/s) is:", v / (4 * l), " Hz", "f = v/4L.",
                 wrongs=[v / (2 * l), v / l, 3 * v / (4 * l)])


@gen("p11-14", weight=2)
def _string(rng):
    t, mu, l = R(rng, 100, 200, 400, 900), R(rng, 0.01, 0.04, 0.1), R(rng, 0.5, 1, 2)
    v = math.sqrt(t / mu)
    kind = rng.choice(["v", "f"])
    if kind == "v":
        return num_q(rng, f"A string under tension {t} N has linear mass density {mu} kg/m. The wave speed on it is:", v, " m/s", "v = √(T/μ).",
                     wrongs=[t / mu, math.sqrt(mu / t), math.sqrt(t * mu)])
    return num_q(rng, f"A {fmt(l)} m string fixed at both ends has wave speed {fmt(v)} m/s. Its fundamental frequency is:", v / (2 * l), " Hz",
                 "f = v/2L.", wrongs=[v / l, v / (4 * l), 2 * v / l])


@gen("p11-14", weight=2)
def _beats(rng):
    f1, b = R(rng, 256, 384, 480, 512), R(rng, 2, 3, 4, 5)
    return Q(f"A tuning fork of {f1} Hz gives {b} beats per second with another fork. Waxing the second fork reduces the beats. The second fork's frequency was:",
             f"{f1 + b} Hz", [f"{f1 - b} Hz", f"{f1 + 2 * b} Hz", f"{f1} Hz"], "Waxing lowers frequency; beats fall only if the fork was above f1.")


@gen("p11-14")
def _doppler(rng):
    f, vs = R(rng, 500, 600, 680, 1000), R(rng, 20, 34, 40)
    v = 340
    approach = rng.random() < 0.5
    fa = f * v / (v - vs) if approach else f * v / (v + vs)
    return num_q(rng, f"A source of {f} Hz moves {'towards' if approach else 'away from'} a stationary listener at {vs} m/s (sound speed 340 m/s). The heard frequency is:",
                 fa, " Hz", "f' = f v/(v ∓ vs).", wrongs=[f * v / (v + vs) if approach else f * v / (v - vs), f, f * (v + vs) / v])


facts("p11-14", [
    "Sound waves in air are longitudinal",
    "Speed of sound in air increases with temperature",
    "Speed of sound in air does not depend on pressure at constant temperature",
    "A closed pipe produces only odd harmonics",
    "An open pipe produces all harmonics",
    "Nodes are separated by half a wavelength",
], [
    "Sound waves in air are transverse",
    "A closed pipe produces all harmonics",
    "Speed of sound in air increases with pressure at constant temperature",
    "Sound travels faster in air than in steel",
    "Nodes are separated by one wavelength",
    "Sound can travel through a vacuum",
], "waves and sound")

# ---------------------------------------------------------------- p12-01 Electric Charges and Fields
@gen("p12-01", weight=3)
def _coulomb(rng):
    q1, q2, r = R(rng, 1, 2, 3, 5), R(rng, 1, 2, 4, 6), R(rng, 0.1, 0.2, 0.3, 0.5)
    f = 9e9 * q1 * q2 * 1e-12 / (r * r)
    return num_q(rng, f"Two charges of {q1} μC and {q2} μC are {fmt(r)} m apart in vacuum. The force between them is:", f, " N", "F = kq1q2/r².",
                 wrongs=[9e9 * q1 * q2 * 1e-12 / r, f * 10, f / 2])


@gen("p12-01", weight=2)
def _gauss(rng):
    where, ans, why = rng.choice([
        ("at the centre of a cube. The electric flux through one face is", "q/(6ε₀)", "Total flux q/ε₀ is shared equally by 6 faces."),
        ("at the centre of a cube. The total electric flux through the cube is", "q/ε₀", "Gauss's law: flux = enclosed charge/ε₀."),
        ("at one corner of a cube. The total electric flux through the cube is", "q/(8ε₀)", "Eight such cubes would enclose the charge."),
        ("at the centre of one face of a cube. The total electric flux through the cube is", "q/(2ε₀)", "Two such cubes would enclose the charge."),
    ])
    return Q(f"A charge q is placed {where}:", ans, ["q/ε₀", "q/(6ε₀)", "q/(8ε₀)", "q/(2ε₀)", "6q/ε₀"], why)


@gen("p12-01", weight=2)
def _scale_force(rng):
    f1, f2 = R(rng, 2, 3, 0.5), R(rng, 2, 3, 0.5)
    return num_q(rng, f"Each charge is multiplied by {fmt(f1)} and the distance by {fmt(f2)}. The Coulomb force becomes how many times?", f1 * f1 / (f2 * f2), " times",
                 "F ∝ q1q2/r².", wrongs=[f1 / f2, f1 * f1 / f2, f1 / (f2 * f2)])


facts("p12-01", [
    "Electric field lines never cross each other",
    "Electric field inside a charged conductor is zero",
    "Charge is quantised in units of e",
    "The torque on a dipole in a uniform field is pE sinθ",
    "A dipole in a uniform field feels no net force",
    "Field of an infinite plane sheet does not depend on distance",
    "Field of an infinite line charge varies as 1/r",
    "Flux through a closed surface depends only on the charge enclosed",
], [
    "Electric field lines can form closed loops in electrostatics",
    "Electric field inside a charged conductor is maximum",
    "Field of an infinite plane sheet varies as 1/r²",
    "A dipole in a uniform field feels a large net force",
    "Flux through a closed surface depends on charges outside it",
    "Field of an infinite line charge varies as 1/r²",
    "Charge can be created in an isolated system",
    "Coulomb's force increases when the medium has a higher dielectric constant",
], "electric charges and fields")

# ---------------------------------------------------------------- p12-02 Electrostatic Potential and Capacitance
@gen("p12-02", weight=3)
def _capacitors(rng):
    c1, c2, c3 = R(rng, 2, 3, 4, 6), R(rng, 2, 3, 6), R(rng, 1, 2, 4)
    kind = rng.choice(["series", "parallel", "mixed"])
    if kind == "series":
        return num_q(rng, f"Capacitors of {c1} μF and {c2} μF are joined in series. The equivalent capacitance is:", c1 * c2 / (c1 + c2), " μF",
                     "1/C = 1/C1 + 1/C2.", wrongs=[c1 + c2, (c1 + c2) / 2, c1 * c2])
    if kind == "parallel":
        return num_q(rng, f"Capacitors of {c1} μF, {c2} μF and {c3} μF are joined in parallel. The equivalent capacitance is:", c1 + c2 + c3, " μF",
                     "C = C1 + C2 + C3.", wrongs=[1 / (1 / c1 + 1 / c2 + 1 / c3), c1 * c2 * c3, (c1 + c2 + c3) / 3])
    cs = c1 * c2 / (c1 + c2)
    return num_q(rng, f"{c1} μF and {c2} μF capacitors in series are joined in parallel with {c3} μF. The equivalent capacitance is:", cs + c3, " μF",
                 "Series pair, then add in parallel.", wrongs=[c1 + c2 + c3, 1 / (1 / (c1 + c3) + 1 / c2), cs])


@gen("p12-02", weight=2)
def _cap_energy(rng):
    c, v = R(rng, 2, 4, 5, 10, 20), R(rng, 10, 20, 50, 100)
    return num_q(rng, f"A {c} μF capacitor is charged to {v} V. The energy stored is:", 0.5 * c * 1e-6 * v * v * 1000, " mJ", "U = ½CV².",
                 wrongs=[c * 1e-6 * v * v * 1000, 0.5 * c * 1e-6 * v * 1000, 0.5 * c * v * v])


@gen("p12-02", weight=2)
def _dielectric(rng):
    k = R(rng, 2, 3, 4, 5)
    kind = rng.choice(["battery", "isolated"])
    if kind == "battery":
        return Q(f"A dielectric of constant K = {k} fills a capacitor that stays connected to a battery. The charge becomes:", f"{k} times",
                 [f"1/{k} times", "Unchanged", f"{k * k} times"], "V fixed, C becomes KC, so Q = CV becomes K times.")
    return Q(f"A charged capacitor is disconnected and then filled with a dielectric of K = {k}. The potential difference becomes:", f"1/{k} times",
             [f"{k} times", "Unchanged", f"1/{k * k} times"], "Q fixed, C becomes KC, so V = Q/C becomes 1/K times.")


@gen("p12-02")
def _pot(rng):
    q, r = R(rng, 1, 2, 3, 5), R(rng, 0.1, 0.3, 0.5, 0.9)
    return num_q(rng, f"The electric potential at {fmt(r)} m from a point charge of {q} μC is:", 9e9 * q * 1e-6 / r, " V", "V = kq/r.",
                 wrongs=[9e9 * q * 1e-6 / (r * r), 9e9 * q / r, 9e9 * q * 1e-6 * r], form=lambda x: sci(x))


facts("p12-02", [
    "Equipotential surfaces are perpendicular to electric field lines",
    "No work is done in moving a charge along an equipotential surface",
    "The potential inside a charged conducting sphere is constant",
    "Capacitance of a parallel plate capacitor is ε₀A/d",
    "Inserting a dielectric increases capacitance",
    "Energy density of an electric field is ½ε₀E²",
], [
    "Equipotential surfaces are parallel to field lines",
    "The potential inside a charged conducting sphere is zero",
    "Capacitance of a parallel plate capacitor increases with plate separation",
    "Inserting a dielectric decreases capacitance",
    "Work is needed to move a charge along an equipotential surface",
    "Capacitors in series add directly",
], "potential and capacitance")

# ---------------------------------------------------------------- p12-03 Current Electricity
@gen("p12-03", weight=3)
def _resistors(rng):
    r1, r2, r3 = R(rng, 2, 3, 4, 6), R(rng, 3, 6, 12), R(rng, 1, 2, 5)
    kind = rng.choice(["par", "mixed", "stretch"])
    if kind == "par":
        return num_q(rng, f"Resistors of {r1} Ω and {r2} Ω are joined in parallel. The equivalent resistance is:", r1 * r2 / (r1 + r2), " Ω",
                     "1/R = 1/R1 + 1/R2.", wrongs=[r1 + r2, (r1 + r2) / 2, r1 * r2])
    if kind == "mixed":
        return num_q(rng, f"{r1} Ω and {r2} Ω in parallel are joined in series with {r3} Ω. The equivalent resistance is:", r1 * r2 / (r1 + r2) + r3, " Ω",
                     "Parallel pair, then add in series.", wrongs=[r1 + r2 + r3, r1 * r2 / (r1 + r2), 1 / (1 / r1 + 1 / r2 + 1 / r3)])
    n = R(rng, 2, 3, 4)
    return num_q(rng, f"A wire of resistance {r1} Ω is stretched uniformly to {n} times its length. Its new resistance is:", r1 * n * n, " Ω",
                 "R ∝ L² when volume is fixed.", wrongs=[r1 * n, r1 / n, r1 * n ** 3])


@gen("p12-03", weight=2)
def _internal(rng):
    e, r, big = R(rng, 2, 3, 6, 12), R(rng, 0.5, 1, 2), R(rng, 4, 5, 10)
    i = e / (big + r)
    return num_q(rng, f"A cell of emf {e} V and internal resistance {fmt(r)} Ω is connected to {big} Ω. The terminal voltage is:", i * big, " V",
                 "V = E - Ir.", wrongs=[e, i * r, e / big * (big - r)])


@gen("p12-03", weight=2)
def _bulb(rng):
    p, v = R(rng, 40, 60, 100, 200), R(rng, 220, 110)
    kind = rng.choice(["R", "half"])
    if kind == "R":
        return num_q(rng, f"A {p} W, {v} V bulb has a resistance of:", v * v / p, " Ω", "R = V²/P.", wrongs=[v / p, p / v, v * p])
    return num_q(rng, f"A {p} W, {v} V bulb is run on {v // 2} V. Its power becomes:", p / 4, " W", "P ∝ V² for fixed R.", wrongs=[p / 2, p, p / 8])


@gen("p12-03")
def _drift(rng):
    i, a = R(rng, 1, 2, 3, 5), R(rng, 1, 2)
    n = 8.5e28
    v = i / (n * 1.6e-19 * a * 1e-6)
    return num_q(rng, f"A copper wire of area {a} mm² carries {i} A (n = 8.5 × 10^28 per m³). The drift speed is:", v * 1000, " mm/s", "v = I/(neA).",
                 wrongs=[v, v * 1e6, v * 100], form=lambda x: sig(x, 2))


facts("p12-03", [
    "Resistance of a metal increases with temperature",
    "Resistivity of a semiconductor decreases with temperature",
    "Kirchhoff's junction rule follows from conservation of charge",
    "Kirchhoff's loop rule follows from conservation of energy",
    "Manganin and constantan have very small temperature coefficients of resistance",
    "A potentiometer measures emf without drawing current at balance",
    "A Wheatstone bridge is balanced when P/Q = R/S",
    "Drift speed is very small, of the order of mm/s",
], [
    "Resistivity of a semiconductor increases with temperature",
    "Resistivity of a wire depends on its length",
    "Kirchhoff's junction rule follows from conservation of energy",
    "A voltmeter has very low resistance",
    "An ammeter is connected in parallel",
    "Drift speed is close to the speed of light",
    "Resistance of a metal decreases with temperature",
    "Cells in parallel give a larger emf",
], "current electricity")

# ---------------------------------------------------------------- p12-04 Moving Charges and Magnetism
@gen("p12-04", weight=3)
def _cyclotron_radius(rng):
    kind = rng.choice(["radius", "loop", "solenoid", "wire"])
    if kind == "radius":
        v, b = R(rng, 1e5, 2e5, 1e6), R(rng, 0.1, 0.2, 0.5)
        r = 9.1e-31 * v / (1.6e-19 * b)
        return num_q(rng, f"An electron moves at {sci(v)} m/s perpendicular to a {fmt(b)} T field. The radius of its path is:", r * 1e6, " μm",
                     "r = mv/(qB).", wrongs=[r * 1e3, r * 1e9, r * 2e6])
    if kind == "loop":
        i, r = R(rng, 1, 2, 5, 10), R(rng, 0.05, 0.1, 0.2)
        b = 4 * math.pi * 1e-7 * i / (2 * r)
        return num_q(rng, f"A circular loop of radius {fmt(r)} m carries {i} A. The field at its centre is (μ₀ = 4π × 10^-7):", b * 1e6, " μT", "B = μ₀I/2r.",
                     wrongs=[b * 2e6, b * 1e6 / math.pi, b * 1e3])
    if kind == "solenoid":
        n, i = R(rng, 1000, 2000, 5000), R(rng, 1, 2, 4)
        b = 4 * math.pi * 1e-7 * n * i
        return num_q(rng, f"A long solenoid has {n} turns per metre and carries {i} A. The field inside is (μ₀ = 4π × 10^-7):", b * 1000, " mT", "B = μ₀nI.",
                     wrongs=[b * 1e6, b * 1000 / 2, b * 1000 * math.pi])
    i, r = R(rng, 5, 10, 20), R(rng, 0.05, 0.1, 0.2)
    b = 2e-7 * i / r
    return num_q(rng, f"A long straight wire carries {i} A. The magnetic field {fmt(r)} m away is (μ₀ = 4π × 10^-7):", b * 1e6, " μT", "B = μ₀I/(2πr).",
                 wrongs=[b * 2e6, b * 1e6 * math.pi, 2e-7 * i / (r * r) * 1e6])


@gen("p12-04", weight=2)
def _galvanometer(rng):
    g, ig, i = R(rng, 10, 20, 50, 100), R(rng, 1, 2, 5), R(rng, 1, 2, 5)
    kind = rng.choice(["shunt", "series"])
    if kind == "shunt":
        s = ig * 1e-3 * g / (i - ig * 1e-3)
        return num_q(rng, f"A galvanometer of {g} Ω gives full deflection at {ig} mA. The shunt needed to make it an ammeter of range {i} A is:", s, " Ω",
                     "S = Ig G/(I - Ig).", wrongs=[g / i, s * 1000, g * i], form=lambda x: sig(x, 3))
    v = R(rng, 5, 10, 50)
    rr = v / (ig * 1e-3) - g
    return num_q(rng, f"A galvanometer of {g} Ω gives full deflection at {ig} mA. The series resistance to make it a voltmeter of range {v} V is:", rr, " Ω",
                 "R = V/Ig - G.", wrongs=[v / (ig * 1e-3), rr + 2 * g, v / ig])


facts("p12-04", [
    "A magnetic force does no work on a moving charge",
    "Parallel currents in the same direction attract",
    "The cyclotron frequency does not depend on the speed of the particle",
    "An ideal ammeter has zero resistance",
    "The field inside a long solenoid is nearly uniform",
    "A current loop behaves like a magnetic dipole",
], [
    "Parallel currents in the same direction repel",
    "The magnetic force on a charge is along its velocity",
    "A charge at rest feels a force in a magnetic field",
    "An ideal voltmeter has zero resistance",
    "The cyclotron frequency increases with the speed of the particle",
    "The field outside a long solenoid is very strong",
], "moving charges and magnetism")

# ---------------------------------------------------------------- p12-05 Magnetism and Matter
groups("p12-05", {
    "diamagnetic": ["Bismuth", "Copper", "Lead", "Silicon", "Water", "Sodium chloride"],
    "paramagnetic": ["Aluminium", "Sodium", "Calcium", "Oxygen at STP", "Copper chloride"],
    "ferromagnetic": ["Iron", "Cobalt", "Nickel", "Gadolinium"],
}, "Which material is NOT {}?", "Which material is {}?", weight=2)
facts("p12-05", [
    "A superconductor is a perfect diamagnet (Meissner effect)",
    "Ferromagnets become paramagnetic above the Curie temperature",
    "Paramagnetic susceptibility varies inversely with absolute temperature (Curie's law)",
    "Soft iron is used for electromagnets because it has low retentivity and coercivity",
    "Steel is used for permanent magnets because of high retentivity and coercivity",
    "Magnetic field lines form closed loops",
    "The angle of dip is 90° at the magnetic poles",
    "Diamagnetic materials move from stronger to weaker field regions",
], [
    "Soft iron is used for permanent magnets",
    "Diamagnetic materials are strongly attracted by magnets",
    "The angle of dip is 90° at the magnetic equator",
    "Magnetic monopoles are commonly found",
    "Ferromagnets stay ferromagnetic at all temperatures",
    "Paramagnetic susceptibility increases with temperature",
    "Magnetic field lines start at the north pole and end at the south pole inside the magnet too",
    "Copper is ferromagnetic",
], "magnetism and matter")

# ---------------------------------------------------------------- p12-06 Electromagnetic Induction
@gen("p12-06", weight=3)
def _emi(rng):
    kind = rng.choice(["rod", "flux", "selfL", "energy"])
    if kind == "rod":
        b, l, v = R(rng, 0.1, 0.2, 0.5, 1), R(rng, 0.5, 1, 2), R(rng, 2, 5, 10)
        return num_q(rng, f"A rod of length {fmt(l)} m moves at {v} m/s perpendicular to a {fmt(b)} T field. The induced emf is:", b * l * v, " V", "e = Blv.",
                     wrongs=[b * v, b * l, b * l * v / 2])
    if kind == "flux":
        n, a, b1, t = R(rng, 50, 100, 200), R(rng, 0.01, 0.02, 0.05), R(rng, 0.2, 0.5, 1), R(rng, 0.1, 0.2, 0.5)
        return num_q(rng, f"A coil of {n} turns and area {a} m² is in a {fmt(b1)} T field normal to it. The field falls to zero in {fmt(t)} s. The average induced emf is:",
                     n * a * b1 / t, " V", "e = NΔΦ/Δt.", wrongs=[a * b1 / t, n * a * b1, n * a * b1 * t])
    if kind == "selfL":
        l, di, dt = R(rng, 0.1, 0.2, 0.5, 2), R(rng, 1, 2, 5), R(rng, 0.01, 0.05, 0.1)
        return num_q(rng, f"The current in a {fmt(l)} H coil changes by {di} A in {fmt(dt)} s. The induced emf is:", l * di / dt, " V", "e = L dI/dt.",
                     wrongs=[l * di, l * di * dt, di / (l * dt)])
    l, i = R(rng, 0.1, 0.2, 0.5, 2), R(rng, 1, 2, 4)
    return num_q(rng, f"A {fmt(l)} H inductor carries {i} A. The energy stored in it is:", 0.5 * l * i * i, " J", "U = ½LI².", wrongs=[l * i * i, 0.5 * l * i, l * i])


facts("p12-06", [
    "Lenz's law follows from conservation of energy",
    "Eddy currents are reduced by using laminated cores",
    "Induced emf depends on the rate of change of magnetic flux",
    "The SI unit of inductance is the henry",
    "Self-inductance of a solenoid is proportional to the square of its number of turns",
    "Electromagnetic damping is used in galvanometers",
], [
    "Lenz's law follows from conservation of charge",
    "Eddy currents are increased by laminated cores",
    "Induced emf depends on the magnetic flux itself, not its change",
    "Self-inductance of a solenoid is independent of the number of turns",
    "The SI unit of magnetic flux is the tesla",
    "A stationary magnet inside a coil induces a steady current",
], "electromagnetic induction")

# ---------------------------------------------------------------- p12-07 Alternating Current
@gen("p12-07", weight=3)
def _ac(rng):
    kind = rng.choice(["rms", "res", "xl", "trans", "pf"])
    if kind == "rms":
        v0 = R(rng, 100, 200, 311, 141.4)
        return num_q(rng, f"An AC voltage has a peak value of {fmt(v0)} V. Its rms value is:", v0 / math.sqrt(2), " V", "Vrms = V₀/√2.",
                     wrongs=[v0 / 2, v0 * math.sqrt(2), v0 * 0.637])
    if kind == "res":
        l, c = R(rng, 0.1, 0.4, 1), R(rng, 10, 40, 100)
        f = 1 / (2 * math.pi * math.sqrt(l * c * 1e-6))
        return num_q(rng, f"An LC circuit has L = {fmt(l)} H and C = {c} μF. Its resonant frequency is:", f, " Hz", "f = 1/(2π√(LC)).",
                     wrongs=[2 * math.pi * f, f / (2 * math.pi), 1 / math.sqrt(l * c * 1e-6)])
    if kind == "xl":
        l, f = R(rng, 0.1, 0.2, 0.5), R(rng, 50, 60, 100)
        return num_q(rng, f"The inductive reactance of a {fmt(l)} H coil at {f} Hz is:", 2 * math.pi * f * l, " Ω", "XL = 2πfL.", wrongs=[f * l, 2 * math.pi * f / l, 1 / (2 * math.pi * f * l)])
    if kind == "trans":
        np_, ns, vp = R(rng, 100, 200, 500), R(rng, 50, 1000, 2000), R(rng, 220, 110, 240)
        return num_q(rng, f"An ideal transformer has {np_} primary and {ns} secondary turns. With {vp} V on the primary, the secondary voltage is:", vp * ns / np_, " V",
                     "Vs/Vp = Ns/Np.", wrongs=[vp * np_ / ns, vp, vp * ns])
    r, x = R(rng, 3, 6, 8, 30), R(rng, 4, 8, 6, 40)
    z = math.sqrt(r * r + x * x)
    return num_q(rng, f"A series circuit has R = {r} Ω and net reactance {x} Ω. Its power factor is:", r / z, "", "cosφ = R/Z.", wrongs=[x / z, r / x, z / r], form=lambda x: fmt(x, 2))


facts("p12-07", [
    "At resonance in a series LCR circuit the current is maximum",
    "A pure inductor draws no average power",
    "Current leads the voltage by 90° in a pure capacitor",
    "Current lags the voltage by 90° in a pure inductor",
    "A capacitor blocks DC",
    "Transformers work only with alternating current",
], [
    "A pure resistor draws no power",
    "Current lags voltage by 90° in a pure capacitor",
    "A step-up transformer increases current",
    "At resonance the impedance is maximum in a series LCR circuit",
    "Capacitive reactance increases with frequency",
    "Transformers work with steady DC",
], "alternating current")

# ---------------------------------------------------------------- p12-08 Electromagnetic Waves
table("p12-08", [
    ("Radio waves", "Above 0.1 m; radio and TV broadcasting"), ("Microwaves", "0.1 m to 1 mm; radar and microwave ovens"),
    ("Infrared", "1 mm to 700 nm; heat radiation and remote controls"), ("Visible light", "700 nm to 400 nm"),
    ("Ultraviolet", "400 nm to 1 nm; absorbed by the ozone layer"), ("X-rays", "1 nm to 10^-3 nm; medical imaging"),
    ("Gamma rays", "Below 10^-3 nm; from nuclear reactions"),
], "{}:", "Which EM radiation: {}?", weight=2)
facts("p12-08", [
    "EM waves are transverse",
    "EM waves are produced by accelerated charges",
    "In an EM wave E and B are in phase and perpendicular to each other",
    "The speed of EM waves in vacuum is 1/√(μ₀ε₀)",
    "Maxwell introduced the displacement current",
    "EM waves carry energy and momentum",
], [
    "EM waves are longitudinal",
    "EM waves need a medium to travel",
    "A charge moving at constant velocity radiates EM waves",
    "E and B in an EM wave are parallel",
    "X-rays have longer wavelength than radio waves",
    "Gamma rays have the lowest frequency",
], "electromagnetic waves")

# ---------------------------------------------------------------- p12-09 Ray Optics and Optical Instruments
@gen("p12-09", weight=3)
def _lens(rng):
    kind = rng.choice(["image", "power", "combo", "tir", "mag"])
    if kind == "image":
        f, u = R(rng, 10, 15, 20), R(rng, 30, 40, 60)
        v = 1 / (1 / f - 1 / u)
        return num_q(rng, f"An object is {u} cm in front of a convex lens of focal length {f} cm. The image forms at:", v, " cm", "1/v - 1/u = 1/f with u = -{u}.",
                     wrongs=[1 / (1 / f + 1 / u), u - f, f * u / (u + f) * 2])
    if kind == "power":
        f = R(rng, 10, 20, 25, 50, -25, -50)
        return num_q(rng, f"A lens has focal length {f} cm. Its power is:", 100 / f, " D", "P = 100/f(cm).", wrongs=[f / 100, -100 / f, 1 / f])
    if kind == "combo":
        p1, p2 = R(rng, 2, 4, 5, 10), R(rng, -2, -1, 1, 2, 4)
        return num_q(rng, f"Two thin lenses of power +{p1} D and {p2:+d} D are in contact. The focal length of the combination is:", 100 / (p1 + p2), " cm",
                     "P = P1 + P2; f = 100/P.", wrongs=[100 / p1 + 100 / p2, 100 / abs(p1 - p2) if p1 != p2 else 50, (p1 + p2)])
    if kind == "tir":
        n = R(rng, 1.5, 2, 1.414, 2.42)
        return num_q(rng, f"The critical angle for a medium of refractive index {fmt(n)} (to air) is:", math.degrees(math.asin(1 / n)), "°", "sin C = 1/n.",
                     wrongs=[math.degrees(math.acos(1 / n)), math.degrees(math.atan(1 / n)), 90 / n], form=lambda x: fmt(x, 1))
    fo, fe = R(rng, 50, 100, 150), R(rng, 5, 2, 10)
    return num_q(rng, f"An astronomical telescope in normal adjustment has fo = {fo} cm and fe = {fe} cm. Its magnifying power is:", fo / fe, "",
                 "m = fo/fe.", wrongs=[fe / fo, fo * fe, fo + fe])


@gen("p12-09", weight=2)
def _prism(rng):
    a, n = R(rng, 60), R(rng, 1.414, 1.732)
    dm = 2 * math.degrees(math.asin(n * math.sin(math.radians(a / 2)))) - a
    return num_q(rng, f"A 60° prism has refractive index {fmt(n, 3)}. Its angle of minimum deviation is:", dm, "°",
                 "n = sin((A + δm)/2)/sin(A/2).", wrongs=[dm / 2, a, dm + 15], form=lambda x: fmt(x, 0))


facts("p12-09", [
    "The focal length of a spherical mirror is half its radius of curvature",
    "A convex mirror always forms a virtual, erect, diminished image",
    "Optical fibres work on total internal reflection",
    "The sky looks blue because of scattering of short wavelengths",
    "Myopia is corrected with a concave lens",
    "Hypermetropia is corrected with a convex lens",
    "Violet light deviates the most in a glass prism",
    "A lens immersed in a liquid of the same refractive index behaves like a plane glass plate",
], [
    "A concave mirror always forms a virtual image",
    "Myopia is corrected with a convex lens",
    "Red light deviates the most in a prism",
    "The focal length of a mirror changes when it is put in water",
    "Optical fibres work on diffraction",
    "The sky looks blue because of refraction only",
    "A convex mirror can form a real image of a real object",
    "Power of a lens is measured in metres",
], "ray optics")

# ---------------------------------------------------------------- p12-10 Wave Optics
@gen("p12-10", weight=3)
def _ydse(rng):
    lam, d, D = R(rng, 500, 600, 400, 700), R(rng, 0.1, 0.2, 0.5, 1), R(rng, 1, 1.5, 2)
    kind = rng.choice(["beta", "change", "single"])
    beta = lam * 1e-9 * D / (d * 1e-3) * 1000
    if kind == "beta":
        return num_q(rng, f"In Young's double slit experiment λ = {lam} nm, slit separation {fmt(d)} mm and screen distance {fmt(D)} m. The fringe width is:", beta, " mm",
                     "β = λD/d.", wrongs=[beta * 2, beta / 2, beta * 10])
    if kind == "change":
        f = R(rng, 2, 3, 0.5)
        return num_q(rng, f"In YDSE the slit separation is made {fmt(f)} times. The fringe width becomes how many times?", 1 / f, " times", "β ∝ 1/d.",
                     wrongs=[f, f * f, 1 / (f * f)], form=lambda x: fmt(x, 3))
    a = R(rng, 0.1, 0.2, 0.5)
    w = 2 * lam * 1e-9 * D / (a * 1e-3) * 1000
    return num_q(rng, f"Light of {lam} nm falls on a single slit of width {fmt(a)} mm. The width of the central maximum on a screen {fmt(D)} m away is:", w, " mm",
                 "Central width = 2λD/a.", wrongs=[w / 2, w * 2, w * 10])


@gen("p12-10", weight=2)
def _malus(rng):
    th = R(rng, 30, 45, 60)
    i0 = R(rng, 16, 32, 64, 100)
    i = i0 * math.cos(math.radians(th)) ** 2
    return num_q(rng, f"Polarised light of intensity {i0} units passes through an analyser at {th}° to its plane. The transmitted intensity is:", i, " units",
                 "I = I₀cos²θ.", wrongs=[i0 * math.cos(math.radians(th)), i0 / 2, i0 * math.sin(math.radians(th)) ** 2])


@gen("p12-10")
def _brewster(rng):
    n = R(rng, 1.732, 1, 1.5)
    if n == 1:
        return None
    return num_q(rng, f"The Brewster angle for a surface of refractive index {fmt(n, 3)} is:", math.degrees(math.atan(n)), "°", "tan iₚ = n.",
                 wrongs=[math.degrees(math.asin(1 / n)), math.degrees(math.atan(1 / n)), 45], form=lambda x: fmt(x, 1))


facts("p12-10", [
    "Huygens' principle treats every point on a wavefront as a source of secondary wavelets",
    "Interference needs coherent sources",
    "Polarisation shows that light waves are transverse",
    "In YDSE with white light the central fringe is white",
    "Fringe width increases if the whole apparatus is moved from water into air",
    "Resolving power of a telescope increases with the aperture of its objective",
], [
    "Two independent bulbs give a sustained interference pattern",
    "Polarisation shows that light is longitudinal",
    "Fringe width increases when the slits are moved further apart",
    "In YDSE with white light the central fringe is dark",
    "Sound waves can be polarised",
    "Resolving power of a telescope decreases with a larger objective",
], "wave optics")

# ---------------------------------------------------------------- p12-11 Dual Nature of Radiation and Matter
@gen("p12-11", weight=3)
def _photo(rng):
    kind = rng.choice(["kmax", "stop", "lambda_e", "threshold"])
    if kind == "kmax":
        e, w = R(rng, 4, 5, 6, 6.2, 10), R(rng, 2, 2.3, 3, 4.2)
        if e <= w:
            return None
        return num_q(rng, f"Light of photon energy {fmt(e)} eV falls on a metal of work function {fmt(w)} eV. The maximum kinetic energy of photoelectrons is:", e - w,
                     " eV", "Kmax = hν - φ.", wrongs=[e + w, e, w])
    if kind == "stop":
        k = R(rng, 1, 1.5, 2, 3.2)
        return num_q(rng, f"The maximum kinetic energy of photoelectrons is {fmt(k)} eV. The stopping potential is:", k, " V", "eV₀ = Kmax.", wrongs=[k * 2, k / 2, k * 1.6])
    if kind == "lambda_e":
        v = R(rng, 100, 150, 400, 10000)
        return num_q(rng, f"An electron is accelerated through {v} V. Its de Broglie wavelength is about:", 1.227 / math.sqrt(v), " nm", "λ = 1.227/√V nm.",
                     wrongs=[1.227 / v, 12.27 / math.sqrt(v), 1.227 * math.sqrt(v)], form=lambda x: sig(x, 3))
    w = R(rng, 2, 2.5, 3.1, 4.14, 6.2)
    return num_q(rng, f"A metal has a work function of {fmt(w)} eV. Its threshold wavelength is about:", 1240 / w, " nm", "λ₀ = 1240/φ(eV) nm.",
                 wrongs=[w * 1240 / 1000, 12400 / w, 620 / w])


@gen("p12-11", weight=2)
def _db_ratio(rng):
    kind = rng.choice(["ke", "mass"])
    if kind == "ke":
        f = R(rng, 4, 9, 16)
        return num_q(rng, f"The kinetic energy of a particle is made {f} times. Its de Broglie wavelength becomes how many times?", 1 / math.sqrt(f), " times",
                     "λ = h/√(2mK).", wrongs=[1 / f, math.sqrt(f), f], form=lambda x: fmt(x, 3))
    return Q("A proton and an alpha particle are accelerated through the same potential difference. The ratio of their de Broglie wavelengths λp : λα is:",
             "2√2 : 1", ["1 : 1", "2 : 1", "1 : 2√2", "√2 : 1"], "λ = h/√(2mqV); mα = 4mp, qα = 2qp, so λp/λα = √8.")


facts("p12-11", [
    "Photoelectric emission is instantaneous",
    "The stopping potential depends on frequency, not intensity",
    "Photocurrent increases with intensity above threshold frequency",
    "Davisson and Germer confirmed the wave nature of electrons",
    "Below the threshold frequency no photoelectrons are emitted however intense the light",
    "The slope of a V₀ against ν graph is h/e",
], [
    "Maximum kinetic energy of photoelectrons increases with light intensity",
    "Photoelectric emission starts after a time lag for dim light",
    "Davisson and Germer showed the particle nature of light",
    "Stopping potential depends on intensity",
    "Electrons are emitted below the threshold frequency if light is intense",
    "The slope of a V₀ against ν graph is e/h",
], "dual nature")

# ---------------------------------------------------------------- p12-12 Atoms
@gen("p12-12", weight=3)
def _hatom(rng):
    kind = rng.choice(["ion", "ratio", "lambda"])
    if kind == "ion":
        n = R(rng, 1, 2, 3, 4)
        return num_q(rng, f"The energy needed to ionise a hydrogen atom from the state n = {n} is:", 13.6 / (n * n), " eV", "E = 13.6/n² eV.",
                     wrongs=[13.6 / n, 13.6 * n, 13.6])
    if kind == "ratio":
        return Q("The ratio of the shortest wavelengths of the Lyman and Balmer series of hydrogen is:", "1 : 4", ["4 : 1", "1 : 2", "2 : 1", "4 : 9"],
                 "Series limits: 1/λ ∝ 1/1² and 1/2².")
    n = R(rng, 3, 4, 5)
    e = 13.6 * (1 / 4 - 1 / (n * n))
    return num_q(rng, f"A hydrogen atom drops from n = {n} to n = 2. The photon energy is:", e, " eV", "ΔE = 13.6(1/4 - 1/n²) eV.",
                 wrongs=[13.6 * (1 - 1 / (n * n)), 13.6 / (n * n), 13.6 / 4])


facts("p12-12", [
    "In the Rutherford experiment most alpha particles passed through undeflected",
    "Bohr postulated that angular momentum is quantised in units of h/2π",
    "The radius of a Bohr orbit is proportional to n²",
    "The speed of the electron in a Bohr orbit is inversely proportional to n",
    "The Balmer series of hydrogen lies in the visible region",
    "The ground-state energy of hydrogen is -13.6 eV",
], [
    "In the Rutherford experiment most alpha particles bounced back",
    "The radius of a Bohr orbit is proportional to n",
    "The electron's speed in a Bohr orbit increases with n",
    "The Lyman series lies in the visible region",
    "The ground-state energy of hydrogen is +13.6 eV",
    "Bohr's model works well for helium atoms",
], "atoms")

# ---------------------------------------------------------------- p12-13 Nuclei
@gen("p12-13", weight=3)
def _decay(rng):
    kind = rng.choice(["left", "time", "radius", "ab"])
    if kind == "left":
        t, n = R(rng, 2, 5, 10, 20), R(rng, 2, 3, 4)
        return Q(f"A radioactive isotope has a half-life of {t} days. The fraction left after {t * n} days is:", f"1/{2 ** n}",
                 [f"1/{2 * n}", f"1/{2 ** (n + 1)}", f"1/{n}"], f"{n} half-lives: (1/2)^{n}.")
    if kind == "time":
        t, f = R(rng, 3, 5, 8, 10), R(rng, 4, 8, 16)
        n = int(math.log2(f))
        return num_q(rng, f"A sample with half-life {t} h decays to 1/{f} of its initial activity in:", t * n, " h", f"1/{f} = (1/2)^{n}.",
                     wrongs=[t * f, t * f / 2, t * (n + 1)])
    if kind == "radius":
        a1, a2 = rng.choice([(27, 125), (8, 64), (1, 27), (64, 216), (27, 64)])
        return Q(f"The ratio of the nuclear radii of mass numbers {a1} and {a2} is:", f"{round(a1 ** (1 / 3))} : {round(a2 ** (1 / 3))}",
                 [f"{a1} : {a2}", f"{round(a1 ** 0.5, 1)} : {round(a2 ** 0.5, 1)}", f"{round(a2 ** (1 / 3))} : {round(a1 ** (1 / 3))}"], "R = R₀A^(1/3).")
    a, z = R(rng, 238, 232, 234), R(rng, 92, 90, 91)
    na, nb = R(rng, 1, 2, 3, 4), R(rng, 1, 2, 3)
    return Q(f"A nucleus (A = {a}, Z = {z}) emits {na} alpha and {nb} beta-minus particles. The new nucleus has:",
             f"A = {a - 4 * na}, Z = {z - 2 * na + nb}",
             [f"A = {a - 4 * na}, Z = {z - 2 * na - nb}", f"A = {a - 2 * na}, Z = {z - 2 * na + nb}", f"A = {a - 4 * na - nb}, Z = {z - na + nb}"],
             "Each α: A - 4, Z - 2; each β⁻: Z + 1.")


@gen("p12-13", weight=2)
def _binding(rng):
    dm = R(rng, 0.01, 0.02, 0.03, 0.1)
    return num_q(rng, f"The mass defect of a nucleus is {fmt(dm)} u. Its binding energy is (1 u = 931.5 MeV):", dm * 931.5, " MeV", "BE = Δm × 931.5 MeV.",
                 wrongs=[dm * 931.5 * 2, dm / 931.5, dm * 9e16])


facts("p12-13", [
    "Nuclear density is nearly the same for all nuclei",
    "Binding energy per nucleon is highest near A = 56 (iron)",
    "Nuclear forces are short-range and charge-independent",
    "Fusion of light nuclei releases energy",
    "Fission of heavy nuclei releases energy",
    "Isotopes have the same atomic number but different mass numbers",
    "Isobars have the same mass number",
    "Isotones have the same number of neutrons",
], [
    "Nuclear density increases with mass number",
    "Nuclear forces are long-range",
    "Binding energy per nucleon is highest for uranium",
    "Isotopes have the same mass number",
    "Beta-minus decay lowers the atomic number by 1",
    "Alpha decay increases the mass number",
    "Gamma decay changes the atomic number",
    "Isobars have the same atomic number",
], "nuclei")

# ---------------------------------------------------------------- p12-14 Semiconductor Electronics
table("p12-14", [
    ("AND gate", "Output is 1 only when all inputs are 1"), ("OR gate", "Output is 1 when any input is 1"),
    ("NAND gate", "Output is 0 only when all inputs are 1"), ("NOR gate", "Output is 1 only when all inputs are 0"),
    ("NOT gate", "Output is the inverse of the input"), ("XOR gate", "Output is 1 when the inputs differ"),
], "{}:", "Which logic gate: {}?", weight=2)


GATES = {"AND": lambda a, b: a & b, "OR": lambda a, b: a | b, "NAND": lambda a, b: 1 - (a & b),
         "NOR": lambda a, b: 1 - (a | b), "XOR": lambda a, b: a ^ b, "XNOR": lambda a, b: 1 - (a ^ b)}


@gen("p12-14", weight=2)
def _gate_out(rng):
    seq = lambda g: ", ".join(str(GATES[g](a, b)) for a, b in ((0, 0), (0, 1), (1, 0), (1, 1)))
    gate = rng.choice(list(GATES))
    if rng.random() < 0.5:
        return Q(f"For inputs (A, B) = (0,0), (0,1), (1,0), (1,1), the outputs of a {gate} gate are:", seq(gate),
                 [seq(g) for g in GATES if g != gate], f"{gate} truth table.")
    return Q(f"A gate gives outputs {seq(gate)} for inputs (0,0), (0,1), (1,0), (1,1). It is a:", f"{gate} gate",
             [f"{g} gate" for g in GATES if g != gate], f"Matches the {gate} truth table.")


@gen("p12-14")
def _rectifier(rng):
    f = R(rng, 50, 60)
    full = rng.random() < 0.5
    return Q(f"The input to a {'full' if full else 'half'}-wave rectifier is {f} Hz AC. The output ripple frequency is:", f"{f * (2 if full else 1)} Hz",
             [f"{f * (1 if full else 2)} Hz", f"{f * 4} Hz", f"{f // 2} Hz"], "Full-wave doubles the frequency; half-wave keeps it.")


facts("p12-14", [
    "In an n-type semiconductor electrons are the majority carriers",
    "Doping silicon with phosphorus makes it n-type",
    "Doping silicon with boron makes it p-type",
    "A Zener diode is used as a voltage regulator in reverse bias",
    "The depletion region widens in reverse bias",
    "NAND and NOR are universal gates",
    "A photodiode is operated in reverse bias",
    "An LED works in forward bias",
], [
    "In an n-type semiconductor holes are the majority carriers",
    "Doping with boron makes silicon n-type",
    "A Zener diode regulates voltage in forward bias",
    "The depletion region widens in forward bias",
    "AND and OR are universal gates",
    "An LED works in reverse bias",
    "An intrinsic semiconductor has more electrons than holes",
    "Resistance of a semiconductor rises with temperature",
], "semiconductors")

# ---------------------------------------------------------------- p12-15 Experimental Skills
table("p12-15", [
    ("Vernier callipers", "Least count = 1 MSD - 1 VSD"), ("Screw gauge", "Least count = pitch / number of circular scale divisions"),
    ("Metre bridge", "Unknown resistance from the balancing length"), ("Potentiometer", "Compares emfs of two cells"),
    ("Searle's apparatus", "Young's modulus of a wire"), ("Sonometer", "Frequency of a stretched string"),
    ("Resonance tube", "Speed of sound in air"),
], "{}:", "Which apparatus: {}?", weight=2)


@gen("p12-15", weight=2)
def _least_count(rng):
    kind = rng.choice(["vernier", "screw"])
    if kind == "vernier":
        n = R(rng, 10, 20, 50)
        return num_q(rng, f"In a vernier calliper {n} vernier divisions equal {n - 1} main scale divisions of 1 mm. The least count is:", 1 / n, " mm",
                     "LC = 1 MSD - 1 VSD.", wrongs=[1 / (n - 1), n / 100, 0.1 if n != 10 else 0.01], form=lambda x: fmt(x, 3))
    p, n = R(rng, 0.5, 1), R(rng, 50, 100)
    return num_q(rng, f"A screw gauge has pitch {fmt(p)} mm and {n} circular scale divisions. Its least count is:", p / n, " mm", "LC = pitch/divisions.",
                 wrongs=[n / p / 1000, p / (n * 10), p * n / 1000], form=lambda x: fmt(x, 4))


@gen("p12-15", weight=2)
def _metre_bridge(rng):
    rk, l = R(rng, 2, 4, 5, 10), R(rng, 20, 25, 40, 60)
    return num_q(rng, f"In a metre bridge with a known {rk} Ω in the right gap, balance is at {l} cm from the left end. The unknown resistance in the left gap is:",
                 rk * l / (100 - l), " Ω", "X/R = l/(100 - l).", wrongs=[rk * (100 - l) / l, rk * l / 100, rk])


# ---------------------------------------------------------------- more for the thinner chapters
@gen("p12-08", weight=3)
def _em_wave(rng):
    kind = rng.choice(["lambda", "b0", "freq"])
    if kind == "lambda":
        f = R(rng, 1e6, 3e6, 1e8, 3e8, 1e10, 3e9)
        return num_q(rng, f"An EM wave in vacuum has frequency {sci(f)} Hz. Its wavelength is:", 3e8 / f, " m", "λ = c/f.",
                     wrongs=[f / 3e8, 3e8 * f, 3e8 / f * 10], form=lambda x: sci(x))
    if kind == "b0":
        e0 = R(rng, 3, 6, 9, 30, 60, 120)
        return num_q(rng, f"In a plane EM wave the electric field amplitude is {e0} V/m. The magnetic field amplitude is:", e0 / 3e8 * 1e9, " nT", "B₀ = E₀/c.",
                     wrongs=[e0 * 3e8, e0 / 3e8 * 1e6, e0 / 3e8 * 1e12], form=lambda x: sci(x))
    lam = R(rng, 1, 3, 10, 300)
    return num_q(rng, f"An EM wave in vacuum has wavelength {lam} m. Its frequency is:", 3e8 / lam / 1e6, " MHz", "f = c/λ.",
                 wrongs=[3e8 * lam / 1e6, 3e8 / lam, lam / 3e8 * 1e6], form=lambda x: sci(x))


table("p12-12", [
    ("Lyman series", "Ultraviolet; transitions to n = 1"), ("Balmer series", "Visible; transitions to n = 2"),
    ("Paschen series", "Infrared; transitions to n = 3"), ("Brackett series", "Infrared; transitions to n = 4"),
    ("Pfund series", "Infrared; transitions to n = 5"),
], "The {} of hydrogen:", "Which hydrogen series: {}?")


@gen("p12-12", weight=2)
def _bohr_scaling(rng):
    q, law = rng.choice([("radius", "n²"), ("speed", "1/n"), ("energy", "1/n²"), ("angular momentum", "n"), ("time period", "n³")])
    return Q(f"In the Bohr model of hydrogen, the {q} of the electron in orbit n is proportional to:", law, ["n²", "1/n", "1/n²", "n", "n³"],
             f"Bohr model: {q} ∝ {law}.")


table("p12-15", [
    ("Positive zero error of a vernier calliper", "Subtract the zero error from the reading"),
    ("Negative zero error of a vernier calliper", "Add the magnitude of the zero error to the reading"),
    ("Backlash error", "Occurs in a screw gauge when the direction of rotation is reversed"),
    ("Parallax error", "Avoided by keeping the eye in line with the scale mark"),
], "{}:", "Which error is described: {}?")

tag(None)
