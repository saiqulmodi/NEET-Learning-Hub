"""High-yield NEET Physics, second batch (Classes 11-12): more original problems of the kinds NEET asks again and again.

Tagged "hy2" so it is generated after the first high-yield batch and existing question ids never move. Answers are computed.
"""
import math

from .core import table, facts, gen, num_q, Q, fmt, sci, tag

tag("hy2")
G = 10


def R(rng, *xs):
    return rng.choice(xs)


# ---------------------------------------------------------------- Class 11
table("p11-01", [
    ("Coefficient of viscosity", "Pa s (poise in CGS)"), ("Surface tension", "N/m"), ("Young's modulus", "N/m² (Pa)"),
    ("Thermal conductivity", "W m⁻¹ K⁻¹"), ("Specific heat capacity", "J kg⁻¹ K⁻¹"), ("Universal gas constant", "J mol⁻¹ K⁻¹"),
    ("Permittivity of free space", "C² N⁻¹ m⁻²"), ("Magnetic permeability", "T m A⁻¹"),
], "The SI unit of {} is:", "{} is the SI unit of:", weight=2)


@gen("p11-02", weight=2)
def _vt_area(rng):
    v, t1, t2 = R(rng, 10, 20, 30), R(rng, 2, 4, 5), R(rng, 5, 10, 6)
    d = 0.5 * v * t1 + v * t2
    return num_q(rng, f"A car accelerates uniformly from rest to {v} m/s in {t1} s, then moves at that speed for {t2} s. The total distance is:", d, " m",
                 "Area under the v-t graph.", wrongs=[v * (t1 + t2), 0.5 * v * (t1 + t2), v * t2])


@gen("p11-02", weight=2)
def _two_balls(rng):
    h = R(rng, 20, 45, 80, 125)
    u = R(rng, 10, 20)
    t = h / u
    return num_q(rng, f"A ball is dropped from {h} m while another is thrown up from the ground at {u} m/s along the same line. They meet after:", t, " s",
                 "Relative speed is u, relative acceleration 0: t = h/u.", wrongs=[math.sqrt(2 * h / G), h / (2 * u), 2 * h / u])


@gen("p11-03", weight=2)
def _rain(rng):
    vr, vm = R(rng, 3, 4, 6, 8), R(rng, 3, 4, 6, 8)
    ang = math.degrees(math.atan(vm / vr))
    return num_q(rng, f"Rain falls vertically at {vr} m/s. A person walks at {vm} m/s. To keep dry, the umbrella should tilt from the vertical by:", ang, "°",
                 "tanθ = v(man)/v(rain).", wrongs=[90 - ang, math.degrees(math.atan(vr / vm)) + 5, 45 if abs(ang - 45) > 1 else 30], form=lambda x: fmt(x, 1))


@gen("p11-04", weight=2)
def _connected(rng):
    m1, m2, f = R(rng, 2, 3, 4), R(rng, 1, 2, 6), R(rng, 12, 18, 24, 30)
    a = f / (m1 + m2)
    return num_q(rng, f"Blocks of {m1} kg and {m2} kg on a smooth floor are pushed by {f} N applied to the {m1} kg block. The contact force between them is:",
                 m2 * a, " N", "a = F/(m1 + m2); contact force = m2 a.", wrongs=[m1 * a, f, f / 2])


@gen("p11-04", weight=2)
def _incline(rng):
    th = R(rng, 30, 37, 45, 53, 60)
    mu = R(rng, 0, 0.2, 0.25, 0.5)
    s, c = math.sin(math.radians(th)), math.cos(math.radians(th))
    a = G * (s - mu * c)
    if a <= 0:
        return None
    return num_q(rng, f"A block slides down a {th}° incline with μk = {mu} (g = 10 m/s²). Its acceleration is:", a, " m/s²", "a = g(sinθ - μ cosθ).",
                 wrongs=[G * s, G * (s + mu * c), G * (c - mu * s)])


@gen("p11-05", weight=2)
def _work_variable(rng):
    k, x1, x2 = R(rng, 100, 200, 500), R(rng, 0, 0.1, 0.2), R(rng, 0.3, 0.4, 0.5)
    return num_q(rng, f"A spring (k = {k} N/m) is stretched from {x1} m to {x2} m. The work done is:", 0.5 * k * (x2 ** 2 - x1 ** 2), " J",
                 "W = ½k(x2² - x1²).", wrongs=[0.5 * k * (x2 - x1) ** 2, k * (x2 ** 2 - x1 ** 2), 0.5 * k * x2 ** 2 if x1 else k * x2])


@gen("p11-05", weight=2)
def _restitution(rng):
    h, e = R(rng, 5, 10, 20), R(rng, 0.5, 0.6, 0.8)
    return num_q(rng, f"A ball dropped from {h} m bounces with a coefficient of restitution of {e}. It rises to:", e * e * h, " m", "h' = e²h.",
                 wrongs=[e * h, h * (1 - e), h / e])


@gen("p11-06", weight=2)
def _torque(rng):
    f, r, th = R(rng, 10, 20, 50), R(rng, 0.2, 0.5, 1), R(rng, 30, 90, 60)
    return num_q(rng, f"A force of {f} N acts at {r} m from the axis, at {th}° to the lever arm. The torque is:", f * r * math.sin(math.radians(th)), " N m",
                 "τ = rF sinθ.", wrongs=[f * r, f * r * math.cos(math.radians(th)) or f, f / r])


@gen("p11-06", weight=2)
def _parallel_axis(rng):
    body, icm, d = rng.choice([("disc about a tangent perpendicular to its plane", "MR²/2", "3MR²/2"), ("ring about a tangent perpendicular to its plane", "MR²", "2MR²"),
                               ("solid sphere about a tangent", "2MR²/5", "7MR²/5"), ("rod about one end (perpendicular)", "ML²/12", "ML²/3"),
                               ("disc about a tangent in its plane", "MR²/4", "5MR²/4")])
    return Q(f"Using the parallel or perpendicular axis theorem, the moment of inertia of a {body} is:", d,
             ["3MR²/2", "2MR²", "7MR²/5", "ML²/3", "5MR²/4", "MR²"], f"I = I(cm) + Md² with I(cm) = {icm}.")


@gen("p11-07", weight=2)
def _orbital(rng):
    f = R(rng, 4, 9, 16)
    ask = rng.choice(["speed", "ke"])
    if ask == "speed":
        return num_q(rng, f"A satellite moves to an orbit of {f} times the radius. Its orbital speed becomes how many times?", 1 / math.sqrt(f), " times",
                     "v = √(GM/r).", wrongs=[math.sqrt(f), 1 / f, f], form=lambda x: fmt(x, 3))
    return Q("For a satellite in a circular orbit, total energy E, kinetic energy K and potential energy U are related by:", "E = -K = U/2",
             ["E = K = U", "E = K + U = 0", "E = -U = K/2", "E = 2K = -U"], "K = GMm/2r, U = -GMm/r, E = -GMm/2r.")


@gen("p11-08", weight=2)
def _bulk(rng):
    b, p = R(rng, 2e9, 2.2e9, 1.6e11), R(rng, 1e6, 2e7, 1e5)
    return num_q(rng, f"A material has bulk modulus {sci(b)} Pa. Under an extra pressure of {sci(p)} Pa, its fractional change in volume is:", p / b, "",
                 "ΔV/V = p/B.", wrongs=[b / p, p * b, p / b * 100], form=lambda x: sci(x))


@gen("p11-09", weight=2)
def _torricelli(rng):
    h = R(rng, 0.45, 0.8, 1.25, 5, 20)
    return num_q(rng, f"Water flows out of a small hole {fmt(h)} m below the surface of a tank (g = 10 m/s²). The efflux speed is:", math.sqrt(2 * G * h), " m/s",
                 "Torricelli: v = √(2gh).", wrongs=[math.sqrt(G * h), 2 * G * h, math.sqrt(4 * G * h)])


@gen("p11-09", weight=2)
def _hydraulic(rng):
    a1, a2, f = R(rng, 1, 2, 5), R(rng, 50, 100, 200), R(rng, 10, 20, 50)
    return num_q(rng, f"In a hydraulic lift the small piston has area {a1} cm² and the large one {a2} cm². A force of {f} N on the small piston lifts:",
                 f * a2 / a1, " N", "Pascal's law: F2 = F1 A2/A1.", wrongs=[f * a1 / a2, f, f * (a2 / a1) ** 2])


@gen("p11-10", weight=2)
def _conduction(rng):
    k, a, dt, l = R(rng, 200, 400, 50), R(rng, 0.01, 0.02, 0.001), R(rng, 50, 100), R(rng, 0.5, 1, 2)
    return num_q(rng, f"A rod of conductivity {k} W/(m K), area {a} m² and length {l} m has ends at a {dt} K difference. The heat current is:", k * a * dt / l, " W",
                 "H = kAΔT/L.", wrongs=[k * a * dt * l, k * dt / l, k * a / l])


@gen("p11-10", weight=2)
def _cooling(rng):
    t1, t2, ts, tm = R(rng, 80, 70, 60), R(rng, 60, 50, 40), R(rng, 20, 25, 30), R(rng, 5, 10)
    if t2 >= t1 or t2 <= ts:
        return None
    k = (t1 - t2) / tm / ((t1 + t2) / 2 - ts)
    # second interval: (t2 - x)/tm = k((t2 + x)/2 - ts), solved for x
    x = (t2 - k * tm * (t2 / 2 - ts)) / (1 + k * tm / 2)
    return num_q(rng, f"A body cools from {t1} °C to {t2} °C in {tm} min in a room at {ts} °C. By Newton's law of cooling (average form), its temperature after another {tm} min is:",
                 x, " °C", "(T1 - T2)/t = k[(T1 + T2)/2 - Ts].", wrongs=[t2 - (t1 - t2), (t2 + ts) / 2, t2 - (t1 - t2) / 2])


@gen("p11-11", weight=2)
def _adiabatic(rng):
    gname, g = rng.choice([("monatomic", 5 / 3), ("diatomic", 7 / 5)])
    f = R(rng, 2, 4, 8)
    return num_q(rng, f"An ideal {gname} gas is compressed adiabatically to 1/{f} of its volume. Its pressure becomes how many times?", f ** g, " times",
                 "PV^γ = constant.", wrongs=[f, f * g, f ** (1 / g)])


@gen("p11-11", weight=2)
def _isothermal_work(rng):
    n, t, f = R(rng, 1, 2), R(rng, 300, 400), R(rng, 2, 10)
    w = n * 8.314 * t * math.log(f)
    return num_q(rng, f"{n} mol of an ideal gas expands isothermally at {t} K to {f} times its volume. The work done by the gas is (R = 8.314):", w, " J",
                 "W = nRT ln(V2/V1).", wrongs=[n * 8.314 * t * f, n * 8.314 * t * math.log10(f), n * 8.314 * t])


@gen("p11-12", weight=2)
def _mean_energy(rng):
    t = R(rng, 300, 400, 600)
    e = 1.5 * 1.38e-23 * t
    return num_q(rng, f"The average translational kinetic energy of a gas molecule at {t} K is (k = 1.38 × 10^-23 J/K):", e, " J", "E = (3/2)kT.",
                 wrongs=[1.38e-23 * t, 2.5 * 1.38e-23 * t, 0.5 * 1.38e-23 * t], form=lambda x: sci(x))


@gen("p11-13", weight=2)
def _springs(rng):
    k1, k2, m = R(rng, 100, 200, 300), R(rng, 100, 200, 600), R(rng, 1, 2, 4)
    series = rng.random() < 0.5
    k = k1 * k2 / (k1 + k2) if series else k1 + k2
    return num_q(rng, f"Springs of {k1} N/m and {k2} N/m are joined in {'series' if series else 'parallel'}. Their effective spring constant is:", k, " N/m",
                 "Series: 1/k = 1/k1 + 1/k2; parallel: k = k1 + k2.", wrongs=[k1 + k2 if series else k1 * k2 / (k1 + k2), (k1 + k2) / 2, k1 * k2])


@gen("p11-13", weight=2)
def _pendulum_g(rng):
    f = R(rng, 4, 6, 9)
    return num_q(rng, f"A pendulum clock is taken to a planet where g is 1/{f} of Earth's. Its period becomes how many times?", math.sqrt(f), " times",
                 "T ∝ 1/√g.", wrongs=[f, 1 / math.sqrt(f), f * f], form=lambda x: fmt(x, 3))


@gen("p11-14", weight=2)
def _wave_eq(rng):
    a, k, w = R(rng, 0.02, 0.05, 0.1), R(rng, 2, 4, 5, 10), R(rng, 100, 200, 314, 50)
    ask = rng.choice(["v", "lambda", "f"])
    if ask == "v":
        return num_q(rng, f"A wave is y = {a} sin({k}x - {w}t) in SI units. Its speed is:", w / k, " m/s", "v = ω/k.", wrongs=[k / w, w * k, w / (2 * math.pi * k)])
    if ask == "lambda":
        return num_q(rng, f"A wave is y = {a} sin({k}x - {w}t) in SI units. Its wavelength is:", 2 * math.pi / k, " m", "λ = 2π/k.", wrongs=[k / (2 * math.pi), 1 / k, math.pi / k])
    return num_q(rng, f"A wave is y = {a} sin({k}x - {w}t) in SI units. Its frequency is:", w / (2 * math.pi), " Hz", "f = ω/2π.", wrongs=[w, 2 * math.pi * w, w / math.pi])


# ---------------------------------------------------------------- Class 12
@gen("p12-01", weight=2)
def _dipole_field(rng):
    p, r = R(rng, 1e-9, 2e-9, 5e-10), R(rng, 0.1, 0.2, 0.3)
    axial = rng.random() < 0.5
    e = 9e9 * (2 if axial else 1) * p / r ** 3
    return num_q(rng, f"The electric field of a short dipole (p = {sci(p)} C m) at {r} m on its {'axis' if axial else 'equatorial line'} is:", e, " N/C",
                 "Axial: 2kp/r³; equatorial: kp/r³.", wrongs=[9e9 * (1 if axial else 2) * p / r ** 3, 9e9 * p / r ** 2, e * 4], form=lambda x: sci(x))


@gen("p12-02", weight=2)
def _sharing(rng):
    c1, v1, c2 = R(rng, 2, 4, 6), R(rng, 10, 20, 30), R(rng, 2, 4, 6)
    v = c1 * v1 / (c1 + c2)
    return num_q(rng, f"A {c1} μF capacitor charged to {v1} V is joined to an uncharged {c2} μF capacitor. The common potential is:", v, " V",
                 "V = C1V1/(C1 + C2).", wrongs=[v1 / 2, c2 * v1 / (c1 + c2), v1])


@gen("p12-03", weight=2)
def _cells(rng):
    n, e, r, big = R(rng, 2, 3, 4), R(rng, 1.5, 2), R(rng, 0.5, 1), R(rng, 2, 4, 6)
    series = rng.random() < 0.5
    i = n * e / (big + n * r) if series else e / (big + r / n)
    return num_q(rng, f"{n} identical cells (emf {e} V, internal resistance {r} Ω) in {'series' if series else 'parallel'} drive a {big} Ω resistor. The current is:", i, " A",
                 "Series: nE/(R + nr); parallel: E/(R + r/n).", wrongs=[e / (big + n * r) if series else n * e / (big + n * r), n * e / big, e / big])


@gen("p12-03", weight=2)
def _heat_joule(rng):
    i, r, t = R(rng, 1, 2, 5), R(rng, 5, 10, 20), R(rng, 10, 60, 100)
    return num_q(rng, f"A current of {i} A flows through a {r} Ω resistor for {t} s. The heat produced is:", i * i * r * t, " J", "H = I²Rt.",
                 wrongs=[i * r * t, i * i * r, i * r * r * t])


@gen("p12-04", weight=2)
def _force_wires(rng):
    i1, i2, d = R(rng, 1, 2, 5, 10), R(rng, 1, 2, 5, 10), R(rng, 0.01, 0.05, 0.1)
    return num_q(rng, f"Two long parallel wires {d} m apart carry {i1} A and {i2} A. The force per metre between them is (μ₀ = 4π × 10^-7):",
                 2e-7 * i1 * i2 / d, " N/m", "F/L = μ₀I1I2/(2πd).", wrongs=[2e-7 * i1 * i2 / d ** 2, 4e-7 * i1 * i2 / d, 2e-7 * (i1 + i2) / d], form=lambda x: sci(x))


@gen("p12-04", weight=2)
def _loop_torque(rng):
    n, i, a, b = R(rng, 10, 50, 100), R(rng, 1, 2), R(rng, 0.01, 0.02), R(rng, 0.1, 0.5, 1)
    return num_q(rng, f"A coil of {n} turns, area {a} m², carries {i} A in a {b} T field with its plane parallel to the field. The torque is:", n * i * a * b, " N m",
                 "τ = NIAB sinθ with θ = 90° between normal and field.", wrongs=[i * a * b, n * i * a, 0.5 * n * i * a * b])


facts("p12-05", [
    "Earth's magnetic field at the equator is about 0.4 G",
    "The declination is the angle between the geographic and magnetic meridians",
    "A bar magnet in a uniform field feels a torque but no net force",
    "The magnetic moment of a current loop is IA",
    "Gauss's law for magnetism says net magnetic flux through a closed surface is zero",
], [
    "The angle of dip is zero at the magnetic poles",
    "Net magnetic flux through a closed surface equals μ₀ times the enclosed pole strength",
    "A bar magnet in a uniform field feels a large net force",
    "Declination is the angle of dip",
    "The magnetic moment of a loop is I/A",
], "Earth's magnetism and magnets")


@gen("p12-06", weight=2)
def _rotating_rod(rng):
    b, l, w = R(rng, 0.2, 0.5, 1), R(rng, 0.5, 1, 2), R(rng, 10, 20, 50)
    return num_q(rng, f"A {l} m rod rotates at {w} rad/s about one end in a {b} T field perpendicular to its plane of rotation. The emf between its ends is:",
                 0.5 * b * w * l * l, " V", "e = ½Bωl².", wrongs=[b * w * l * l, b * w * l, 0.5 * b * w * l])


@gen("p12-06", weight=2)
def _mutual(rng):
    m, di, dt = R(rng, 0.1, 0.5, 1.5), R(rng, 2, 4, 10), R(rng, 0.1, 0.2, 0.5)
    return num_q(rng, f"Two coils have mutual inductance {m} H. The current in one changes by {di} A in {dt} s. The emf in the other is:", m * di / dt, " V",
                 "e = M dI/dt.", wrongs=[m * di, m * dt / di, di / dt])


@gen("p12-07", weight=2)
def _xc(rng):
    c, f = R(rng, 10, 50, 100), R(rng, 50, 60, 100)
    xc = 1 / (2 * math.pi * f * c * 1e-6)
    return num_q(rng, f"The reactance of a {c} μF capacitor at {f} Hz is:", xc, " Ω", "Xc = 1/(2πfC).", wrongs=[2 * math.pi * f * c * 1e-6, xc * 2 * math.pi, 1 / (f * c * 1e-6)])


@gen("p12-07", weight=2)
def _impedance(rng):
    r, xl, xc = R(rng, 30, 40, 60), R(rng, 80, 100, 120), R(rng, 20, 40, 50)
    z = math.sqrt(r * r + (xl - xc) ** 2)
    return num_q(rng, f"A series LCR circuit has R = {r} Ω, XL = {xl} Ω and XC = {xc} Ω. Its impedance is:", z, " Ω", "Z = √(R² + (XL - XC)²).",
                 wrongs=[r + xl - xc, math.sqrt(r * r + (xl + xc) ** 2), r + xl + xc])


@gen("p12-07")
def _q_factor(rng):
    l, c, r = R(rng, 0.1, 1), R(rng, 10, 100), R(rng, 10, 20, 50)
    q = math.sqrt(l / (c * 1e-6)) / r
    return num_q(rng, f"The quality factor of a series LCR circuit with L = {l} H, C = {c} μF and R = {r} Ω is:", q, "", "Q = (1/R)√(L/C).",
                 wrongs=[r * math.sqrt(c * 1e-6 / l), math.sqrt(l / (c * 1e-6)), q * r * r])


@gen("p12-09", weight=2)
def _mirror(rng):
    f, u = R(rng, 10, 15, 20), R(rng, 30, 40, 60)
    v = 1 / (1 / f - 1 / u)
    m = v / u
    ask = rng.choice(["v", "m"])
    if ask == "v":
        return num_q(rng, f"An object is {u} cm in front of a concave mirror of focal length {f} cm. The image distance from the mirror is:", v, " cm",
                     "1/v + 1/u = 1/f (real image in front).", wrongs=[1 / (1 / f + 1 / u), u - f, 2 * f])
    return num_q(rng, f"An object is {u} cm in front of a concave mirror of focal length {f} cm. The size of the image compared with the object is:", m, " times",
                 "|m| = v/u.", wrongs=[u / v, f / u, 1])


@gen("p12-09", weight=2)
def _lensmaker(rng):
    n, r1 = R(rng, 1.5, 1.6), R(rng, 10, 20, 30)
    f = 1 / ((n - 1) * 2 / r1)
    return num_q(rng, f"An equiconvex lens of refractive index {n} has radii of {r1} cm. Its focal length is:", f, " cm", "1/f = (n - 1)(1/R1 - 1/R2).",
                 wrongs=[r1, r1 / (n - 1), 2 * f])


@gen("p12-09")
def _apparent_depth(rng):
    d, n = R(rng, 12, 20, 40), R(rng, 1.33, 1.5)
    return num_q(rng, f"A coin lies {d} cm below the surface of a liquid of refractive index {n}. Its apparent depth is:", d / n, " cm", "Apparent depth = real/n.",
                 wrongs=[d * n, d - n, d / (n - 1)])


@gen("p12-10", weight=2)
def _intensity_ratio(rng):
    r = R(rng, 4, 9, 16, 25)
    a = round(math.sqrt(r))
    imax, imin = (a + 1) ** 2, (a - 1) ** 2
    return Q(f"Two coherent waves have intensity ratio {r} : 1. The ratio Imax : Imin in their interference is:", f"{imax} : {imin}",
             [f"{r + 1} : {r - 1}", f"{a + 1} : {a - 1}", f"{r} : 1"], "Amplitudes ∝ √I; Imax/Imin = (a1 + a2)²/(a1 - a2)².")


@gen("p12-11", weight=2)
def _photon_count(rng):
    p, lam = R(rng, 1, 2, 5, 10), R(rng, 400, 500, 600, 662)
    n = p * lam * 1e-9 / (6.626e-34 * 3e8)
    return num_q(rng, f"A {p} mW laser emits light of {lam} nm. The number of photons emitted per second is about:", n * 1e-3, "",
                 "N = P/(hc/λ).", wrongs=[n, n * 1e-6, n * 1e-4], form=lambda x: sci(x, 2))


@gen("p12-12", weight=2)
def _bohr_ratio(rng):
    n1, n2 = rng.choice([(1, 2), (1, 3), (2, 3), (2, 4)])
    ask = rng.choice(["r", "v", "e"])
    if ask == "r":
        return Q(f"The ratio of the radii of Bohr orbits n = {n1} and n = {n2} in hydrogen is:", f"{n1 * n1} : {n2 * n2}",
                 [f"{n1} : {n2}", f"{n2 * n2} : {n1 * n1}", f"{n2} : {n1}"], "r ∝ n².")
    if ask == "v":
        return Q(f"The ratio of electron speeds in Bohr orbits n = {n1} and n = {n2} of hydrogen is:", f"{n2} : {n1}",
                 [f"{n1} : {n2}", f"{n2 * n2} : {n1 * n1}", f"{n1 * n1} : {n2 * n2}"], "v ∝ 1/n.")
    return Q(f"The ratio of energies (magnitudes) of Bohr orbits n = {n1} and n = {n2} of hydrogen is:", f"{n2 * n2} : {n1 * n1}",
             [f"{n1 * n1} : {n2 * n2}", f"{n2} : {n1}", f"{n1} : {n2}"], "|E| ∝ 1/n².")


@gen("p12-13", weight=2)
def _q_value(rng):
    dm = R(rng, 0.001, 0.002, 0.005, 0.0186)
    return num_q(rng, f"In a nuclear reaction the total mass decreases by {dm} u. The energy released is (1 u = 931.5 MeV):", dm * 931.5, " MeV",
                 "Q = Δm × 931.5 MeV.", wrongs=[dm * 931.5 * 1000, dm / 931.5, dm * 931.5 / 2])


@gen("p12-13", weight=2)
def _mean_life(rng):
    t = R(rng, 1.386, 2.772, 6.93, 13.86)
    lam = 0.693 / t
    ask = rng.choice(["lambda", "tau"])
    if ask == "lambda":
        return num_q(rng, f"A nucleus has half-life {t} s. Its decay constant is:", lam, " per s", "λ = 0.693/T½.", wrongs=[t / 0.693, 1 / t, 0.693 * t])
    return num_q(rng, f"A nucleus has half-life {t} s. Its mean life is:", 1 / lam, " s", "τ = 1/λ = T½/0.693.", wrongs=[t, t * 0.693, t / 2])


table("p12-14", [
    ("Germanium energy gap", "About 0.7 eV"), ("Silicon energy gap", "About 1.1 eV"), ("Diamond energy gap", "More than 3 eV (insulator)"),
    ("Conductors", "Valence and conduction bands overlap"),
], "{}:", None)
facts("p12-14", [
    "In forward bias the barrier potential decreases",
    "Solar cells are p-n junctions that generate emf without bias",
    "Silicon and germanium are tetravalent",
    "Trivalent impurity atoms are acceptors",
    "Pentavalent impurity atoms are donors",
    "Ripple in rectifier output is reduced with a capacitor filter",
], [
    "In forward bias the barrier potential increases",
    "Pentavalent impurities are acceptors",
    "Germanium has a larger band gap than silicon",
    "A capacitor filter increases ripple",
    "Silicon is pentavalent",
    "An insulator has overlapping valence and conduction bands",
], "semiconductors")


@gen("p12-15", weight=2)
def _vernier_read(rng):
    msr, vsd, lc = R(rng, 20, 31, 45), R(rng, 3, 4, 7), R(rng, 0.1, 0.01)
    z = R(rng, 2, 3, -2, -3)
    reading = msr + vsd * lc - z * lc
    return num_q(rng, f"A vernier calliper (least count {lc} mm, zero error {z:+d} divisions) shows a main scale reading of {msr} mm with the {vsd}th vernier division coinciding. The corrected reading is:",
                 reading, " mm", "Reading = MSR + VSD × LC - zero error.", wrongs=[msr + vsd * lc, msr + vsd * lc + z * lc, msr + vsd],
                 form=lambda x: fmt(x, 2))


tag(None)
