"""NEET Physics, Classes 11-12: computed numericals and concept tables."""
import math

from .core import table, facts, gen, num_q, Q, sig, sci, fmt

G = 9.8


def R(rng, *xs):
    return rng.choice(xs)


# ---------------------------------------------------------------- p11-01 Units and Measurement
table("p11-01", [
    ("Force", "[M L T^-2]"), ("Work or energy", "[M L^2 T^-2]"), ("Power", "[M L^2 T^-3]"),
    ("Pressure or stress", "[M L^-1 T^-2]"), ("Momentum", "[M L T^-1]"), ("Gravitational constant G", "[M^-1 L^3 T^-2]"),
    ("Planck's constant", "[M L^2 T^-1]"), ("Surface tension", "[M T^-2]"), ("Coefficient of viscosity", "[M L^-1 T^-1]"),
    ("Frequency", "[T^-1]"), ("Acceleration", "[L T^-2]"), ("Density", "[M L^-3]"),
], "The dimensional formula of {} is:", "Which quantity has the dimensions {}?", weight=3)


@gen("p11-01", weight=2)
def _sigfig(rng):
    n, val = rng.choice([("0.00450", 3), ("4.500", 4), ("2.30 × 10^3", 3), ("0.0203", 3), ("100.0", 4), ("6.022 × 10^23", 4),
                         ("0.010", 2), ("3.0800", 5), ("5.07", 3), ("0.5", 1)])
    return Q(f"How many significant figures are there in {n}?", str(val), [str(x) for x in {1, 2, 3, 4, 5, 6} - {val}],
             "Leading zeros are not significant; trailing zeros after a decimal point are.")


@gen("p11-01", weight=2)
def _perr(rng):
    a, b = R(rng, 1, 2, 0.5), R(rng, 1, 2, 1.5, 0.5)
    p, q = R(rng, 2, 3, 1), R(rng, 2, 1, 3)
    val = p * a + q * b
    return num_q(rng, f"A quantity X = A^{p} B^{q}. If A has {a}% error and B has {b}% error, the maximum % error in X is:",
                 val, "%", f"%X = {p}×{a} + {q}×{b}.", wrongs=[a + b, p * a, q * b, p * b + q * a])


# ---------------------------------------------------------------- p11-02 Motion in a Straight Line
@gen("p11-02", weight=3)
def _suvat(rng):
    u, a, t = R(rng, 0, 2, 5, 10, 20), R(rng, 1, 2, 3, 4, 5), R(rng, 2, 3, 4, 5, 10)
    kind = rng.choice(["v", "s"])
    if kind == "v":
        return num_q(rng, f"A body starts with {u} m/s and accelerates uniformly at {a} m/s². Its speed after {t} s is:",
                     u + a * t, " m/s", "v = u + at.", wrongs=[u * t + a, a * t, u + a * t * t / 2])
    s = u * t + 0.5 * a * t * t
    return num_q(rng, f"A body starts with {u} m/s and accelerates uniformly at {a} m/s². Distance covered in {t} s is:",
                 s, " m", "s = ut + ½at².", wrongs=[u * t + a * t * t, (u + a * t) * t, a * t * t / 2])


@gen("p11-02", weight=2)
def _freefall(rng):
    h = R(rng, 5, 20, 45, 80, 125, 180)
    g = 10
    kind = rng.choice(["time", "speed"])
    if kind == "time":
        return num_q(rng, f"A ball is dropped from {h} m (g = 10 m/s²). Time to reach the ground is:", math.sqrt(2 * h / g), " s",
                     "t = √(2h/g).", wrongs=[math.sqrt(h / g), 2 * h / g, h / g])
    return num_q(rng, f"A ball is dropped from {h} m (g = 10 m/s²). Its speed just before hitting the ground is:",
                 math.sqrt(2 * g * h), " m/s", "v = √(2gh).", wrongs=[math.sqrt(g * h), 2 * g * h / 10, g * h / 10])


@gen("p11-02", weight=2)
def _stop(rng):
    v, a = R(rng, 10, 20, 30, 40), R(rng, 2, 4, 5, 8)
    return num_q(rng, f"A car moving at {v} m/s brakes with a uniform retardation of {a} m/s². Its stopping distance is:",
                 v * v / (2 * a), " m", "s = v²/2a.", wrongs=[v * v / a, v / a, v * v / (4 * a)])


@gen("p11-02")
def _avg(rng):
    v1, v2 = R(rng, 20, 30, 40, 60), R(rng, 30, 40, 60, 80)
    if v1 == v2:
        return None
    return num_q(rng, f"A car covers half a distance at {v1} km/h and the other half at {v2} km/h. Average speed is:",
                 2 * v1 * v2 / (v1 + v2), " km/h", "Average speed = 2v1v2/(v1 + v2).", wrongs=[(v1 + v2) / 2, v1 * v2 / (v1 + v2)])


facts("p11-02", [
    "The slope of a position-time graph gives velocity",
    "The slope of a velocity-time graph gives acceleration",
    "The area under a velocity-time graph gives displacement",
    "In free fall without air resistance all bodies have the same acceleration",
    "Displacement can be zero even when distance travelled is not",
], [
    "The area under a position-time graph gives velocity",
    "Speed can be negative",
    "A body with zero velocity always has zero acceleration",
    "Heavier bodies fall faster in a vacuum",
    "Distance can be less than the magnitude of displacement",
], "Motion in a Straight Line")


# ---------------------------------------------------------------- p11-03 Motion in a Plane
@gen("p11-03", weight=2)
def _horizontal(rng):
    h, u = R(rng, 20, 45, 80, 125), R(rng, 5, 10, 15, 20)
    t = math.sqrt(2 * h / 10)
    return num_q(rng, f"A ball is thrown horizontally at {u} m/s from a {h} m high cliff (g = 10 m/s²). How far from the base does it land?",
                 u * t, " m", f"t = √(2h/g) = {fmt(t)} s; x = u t.", wrongs=[u * h / 10, u * t / 2, u * 2 * t])


@gen("p11-03", weight=2)
def _circular(rng):
    v, r = R(rng, 5, 10, 20, 30), R(rng, 5, 10, 20, 50)
    return num_q(rng, f"A particle moves in a circle of radius {r} m at a constant speed of {v} m/s. Its centripetal acceleration is:",
                 v * v / r, " m/s²", "a = v²/r.", wrongs=[v / r, v * r, v * v * r])


@gen("p11-03")
def _omega(rng):
    t = R(rng, 2, 4, 10, 60)
    return num_q(rng, f"A wheel completes one revolution in {t} s. Its angular speed is:", 2 * math.pi / t, " rad/s",
                 "ω = 2π/T.", wrongs=[math.pi / t, t / (2 * math.pi), 1 / t])


@gen("p11-03")
def _maxrange(rng):
    u = R(rng, 10, 20, 30, 40)
    return num_q(rng, f"A projectile is thrown at {u} m/s. Its maximum possible horizontal range is (g = 10 m/s²):",
                 u * u / 10, " m", "Maximum range u²/g at 45°.", wrongs=[u * u / 20, u * u / 5, u / 10])


facts("p11-03", [
    "The range of a projectile is maximum at 45° launch angle",
    "Projectiles launched at θ and (90° - θ) with the same speed have equal ranges",
    "At the highest point of a projectile, the vertical velocity is zero",
    "In uniform circular motion the acceleration points towards the centre",
    "The horizontal velocity of a projectile stays constant (no air resistance)",
], [
    "The range of a projectile is maximum at 60°",
    "At the highest point the speed of a projectile is zero",
    "In uniform circular motion the velocity is constant",
    "The path of a projectile is a straight line",
    "Centripetal acceleration points along the tangent",
], "Motion in a Plane")


# ---------------------------------------------------------------- p11-04 Laws of Motion
@gen("p11-04", weight=2)
def _lift(rng):
    m, a = R(rng, 50, 60, 70, 80), R(rng, 1, 2, 3)
    up = rng.random() < 0.5
    val = m * (G + a) if up else m * (G - a)
    return num_q(rng, f"A {m} kg person stands in a lift accelerating {'upwards' if up else 'downwards'} at {a} m/s². The reading of a weighing scale (in N) is (g = 9.8):",
                 val, " N", "Apparent weight = m(g ± a).", wrongs=[m * G, m * (G - a) if up else m * (G + a), m * a])


@gen("p11-04", weight=2)
def _atwood(rng):
    m1, m2 = R(rng, 3, 4, 5, 6), R(rng, 1, 2)
    a = (m1 - m2) * G / (m1 + m2)
    t = 2 * m1 * m2 * G / (m1 + m2)
    if rng.random() < 0.5:
        return num_q(rng, f"Masses {m1} kg and {m2} kg hang over a frictionless pulley. Their acceleration is (g = 9.8):",
                     a, " m/s²", "a = (m1 - m2)g/(m1 + m2).", wrongs=[(m1 - m2) * G / m1, G, (m1 + m2) * G / (m1 - m2)])
    return num_q(rng, f"Masses {m1} kg and {m2} kg hang over a frictionless pulley. The string tension is (g = 9.8):",
                 t, " N", "T = 2m1m2g/(m1 + m2).", wrongs=[m1 * G, m2 * G, (m1 - m2) * G])


@gen("p11-04", weight=2)
def _impulse(rng):
    m, v1, v2 = R(rng, 0.1, 0.15, 0.2, 0.5), R(rng, 10, 20, 30), R(rng, 10, 20, 30)
    return num_q(rng, f"A {m} kg ball hits a wall at {v1} m/s and rebounds at {v2} m/s. The impulse on the ball has magnitude:",
                 m * (v1 + v2), " N s", "Impulse = change in momentum = m(v1 + v2).", wrongs=[m * abs(v1 - v2) or m, m * v1, 2 * m * v1 + 1])


@gen("p11-04")
def _incline(rng):
    th = R(rng, 30, 45, 60)
    return num_q(rng, f"A block slides down a smooth incline of {th}°. Its acceleration is (g = 9.8):", G * math.sin(math.radians(th)),
                 " m/s²", "a = g sin θ.", wrongs=[G * math.cos(math.radians(th)), G, G * math.tan(math.radians(th))])


facts("p11-04", [
    "Action and reaction act on different bodies",
    "Static friction can take any value up to its limiting value",
    "Kinetic friction is usually less than limiting static friction",
    "Inertia of a body depends on its mass",
    "The angle of repose equals the angle of friction",
], [
    "Action and reaction act on the same body and cancel",
    "Friction always opposes motion of the body as a whole, never helps it",
    "Kinetic friction depends on the area of contact",
    "A body moving at constant velocity has a net force on it",
    "Rolling friction is greater than sliding friction",
], "Laws of Motion")


# ---------------------------------------------------------------- p11-05 Work, Energy and Power
@gen("p11-05", weight=2)
def _ke(rng):
    m, v = R(rng, 2, 4, 5, 10), R(rng, 2, 4, 5, 10)
    return num_q(rng, f"Kinetic energy of a {m} kg body moving at {v} m/s is:", 0.5 * m * v * v, " J", "KE = ½mv².",
                 wrongs=[m * v * v, m * v, 0.5 * m * v])


@gen("p11-05", weight=2)
def _kescale(rng):
    f = R(rng, 2, 3, 4)
    kind = rng.choice(["speed", "momentum"])
    if kind == "speed":
        return num_q(rng, f"If the speed of a body becomes {f} times, its kinetic energy becomes:", f * f, " times", "KE ∝ v².",
                     form=lambda x: fmt(x), wrongs=[f, 2 * f, f ** 3])
    return num_q(rng, f"If the momentum of a body becomes {f} times (same mass), its kinetic energy becomes:", f * f, " times",
                 "KE = p²/2m.", form=lambda x: fmt(x), wrongs=[f, 2 * f, f ** 3])


@gen("p11-05", weight=2)
def _spring(rng):
    k, x = R(rng, 100, 200, 400, 800), R(rng, 0.05, 0.1, 0.2)
    return num_q(rng, f"A spring of constant {k} N/m is compressed by {x} m. Energy stored is:", 0.5 * k * x * x, " J",
                 "U = ½kx².", wrongs=[k * x * x, k * x, 0.5 * k * x])


@gen("p11-05", weight=2)
def _power(rng):
    m, h, t = R(rng, 50, 60, 100, 200), R(rng, 5, 10, 20), R(rng, 10, 20, 50)
    return num_q(rng, f"A motor lifts {m} kg through {h} m in {t} s. Its power is (g = 9.8):", m * G * h / t, " W", "P = mgh/t.",
                 wrongs=[m * h / t, m * G * h, m * G * h / t / 2])


facts("p11-05", [
    "Work done by a conservative force over a closed path is zero",
    "In an elastic collision both momentum and kinetic energy are conserved",
    "In a perfectly inelastic collision the bodies stick together",
    "Work done by the centripetal force in uniform circular motion is zero",
    "The work-energy theorem states that net work equals the change in kinetic energy",
], [
    "Kinetic energy is conserved in every collision",
    "Friction is a conservative force",
    "Work done by gravity depends on the path taken",
    "Power is the product of work and time",
    "Momentum is not conserved in an inelastic collision",
], "Work, Energy and Power")


# ---------------------------------------------------------------- p11-06 Rotational Motion
table("p11-06", [
    ("Ring about its central axis", "MR²"), ("Disc about its central axis", "½MR²"),
    ("Solid sphere about a diameter", "(2/5)MR²"), ("Hollow sphere about a diameter", "(2/3)MR²"),
    ("Thin rod about an axis through its centre, perpendicular to length", "ML²/12"),
    ("Thin rod about an axis through one end, perpendicular to length", "ML²/3"),
], "The moment of inertia of a {} is:", "Which body has moment of inertia {}?", weight=2)


@gen("p11-06", weight=2)
def _com(rng):
    m1, m2, d = R(rng, 1, 2, 3, 4), R(rng, 2, 3, 6), R(rng, 1, 2, 3, 4)
    return num_q(rng, f"Masses {m1} kg and {m2} kg are {d} m apart. The centre of mass is how far from the {m1} kg mass?",
                 m2 * d / (m1 + m2), " m", "x = m2 d/(m1 + m2).", wrongs=[m1 * d / (m1 + m2), d / 2, m2 * d / m1])


@gen("p11-06", weight=2)
def _torque(rng):
    f, r, th = R(rng, 10, 20, 50), R(rng, 0.2, 0.5, 1), R(rng, 30, 90)
    return num_q(rng, f"A force of {f} N acts at {r} m from the axis at {th}° to the lever arm. Torque is:",
                 f * r * math.sin(math.radians(th)), " N m", "τ = rF sin θ.", wrongs=[f * r * math.cos(math.radians(th)) or f * r / 3, f / r, f * r * 2])


@gen("p11-06")
def _rollke(rng):
    body, frac = rng.choice([("ring", 0.5), ("disc", 1 / 3), ("solid sphere", 2 / 7), ("hollow sphere", 0.4)])
    return num_q(rng, f"For a {body} rolling without slipping, the fraction of its kinetic energy that is rotational is:",
                 frac, form=lambda x: f"{x:.2f}", wrongs=[0.5, 1 / 3, 2 / 7, 0.4, 2 / 3],
                 explanation="Rotational fraction = k²/(k² + R²).")


facts("p11-06", [
    "Angular momentum is conserved when no external torque acts",
    "A spinning skater who pulls in her arms spins faster",
    "Torque is the rotational analogue of force",
    "Moment of inertia depends on the axis of rotation",
    "The parallel axis theorem is I = I_cm + Md²",
], [
    "Moment of inertia depends only on mass, not on its distribution",
    "A solid sphere and a ring of equal mass and radius have equal moments of inertia",
    "Angular momentum is conserved only when external torque acts",
    "The centre of mass must lie inside the body",
    "Torque and work have different dimensions",
], "Rotational Motion")


# ---------------------------------------------------------------- p11-07 Gravitation
@gen("p11-07", weight=2)
def _gheight(rng):
    k = R(rng, 1, 2, 3)
    return num_q(rng, f"At a height equal to {k} times the Earth's radius, g becomes what fraction of its surface value?",
                 1 / (k + 1) ** 2, form=lambda x: f"1/{round(1 / x)}", wrongs=[1 / (k + 1), 1 / k ** 2, 1 / (k + 2) ** 2],
                 explanation="g' = g R²/(R + h)².")


@gen("p11-07", weight=2)
def _kepler(rng):
    f = R(rng, 4, 9, 16)
    return num_q(rng, f"If a satellite's orbital radius becomes {f} times, its period becomes:", f ** 1.5, " times", "T² ∝ r³.",
                 form=lambda x: fmt(x), wrongs=[f, f * f, math.sqrt(f)])


@gen("p11-07", weight=2)
def _escape(rng):
    m, r = R(rng, 2, 4, 8, 9), R(rng, 2, 4, 1)
    return num_q(rng, f"A planet has {m} times Earth's mass and {r} times its radius. Its escape velocity is how many times Earth's?",
                 math.sqrt(m / r), " times", "ve = √(2GM/R).", form=lambda x: sig(x), wrongs=[m / r, math.sqrt(m * r), m / (r * r)])


@gen("p11-07")
def _weight(rng):
    m, r = R(rng, 2, 4, 0.5), R(rng, 2, 0.5)
    return num_q(rng, f"A planet has {m} times Earth's mass and {r} times its radius. A 60 kg person's weight there is (g on Earth = 10 m/s²):",
                 600 * m / (r * r), " N", "g ∝ M/R².", wrongs=[600 * m / r, 600 * m, 600 / (r * r)])


facts("p11-07", [
    "Escape velocity from Earth is about 11.2 km/s",
    "Orbital speed of a satellite close to Earth's surface is about 7.9 km/s",
    "A geostationary satellite has a period of 24 hours",
    "Acceleration due to gravity is zero at the centre of the Earth",
    "Kepler's second law follows from conservation of angular momentum",
], [
    "Escape velocity depends on the mass of the escaping body",
    "g increases with depth below the Earth's surface",
    "A geostationary satellite orbits from pole to pole",
    "Weightlessness in orbit means gravity is absent",
    "Orbital speed increases with orbit radius",
], "Gravitation")


# ---------------------------------------------------------------- p11-08 Mechanical Properties of Solids
@gen("p11-08", weight=2)
def _stress(rng):
    f, a = R(rng, 100, 200, 500, 1000), R(rng, 1e-6, 2e-6, 5e-6)
    return num_q(rng, f"A force of {f} N acts on a wire of cross-section {sci(a)} m². The stress is:", f / a, " N/m²",
                 "Stress = F/A.", form=sci, wrongs=[f * a, a / f, f / a / 10])


@gen("p11-08")
def _stretch(rng):
    n = R(rng, 2, 3)
    return num_q(rng, f"A wire is stretched to {n} times its length (volume constant). Its resistance becomes:", n * n, " times",
                 "R ∝ L² at constant volume.", form=lambda x: fmt(x), wrongs=[n, n ** 3, 1 / n])


table("p11-08", [
    ("Young's modulus", "Longitudinal stress / longitudinal strain"), ("Bulk modulus", "Hydraulic stress / volume strain"),
    ("Shear (rigidity) modulus", "Shearing stress / shearing strain"), ("Poisson's ratio", "Lateral strain / longitudinal strain"),
], "{} =", "Which quantity equals {}?")
facts("p11-08", [
    "Steel is more elastic than rubber",
    "Hooke's law holds within the elastic limit",
    "Strain has no units",
    "Elastic potential energy per unit volume = ½ × stress × strain",
], [
    "Rubber is more elastic than steel",
    "Strain is measured in N/m²",
    "Young's modulus of a material depends on the length of the wire",
    "Stress and pressure have different units",
], "Mechanical Properties of Solids")


# ---------------------------------------------------------------- p11-09 Mechanical Properties of Fluids
@gen("p11-09", weight=2)
def _torricelli(rng):
    h = R(rng, 5, 20, 45, 80)
    return num_q(rng, f"Water flows out of a small hole {h} m below the surface of a tank. Efflux speed is (g = 10):",
                 math.sqrt(20 * h), " m/s", "v = √(2gh).", wrongs=[math.sqrt(10 * h), 2 * h, 10 * h / 5])


@gen("p11-09", weight=2)
def _continuity(rng):
    a1, a2, v1 = R(rng, 10, 20, 40), R(rng, 2, 4, 5), R(rng, 1, 2, 3)
    return num_q(rng, f"Water flows at {v1} m/s through a pipe of area {a1} cm², which narrows to {a2} cm². Speed in the narrow part is:",
                 a1 * v1 / a2, " m/s", "A1v1 = A2v2.", wrongs=[a2 * v1 / a1, v1, a1 * v1 / a2 / 2])


@gen("p11-09", weight=2)
def _terminal(rng):
    f = R(rng, 2, 3, 4)
    return num_q(rng, f"If the radius of a falling raindrop is made {f} times, its terminal velocity becomes:", f * f, " times",
                 "vt ∝ r² (Stokes' law).", form=lambda x: fmt(x), wrongs=[f, f ** 3, math.sqrt(f)])


@gen("p11-09")
def _capillary(rng):
    f = R(rng, 2, 3, 4)
    return num_q(rng, f"If the radius of a capillary tube is made {f} times, the height of water rise becomes:", 1 / f, " times",
                 "h = 2T cos θ/(rρg), so h ∝ 1/r.", form=lambda x: f"1/{round(1 / x)}", wrongs=[f, 1 / f ** 2, f * f])


facts("p11-09", [
    "Pascal's law is used in hydraulic lifts and brakes",
    "Bernoulli's principle explains the lift on an aeroplane wing",
    "Viscosity of liquids decreases with rising temperature",
    "Viscosity of gases increases with rising temperature",
    "Excess pressure inside a liquid drop is 2T/r",
    "Surface tension decreases with rising temperature",
], [
    "Viscosity of liquids increases with temperature",
    "Excess pressure inside a soap bubble is 2T/r",
    "Surface tension increases with temperature",
    "Mercury rises in a glass capillary",
    "In streamline flow the velocity at a point keeps changing",
], "Mechanical Properties of Fluids")


# ---------------------------------------------------------------- p11-10 Thermal Properties of Matter
@gen("p11-10", weight=2)
def _ctof(rng):
    c = R(rng, -40, 0, 25, 37, 100, 50, -10)
    if rng.random() < 0.5:
        return num_q(rng, f"{c} °C on the Fahrenheit scale is:", c * 9 / 5 + 32, " °F", "F = 9C/5 + 32.",
                     wrongs=[c * 5 / 9 + 32, c * 9 / 5, c + 32], form=lambda x: fmt(x, 1))
    return num_q(rng, f"{c} °C in kelvin is:", c + 273.15, " K", "T = C + 273.15.", form=lambda x: fmt(x, 2),
                 wrongs=[c + 273.15 + 10, c - 273.15, c + 237.15])


@gen("p11-10", weight=2)
def _latent(rng):
    m = R(rng, 0.1, 0.5, 1, 2)
    kind = rng.choice([("melt ice at 0 °C", 3.34e5), ("boil water at 100 °C", 2.256e6)])
    return num_q(rng, f"Heat needed to {kind[0]} for {m} kg (L = {sci(kind[1])} J/kg) is:", m * kind[1], " J", "Q = mL.",
                 form=sci, wrongs=[kind[1] / m, m * kind[1] / 10, m * kind[1] * 2])


@gen("p11-10", weight=2)
def _wien(rng):
    t = R(rng, 3000, 5800, 6000, 1000)
    return num_q(rng, f"Using Wien's law (b = 2.9 × 10^-3 m K), the peak wavelength of a body at {t} K is:", 2.9e-3 / t * 1e9, " nm",
                 "λm = b/T.", wrongs=[2.9e-3 * t, 2.9e-3 / t * 1e6, 2.9e-3 / t * 1e10])


@gen("p11-10")
def _stefan(rng):
    f = R(rng, 2, 3, 0.5)
    return num_q(rng, f"If the absolute temperature of a black body becomes {f} times, the power it radiates becomes:", f ** 4, " times",
                 "P ∝ T⁴ (Stefan's law).", form=lambda x: fmt(x, 4), wrongs=[f * f, f ** 3, f])


facts("p11-10", [
    "Water has its maximum density at 4 °C",
    "The coefficient of volume expansion is about three times the linear coefficient",
    "Convection cannot take place in solids",
    "A good absorber of radiation is also a good emitter",
    "Heat transfer in vacuum is only by radiation",
], [
    "Water has its maximum density at 0 °C",
    "Radiation needs a material medium",
    "Metals are bad conductors of heat",
    "Black surfaces are poor emitters of radiation",
    "Linear expansion coefficient is three times the volume coefficient",
], "Thermal Properties of Matter")


# ---------------------------------------------------------------- p11-11 Thermodynamics
table("p11-11", [
    ("Isothermal process", "Temperature stays constant (ΔU = 0 for an ideal gas)"),
    ("Adiabatic process", "No heat exchange (Q = 0)"), ("Isochoric process", "Volume constant, so W = 0"),
    ("Isobaric process", "Pressure stays constant"), ("Cyclic process", "ΔU = 0 over the full cycle"),
], "In an {}:", "Which process: {}?")


@gen("p11-11", weight=3)
def _carnot(rng):
    t1, t2 = R(rng, 500, 600, 800, 400, 1000), R(rng, 300, 250, 200)
    if t2 >= t1:
        return None
    return num_q(rng, f"A Carnot engine works between {t1} K and {t2} K. Its efficiency is:", (1 - t2 / t1) * 100, "%",
                 "η = 1 - T2/T1.", wrongs=[t2 / t1 * 100, (t1 - t2) / t2 * 100, (1 - t2 / t1) * 50])


@gen("p11-11", weight=2)
def _firstlaw(rng):
    q, w = R(rng, 500, 800, 1000, 1200), R(rng, 200, 300, 400)
    return num_q(rng, f"A gas absorbs {q} J of heat and does {w} J of work. Change in its internal energy is:", q - w, " J",
                 "ΔU = Q - W.", form=lambda x: str(int(x)), wrongs=[q + w, w - q, q])


@gen("p11-11")
def _cop(rng):
    t1, t2 = R(rng, 300, 310), R(rng, 250, 260, 270)
    return num_q(rng, f"An ideal refrigerator keeps its inside at {t2} K in a room at {t1} K. Its coefficient of performance is:",
                 t2 / (t1 - t2), explanation="COP = T2/(T1 - T2).", wrongs=[t1 / (t1 - t2), (t1 - t2) / t2, t2 / t1])


facts("p11-11", [
    "The first law of thermodynamics is the law of conservation of energy",
    "The zeroth law of thermodynamics defines temperature",
    "No heat engine can be 100 per cent efficient",
    "In an adiabatic expansion an ideal gas cools",
    "Entropy of an isolated system never decreases",
], [
    "In an isothermal process no heat is exchanged",
    "A Carnot engine can be 100 per cent efficient",
    "In an isochoric process the gas does work",
    "Internal energy of an ideal gas depends on its volume",
    "The second law allows heat to flow on its own from cold to hot",
], "Thermodynamics")


# ---------------------------------------------------------------- p11-12 Kinetic Theory
table("p11-12", [
    ("Monatomic gas (He, Ne)", "γ = 5/3"), ("Diatomic gas (N2, O2) at room temperature", "γ = 7/5"),
    ("Polyatomic gas (non-linear, rigid)", "γ = 4/3"),
], "For a {}:", "Which gas has {}?")
table("p11-12", [
    ("Monatomic gas", "3 degrees of freedom"), ("Rigid diatomic gas", "5 degrees of freedom"),
    ("Rigid non-linear polyatomic gas", "6 degrees of freedom"),
], "A {} has:", None)


@gen("p11-12", weight=2)
def _rms(rng):
    f = R(rng, 4, 9, 16, 0.25)
    return num_q(rng, f"If the absolute temperature of a gas becomes {f} times, its rms speed becomes:", math.sqrt(f), " times",
                 "vrms ∝ √T.", form=lambda x: fmt(x), wrongs=[f, f * f, 1 / math.sqrt(f)])


@gen("p11-12", weight=2)
def _rmsmass(rng):
    pair = rng.choice([("H2", 2, "O2", 32), ("He", 4, "CH4", 16), ("H2", 2, "He", 4)])
    return num_q(rng, f"At the same temperature, the ratio of rms speeds v({pair[0]}) : v({pair[2]}) is:",
                 math.sqrt(pair[3] / pair[1]), " : 1", "vrms ∝ 1/√M.", form=lambda x: fmt(x),
                 wrongs=[pair[3] / pair[1], math.sqrt(pair[1] / pair[3]), pair[1] / pair[3]])


@gen("p11-12")
def _meanke(rng):
    t = R(rng, 300, 400, 600)
    return num_q(rng, f"The mean translational kinetic energy of a gas molecule at {t} K is (k = 1.38 × 10^-23 J/K):",
                 1.5 * 1.38e-23 * t, " J", "E = (3/2)kT.", form=sci, wrongs=[1.38e-23 * t, 3 * 1.38e-23 * t, 0.5 * 1.38e-23 * t])


# ---------------------------------------------------------------- p11-13 Oscillations
@gen("p11-13", weight=2)
def _shm(rng):
    a, w = R(rng, 0.02, 0.05, 0.1, 0.2), R(rng, 2, 5, 10, 20)
    if rng.random() < 0.5:
        return num_q(rng, f"A particle in SHM has amplitude {a} m and angular frequency {w} rad/s. Its maximum speed is:", a * w,
                     " m/s", "vmax = Aω.", wrongs=[a * w * w, a / w, w / a])
    return num_q(rng, f"A particle in SHM has amplitude {a} m and angular frequency {w} rad/s. Its maximum acceleration is:",
                 a * w * w, " m/s²", "amax = Aω².", wrongs=[a * w, a * w * w / 2, w * w / a])


@gen("p11-13", weight=2)
def _springcombo(rng):
    k = R(rng, 100, 200, 300)
    kind = rng.choice(["series", "parallel"])
    val = k / 2 if kind == "series" else 2 * k
    return num_q(rng, f"Two identical springs of constant {k} N/m are joined in {kind}. The effective spring constant is:", val,
                 " N/m", "Series: k/2; parallel: 2k.", form=lambda x: fmt(x), wrongs=[2 * k if kind == "series" else k / 2, k, 4 * k])


@gen("p11-13")
def _pendulum_scale(rng):
    f = R(rng, 4, 9, 16)
    return num_q(rng, f"If the length of a simple pendulum becomes {f} times, its period becomes:", math.sqrt(f), " times",
                 "T ∝ √L.", form=lambda x: fmt(x), wrongs=[f, f * f, 1 / math.sqrt(f)])


facts("p11-13", [
    "In SHM the acceleration is proportional to displacement and directed opposite to it",
    "The total energy of a simple harmonic oscillator is constant",
    "The period of a simple pendulum does not depend on the mass of the bob",
    "Kinetic energy in SHM is maximum at the mean position",
], [
    "The period of a simple pendulum depends on the mass of the bob",
    "In SHM the velocity is maximum at the extreme positions",
    "A pendulum clock runs faster on the Moon",
    "In SHM the acceleration is maximum at the mean position",
], "Oscillations")


# ---------------------------------------------------------------- p11-14 Waves
@gen("p11-14", weight=2)
def _pipes(rng):
    v, l = R(rng, 320, 330, 340), R(rng, 0.5, 0.85, 1, 0.25)
    kind = rng.choice(["open", "closed"])
    f = v / (2 * l) if kind == "open" else v / (4 * l)
    return num_q(rng, f"The fundamental frequency of an organ pipe {l} m long, {kind} at {'both ends' if kind == 'open' else 'one end'}, is (v = {v} m/s):",
                 f, " Hz", "Open: v/2L; closed: v/4L.", wrongs=[v / (4 * l) if kind == "open" else v / (2 * l), v / l, v * l])


@gen("p11-14", weight=2)
def _beats(rng):
    f1, d = R(rng, 256, 300, 440, 512), R(rng, 2, 3, 4, 5)
    return num_q(rng, f"Two tuning forks of {f1} Hz and {f1 + d} Hz are sounded together. Beats heard per second:", d, "",
                 "Beat frequency = |f1 - f2|.", form=lambda x: str(int(x)), wrongs=[2 * d, d + 1, f1 + d - f1 // 2])


@gen("p11-14", weight=2)
def _doppler(rng):
    f, vs, v = R(rng, 500, 600, 1000), R(rng, 10, 20, 30), 340
    return num_q(rng, f"A source of {f} Hz approaches a stationary listener at {vs} m/s (v = 340 m/s). The heard frequency is:",
                 f * v / (v - vs), " Hz", "f' = f v/(v - vs).", wrongs=[f * v / (v + vs), f * (v + vs) / v, f])


@gen("p11-14")
def _string(rng):
    t, mu, l = R(rng, 100, 160, 400), R(rng, 0.01, 0.04), R(rng, 0.5, 1)
    v = math.sqrt(t / mu)
    return num_q(rng, f"A string {l} m long with tension {t} N and linear density {mu} kg/m vibrates in its fundamental mode. Frequency:",
                 v / (2 * l), " Hz", f"v = √(T/μ) = {fmt(v)} m/s; f = v/2L.", wrongs=[v / l, v / (4 * l), v * 2 * l])


facts("p11-14", [
    "Sound waves in air are longitudinal",
    "Sound cannot travel through a vacuum",
    "A closed organ pipe produces only odd harmonics",
    "Speed of sound in air increases with temperature",
    "Speed of sound is greater in solids than in gases",
], [
    "Sound travels faster in air than in steel",
    "Light waves are longitudinal",
    "A closed pipe produces all harmonics",
    "Speed of sound in air depends on pressure at constant temperature",
    "Sound travels through a vacuum",
], "Waves")


# ---------------------------------------------------------------- p12-01 Electric Charges and Fields
@gen("p12-01", weight=2)
def _coulomb(rng):
    f = R(rng, 2, 3, 4, 0.5)
    kind = rng.choice(["distance", "each charge"])
    val = 1 / f ** 2 if kind == "distance" else f * f
    return num_q(rng, f"If the {kind} between/of two point charges is made {f} times, the Coulomb force becomes:", val, " times",
                 "F ∝ q1q2/r².", form=lambda x: fmt(x, 4), wrongs=[f, 1 / f, f ** 3 if kind == "each charge" else f * f])


@gen("p12-01", weight=2)
def _field(rng):
    q, r = R(rng, 1e-9, 2e-9, 5e-9, 1e-6), R(rng, 0.1, 0.3, 0.5, 1)
    return num_q(rng, f"Electric field at {r} m from a point charge of {sci(q)} C is (k = 9 × 10^9):", 9e9 * q / r ** 2, " N/C",
                 "E = kq/r².", form=sci, wrongs=[9e9 * q / r, 9e9 * q * r, 9e9 * q / r ** 3])


@gen("p12-01")
def _flux(rng):
    q = R(rng, 1, 2, 4, 8.85)
    return num_q(rng, f"A charge of {q} × 10^-12 C is enclosed in a closed surface. The electric flux through it is (ε0 = 8.85 × 10^-12):",
                 q / 8.85, " N m²/C", "Φ = q/ε0 (Gauss's law).", form=lambda x: sig(x), wrongs=[q * 8.85, 8.85 / q, q / 8.85 / 4])


facts("p12-01", [
    "Charge is quantised in units of e = 1.6 × 10^-19 C",
    "Electric field lines never cross each other",
    "Electric field inside a charged conductor is zero",
    "A dipole in a uniform field feels a torque but no net force",
    "Flux through a closed surface depends only on the enclosed charge",
], [
    "Electric field lines form closed loops",
    "Charge can be created or destroyed in isolation",
    "A dipole in a uniform field feels a large net force",
    "Field inside a charged conductor is maximum",
    "Like charges attract each other",
], "Electric Charges and Fields")


# ---------------------------------------------------------------- p12-02 Electrostatic Potential and Capacitance
@gen("p12-02", weight=2)
def _caps(rng):
    c1, c2 = R(rng, 2, 3, 4, 6), R(rng, 3, 6, 12)
    kind = rng.choice(["series", "parallel"])
    val = c1 * c2 / (c1 + c2) if kind == "series" else c1 + c2
    return num_q(rng, f"Capacitors of {c1} μF and {c2} μF are connected in {kind}. Equivalent capacitance:", val, " μF",
                 "Series: C1C2/(C1+C2); parallel: C1 + C2.", wrongs=[c1 + c2 if kind == "series" else c1 * c2 / (c1 + c2), c1 * c2, abs(c1 - c2) or 1])


@gen("p12-02", weight=2)
def _capenergy(rng):
    c, v = R(rng, 2, 5, 10, 20), R(rng, 10, 50, 100, 200)
    return num_q(rng, f"Energy stored in a {c} μF capacitor charged to {v} V is:", 0.5 * c * 1e-6 * v * v, " J", "U = ½CV².",
                 form=sci, wrongs=[c * 1e-6 * v * v, c * 1e-6 * v, 0.5 * c * 1e-6 * v])


@gen("p12-02", weight=2)
def _dielectric(rng):
    k = R(rng, 2, 3, 4, 5)
    return num_q(rng, f"A dielectric of constant {k} fills the gap of a parallel-plate capacitor. Its capacitance becomes:", k, " times",
                 "C = Kε0A/d.", form=lambda x: fmt(x), wrongs=[1 / k, k * k, math.sqrt(k)])


@gen("p12-02")
def _potential(rng):
    q, r = R(rng, 1e-9, 2e-9, 5e-9), R(rng, 0.1, 0.2, 0.5)
    return num_q(rng, f"Potential at {r} m from a {sci(q)} C point charge is (k = 9 × 10^9):", 9e9 * q / r, " V", "V = kq/r.",
                 wrongs=[9e9 * q / r ** 2, 9e9 * q * r, 9e9 * q / (2 * r)])


facts("p12-02", [
    "Equipotential surfaces are perpendicular to field lines",
    "No work is done in moving a charge on an equipotential surface",
    "Inside a hollow charged conductor the potential is constant",
    "Inserting a dielectric slab increases capacitance",
], [
    "Potential is a vector quantity",
    "Field lines run along equipotential surfaces",
    "Inserting a dielectric decreases capacitance",
    "Capacitors in series add up directly",
], "Electrostatic Potential and Capacitance")


# ---------------------------------------------------------------- p12-03 Current Electricity
@gen("p12-03", weight=2)
def _drift(rng):
    i, n, a = R(rng, 1, 2, 5), 8.5e28, R(rng, 1e-6, 2e-6)
    return num_q(rng, f"A current of {i} A flows in a copper wire of cross-section {sci(a)} m² (n = 8.5 × 10^28 /m³, e = 1.6 × 10^-19 C). Drift speed:",
                 i / (n * 1.6e-19 * a), " m/s", "v = I/(neA).", form=sci, wrongs=[i / (n * a), i * n * a, i / (n * 1.6e-19 * a) * 10])


@gen("p12-03", weight=2)
def _wheatstone(rng):
    p, q, r = R(rng, 2, 5, 10), R(rng, 4, 10, 20), R(rng, 3, 6, 15)
    return num_q(rng, f"A Wheatstone bridge is balanced with P = {p} Ω, Q = {q} Ω and R = {r} Ω. The fourth resistance S is:",
                 q * r / p, " Ω", "P/Q = R/S.", wrongs=[p * r / q, p * q / r, q / r * p])


@gen("p12-03", weight=2)
def _resist(rng):
    rho, l, a = R(rng, 1.7e-8, 2.8e-8, 1e-6), R(rng, 1, 10, 100), R(rng, 1e-6, 2e-6, 5e-7)
    return num_q(rng, f"A wire of resistivity {sci(rho)} Ω m, length {l} m and area {sci(a)} m² has resistance:", rho * l / a, " Ω",
                 "R = ρL/A.", form=sci, wrongs=[rho * a / l, rho / (l * a), rho * l * a])


table("p12-03", [
    ("Black", "0"), ("Brown", "1"), ("Red", "2"), ("Orange", "3"), ("Yellow", "4"), ("Green", "5"),
    ("Blue", "6"), ("Violet", "7"), ("Grey", "8"), ("White", "9"),
], "In the resistor colour code, {} stands for:", "Which colour stands for {} in the resistor colour code?")
facts("p12-03", [
    "Resistivity of metals increases with temperature",
    "Kirchhoff's junction rule follows from conservation of charge",
    "Kirchhoff's loop rule follows from conservation of energy",
    "A meter bridge works on the principle of a Wheatstone bridge",
    "Terminal voltage of a cell is less than its EMF while it supplies current",
], [
    "Resistivity of a wire depends on its length",
    "Resistivity of semiconductors increases with temperature",
    "Kirchhoff's junction rule follows from conservation of energy",
    "EMF of a cell depends on the external resistance",
    "Drift speed of electrons is close to the speed of light",
], "Current Electricity")


# ---------------------------------------------------------------- p12-04 Moving Charges and Magnetism
@gen("p12-04", weight=2)
def _loop(rng):
    i, r = R(rng, 1, 2, 5, 10), R(rng, 0.05, 0.1, 0.2)
    return num_q(rng, f"Magnetic field at the centre of a circular loop of radius {r} m carrying {i} A is (μ0 = 4π × 10^-7):",
                 4 * math.pi * 1e-7 * i / (2 * r), " T", "B = μ0 I/2R.", form=sci,
                 wrongs=[4 * math.pi * 1e-7 * i / (2 * math.pi * r), 4 * math.pi * 1e-7 * i / r, 4 * math.pi * 1e-7 * i * 2 * r])


@gen("p12-04", weight=2)
def _wire(rng):
    i, r = R(rng, 1, 2, 5, 10), R(rng, 0.01, 0.02, 0.05, 0.1)
    return num_q(rng, f"Magnetic field at {r} m from a long straight wire carrying {i} A is (μ0 = 4π × 10^-7):",
                 2e-7 * i / r, " T", "B = μ0 I/(2πr).", form=sci, wrongs=[2e-7 * i * r, 4e-7 * i / r, 2e-7 * i / r ** 2])


@gen("p12-04", weight=2)
def _radius(rng):
    f = R(rng, 2, 3, 4)
    kind = rng.choice(["speed", "magnetic field"])
    val = f if kind == "speed" else 1 / f
    return num_q(rng, f"A charged particle moves perpendicular to a uniform magnetic field. If its {kind} becomes {f} times, the radius of its path becomes:",
                 val, " times", "r = mv/qB.", form=lambda x: fmt(x, 3), wrongs=[1 / f if kind == "speed" else f, f * f, 1 / f ** 2])


@gen("p12-04")
def _shunt(rng):
    g, ig, i = R(rng, 50, 100), R(rng, 0.001, 0.005, 0.01), R(rng, 1, 5, 10)
    return num_q(rng, f"A galvanometer of resistance {g} Ω gives full deflection at {ig} A. The shunt needed to convert it into a {i} A ammeter:",
                 ig * g / (i - ig), " Ω", "S = Ig G/(I - Ig).", form=sci, wrongs=[g * i / ig, ig * g / i * 10, (i - ig) / (ig * g)])


facts("p12-04", [
    "A magnetic force on a moving charge does no work",
    "Parallel wires carrying currents in the same direction attract",
    "The cyclotron frequency does not depend on the speed of the particle",
    "A moving coil galvanometer is converted to a voltmeter with a high series resistance",
], [
    "A magnetic field changes the speed of a moving charge",
    "Parallel currents in the same direction repel",
    "An ammeter is made by adding a high resistance in series",
    "A stationary charge experiences a magnetic force",
], "Moving Charges and Magnetism")


# ---------------------------------------------------------------- p12-05 Magnetism and Matter
table("p12-05", [
    ("Bismuth", "Diamagnetic"), ("Copper", "Diamagnetic"), ("Water", "Diamagnetic"), ("Aluminium", "Paramagnetic"),
    ("Sodium", "Paramagnetic"), ("Oxygen gas", "Paramagnetic"), ("Iron", "Ferromagnetic"), ("Cobalt", "Ferromagnetic"),
    ("Nickel", "Ferromagnetic"),
], "{} is:", "Which of these is {}?", weight=2)
table("p12-05", [
    ("Diamagnetic substances", "Small negative susceptibility; weakly repelled by magnets"),
    ("Paramagnetic substances", "Small positive susceptibility; weakly attracted"),
    ("Ferromagnetic substances", "Large positive susceptibility; strongly attracted"),
    ("Curie temperature", "Above it a ferromagnet becomes paramagnetic"),
    ("Soft iron", "Low retentivity and coercivity; used in electromagnet cores"),
    ("Steel", "High retentivity and coercivity; used for permanent magnets"),
], "{}:", "Which is described: {}?")


@gen("p12-05", weight=2)
def _dip(rng):
    b, d = R(rng, 0.4, 0.5, 0.6), R(rng, 30, 45, 60)
    h = b * math.cos(math.radians(d))
    return num_q(rng, f"Earth's total magnetic field is {b} G and the angle of dip is {d}°. The horizontal component is:", h, " G",
                 "H = B cos δ.", wrongs=[b * math.sin(math.radians(d)), b * math.tan(math.radians(d)), b])


facts("p12-05", [
    "Magnetic field lines form closed loops",
    "Magnetic monopoles have not been found",
    "Susceptibility of a paramagnet varies inversely with temperature (Curie's law)",
    "The angle of dip is 90° at the magnetic poles",
], [
    "Magnetic field lines start at the north pole and end inside the magnet at the south pole only",
    "Isolated magnetic poles are common",
    "Diamagnetism depends strongly on temperature",
    "The angle of dip is 90° at the magnetic equator",
], "Magnetism and Matter")


# ---------------------------------------------------------------- p12-06 Electromagnetic Induction
@gen("p12-06", weight=2)
def _faraday(rng):
    n, d_phi, t = R(rng, 50, 100, 200), R(rng, 0.01, 0.02, 0.05), R(rng, 0.1, 0.2, 0.5)
    return num_q(rng, f"Flux through each turn of a {n}-turn coil changes by {d_phi} Wb in {t} s. Induced EMF is:", n * d_phi / t,
                 " V", "ε = N dΦ/dt.", wrongs=[d_phi / t, n * d_phi * t, n * t / d_phi])


@gen("p12-06", weight=2)
def _inductor(rng):
    l, i = R(rng, 0.1, 0.2, 0.5, 2), R(rng, 1, 2, 4, 5)
    return num_q(rng, f"Energy stored in an inductor of {l} H carrying {i} A is:", 0.5 * l * i * i, " J", "U = ½LI².",
                 wrongs=[l * i * i, l * i, 0.5 * l * i])


facts("p12-06", [
    "Lenz's law follows from conservation of energy",
    "Eddy currents are reduced by using laminated cores",
    "The induced EMF opposes the change in flux that causes it",
    "Self-inductance of a coil increases with the number of turns",
], [
    "Lenz's law follows from conservation of charge",
    "Eddy currents are increased by laminating the core",
    "The induced current always helps the change that produces it",
    "A steady current induces an EMF in a nearby coil",
], "Electromagnetic Induction")


# ---------------------------------------------------------------- p12-07 Alternating Current
@gen("p12-07", weight=2)
def _xl(rng):
    f, l = R(rng, 50, 60, 100), R(rng, 0.1, 0.2, 0.5)
    return num_q(rng, f"Inductive reactance of a {l} H inductor at {f} Hz is:", 2 * math.pi * f * l, " Ω", "XL = 2πfL.",
                 wrongs=[f * l, 2 * math.pi * f / l, 1 / (2 * math.pi * f * l)])


@gen("p12-07", weight=2)
def _xc(rng):
    f, c = R(rng, 50, 60, 100), R(rng, 10e-6, 20e-6, 100e-6)
    return num_q(rng, f"Capacitive reactance of a {fmt(c * 1e6)} μF capacitor at {f} Hz is:", 1 / (2 * math.pi * f * c), " Ω",
                 "XC = 1/(2πfC).", wrongs=[2 * math.pi * f * c, 1 / (f * c), 1 / (2 * math.pi * f * c) / 10])


@gen("p12-07")
def _impedance(rng):
    r, x = rng.choice([(3, 4), (6, 8), (5, 12), (8, 15)])
    return num_q(rng, f"A series circuit has R = {r} Ω and net reactance {x} Ω. Its impedance is:", math.hypot(r, x), " Ω",
                 "Z = √(R² + X²).", wrongs=[r + x, abs(x - r), r * x / (r + x)])


facts("p12-07", [
    "At resonance in a series LCR circuit, current is maximum",
    "In a purely inductive circuit, current lags voltage by 90°",
    "In a purely capacitive circuit, current leads voltage by 90°",
    "Average power in a purely inductive circuit is zero",
    "A step-up transformer has more turns in the secondary coil",
], [
    "At resonance the impedance of a series LCR circuit is maximum",
    "In a purely capacitive circuit, current lags voltage",
    "A transformer works on DC",
    "A step-up transformer increases both voltage and current",
    "The power factor of a purely resistive circuit is zero",
], "Alternating Current")


# ---------------------------------------------------------------- p12-08 Electromagnetic Waves
table("p12-08", [
    ("Gamma rays", "Nuclear reactions and radioactive decay; used to treat cancer"),
    ("X-rays", "Medical diagnosis of bone fractures"),
    ("Ultraviolet rays", "Water purification; absorbed by the ozone layer"),
    ("Infrared rays", "Heat waves; used in TV remotes and physical therapy"),
    ("Microwaves", "Radar and microwave ovens"),
    ("Radio waves", "Radio and TV broadcasting"),
], "Use or source of {}:", "Which radiation: {}?", weight=2)


@gen("p12-08", weight=2)
def _order(rng):
    seq = ["Radio waves", "Microwaves", "Infrared", "Visible light", "Ultraviolet", "X-rays", "Gamma rays"]
    i = rng.randrange(len(seq) - 1)
    kind = rng.choice(["longer", "shorter"])
    if kind == "shorter":
        ans = seq[i + 1]
        wr = [s for s in seq if seq.index(s) <= i][-3:]
    else:
        ans = seq[i]
        wr = [s for s in seq if seq.index(s) > i + 1][:3]
        if len(wr) < 3:
            wr = wr + [s for s in seq if seq.index(s) < i][: 3 - len(wr)]
    if len(wr) < 3:
        return None
    return Q(f"Which radiation is next {'shorter' if kind == 'shorter' else 'longer'} in wavelength than {seq[i] if kind == 'shorter' else seq[i + 1]}?",
             ans, wr, "Order of decreasing wavelength: " + ", ".join(seq) + ".")


@gen("p12-08")
def _c(rng):
    f = R(rng, 1e6, 1e8, 3e9, 6e14)
    return num_q(rng, f"An electromagnetic wave has frequency {sci(f)} Hz. Its wavelength in vacuum is:", 3e8 / f, " m", "λ = c/f.",
                 form=sci, wrongs=[f / 3e8, 3e8 * f, 3e8 / f * 10])


facts("p12-08", [
    "Electromagnetic waves are transverse",
    "Electromagnetic waves need no medium to travel",
    "Maxwell introduced the displacement current",
    "Hertz first produced electromagnetic waves in the laboratory",
], [
    "Electromagnetic waves are longitudinal",
    "Electromagnetic waves cannot travel in vacuum",
    "X-rays have longer wavelength than microwaves",
    "Infrared has shorter wavelength than ultraviolet",
], "Electromagnetic Waves")


# ---------------------------------------------------------------- p12-09 Ray Optics
@gen("p12-09", weight=2)
def _mirror(rng):
    f, u = R(rng, -10, -15, -20), R(rng, -30, -40, -60)
    if u == f:
        return None
    v = 1 / (1 / f - 1 / u)
    return num_q(rng, f"An object is {abs(u)} cm in front of a concave mirror of focal length {abs(f)} cm. The image distance is:",
                 abs(v), " cm in front of the mirror", "1/v + 1/u = 1/f.", wrongs=[abs(1 / (1 / f + 1 / u)), abs(u - f), abs(u + f)])


@gen("p12-09", weight=2)
def _prism(rng):
    a, d = rng.choice([(60, 30), (60, 38), (60, 48), (60, 60)])
    n = math.sin(math.radians((a + d) / 2)) / math.sin(math.radians(a / 2))
    return num_q(rng, f"A prism of angle {a}° gives a minimum deviation of {d}°. Its refractive index is:", n,
                 explanation="n = sin((A + D)/2)/sin(A/2).", wrongs=[math.sin(math.radians(a)) / math.sin(math.radians(d)), (a + d) / a, n + 0.2])


@gen("p12-09", weight=2)
def _telescope(rng):
    fo, fe = R(rng, 100, 150, 200), R(rng, 5, 10, 20)
    if rng.random() < 0.5:
        return num_q(rng, f"An astronomical telescope has objective focal length {fo} cm and eyepiece {fe} cm. Magnifying power (normal adjustment):",
                     fo / fe, "", "m = fo/fe.", form=lambda x: fmt(x), wrongs=[fe / fo, fo * fe / 100, fo + fe])
    return num_q(rng, f"An astronomical telescope has objective {fo} cm and eyepiece {fe} cm. Its tube length in normal adjustment is:",
                 fo + fe, " cm", "L = fo + fe.", form=lambda x: fmt(x), wrongs=[fo - fe, fo / fe, fo * fe])


@gen("p12-09")
def _power_lens(rng):
    f = R(rng, 20, 25, 50, -40, -50)
    return num_q(rng, f"The power of a lens of focal length {f} cm is:", 100 / f, " D", "P = 100/f(cm).",
                 wrongs=[f / 100, -100 / f, 1 / f])


facts("p12-09", [
    "Total internal reflection happens only when light goes from a denser to a rarer medium",
    "Optical fibres work by total internal reflection",
    "A convex mirror always forms a virtual, erect, diminished image",
    "The refractive index of a medium is highest for violet light",
    "Mirages are caused by total internal reflection",
], [
    "A concave mirror always forms a virtual image",
    "Red light is deviated more than violet light by a prism",
    "Total internal reflection happens from rarer to denser medium",
    "A convex lens always forms a real image",
    "The critical angle is larger for a denser medium",
], "Ray Optics and Optical Instruments")


# ---------------------------------------------------------------- p12-10 Wave Optics
@gen("p12-10", weight=2)
def _malus(rng):
    th = R(rng, 30, 45, 60)
    return num_q(rng, f"Polarised light of intensity I0 falls on an analyser at {th}° to the polariser axis. Transmitted intensity is:",
                 math.cos(math.radians(th)) ** 2, " I0", "I = I0 cos²θ (Malus's law).", form=lambda x: f"{x:.2f}",
                 wrongs=[math.cos(math.radians(th)), math.sin(math.radians(th)) ** 2, 0.5])


@gen("p12-10", weight=2)
def _brewster(rng):
    n = R(rng, 1.5, 1.73, 1.33)
    return num_q(rng, f"The Brewster angle for light going from air to a medium of refractive index {n} is about:",
                 math.degrees(math.atan(n)), "°", "tan θB = n.", form=lambda x: f"{x:.0f}",
                 wrongs=[math.degrees(math.asin(1 / n)), math.degrees(math.atan(1 / n)), 45])


@gen("p12-10")
def _fringe_scale(rng):
    f = R(rng, 2, 3)
    kind = rng.choice(["slit separation", "screen distance"])
    val = 1 / f if kind == "slit separation" else f
    return num_q(rng, f"In Young's experiment, if the {kind} is made {f} times, the fringe width becomes:", val, " times",
                 "β = λD/d.", form=lambda x: fmt(x, 3), wrongs=[f if kind == "slit separation" else 1 / f, f * f, 1])


facts("p12-10", [
    "Polarisation shows that light is a transverse wave",
    "Huygens' principle treats every point on a wavefront as a source of secondary wavelets",
    "Coherent sources are needed for a sustained interference pattern",
    "In single-slit diffraction the central maximum is twice as wide as the others",
], [
    "Sound waves can be polarised",
    "Interference violates conservation of energy",
    "In single-slit diffraction all maxima have equal width",
    "Fringe width increases when slit separation increases",
], "Wave Optics")


# ---------------------------------------------------------------- p12-11 Dual Nature
@gen("p12-11", weight=2)
def _photon(rng):
    lam = R(rng, 200, 310, 400, 496, 620)
    return num_q(rng, f"Energy of a photon of wavelength {lam} nm (hc = 1240 eV nm) is:", 1240 / lam, " eV", "E = hc/λ.",
                 wrongs=[lam / 1240, 1240 / lam / 2, 12400 / lam])


@gen("p12-11", weight=2)
def _stopping(rng):
    lam, phi = R(rng, 200, 248, 310), R(rng, 2, 2.5, 3)
    k = 1240 / lam - phi
    if k <= 0:
        return None
    return num_q(rng, f"Light of {lam} nm falls on a metal of work function {phi} eV. The stopping potential is:", k, " V",
                 "eV0 = hc/λ - φ.", wrongs=[1240 / lam, 1240 / lam + phi, phi])


@gen("p12-11", weight=2)
def _debroglie(rng):
    v = R(rng, 100, 150, 400, 10000)
    return num_q(rng, f"An electron is accelerated through {v} V. Its de Broglie wavelength is (λ = 1.227/√V nm):",
                 1.227 / math.sqrt(v), " nm", "λ = 1.227/√V nm.", wrongs=[1.227 / v, 1.227 * math.sqrt(v), 12.27 / math.sqrt(v)])


@gen("p12-11")
def _threshold(rng):
    phi = R(rng, 2, 2.48, 3.1, 4.13)
    return num_q(rng, f"The threshold wavelength for a metal of work function {phi} eV is (hc = 1240 eV nm):", 1240 / phi, " nm",
                 "λ0 = hc/φ.", wrongs=[phi * 1240 / 1000, 1240 / phi / 2, 124 / phi])


facts("p12-11", [
    "Photoelectric emission is instantaneous",
    "The maximum kinetic energy of photoelectrons depends on frequency, not intensity",
    "Photocurrent increases with intensity above the threshold frequency",
    "The Davisson-Germer experiment showed the wave nature of electrons",
], [
    "Photoelectric emission occurs for any frequency if the light is bright enough",
    "The kinetic energy of photoelectrons increases with intensity",
    "Stopping potential depends on the intensity of light",
    "Davisson-Germer showed the particle nature of light",
], "Dual Nature of Radiation and Matter")


# ---------------------------------------------------------------- p12-12 Atoms
table("p12-12", [
    ("Lyman series", "Transitions to n = 1; ultraviolet"), ("Balmer series", "Transitions to n = 2; visible"),
    ("Paschen series", "Transitions to n = 3; infrared"), ("Brackett series", "Transitions to n = 4; infrared"),
    ("Pfund series", "Transitions to n = 5; infrared"),
], "The {} of hydrogen involves:", "Which hydrogen series: {}?")


@gen("p12-12", weight=2)
def _bohr_r(rng):
    n = R(rng, 2, 3, 4, 5)
    return num_q(rng, f"The radius of the n = {n} Bohr orbit of hydrogen (a0 = 0.53 Å) is:", 0.53 * n * n, " Å", "r = n² a0.",
                 wrongs=[0.53 * n, 0.53 / n, 0.53 * n ** 3])


@gen("p12-12", weight=2)
def _transition(rng):
    n1, n2 = rng.choice([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (1, 4)])
    e = 13.6 * (1 / n1 ** 2 - 1 / n2 ** 2)
    return num_q(rng, f"Energy of the photon emitted when a hydrogen electron falls from n = {n2} to n = {n1} is:", e, " eV",
                 "ΔE = 13.6(1/n1² - 1/n2²) eV.", wrongs=[13.6 / n2 ** 2, 13.6 / n1 ** 2, 13.6 * (1 / n1 - 1 / n2)])


facts("p12-12", [
    "Rutherford's alpha-scattering showed that the nucleus is tiny and positive",
    "In Bohr's model, angular momentum is quantised as nh/2π",
    "The ionisation energy of hydrogen in its ground state is 13.6 eV",
    "Most alpha particles passed undeflected through the gold foil",
], [
    "Most alpha particles bounced straight back from the gold foil",
    "Electron energy in a Bohr orbit is positive",
    "The Balmer series lies in the ultraviolet",
    "Orbit radius in hydrogen is proportional to n",
], "Atoms")


# ---------------------------------------------------------------- p12-13 Nuclei
@gen("p12-13", weight=2)
def _decay(rng):
    a, z = rng.choice([(238, 92), (226, 88), (232, 90), (210, 84)])
    na, nb = rng.choice([(1, 0), (1, 1), (2, 1), (1, 2), (3, 2), (2, 2)])
    a2, z2 = a - 4 * na, z - 2 * na + nb
    ans = f"A = {a2}, Z = {z2}"
    wr = [f"A = {a - 4 * na}, Z = {z - 2 * na - nb}", f"A = {a - 2 * na}, Z = {z - 4 * na + nb}", f"A = {a - 4 * na - nb}, Z = {z - 2 * na}",
          f"A = {a}, Z = {z - na + nb}"]
    return Q(f"A nucleus with A = {a}, Z = {z} emits {na} alpha and {nb} beta-minus particle(s). The final nucleus has:", ans, wr,
             "Each alpha: A - 4, Z - 2. Each beta-minus: Z + 1.")


@gen("p12-13", weight=2)
def _radius_n(rng):
    a1, a2 = rng.choice([(27, 64), (8, 27), (1, 125), (27, 216), (64, 125)])
    r1, r2 = round(a1 ** (1 / 3)), round(a2 ** (1 / 3))
    return Q(f"The ratio of nuclear radii for mass numbers {a1} and {a2} is:", f"{r1} : {r2}",
             [f"{a1} : {a2}", f"{r2} : {r1}", f"{r1 * r1} : {r2 * r2}"], "R = R0 A^(1/3).")


@gen("p12-13", weight=2)
def _binding(rng):
    dm = R(rng, 0.01, 0.02, 0.03, 0.1)
    return num_q(rng, f"A nucleus has a mass defect of {dm} u. Its binding energy is (1 u = 931.5 MeV):", dm * 931.5, " MeV",
                 "BE = Δm × 931.5 MeV.", wrongs=[dm * 931.5 / 2, dm * 9.315, dm * 3e8])


@gen("p12-13")
def _halflife(rng):
    t, n = R(rng, 2, 5, 10, 20), R(rng, 2, 3, 4)
    return num_q(rng, f"A radioactive sample has a half-life of {t} days. What fraction remains after {n * t} days?", 1 / 2 ** n, "",
                 f"{n} half-lives: (1/2)^{n}.", form=lambda x: f"1/{round(1 / x)}", wrongs=[1 / (2 * n), 1 / n, 1 / 2 ** (n + 1)])


facts("p12-13", [
    "Nuclear forces are short-range and charge-independent",
    "Binding energy per nucleon is highest near iron (A ≈ 56)",
    "Nuclear density is roughly the same for all nuclei",
    "Fusion of light nuclei powers the Sun",
    "Gamma emission does not change A or Z",
], [
    "Nuclear forces are long-range",
    "Nuclear density increases with mass number",
    "Beta-minus decay reduces the atomic number by one",
    "Fission powers the Sun",
    "Binding energy per nucleon is highest for uranium",
], "Nuclei")


# ---------------------------------------------------------------- p12-14 Semiconductor Electronics
table("p12-14", [
    ("Phosphorus", "n-type (pentavalent donor)"), ("Arsenic", "n-type (pentavalent donor)"), ("Antimony", "n-type (pentavalent donor)"),
    ("Boron", "p-type (trivalent acceptor)"), ("Aluminium", "p-type (trivalent acceptor)"), ("Indium", "p-type (trivalent acceptor)"),
], "Doping silicon with {} makes it:", "Which dopant makes silicon {}?")


@gen("p12-14", weight=3)
def _gate(rng):
    gate = rng.choice(["AND", "OR", "NAND", "NOR"])
    a, b = rng.choice([0, 1]), rng.choice([0, 1])
    out = {"AND": a & b, "OR": a | b, "NAND": 1 - (a & b), "NOR": 1 - (a | b)}[gate]
    return Q(f"Inputs A = {a} and B = {b} are fed to a {gate} gate. The output is:", str(out),
             [str(1 - out), "Cannot be determined", "2"], f"{gate}({a}, {b}) = {out}.")


facts("p12-14", [
    "In a forward-biased p-n junction the depletion layer becomes thinner",
    "A Zener diode is used as a voltage regulator in reverse bias",
    "NAND and NOR are universal gates",
    "In an n-type semiconductor electrons are the majority carriers",
    "A full-wave rectifier uses both halves of the AC cycle",
], [
    "In reverse bias the depletion layer becomes thinner",
    "Holes are the majority carriers in n-type semiconductors",
    "A Zener diode regulates voltage in forward bias",
    "AND and OR are universal gates",
    "An intrinsic semiconductor has more electrons than holes",
], "Semiconductor Electronics")


# ---------------------------------------------------------------- p12-15 Experimental Skills
@gen("p12-15", weight=3)
def _vernier(rng):
    msr = R(rng, 2.1, 3.4, 1.5, 4.2, 0.8)
    vc = R(rng, 3, 5, 7, 8)
    lc = 0.01
    zero = R(rng, 0, 0, 0.02, -0.03)
    val = msr + vc * lc - zero
    return num_q(rng, f"A vernier caliper (least count 0.01 cm, zero error {zero:+.2f} cm) shows main scale {msr} cm and vernier division {vc}. The corrected length is:",
                 val, " cm", "Reading = MSR + VSD × LC - zero error.", form=lambda x: f"{x:.2f}",
                 wrongs=[msr + vc * lc + zero if zero else msr + vc * 0.1, msr + vc * 0.1 - zero, msr - zero])


@gen("p12-15", weight=2)
def _screw(rng):
    pitch, div = R(rng, 0.5, 1), R(rng, 50, 100)
    lc = pitch / div
    return num_q(rng, f"A screw gauge has a pitch of {pitch} mm and {div} circular scale divisions. Its least count is:", lc, " mm",
                 "LC = pitch/number of divisions.", form=lambda x: f"{x:.3f}", wrongs=[div / pitch / 1000, pitch / 10, lc * 10])


@gen("p12-15", weight=2)
def _meterbridge(rng):
    s, l = R(rng, 2, 4, 5, 10), R(rng, 40, 60, 25, 75)
    return num_q(rng, f"In a metre bridge, the balance point is {l} cm from the end of the unknown resistance X with S = {s} Ω in the other gap. X is:",
                 s * l / (100 - l), " Ω", "X/S = l/(100 - l).", wrongs=[s * (100 - l) / l, s * l / 100, s])


table("p12-15", [
    ("Young's modulus of a wire", "Searle's apparatus"), ("Speed of sound in air", "Resonance tube"),
    ("Surface tension of water", "Capillary rise"), ("Viscosity of a liquid", "Terminal velocity of a falling ball"),
    ("Specific heat of a liquid", "Method of mixtures"), ("Resistivity of a wire", "Metre bridge"),
    ("Resistance of a galvanometer", "Half-deflection method"),
    ("Focal length of a convex lens", "u-v method on an optical bench"),
    ("Refractive index of a glass slab", "Travelling microscope"),
], "{} is measured using:", "{} is used to measure:", weight=2)
