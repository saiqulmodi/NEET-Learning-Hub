"""High-yield NEET Physics, third batch (Classes 11-12): more original problems of the kinds NEET asks again and again.

Tagged "hy3" so it is generated after the earlier batches and existing question ids never move. Answers are computed.
"""
import math

from .core import table, facts, gen, num_q, Q, fmt, sci, tag

tag("hy3")
G = 10


def R(rng, *xs):
    return rng.choice(xs)


# ---------------------------------------------------------------- Class 11
@gen("p11-01", weight=2)
def _dim_power(rng):
    qty, m, l, t = rng.choice([("power", 1, 2, -3), ("pressure", 1, -1, -2), ("impulse", 1, 1, -1), ("angular momentum", 1, 2, -1),
                               ("work", 1, 2, -2), ("momentum", 1, 1, -1), ("force", 1, 1, -2)])
    ask = rng.choice(["L", "T"])
    val = l if ask == "L" else t
    return Q(f"In the dimensional formula of {qty}, the power of {ask} is:", str(val), [str(x) for x in (-3, -2, -1, 1, 2, 3) if x != val],
             f"{qty}: [M^{m} L^{l} T^{t}].")


@gen("p11-02", weight=2)
def _avg_velocity(rng):
    d1, t1, d2, t2 = R(rng, 100, 200, 300), R(rng, 10, 20), R(rng, 100, 300, 500), R(rng, 20, 30, 50)
    return num_q(rng, f"A runner covers {d1} m in {t1} s and then {d2} m in {t2} s in the same direction. The average speed is:", (d1 + d2) / (t1 + t2), " m/s",
                 "Average speed = total distance / total time.", wrongs=[(d1 / t1 + d2 / t2) / 2, (d1 + d2) / t2, d1 / t1])


@gen("p11-03", weight=2)
def _rel_plane(rng):
    va, vb = R(rng, 3, 6, 8, 5), R(rng, 4, 8, 6, 12)
    return num_q(rng, f"Car A moves east at {va} m/s and car B moves north at {vb} m/s. The speed of B relative to A is:", math.hypot(va, vb), " m/s",
                 "v(BA) = v(B) - v(A); perpendicular, so use Pythagoras.", wrongs=[va + vb, abs(vb - va) or 1, (va + vb) / 2])


@gen("p11-03", weight=2)
def _dot_cross(rng):
    a, b, th = R(rng, 2, 3, 4, 5), R(rng, 2, 4, 6), R(rng, 0, 30, 60, 90)
    dot = rng.random() < 0.5
    v = a * b * (math.cos(math.radians(th)) if dot else math.sin(math.radians(th)))
    return num_q(rng, f"Vectors of magnitude {a} and {b} are at {th}°. The magnitude of their {'dot' if dot else 'cross'} product is:", v, "",
                 "A·B = AB cosθ; |A×B| = AB sinθ.", wrongs=[a * b * (math.sin(math.radians(th)) if dot else math.cos(math.radians(th))) or a * b / 2, a + b, a * b])


@gen("p11-04", weight=2)
def _circular_tension(rng):
    m, v, r = R(rng, 0.5, 1, 2), R(rng, 2, 4, 5), R(rng, 0.5, 1, 2)
    return num_q(rng, f"A {m} kg stone tied to a {r} m string is whirled in a horizontal circle at {v} m/s (ignore gravity). The tension is:", m * v * v / r, " N",
                 "T = mv²/r.", wrongs=[m * v / r, m * v * v * r, m * v * v / (2 * r)])


@gen("p11-04", weight=2)
def _rocket(rng):
    u, dm, m = R(rng, 500, 1000, 2000), R(rng, 10, 20, 50), R(rng, 1000, 2000, 5000)
    return num_q(rng, f"A rocket ejects gas at {u} m/s relative to it at {dm} kg/s. The thrust on the rocket is:", u * dm, " N", "F = u dm/dt.",
                 wrongs=[u / dm, u * dm / m, u * m])


@gen("p11-05", weight=2)
def _pe_ke(rng):
    m, h = R(rng, 1, 2, 5), R(rng, 5, 10, 20, 45)
    return num_q(rng, f"A {m} kg ball falls freely from {h} m (g = 10 m/s²). Its kinetic energy just before hitting the ground is:", m * G * h, " J",
                 "KE = loss in PE = mgh.", wrongs=[0.5 * m * G * h, m * h, m * G * h * 2])


@gen("p11-05", weight=2)
def _power_force(rng):
    f, v = R(rng, 100, 200, 500, 1000), R(rng, 2, 5, 10, 20)
    return num_q(rng, f"An engine pulls with a force of {f} N at a constant speed of {v} m/s. Its power is:", f * v, " W", "P = Fv.",
                 wrongs=[f / v, f * v * v, f + v])


@gen("p11-06", weight=2)
def _ang_accel(rng):
    i, tau = R(rng, 2, 4, 5, 10), R(rng, 10, 20, 40)
    t = R(rng, 2, 5)
    a = tau / i
    ask = rng.choice(["alpha", "omega"])
    if ask == "alpha":
        return num_q(rng, f"A torque of {tau} N m acts on a wheel of moment of inertia {i} kg m². Its angular acceleration is:", a, " rad/s²", "α = τ/I.",
                     wrongs=[tau * i, i / tau, tau / (2 * i)])
    return num_q(rng, f"A torque of {tau} N m acts on a wheel (I = {i} kg m²) initially at rest. Its angular speed after {t} s is:", a * t, " rad/s", "ω = αt.",
                 wrongs=[a, tau * t, a * t * t / 2])


@gen("p11-06", weight=2)
def _rot_ke(rng):
    i, w = R(rng, 0.5, 1, 2, 4), R(rng, 5, 10, 20)
    return num_q(rng, f"A flywheel of moment of inertia {i} kg m² spins at {w} rad/s. Its rotational kinetic energy is:", 0.5 * i * w * w, " J", "K = ½Iω².",
                 wrongs=[i * w * w, 0.5 * i * w, i * w])


@gen("p11-07", weight=2)
def _grav_force(rng):
    m1, m2, r = R(rng, 50, 100, 1000), R(rng, 50, 100, 200), R(rng, 1, 2, 5)
    f = 6.67e-11 * m1 * m2 / (r * r)
    return num_q(rng, f"Two masses of {m1} kg and {m2} kg are {r} m apart. The gravitational force between them is (G = 6.67 × 10^-11):", f, " N",
                 "F = Gm1m2/r².", wrongs=[f * r, f / r, f * 10], form=lambda x: sci(x))


@gen("p11-07", weight=2)
def _weight_planet(rng):
    w, fm, fr = R(rng, 500, 600, 700), R(rng, 2, 4, 0.5), R(rng, 2, 0.5, 1)
    return num_q(rng, f"A person weighs {w} N on Earth. On a planet with {fmt(fm)} times Earth's mass and {fmt(fr)} times its radius, the weight is:", w * fm / (fr * fr), " N",
                 "g ∝ M/R².", wrongs=[w * fm / fr, w * fm * fr * fr, w])


@gen("p11-08", weight=2)
def _stress_strain(rng):
    f, a, l = R(rng, 100, 200, 500), R(rng, 1e-6, 2e-6, 5e-6), R(rng, 1, 2, 4)
    y = R(rng, 1e11, 2e11, 0.7e11, 1.2e11)            # realistic metals: steel 2, copper 1.2, aluminium 0.7 (× 10^11)
    dl = f * l / (a * y) * 1000                        # mm
    return num_q(rng, f"A {l} m wire of area {sci(a)} m² stretches by {fmt(dl, 3)} mm under {f} N. Its Young's modulus is:", y, " N/m²", "Y = (F/A)/(ΔL/L).",
                 wrongs=[y / 1000, y * 1000, f / a], form=lambda x: sci(x))


@gen("p11-09", weight=2)
def _pressure_depth(rng):
    h, rho = R(rng, 5, 10, 20, 50), R(rng, 1000, 800, 13600)
    return num_q(rng, f"The pressure due to a {h} m column of liquid of density {rho} kg/m³ (g = 10 m/s²) is:", h * rho * G, " Pa", "p = hρg.",
                 wrongs=[h * rho, h * G, h * rho * G + 1e5], form=lambda x: sci(x))


@gen("p11-09", weight=2)
def _buoyancy(rng):
    v, rho = R(rng, 0.001, 0.002, 0.005), R(rng, 1000, 800)
    return num_q(rng, f"A body of volume {v} m³ is fully immersed in a liquid of density {rho} kg/m³ (g = 10 m/s²). The buoyant force is:", v * rho * G, " N",
                 "Archimedes: F = Vρg.", wrongs=[v * rho, v * G, v * rho * G * 2])


@gen("p11-10", weight=2)
def _linear_exp(rng):
    l, a, dt = R(rng, 1, 2, 10), R(rng, 1.2e-5, 2e-5, 2.4e-5), R(rng, 50, 100)
    return num_q(rng, f"A rod of length {l} m (α = {sci(a)} /°C) is heated by {dt} °C. Its increase in length is:", l * a * dt * 1000, " mm", "ΔL = LαΔT.",
                 wrongs=[l * a * dt, l * a * dt * 1e6, 3 * l * a * dt * 1000])


@gen("p11-10", weight=2)
def _scales(rng):
    c = R(rng, -40, 0, 25, 37, 100)
    ask = rng.choice(["F", "K"])
    if ask == "F":
        return num_q(rng, f"{c} °C on the Fahrenheit scale is:", c * 9 / 5 + 32, " °F", "F = 9C/5 + 32.", wrongs=[c * 5 / 9 + 32, c + 32, c * 9 / 5])
    return num_q(rng, f"{c} °C on the Kelvin scale is:", c + 273.15, " K", "K = C + 273.15.", wrongs=[c - 273.15, c + 373, c * 273.15 / 100])


@gen("p11-11", weight=2)
def _engine_work(rng):
    q1, q2 = R(rng, 1000, 2000, 5000), R(rng, 600, 800, 3000)
    if q2 >= q1:
        return None
    ask = rng.choice(["w", "eff"])
    if ask == "w":
        return num_q(rng, f"A heat engine takes {q1} J from the source and rejects {q2} J to the sink. The work done is:", q1 - q2, " J", "W = Q1 - Q2.",
                     wrongs=[q1 + q2, q2, q1])
    return num_q(rng, f"A heat engine takes {q1} J from the source and rejects {q2} J to the sink. Its efficiency is:", 100 * (q1 - q2) / q1, "%",
                 "η = 1 - Q2/Q1.", wrongs=[100 * q2 / q1, 100 * (q1 - q2) / q2, 100 * q1 / (q1 + q2)])


@gen("p11-12", weight=2)
def _ideal_gas(rng):
    p, v, t = R(rng, 1e5, 2e5), R(rng, 0.01, 0.02, 0.0224), R(rng, 273, 300)
    n = p * v / (8.314 * t)
    return num_q(rng, f"An ideal gas at {sci(p)} Pa occupies {v} m³ at {t} K. The number of moles is (R = 8.314):", n, " mol", "n = PV/RT.",
                 wrongs=[n * 2, p * v / t, n / 10])


@gen("p11-12", weight=2)
def _charles(rng):
    v1, t1, t2 = R(rng, 1, 2, 5), R(rng, 300, 273), R(rng, 600, 546, 450)
    return num_q(rng, f"At constant pressure a gas of volume {v1} L at {t1} K is heated to {t2} K. Its new volume is:", v1 * t2 / t1, " L", "V/T = constant.",
                 wrongs=[v1 * t1 / t2, v1 * (t2 - t1) / t1, v1 + t2 - t1])


@gen("p11-13", weight=2)
def _shm_eq(rng):
    a, w = R(rng, 0.02, 0.05, 0.1), R(rng, 2, 4, 10, 20)
    ask = rng.choice(["T", "f", "a"])
    if ask == "T":
        return num_q(rng, f"A particle moves as x = {a} sin({w}t) in SI units. Its period is:", 2 * math.pi / w, " s", "T = 2π/ω.", wrongs=[w / (2 * math.pi), 1 / w, math.pi / w])
    if ask == "f":
        return num_q(rng, f"A particle moves as x = {a} sin({w}t) in SI units. Its frequency is:", w / (2 * math.pi), " Hz", "f = ω/2π.", wrongs=[w, 2 * math.pi / w, w / math.pi])
    return num_q(rng, f"A particle moves as x = {a} sin({w}t) in SI units. Its maximum acceleration is:", a * w * w, " m/s²", "amax = Aω².",
                 wrongs=[a * w, a / w, a * w * w * 2])


@gen("p11-14", weight=2)
def _harmonics(rng):
    l, n = R(rng, 0.5, 1, 1.7), R(rng, 2, 3, 4, 5)
    open_pipe = rng.random() < 0.5
    v = 340
    if open_pipe:
        return num_q(rng, f"An open pipe of length {fmt(l)} m (sound speed 340 m/s). The frequency of its harmonic number {n} is:", n * v / (2 * l), " Hz",
                     "fn = nv/2L.", wrongs=[n * v / (4 * l), v / (2 * l), (2 * n - 1) * v / (4 * l)])
    k = 2 * n - 1
    return num_q(rng, f"A pipe closed at one end has length {fmt(l)} m (sound speed 340 m/s). The frequency of its {k}th harmonic is:", k * v / (4 * l), " Hz",
                 "Closed pipe: f = kv/4L, k odd.", wrongs=[k * v / (2 * l), v / (4 * l), n * v / (4 * l)])


@gen("p11-14", weight=2)
def _speed_temp(rng):
    t1, t2, v1 = R(rng, 273, 300), R(rng, 1092, 1200, 4 * 300), R(rng, 330, 340)
    return num_q(rng, f"The speed of sound in a gas is {v1} m/s at {t1} K. At {t2} K it becomes:", v1 * math.sqrt(t2 / t1), " m/s", "v ∝ √T.",
                 wrongs=[v1 * t2 / t1, v1 * math.sqrt(t1 / t2), v1 + t2 - t1])


# ---------------------------------------------------------------- Class 12
@gen("p12-01", weight=2)
def _field_point(rng):
    q, r = R(rng, 1, 2, 5, 10), R(rng, 0.1, 0.2, 0.3, 0.5)
    return num_q(rng, f"The electric field at {r} m from a point charge of {q} nC is:", 9e9 * q * 1e-9 / (r * r), " N/C", "E = kq/r².",
                 wrongs=[9e9 * q * 1e-9 / r, 9e9 * q / (r * r), 9e9 * q * 1e-9 * r])


@gen("p12-01", weight=2)
def _sphere_field(rng):
    q, r, d = R(rng, 1, 2, 5), R(rng, 0.1, 0.2), R(rng, 0.3, 0.5, 1)
    inside = rng.random() < 0.4
    if inside:
        return Q(f"A thin spherical shell of radius {r} m carries {q} μC. The electric field at its centre is:", "Zero",
                 [f"{fmt(9e9 * q * 1e-6 / (r * r))} N/C", f"{fmt(9e9 * q * 1e-6 / r)} N/C", "Infinite"], "No charge is enclosed inside a shell.")
    return num_q(rng, f"A thin spherical shell of radius {r} m carries {q} μC. The field {d} m from its centre is:", 9e9 * q * 1e-6 / (d * d), " N/C",
                 "Outside, the shell acts like a point charge.", wrongs=[9e9 * q * 1e-6 / (r * r), 9e9 * q * 1e-6 / d, 0.5 * 9e9 * q * 1e-6 / (d * d)])


@gen("p12-02", weight=2)
def _parallel_plate(rng):
    a, d, k = R(rng, 0.01, 0.02, 0.1), R(rng, 1, 2, 5), R(rng, 1, 2, 5)
    c = k * 8.85e-12 * a / (d * 1e-3)
    return num_q(rng, f"A parallel plate capacitor has plates of area {a} m², {d} mm apart, filled with a dielectric K = {k}. Its capacitance is:", c * 1e12, " pF",
                 "C = Kε₀A/d.", wrongs=[c * 1e9, 8.85e-12 * a / (d * 1e-3) * 1e12 if k != 1 else c * 2e12, c * 1e12 * d])


@gen("p12-02", weight=2)
def _work_charge(rng):
    q, v = R(rng, 1, 2, 5), R(rng, 10, 20, 100)
    return num_q(rng, f"The work done in moving a {q} μC charge through a potential difference of {v} V is:", q * 1e-6 * v * 1e6, " μJ", "W = qV.",
                 wrongs=[q * v * 1e-6, q / v, q * v * 2])


@gen("p12-03", weight=2)
def _resistivity(rng):
    rho, l, a = R(rng, 1.7e-8, 2.8e-8, 1e-6), R(rng, 1, 2, 10), R(rng, 1e-6, 2e-6, 0.5e-6)
    return num_q(rng, f"A wire of resistivity {sci(rho)} Ω m, length {l} m and area {sci(a)} m² has a resistance of:", rho * l / a, " Ω", "R = ρL/A.",
                 wrongs=[rho * a / l, rho / (l * a), rho * l * a], form=lambda x: sci(x))


@gen("p12-03", weight=2)
def _temp_coeff(rng):
    r0, al, t = R(rng, 10, 20, 50), R(rng, 0.004, 0.002, 0.0039), R(rng, 50, 100)
    return num_q(rng, f"A wire has resistance {r0} Ω at 0 °C and α = {al} per °C. Its resistance at {t} °C is:", r0 * (1 + al * t), " Ω", "Rt = R0(1 + αt).",
                 wrongs=[r0 * al * t, r0 / (1 + al * t), r0 + al * t])


@gen("p12-04", weight=2)
def _lorentz(rng):
    q, v, b = R(rng, 1.6e-19, 3.2e-19), R(rng, 1e5, 1e6, 2e6), R(rng, 0.1, 0.5, 1)
    return num_q(rng, f"A charge of {sci(q)} C moves at {sci(v)} m/s perpendicular to a {b} T field. The magnetic force on it is:", q * v * b, " N", "F = qvB.",
                 wrongs=[q * b / v, q * v / b, q * v * b * 2], form=lambda x: sci(x))


@gen("p12-04", weight=2)
def _wire_force(rng):
    i, l, b, th = R(rng, 2, 5, 10), R(rng, 0.2, 0.5, 1), R(rng, 0.1, 0.5), R(rng, 30, 90)
    return num_q(rng, f"A {l} m wire carrying {i} A lies at {th}° to a {b} T field. The force on it is:", i * l * b * math.sin(math.radians(th)), " N",
                 "F = BIL sinθ.", wrongs=[i * l * b * math.cos(math.radians(th)) or i * l * b / 2, i * b / l, i * l * b * 2])


@gen("p12-05", weight=2)
def _magnet_torque(rng):
    m, b, th = R(rng, 1, 2, 5), R(rng, 0.1, 0.2, 0.5), R(rng, 30, 60, 90)
    ask = rng.choice(["torque", "pe"])
    if ask == "torque":
        return num_q(rng, f"A bar magnet of moment {m} A m² is at {th}° to a {b} T field. The torque on it is:", m * b * math.sin(math.radians(th)), " N m",
                     "τ = mB sinθ.", wrongs=[m * b * math.cos(math.radians(th)) or m * b / 2, m * b, m / b])
    return num_q(rng, f"A bar magnet of moment {m} A m² is at {th}° to a {b} T field. Its potential energy is:", -m * b * math.cos(math.radians(th)), " J",
                 "U = -mB cosθ.", wrongs=[m * b * math.cos(math.radians(th)) or 1, -m * b * math.sin(math.radians(th)), -m * b])


@gen("p12-06", weight=2)
def _solenoid_L(rng):
    n, l, a = R(rng, 500, 1000, 2000), R(rng, 0.5, 1), R(rng, 1e-4, 5e-4, 1e-3)
    ind = 4 * math.pi * 1e-7 * n * n * a / l
    return num_q(rng, f"A solenoid has {n} turns, length {l} m and cross-section {sci(a)} m². Its self-inductance is:", ind * 1000, " mH", "L = μ₀N²A/l.",
                 wrongs=[ind * 1000 / n, ind, ind * 1000 * 2])


@gen("p12-07", weight=2)
def _ac_power(rng):
    v, i, pf = R(rng, 220, 110, 240), R(rng, 1, 2, 5), R(rng, 0.5, 0.8, 1)
    return num_q(rng, f"An AC circuit has Vrms = {v} V, Irms = {i} A and power factor {pf}. The average power is:", v * i * pf, " W", "P = VI cosφ.",
                 wrongs=[v * i, v * i / pf, v * i * pf / 2])


@gen("p12-07", weight=2)
def _peak_current(rng):
    irms = R(rng, 1, 2, 5, 10)
    return num_q(rng, f"An AC ammeter reads {irms} A. The peak current is:", irms * math.sqrt(2), " A", "I₀ = √2 Irms.", wrongs=[irms / math.sqrt(2), irms * 2, irms])


@gen("p12-08", weight=2)
def _intensity_em(rng):
    p, r = R(rng, 100, 60, 1000), R(rng, 1, 2, 5)
    return num_q(rng, f"A {p} W point source radiates uniformly. The intensity {r} m away is:", p / (4 * math.pi * r * r), " W/m²", "I = P/(4πr²).",
                 wrongs=[p / (math.pi * r * r), p / (4 * math.pi * r), p / r])


@gen("p12-09", weight=2)
def _snell(rng):
    n1, n2, i = R(rng, 1, 1.33), R(rng, 1.5, 1.33, 1.6), R(rng, 30, 45, 60)
    s = n1 * math.sin(math.radians(i)) / n2
    if s >= 1 or n1 == n2:
        return None
    return num_q(rng, f"Light goes from a medium of index {n1} to one of index {n2} at an incidence of {i}°. The angle of refraction is:", math.degrees(math.asin(s)), "°",
                 "n1 sin i = n2 sin r.", wrongs=[i * n1 / n2, i, math.degrees(math.asin(min(1, n2 * math.sin(math.radians(i)) / (n1 + 1))))], form=lambda x: fmt(x, 1))


@gen("p12-09", weight=2)
def _microscope(rng):
    fe, d = R(rng, 2.5, 5, 10), 25
    ask = rng.choice(["near", "far"])
    m = 1 + d / fe if ask == "near" else d / fe
    return num_q(rng, f"A simple microscope has focal length {fe} cm. Its magnifying power with the image at {'the near point (25 cm)' if ask == 'near' else 'infinity'} is:", m, "",
                 "m = 1 + D/f (near point), D/f (infinity).", wrongs=[d / fe if ask == "near" else 1 + d / fe, fe / d, d * fe])


@gen("p12-10", weight=2)
def _resolving(rng):
    lam, dd = R(rng, 500, 550, 600), R(rng, 0.1, 0.2, 1, 2.54)
    ang = 1.22 * lam * 1e-9 / dd
    return num_q(rng, f"The limit of resolution of a telescope with an objective of diameter {dd} m for light of {lam} nm is:", ang, " rad", "θ = 1.22λ/D.",
                 wrongs=[lam * 1e-9 / dd, 1.22 * lam / dd, ang * 2], form=lambda x: sci(x))


@gen("p12-11", weight=2)
def _momentum_photon(rng):
    lam = R(rng, 400, 500, 600, 662)
    p = 6.626e-34 / (lam * 1e-9)
    return num_q(rng, f"The momentum of a photon of wavelength {lam} nm is (h = 6.626 × 10^-34):", p, " kg m/s", "p = h/λ.",
                 wrongs=[p * 3e8, p / 3e8, p * 10], form=lambda x: sci(x))


@gen("p12-12", weight=2)
def _wavelength_h(rng):
    n2 = R(rng, 3, 4, 5)
    e = 13.6 * (1 / 4 - 1 / n2 ** 2)
    return num_q(rng, f"A hydrogen atom drops from n = {n2} to n = 2. The wavelength of the emitted light is about (hc = 1240 eV nm):", 1240 / e, " nm",
                 "λ = 1240/ΔE.", wrongs=[1240 / (13.6 * (1 - 1 / n2 ** 2)), 1240 * e, 1240 / (13.6 / n2 ** 2)])


@gen("p12-13", weight=2)
def _activity(rng):
    n0, f = R(rng, 1e20, 4e20, 1e22), R(rng, 2, 4, 8)
    k = int(math.log2(f))
    return num_q(rng, f"A sample has {sci(n0)} radioactive nuclei. After {k} half-lives the number left is:", n0 / f, "", f"N = N₀/2^{k}.",
                 wrongs=[n0 / (2 * k), n0 * (1 - 1 / f), n0 / (f * 2)], form=lambda x: sci(x))


table("p12-13", [
    ("Alpha particle", "Helium nucleus; charge +2e; low penetration"), ("Beta-minus particle", "Fast electron from the nucleus"),
    ("Gamma ray", "High-energy photon; no charge; high penetration"), ("Neutrino", "Nearly massless neutral particle in beta decay"),
    ("Positron", "Antiparticle of the electron"),
], "{}:", "Which radiation or particle: {}?")


@gen("p12-14", weight=2)
def _transistor(rng):
    beta, ib = R(rng, 50, 100, 200), R(rng, 10, 20, 50)
    ask = rng.choice(["ic", "alpha"])
    if ask == "ic":
        return num_q(rng, f"A transistor has current gain β = {beta}. With a base current of {ib} μA, the collector current is:", beta * ib / 1000, " mA", "Ic = βIb.",
                     wrongs=[ib / beta, beta * ib, beta * ib / 100])
    return num_q(rng, f"A transistor has β = {beta}. Its α (= Ic/Ie) is:", beta / (beta + 1), "", "α = β/(1 + β).",
                 wrongs=[(beta + 1) / beta, 1 / beta, beta / (beta - 1)], form=lambda x: fmt(x, 4))


facts("p12-15", [
    "The time period of a simple pendulum is measured over 20 or more oscillations to reduce error",
    "In a metre bridge the balance point should be near the middle for best accuracy",
    "A sonometer uses resonance of a stretched wire with a tuning fork",
    "In the resonance tube experiment the end correction is about 0.3 times the diameter",
    "A screw gauge with positive zero error gives readings that are too large",
    "Least count of a vernier calliper is usually 0.1 mm",
], [
    "A balance point near one end of a metre bridge gives the best accuracy",
    "A screw gauge with positive zero error gives readings that are too small",
    "The end correction in a resonance tube is about 3 times the diameter",
    "The pendulum period should be timed over a single swing only",
    "Least count of a vernier calliper is usually 1 cm",
    "A sonometer measures electric current",
], "experimental skills")

tag(None)
