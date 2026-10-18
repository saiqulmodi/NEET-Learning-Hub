"""High-yield NEET Chemistry, Classes 11-12: original questions on the topics NEET (and AIPMT before it) asks again and again.

Numerical answers are computed; facts follow the NCERT Chemistry textbooks. Nothing is copied from past papers.
"""
import math

from .core import table, facts, gen, num_q, Q, sig, sci, fmt, tag

tag("hy")


def R(rng, *xs):
    return rng.choice(xs)


# ---------------------------------------------------------------- c11-01 Some Basic Concepts of Chemistry
MOLAR = {"H2O": 18, "CO2": 44, "NH3": 17, "CH4": 16, "O2": 32, "N2": 28, "NaOH": 40, "HCl": 36.5, "H2SO4": 98, "CaCO3": 100, "C6H12O6": 180, "NaCl": 58.5}


@gen("c11-01", weight=3)
def _moles(rng):
    sp = rng.choice(list(MOLAR))
    m = MOLAR[sp]
    n = R(rng, 0.1, 0.25, 0.5, 2, 3, 5)
    kind = rng.choice(["mass", "molecules"])
    if kind == "mass":
        return num_q(rng, f"The mass of {fmt(n)} mol of {sp} (molar mass {fmt(m)} g/mol) is:", n * m, " g", "mass = n × M.",
                     wrongs=[m / n, n * m * 2, n + m])
    return Q(f"How many molecules are present in {fmt(n * m)} g of {sp} (molar mass {fmt(m)} g/mol)?",
             sci(n * 6.022e23, 4), [sci(x * 6.022e23, 4) for x in (n * 2, n / 2, n * 10, 1) if x != n],
             f"n = {fmt(n * m)}/{fmt(m)} = {fmt(n)} mol; N = n × 6.022 × 10^23.")


@gen("c11-01", weight=3)
def _molarity(rng):
    sp, m = rng.choice([("NaOH", 40), ("NaCl", 58.5), ("glucose", 180), ("HCl", 36.5), ("KOH", 56)])
    g = R(rng, 2, 4, 5, 10, 20, 36)
    v = R(rng, 100, 250, 500, 1000)
    M = g / m / (v / 1000)
    return num_q(rng, f"{g} g of {sp} (M = {m} g/mol) is dissolved to make {v} mL of solution. Its molarity is:", M, " M",
                 "M = (mass/M) / volume in L.", wrongs=[g / m, g / m * v / 1000, M * 2])


@gen("c11-01", weight=2)
def _limiting(rng):
    h = R(rng, 2, 4, 6, 10)
    o = R(rng, 16, 32, 48, 64)
    # 2H2 + O2 -> 2H2O; masses in g
    nh, no = h / 2, o / 32
    water = min(nh, 2 * no) * 18
    return num_q(rng, f"{h} g of H2 reacts with {o} g of O2 (2H2 + O2 → 2H2O). The mass of water formed is:", water, " g",
                 "Find the limiting reagent, then use the mole ratio.", wrongs=[(h + o), nh * 18 * 2, no * 18])


@gen("c11-01", weight=2)
def _empirical_pct(rng):
    sp, m, el, mass = rng.choice([("H2O", 18, "hydrogen", 2), ("CO2", 44, "carbon", 12), ("CH4", 16, "carbon", 12),
                                 ("NH3", 17, "nitrogen", 14), ("CaCO3", 100, "calcium", 40), ("C6H12O6", 180, "carbon", 72)])
    return num_q(rng, f"The mass percentage of {el} in {sp} is:", 100 * mass / m, "%", f"{mass}/{m} × 100.",
                 wrongs=[100 * (m - mass) / m, 100 * mass / (m * 2), mass])


# ---------------------------------------------------------------- c11-02 Structure of Atom
@gen("c11-02", weight=3)
def _bohr_energy(rng):
    n = R(rng, 1, 2, 3, 4)
    z = R(rng, 1, 1, 2, 3)
    ion = {1: "a hydrogen atom", 2: "He+", 3: "Li2+"}[z]
    e = -13.6 * z * z / (n * n)
    return num_q(rng, f"The energy of the electron in orbit n = {n} of {ion} is:", e, " eV", "E = -13.6 Z²/n² eV.",
                 wrongs=[-13.6 * z / n, -13.6 * z * z / n, -13.6 / (n * n)])


@gen("c11-02", weight=2)
def _radius(rng):
    n = R(rng, 1, 2, 3, 4)
    z = R(rng, 1, 2, 3)
    ion = {1: "hydrogen", 2: "He+", 3: "Li2+"}[z]
    return num_q(rng, f"The radius of orbit n = {n} of {ion} is:", 52.9 * n * n / z, " pm", "r = 52.9 n²/Z pm.",
                 wrongs=[52.9 * n / z, 52.9 * n * n * z, 52.9 * n * n])


@gen("c11-02", weight=2)
def _lines(rng):
    n = R(rng, 3, 4, 5, 6)
    return num_q(rng, f"An electron falls from n = {n} to n = 1 in a sample of hydrogen atoms. The maximum number of spectral lines is:",
                 n * (n - 1) // 2, "", "Lines = n(n - 1)/2.", wrongs=[n - 1, n, n * (n + 1) // 2], form=lambda x: str(int(x)))


@gen("c11-02", weight=2)
def _orbital_nodes(rng):
    n, l, name = rng.choice([(2, 0, "2s"), (3, 0, "3s"), (3, 1, "3p"), (4, 1, "4p"), (3, 2, "3d"), (4, 2, "4d"), (4, 0, "4s"), (5, 1, "5p")])
    return Q(f"The number of radial nodes in a {name} orbital is:", str(n - l - 1), [str(x) for x in (n - 1, l, n, n - l, 0, 1, 2) if x != n - l - 1],
             f"Radial nodes = n - l - 1 = {n} - {l} - 1.")


table("c11-02", [
    ("Spectral series in the ultraviolet", "Lyman"), ("Spectral series in the visible region", "Balmer"),
    ("Series ending at n = 3", "Paschen"), ("Series ending at n = 4", "Brackett"), ("Series ending at n = 5", "Pfund"),
], "{} (hydrogen):", "The {} series is:")
facts("c11-02", [
    "The Aufbau principle fills orbitals in order of increasing n + l",
    "No two electrons in an atom can have the same four quantum numbers",
    "Hund's rule says electron pairing begins only after each orbital of a subshell has one electron",
    "Chromium has the configuration [Ar] 3d5 4s1",
    "Copper has the configuration [Ar] 3d10 4s1",
    "A d subshell has 5 orbitals",
    "The magnetic quantum number gives the orientation of an orbital",
    "The effect of the uncertainty principle is significant only for microscopic particles such as electrons",
], [
    "Chromium has the configuration [Ar] 3d4 4s2",
    "A p subshell has 5 orbitals",
    "The azimuthal quantum number gives the spin of the electron",
    "The 4s orbital is filled after the 3d orbital",
    "An s orbital is dumbbell-shaped",
    "Two electrons in the same orbital have the same spin",
    "The Balmer series lies in the ultraviolet region",
    "Bohr's model explains spectra of many-electron atoms",
], "atomic structure")

# ---------------------------------------------------------------- c11-03 Classification of Elements and Periodicity
table("c11-03", [
    ("Element with the highest electronegativity", "Fluorine"), ("Element with the most negative electron gain enthalpy", "Chlorine"),
    ("Element with the highest first ionisation enthalpy", "Helium"), ("Most electropositive stable element", "Caesium"),
    ("Element with the largest atomic radius in period 3", "Sodium"), ("Lightest element", "Hydrogen"),
], "{}:", None)
facts("c11-03", [
    "Atomic radius decreases across a period",
    "Ionisation enthalpy generally increases across a period",
    "Nitrogen has a higher first ionisation enthalpy than oxygen",
    "Isoelectronic ions with more protons are smaller",
    "Al3+ is smaller than Na+",
    "Chlorine has a more negative electron gain enthalpy than fluorine",
    "Moseley showed that atomic number is the basis of the periodic law",
    "The element with Z = 120 would be named unbinilium",
], [
    "Atomic radius increases across a period",
    "Oxygen has a higher first ionisation enthalpy than nitrogen",
    "Fluorine has the most negative electron gain enthalpy",
    "Na+ is smaller than Mg2+",
    "Mendeleev's periodic law was based on atomic number",
    "Noble gases have large negative electron gain enthalpies",
    "Electronegativity decreases across a period",
    "O2- is smaller than F-",
], "periodic properties")

# ---------------------------------------------------------------- c11-04 Chemical Bonding and Molecular Structure
table("c11-04", [
    ("BeCl2", "sp, linear"), ("BF3", "sp2, trigonal planar"), ("CH4", "sp3, tetrahedral"), ("PCl5", "sp3d, trigonal bipyramidal"),
    ("SF6", "sp3d2, octahedral"), ("NH3", "sp3, trigonal pyramidal"), ("H2O", "sp3, bent"), ("XeF4", "sp3d2, square planar"),
    ("ClF3", "sp3d, T-shaped"), ("SF4", "sp3d, see-saw"), ("IF7", "sp3d3, pentagonal bipyramidal"), ("XeF2", "sp3d, linear"),
], "The hybridisation and shape of {} are:", "Which molecule is {}?", weight=3)
table("c11-04", [
    ("O2", "2"), ("N2", "3"), ("O2+", "2.5"), ("O2-", "1.5"), ("O2 2- (peroxide)", "1"), ("He2+", "0.5"), ("C2", "2", ["2"]), ("NO", "2.5", ["2.5"]),
], "The bond order of {} is:", None, weight=2)
facts("c11-04", [
    "O2 is paramagnetic with two unpaired electrons",
    "N2 is diamagnetic",
    "Bond order is directly related to bond energy and inversely to bond length",
    "Lone pair-lone pair repulsion is the strongest",
    "The dipole moment of NH3 is higher than that of NF3",
    "BF3 has zero dipole moment",
    "Intramolecular hydrogen bonding occurs in o-nitrophenol",
    "The H-O-H bond angle in water is about 104.5°",
], [
    "N2 is paramagnetic",
    "NF3 has a higher dipole moment than NH3",
    "CO2 is a bent molecule",
    "Bond pair-bond pair repulsion is the strongest",
    "H2O has a bond angle of 109.5°",
    "O2 is diamagnetic",
    "Sigma bonds are formed by sideways overlap",
    "BF3 has a pyramidal shape",
], "chemical bonding")


@gen("c11-04", weight=2)
def _formal_charge(rng):
    v, nb, b, atom = rng.choice([(6, 2, 6, "the central O of O3"), (6, 6, 2, "the singly bonded end O of O3"), (5, 0, 8, "N in NH4+"),
                                 (6, 4, 4, "the doubly bonded end O of O3")])
    fc = v - nb - b // 2
    return Q(f"The formal charge on {atom} is:", f"{fc:+d}" if fc else "0", ["+1", "-1", "0", "+2", "-2"],
             f"FC = V - L - B/2 = {v} - {nb} - {b // 2}.")


# ---------------------------------------------------------------- c11-05 Thermodynamics
@gen("c11-05", weight=3)
def _gibbs(rng):
    dh = R(rng, -100, -50, 20, 40, 60, 90)
    ds = R(rng, -200, -100, 50, 100, 150, 200)
    t = R(rng, 300, 400, 500, 1000)
    dg = dh - t * ds / 1000
    return num_q(rng, f"For a reaction ΔH = {dh} kJ/mol and ΔS = {ds} J/(K·mol). ΔG at {t} K is:", dg, " kJ/mol",
                 "ΔG = ΔH - TΔS (convert ΔS to kJ).", wrongs=[dh - t * ds, dh + t * ds / 1000, dh - ds / 1000])


@gen("c11-05", weight=2)
def _teq(rng):
    dh = R(rng, 20, 30, 40, 60, 90, 180)
    ds = R(rng, 50, 80, 100, 120, 150, 200)
    return num_q(rng, f"A reaction has ΔH = +{dh} kJ/mol and ΔS = +{ds} J/(K·mol). Above what temperature does it become spontaneous?",
                 dh * 1000 / ds, " K", "T = ΔH/ΔS.", wrongs=[dh / ds, ds / dh * 1000, dh * ds])


@gen("c11-05", weight=2)
def _work(rng):
    p = R(rng, 1, 2, 3, 5)
    v1, v2 = R(rng, 1, 2, 5), R(rng, 10, 15, 20)
    return num_q(rng, f"A gas expands against a constant external pressure of {p} atm from {v1} L to {v2} L. The work done on the gas is:",
                 -p * (v2 - v1) * 101.3, " J", "w = -p(ext)ΔV; 1 L atm = 101.3 J.", wrongs=[p * (v2 - v1) * 101.3, -p * (v2 - v1), -p * v2 * 101.3])


@gen("c11-05", weight=2)
def _dh_du(rng):
    dng, eq = rng.choice([("-2", "N2(g) + 3H2(g) → 2NH3(g)"), ("1", "PCl5(g) → PCl3(g) + Cl2(g)"), ("0", "H2(g) + Cl2(g) → 2HCl(g)"),
                          ("-1", "2SO2(g) + O2(g) → 2SO3(g)"), ("1", "CaCO3(s) → CaO(s) + CO2(g)"), ("-0.5", "H2(g) + ½O2(g) → H2O(g)")])
    return Q(f"For the reaction {eq}, Δng is:", dng, [x for x in ("-2", "-1", "-0.5", "0", "1", "2") if x != dng],
             "Δng = moles of gaseous products - moles of gaseous reactants; ΔH = ΔU + ΔngRT.")


facts("c11-05", [
    "Enthalpy and entropy are state functions",
    "Work and heat are path functions",
    "For an isolated system ΔU = 0",
    "A reaction with ΔH negative and ΔS positive is spontaneous at all temperatures",
    "For an ideal gas in a free expansion w = 0",
    "Entropy of a perfect crystal at 0 K is zero",
    "Mass and volume are extensive properties",
    "Temperature and pressure are intensive properties",
], [
    "Heat is a state function",
    "A reaction with ΔH positive and ΔS negative is spontaneous at high temperature",
    "Volume is an intensive property",
    "Entropy decreases when ice melts",
    "ΔG > 0 means the reaction is spontaneous",
    "Internal energy of an isolated system keeps rising",
    "Density is an extensive property",
    "ΔH = ΔU for every gas-phase reaction",
], "thermodynamics")

# ---------------------------------------------------------------- c11-06 Equilibrium
@gen("c11-06", weight=3)
def _ph(rng):
    kind = rng.choice(["acid", "base", "weak"])
    if kind == "acid":
        e = R(rng, 1, 2, 3, 4, 5)
        c = R(rng, 1, 2, 5)
        conc = c * 10 ** -e
        return num_q(rng, f"The pH of {c} × 10^-{e} M HCl is:", -math.log10(conc), "", "pH = -log[H+].",
                     wrongs=[e, 14 + math.log10(conc), -math.log10(conc / 2)], form=lambda x: fmt(x, 2))
    if kind == "base":
        e = R(rng, 1, 2, 3, 4)
        return num_q(rng, f"The pH of 10^-{e} M NaOH at 25 °C is:", 14 - e, "", "pOH = -log[OH-]; pH = 14 - pOH.",
                     wrongs=[e, 14 + e, 7 + e], form=lambda x: fmt(x, 2))
    ka = R(rng, 1e-5, 1.8e-5, 4e-6, 1e-4)
    c = R(rng, 0.1, 0.01, 0.2)
    h = math.sqrt(ka * c)
    return num_q(rng, f"The pH of a {c} M weak acid with Ka = {sci(ka, 2)} is about:", -math.log10(h), "", "[H+] = √(Ka C).",
                 wrongs=[-math.log10(ka * c), -math.log10(c), -math.log10(ka)], form=lambda x: fmt(x, 2))


@gen("c11-06", weight=2)
def _ksp(rng):
    salt, kind = rng.choice([("AgCl", "AB"), ("BaSO4", "AB"), ("CaF2", "AB2"), ("PbI2", "AB2"), ("Ag2CrO4", "A2B"), ("Al(OH)3", "AB3"),
                             ("Ca3(PO4)2", "A3B2")])
    expr = {"AB": "s²", "AB2": "4s³", "A2B": "4s³", "AB3": "27s⁴", "A3B2": "108s⁵"}[kind]
    if rng.random() < 0.5 or kind in ("AB3", "A3B2"):
        return Q(f"The solubility of {salt} is s mol/L. Its solubility product Ksp in terms of s is:", expr,
                 ["s²", "4s³", "27s⁴", "108s⁵", "s³", "2s²"], f"Write Ksp from the ions {salt} gives: Ksp = {expr}.")
    s, e = R(rng, 1, 2, 3, 5), R(rng, 3, 4, 5)
    mult, power = {"AB": (1, 2), "AB2": (4, 3), "A2B": (4, 3), "AB3": (27, 4), "A3B2": (108, 5)}[kind]
    sv = s * 10.0 ** -e
    ksp = mult * sv ** power
    return Q(f"The solubility of {salt} is {s} × 10^-{e} mol/L. Its Ksp is:", sci(ksp),
             [sci(mult * sv ** p) for p in (2, 3, 4) if p != power] + [sci(sv ** power), sci(2 * ksp)],
             f"Ksp = {mult}s^{power}.")


@gen("c11-06", weight=2)
def _kpkc(rng):
    eq, dn = rng.choice([("N2 + 3H2 ⇌ 2NH3", -2), ("PCl5 ⇌ PCl3 + Cl2", 1), ("H2 + I2 ⇌ 2HI", 0), ("2SO2 + O2 ⇌ 2SO3", -1),
                         ("N2O4 ⇌ 2NO2", 1), ("2NO2 ⇌ N2O4", -1)])
    ans = "Kp = Kc" if dn == 0 else f"Kp = Kc(RT)^{dn}"
    return Q(f"For the gas-phase equilibrium {eq}, Kp and Kc are related by:", ans,
             ["Kp = Kc", "Kp = Kc(RT)^1", "Kp = Kc(RT)^-1", "Kp = Kc(RT)^-2", "Kp = Kc(RT)^2"], f"Δn(g) = {dn}.")


facts("c11-06", [
    "Increasing pressure shifts N2 + 3H2 ⇌ 2NH3 towards ammonia",
    "Adding a catalyst does not change the equilibrium constant",
    "The equilibrium constant changes only with temperature",
    "A buffer of acetic acid and sodium acetate resists change in pH",
    "Common ion effect lowers the ionisation of a weak electrolyte",
    "Water is amphoteric",
    "BF3 is a Lewis acid",
    "The conjugate base of a strong acid is weak",
], [
    "A catalyst shifts the equilibrium towards products",
    "Kc changes when the concentration of a reactant changes",
    "The conjugate base of a strong acid is strong",
    "NH3 is a Lewis acid",
    "Adding inert gas at constant volume shifts the equilibrium",
    "pH of pure water at 25 °C is 14",
    "The common ion effect increases the ionisation of a weak acid",
    "Increasing pressure favours the side with more gas molecules",
], "equilibrium")

# ---------------------------------------------------------------- c11-07 Redox Reactions
table("c11-07", [
    ("S in H2SO4", "+6"), ("Cr in K2Cr2O7", "+6", ["+6"]), ("Mn in KMnO4", "+7"), ("O in H2O2", "-1"), ("O in OF2", "+2"),
    ("N in HNO3", "+5"), ("N in NH3", "-3"), ("C in CH4", "-4"), ("Fe in Fe3O4", "+8/3"), ("S in Na2S4O6", "+2.5"),
    ("P in H3PO4", "+5", ["+5"]), ("Cl in HClO4", "+7", ["+7"]), ("H in NaH", "-1", ["-1"]),
], "The oxidation number of {} is:", None, weight=3)
facts("c11-07", [
    "Oxidation is loss of electrons",
    "In a disproportionation reaction the same element is both oxidised and reduced",
    "Fluorine always has oxidation number -1 in its compounds",
    "KMnO4 is a strong oxidising agent in acidic medium",
    "A more negative standard reduction potential means a stronger reducing agent",
    "In 2H2O2 → 2H2O + O2, oxygen disproportionates",
    "Zinc displaces copper from copper sulphate solution",
    "Oxygen has oxidation number -1/2 in KO2",
], [
    "Oxidation is gain of electrons",
    "Fluorine shows +1 in OF2",
    "Copper displaces zinc from zinc sulphate solution",
    "The oxidation number of oxygen is always -2",
    "A reducing agent is itself reduced",
    "In KO2 oxygen has oxidation number -2",
    "Hydrogen has oxidation number +1 in all its compounds",
    "A higher standard reduction potential means a stronger reducing agent",
], "redox reactions")

# ---------------------------------------------------------------- c11-08 Organic Chemistry: Some Basic Principles
table("c11-08", [
    ("Lassaigne's test for nitrogen", "Prussian blue colour"), ("Lassaigne's test for sulphur with sodium nitroprusside", "Violet colour"),
    ("Lassaigne's test for chlorine", "White precipitate soluble in ammonia"), ("Beilstein test", "Green flame for halogens"),
    ("Kjeldahl's method", "Estimation of nitrogen"), ("Carius method", "Estimation of halogens and sulphur"),
    ("Dumas method", "Estimation of nitrogen as N2 gas"),
], "{}:", "Which test or method: {}?")
facts("c11-08", [
    "A tertiary carbocation is more stable than a secondary one",
    "Hyperconjugation is also called no-bond resonance",
    "The -NO2 group has a -I and -R effect",
    "Electrophiles are electron-seeking species",
    "Homolytic cleavage forms free radicals",
    "Steam distillation is used for substances volatile in steam and immiscible with water, such as aniline",
    "Kjeldahl's method cannot be used for nitro and azo compounds or nitrogen in rings",
    "Chromatography separates substances by differential adsorption or partition",
], [
    "A primary carbocation is the most stable",
    "Nucleophiles are electron-deficient species",
    "Heterolytic cleavage forms free radicals",
    "The -OH group has a -R effect",
    "Kjeldahl's method works for pyridine nitrogen",
    "Resonance structures differ in the positions of atoms",
    "A methyl group shows a -I effect",
    "Sublimation is used for liquids that boil without decomposing",
], "basic organic chemistry")

# ---------------------------------------------------------------- c11-09 Hydrocarbons
table("c11-09", [
    ("Wurtz reaction", "Alkyl halide + sodium in dry ether gives a higher alkane"),
    ("Kolbe's electrolysis", "Electrolysis of sodium salts of carboxylic acids gives alkanes"),
    ("Markovnikov's rule", "H adds to the carbon with more hydrogens in HX addition to unsymmetrical alkenes"),
    ("Peroxide (Kharasch) effect", "Anti-Markovnikov addition of HBr only"),
    ("Ozonolysis", "Breaks a C=C bond to give carbonyl compounds"), ("Lindlar's catalyst", "Reduces alkynes to cis-alkenes"),
    ("Friedel-Crafts alkylation", "Alkyl group added to benzene using anhydrous AlCl3"),
], "{}:", "Which reaction or rule: {}?", weight=2)
facts("c11-09", [
    "Benzene has 6 delocalised π electrons and follows Hückel's rule",
    "Staggered ethane is more stable than eclipsed ethane",
    "Ethyne is more acidic than ethene",
    "Sodium in liquid ammonia reduces alkynes to trans-alkenes",
    "Benzene undergoes mainly electrophilic substitution",
    "The -OH group of phenol directs incoming groups to ortho and para positions",
    "Propyne with dilute H2SO4 and HgSO4 gives acetone",
    "Cyclooctatetraene is non-aromatic",
], [
    "Eclipsed ethane is more stable than staggered ethane",
    "Ethene is more acidic than ethyne",
    "The peroxide effect is seen with HCl and HI",
    "Benzene mainly undergoes electrophilic addition",
    "The -NO2 group is ortho-para directing",
    "Lindlar's catalyst gives trans-alkenes",
    "Wurtz reaction is used to make methane",
    "Cyclooctatetraene is aromatic",
], "hydrocarbons")

# ---------------------------------------------------------------- c12-01 Solutions
@gen("c12-01", weight=3)
def _colligative(rng):
    kind = rng.choice(["bp", "fp", "osm"])
    m = R(rng, 0.1, 0.2, 0.5, 1)
    i, name = rng.choice([(1, "glucose"), (2, "NaCl"), (3, "CaCl2"), (1, "urea"), (2, "KCl")])
    if kind == "bp":
        return num_q(rng, f"The elevation in boiling point of a {m} molal aqueous {name} solution (Kb = 0.52 K kg/mol, complete dissociation) is:",
                     i * 0.52 * m, " K", "ΔTb = i Kb m.", wrongs=[0.52 * m, i * 1.86 * m, 0.52 * m / i])
    if kind == "fp":
        return num_q(rng, f"The depression in freezing point of a {m} molal aqueous {name} solution (Kf = 1.86 K kg/mol, complete dissociation) is:",
                     i * 1.86 * m, " K", "ΔTf = i Kf m.", wrongs=[1.86 * m, i * 0.52 * m, 1.86 * m / i])
    t = R(rng, 273, 300, 310)
    return num_q(rng, f"The osmotic pressure of a {m} M {name} solution at {t} K (R = 0.0821 L atm/(K mol), complete dissociation) is:",
                 i * m * 0.0821 * t, " atm", "π = iCRT.", wrongs=[m * 0.0821 * t, i * m * 8.314 * t, i * m * 0.0821])


@gen("c12-01", weight=2)
def _raoult(rng):
    pa, pb = R(rng, 100, 200, 400, 600), R(rng, 50, 150, 300, 450)
    xa = R(rng, 0.2, 0.25, 0.4, 0.5, 0.6, 0.75)
    p = pa * xa + pb * (1 - xa)
    return num_q(rng, f"Two liquids form an ideal solution. Vapour pressures of pure A and B are {pa} and {pb} mm Hg. For x(A) = {xa}, the total vapour pressure is:",
                 p, " mm Hg", "P = pA° xA + pB° xB.", wrongs=[pa + pb, (pa + pb) / 2, pa * xa])


@gen("c12-01")
def _vant_hoff(rng):
    salt, i = rng.choice([("K4[Fe(CN)6]", 5), ("Al2(SO4)3", 5), ("K2SO4", 3), ("NaCl", 2), ("MgCl2", 3), ("glucose", 1), ("K3[Fe(CN)6]", 4)])
    return Q(f"The van 't Hoff factor of {salt} assuming complete dissociation is:", str(i), [str(x) for x in range(1, 7) if x != i],
             f"{salt} gives {i} particle(s) per formula unit.")


facts("c12-01", [
    "A solution of ethanol and water shows positive deviation from Raoult's law",
    "Chloroform and acetone show negative deviation from Raoult's law",
    "Maximum boiling azeotropes show negative deviation",
    "Henry's law constant KH increases with temperature for gases in water",
    "Molality does not change with temperature",
    "Reverse osmosis is used to desalinate sea water",
    "0.9% NaCl solution is isotonic with blood",
    "Association of acetic acid in benzene makes i less than 1",
], [
    "Molarity does not change with temperature",
    "Ethanol and water show negative deviation",
    "Chloroform and acetone show positive deviation",
    "Solubility of a gas in a liquid increases with temperature",
    "Cells swell in a hypertonic solution",
    "Colligative properties depend on the nature of the solute",
    "Dissociation makes i less than 1",
    "A higher KH means higher solubility of a gas",
], "solutions")

# ---------------------------------------------------------------- c12-02 Electrochemistry
@gen("c12-02", weight=3)
def _emf(rng):
    pairs = [("Zn2+/Zn", -0.76), ("Cu2+/Cu", 0.34), ("Ag+/Ag", 0.80), ("Fe2+/Fe", -0.44), ("Mg2+/Mg", -2.37), ("Ni2+/Ni", -0.25)]
    (a, ea), (b, eb) = rng.sample(pairs, 2)
    cat, an = ((a, ea), (b, eb)) if ea > eb else ((b, eb), (a, ea))
    e = cat[1] - an[1]
    return num_q(rng, f"Standard reduction potentials: {a} = {ea} V, {b} = {eb} V. The standard emf of the cell built from them is:",
                 e, " V", "E°cell = E°cathode - E°anode.", wrongs=[ea + eb, abs(ea + eb) + 0.1, -e], form=lambda x: fmt(x, 2))


@gen("c12-02", weight=2)
def _dg_cell(rng):
    n = R(rng, 1, 2, 3)
    e = R(rng, 0.34, 0.46, 1.1, 1.56, 0.8)
    return num_q(rng, f"For a cell reaction with n = {n} and E°cell = {e} V, ΔG° is (F = 96500 C/mol):", -n * 96500 * e / 1000, " kJ/mol",
                 "ΔG° = -nFE°.", wrongs=[n * 96500 * e / 1000, -96500 * e / 1000, -n * 96500 * e])


@gen("c12-02", weight=2)
def _faraday(rng):
    metal, z, m = rng.choice([("copper", 2, 63.5), ("silver", 1, 108), ("aluminium", 3, 27), ("zinc", 2, 65.4)])
    i, t = R(rng, 1, 2, 5, 10), R(rng, 965, 1930, 9650)
    w = i * t * m / (z * 96500)
    return num_q(rng, f"A current of {i} A is passed for {t} s through a solution of a {metal} salt (M = {m}, charge {z}+). The mass of {metal} deposited is:",
                 w, " g", "w = I t M / (z F).", wrongs=[i * t * m / 96500, w * z * z, i * t / 96500])


facts("c12-02", [
    "Molar conductivity increases on dilution for both strong and weak electrolytes",
    "Conductivity (specific conductance) decreases on dilution",
    "Kohlrausch's law gives the limiting molar conductivity of weak electrolytes",
    "The SI unit of conductivity is S/m",
    "In a galvanic cell the anode is negative",
    "A salt bridge keeps the two half-cells electrically neutral",
    "Rusting of iron is an electrochemical process",
    "The hydrogen-oxygen fuel cell was used in the Apollo space programme",
], [
    "Conductivity increases on dilution",
    "In a galvanic cell the cathode is negative",
    "Molar conductivity of a strong electrolyte decreases sharply on dilution",
    "The standard hydrogen electrode has E° = 1 V",
    "Lead storage battery uses KOH as the electrolyte",
    "A more negative E° means a stronger oxidising agent",
    "Galvanising means coating iron with tin",
    "Faraday's constant is 96500 C per electron",
], "electrochemistry")

# ---------------------------------------------------------------- c12-03 Chemical Kinetics
@gen("c12-03", weight=3)
def _half_life(rng):
    k = R(rng, 0.693, 0.0693, 0.1386, 0.231, 6.93e-3)
    ask = rng.choice(["t", "frac"])
    t = 0.693 / k
    if ask == "t":
        return num_q(rng, f"A first-order reaction has k = {sig(k, 3)} per minute. Its half-life is:", t, " min", "t½ = 0.693/k.",
                     wrongs=[1 / k, k / 0.693, 2 * t])
    n = R(rng, 2, 3, 4, 5)
    return Q(f"For a first-order reaction, the fraction of reactant left after {n} half-lives is:", f"1/{2 ** n}",
             [f"1/{x}" for x in (2 * n, 2 ** (n + 1), 2 ** (n - 1), n * n)], f"(1/2)^{n} = 1/{2 ** n}.")


@gen("c12-03", weight=2)
def _order_units(rng):
    order, unit = rng.choice([(0, "mol L^-1 s^-1"), (1, "s^-1"), (2, "L mol^-1 s^-1"), (3, "L^2 mol^-2 s^-1")])
    names = {0: "zero", 1: "first", 2: "second", 3: "third"}
    return Q(f"The unit of the rate constant of a {names[order]}-order reaction is:", unit,
             ["mol L^-1 s^-1", "s^-1", "L mol^-1 s^-1", "L^2 mol^-2 s^-1"], "Unit = (mol L^-1)^(1 - n) s^-1.")


@gen("c12-03", weight=2)
def _rate_change(rng):
    n = R(rng, 1, 2, 3)
    f = R(rng, 2, 3, 4)
    return num_q(rng, f"A reaction is of order {n} in A. If [A] is made {f} times, the rate becomes how many times?", f ** n, " times",
                 "rate ∝ [A]^n.", wrongs=[f * n, f, f ** (n + 1)], form=lambda x: str(int(x)))


@gen("c12-03")
def _temp(rng):
    rise = R(rng, 10, 20, 30, 40)
    return num_q(rng, f"If the rate of a reaction doubles for every 10 °C rise, by how many times does it increase for a {rise} °C rise?",
                 2 ** (rise // 10), " times", "Factor = 2^(ΔT/10).", wrongs=[2 * rise // 10, rise // 10, 2 ** (rise // 10 + 1)], form=lambda x: str(int(x)))


facts("c12-03", [
    "The half-life of a first-order reaction does not depend on initial concentration",
    "The half-life of a zero-order reaction is proportional to the initial concentration",
    "Hydrolysis of ethyl acetate in excess water is a pseudo first-order reaction",
    "Radioactive decay follows first-order kinetics",
    "A catalyst lowers the activation energy",
    "Order of a reaction can be zero or fractional",
    "Molecularity cannot be zero or fractional",
    "Decomposition of NH3 on a hot platinum surface is zero order at high pressure",
], [
    "Molecularity can be fractional",
    "A catalyst changes the equilibrium constant",
    "The half-life of a first-order reaction depends on initial concentration",
    "Rate constant does not depend on temperature",
    "Order is always equal to molecularity",
    "A catalyst raises the activation energy",
    "Zero-order reactions have a half-life independent of concentration",
    "The unit of a first-order rate constant is mol L^-1 s^-1",
], "chemical kinetics")

# ---------------------------------------------------------------- c12-04 The d- and f-Block Elements
IONS = [("Sc3+", 0), ("Ti3+", 1), ("V3+", 2), ("Cr3+", 3), ("Mn2+", 5), ("Fe2+", 4), ("Fe3+", 5), ("Co2+", 3), ("Ni2+", 2), ("Cu2+", 1), ("Zn2+", 0), ("Cu+", 0)]


@gen("c12-04", weight=3)
def _spin_only(rng):
    ion, n = rng.choice(IONS)
    mu = math.sqrt(n * (n + 2))
    return num_q(rng, f"The spin-only magnetic moment of {ion} (aqueous) is about:", mu, " BM", f"μ = √(n(n + 2)) with n = {n} unpaired electrons.",
                 wrongs=[math.sqrt(k * (k + 2)) for k in (n + 1, n - 1, n + 2, 5, 1) if k >= 1 and k != n], form=lambda x: fmt(x, 2))


table("c12-04", [
    ("Manganese", "Shows the highest oxidation state (+7) in the first transition series"), ("Zinc", "Not regarded as a transition element; no partly filled d orbitals"),
    ("Scandium", "Shows only +3 in its common compounds"), ("Copper", "Has a positive standard reduction potential E°(M2+/M)"),
    ("Chromium", "Its +6 compound K2Cr2O7 is orange"),
], "{}:", "Which first-row metal: {}?")
facts("c12-04", [
    "Lanthanoid contraction makes Zr and Hf nearly equal in size",
    "Most transition metal ions are coloured because of d-d transitions",
    "KMnO4 is purple and is made from pyrolusite (MnO2)",
    "Cr2O7 2- changes to CrO4 2- when the pH is raised",
    "Actinoids show a wider range of oxidation states than lanthanoids",
    "The common oxidation state of lanthanoids is +3",
    "Ce4+ is a good oxidising agent",
    "Transition metals and their compounds are good catalysts",
], [
    "Zn2+ salts are deeply coloured",
    "Lanthanoid contraction makes Hf much larger than Zr",
    "Lanthanoids commonly show +2 as the most stable state",
    "Sc3+ has five unpaired electrons",
    "Cr2O7 2- is formed when chromate solution is made alkaline",
    "Transition metals have low melting points",
    "Mn shows a maximum oxidation state of +4",
    "Eu2+ is a strong oxidising agent",
], "d- and f-block elements")

# ---------------------------------------------------------------- c12-05 Coordination Compounds
table("c12-05", [
    ("[Ni(CO)4]", "sp3, tetrahedral, diamagnetic"), ("[Ni(CN)4]2-", "dsp2, square planar, diamagnetic"),
    ("[NiCl4]2-", "sp3, tetrahedral, paramagnetic"), ("[Co(NH3)6]3+", "d2sp3, octahedral, diamagnetic"),
    ("[CoF6]3-", "sp3d2, octahedral, paramagnetic"), ("[Fe(CN)6]4-", "d2sp3, octahedral, diamagnetic", ["d2sp3, octahedral, diamagnetic"]),
], "The hybridisation, shape and magnetism of {} are:", None, weight=2)
table("c12-05", [
    ("[Co(NH3)5Cl]Cl2", "3 ions in solution"), ("[Co(NH3)6]Cl3", "4 ions in solution"), ("[Co(NH3)4Cl2]Cl", "2 ions in solution"),
    ("[Co(NH3)3Cl3]", "No ions; non-electrolyte"), ("K4[Fe(CN)6]", "5 ions in solution"),
], "{} gives:", "Which complex gives {}?")
facts("c12-05", [
    "CO and CN- are strong field ligands",
    "EDTA is a hexadentate ligand",
    "Ethylenediamine is a bidentate ligand",
    "In the spectrochemical series I- is a weaker field ligand than F-",
    "Square planar complexes of type MA2B2 show geometrical isomerism",
    "[Co(en)3]3+ shows optical isomerism",
    "Haemoglobin contains Fe and chlorophyll contains Mg",
    "Wilkinson's catalyst is a rhodium complex used in hydrogenation",
], [
    "I- is a strong field ligand",
    "EDTA is a bidentate ligand",
    "Tetrahedral complexes show geometrical isomerism",
    "Chlorophyll contains iron",
    "Vitamin B12 contains nickel",
    "Ammonia is a chelating ligand",
    "Cisplatin is the trans isomer of [Pt(NH3)2Cl2]",
    "Strong field ligands give high-spin octahedral complexes",
], "coordination compounds")

# ---------------------------------------------------------------- c12-06 Haloalkanes and Haloarenes
table("c12-06", [
    ("SN2 reaction", "One step, inversion of configuration, fastest for primary halides"),
    ("SN1 reaction", "Carbocation intermediate, racemisation, fastest for tertiary halides"),
    ("Finkelstein reaction", "R-Cl or R-Br with NaI in dry acetone gives R-I"),
    ("Swarts reaction", "Alkyl fluorides made using AgF, Hg2F2 or SbF3"),
    ("Sandmeyer reaction", "Diazonium salt with Cu2Cl2/HCl gives chlorobenzene"),
    ("Wurtz-Fittig reaction", "Aryl halide + alkyl halide + sodium gives an alkylbenzene"),
], "{}:", "Which reaction: {}?", weight=2)
facts("c12-06", [
    "Chloroform is stored in dark bottles because it forms phosgene in light and air",
    "DDT is non-biodegradable and accumulates in fatty tissue",
    "Haloarenes are less reactive to nucleophilic substitution than haloalkanes",
    "An -NO2 group at ortho or para increases the reactivity of chlorobenzene to nucleophiles",
    "Alcoholic KOH favours elimination; aqueous KOH favours substitution",
    "Saytzeff's rule says the more substituted alkene is the main product of elimination",
    "Grignard reagents must be made in dry ether",
    "Iodoform has antiseptic properties due to liberated iodine",
], [
    "SN2 reactions are fastest for tertiary halides",
    "SN1 reactions give complete inversion",
    "Chlorobenzene reacts with NaOH easily at room temperature",
    "Aqueous KOH mainly gives alkenes",
    "Freons are highly reactive and toxic gases",
    "Chloroform is stored in clear bottles in sunlight",
    "Grignard reagents are stable in water",
    "A meta -NO2 group activates chlorobenzene most strongly",
], "haloalkanes and haloarenes")

# ---------------------------------------------------------------- c12-07 Alcohols, Phenols and Ethers
table("c12-07", [
    ("Lucas test", "Distinguishes primary, secondary and tertiary alcohols by turbidity"),
    ("Reimer-Tiemann reaction", "Phenol + CHCl3 + NaOH gives salicylaldehyde"),
    ("Kolbe's reaction", "Sodium phenoxide + CO2 gives salicylic acid"),
    ("Williamson synthesis", "Alkyl halide + sodium alkoxide gives an ether"),
    ("Cumene process", "Makes phenol and acetone"), ("Hydroboration-oxidation", "Anti-Markovnikov alcohol from an alkene"),
], "{}:", "Which reaction or test: {}?", weight=2)
facts("c12-07", [
    "Phenol is more acidic than ethanol",
    "o-Nitrophenol is steam volatile because of intramolecular hydrogen bonding",
    "Tertiary alcohols react fastest in the Lucas test",
    "Phenol with bromine water gives 2,4,6-tribromophenol",
    "Methanol is very poisonous and can cause blindness",
    "Alcohols have higher boiling points than ethers of similar mass because of hydrogen bonding",
    "The -NO2 group increases the acidity of phenol",
    "PCC oxidises primary alcohols to aldehydes",
], [
    "Ethanol is more acidic than phenol",
    "p-Nitrophenol is steam volatile",
    "Primary alcohols react fastest in the Lucas test",
    "The -CH3 group increases the acidity of phenol",
    "Ethers have higher boiling points than alcohols of similar mass",
    "Phenol does not react with bromine water",
    "Williamson synthesis works best with tertiary alkyl halides",
    "Ethanol is called wood spirit",
], "alcohols, phenols and ethers")

# ---------------------------------------------------------------- c12-08 Aldehydes, Ketones and Carboxylic Acids
table("c12-08", [
    ("Cannizzaro reaction", "Aldehydes without α-hydrogen disproportionate in concentrated alkali"),
    ("Aldol condensation", "Aldehydes or ketones with α-hydrogen in dilute alkali give β-hydroxy carbonyls"),
    ("Clemmensen reduction", "C=O to CH2 with Zn-Hg and conc. HCl"), ("Wolff-Kishner reduction", "C=O to CH2 with NH2NH2 and KOH in glycol"),
    ("Rosenmund reduction", "Acid chloride to aldehyde with H2, Pd-BaSO4"), ("Stephen reaction", "Nitrile to aldehyde with SnCl2/HCl then water"),
    ("HVZ reaction", "α-halogenation of carboxylic acids with X2 and red phosphorus"), ("Etard reaction", "Toluene to benzaldehyde with chromyl chloride"),
], "{}:", "Which reaction: {}?", weight=2)
facts("c12-08", [
    "Tollens' reagent gives a silver mirror with aldehydes",
    "Fehling's solution is not reduced by aromatic aldehydes",
    "Ketones with a CH3CO- group give the iodoform test",
    "Formic acid reduces Tollens' reagent",
    "Electron-withdrawing groups increase the acidity of carboxylic acids",
    "Carboxylic acids exist as dimers in the vapour phase",
    "Benzaldehyde undergoes the Cannizzaro reaction",
    "Ethanol gives a positive iodoform test",
], [
    "Ketones give a silver mirror with Tollens' reagent",
    "Acetaldehyde undergoes the Cannizzaro reaction",
    "Formaldehyde gives a positive iodoform test",
    "Acetic acid is stronger than chloroacetic acid",
    "Benzaldehyde reduces Fehling's solution readily",
    "Carboxylic acids are weaker acids than phenols",
    "Clemmensen reduction converts C=O to CH-OH",
    "Methanol gives a positive iodoform test",
], "carbonyl compounds")

# ---------------------------------------------------------------- c12-09 Amines
table("c12-09", [
    ("Hoffmann bromamide degradation", "Amide with Br2/NaOH gives an amine with one carbon less"),
    ("Gabriel phthalimide synthesis", "Makes pure primary aliphatic amines"), ("Carbylamine reaction", "Primary amine + CHCl3 + KOH gives a foul-smelling isocyanide"),
    ("Hinsberg's reagent", "Benzenesulphonyl chloride; distinguishes 1°, 2° and 3° amines"), ("Diazotisation", "Aniline + NaNO2/HCl at 273-278 K"),
    ("Coupling reaction", "Benzenediazonium chloride + phenol gives an orange azo dye"),
], "{}:", "Which reaction or reagent: {}?", weight=2)
facts("c12-09", [
    "In aqueous solution (CH3)2NH is the strongest base among the methylamines",
    "Aniline is a weaker base than methylamine",
    "Gabriel synthesis cannot make aromatic primary amines",
    "Direct nitration of aniline gives a large amount of meta product because of anilinium ion",
    "Acetylation of aniline moderates the activating effect of -NH2",
    "Tertiary amines do not react with Hinsberg's reagent",
    "Aromatic diazonium salts are more stable than aliphatic ones",
    "Only primary amines give the carbylamine test",
], [
    "Aniline is a stronger base than methylamine",
    "Gabriel synthesis is used to make aniline",
    "Secondary amines give the carbylamine test",
    "Tertiary amines react with Hinsberg's reagent to give a soluble product",
    "Aliphatic diazonium salts are stable at room temperature",
    "Aniline undergoes Friedel-Crafts reaction easily",
    "Hoffmann bromamide degradation adds one carbon atom",
    "(CH3)3N is the strongest base among the methylamines in water",
], "amines")

# ---------------------------------------------------------------- c12-10 Biomolecules
table("c12-10", [
    ("Vitamin A", "Night blindness"), ("Vitamin B1", "Beriberi"), ("Vitamin B12", "Pernicious anaemia"), ("Vitamin C", "Scurvy"),
    ("Vitamin D", "Rickets"), ("Vitamin K", "Increased blood clotting time"), ("Vitamin E", "Increased fragility of red blood cells"),
    ("Vitamin B6", "Convulsions"),
], "Deficiency of {} causes:", "Which vitamin deficiency causes {}?", weight=2)
facts("c12-10", [
    "Sucrose is a non-reducing sugar",
    "Maltose and lactose are reducing sugars",
    "Glucose has four chiral carbons in its open-chain form",
    "Starch is made of amylose and amylopectin",
    "DNA contains deoxyribose and thymine, RNA contains ribose and uracil",
    "Vitamins A, D, E and K are fat-soluble",
    "Denaturation destroys secondary and tertiary structure but not primary structure",
    "Insulin is a protein hormone",
], [
    "Sucrose is a reducing sugar",
    "Vitamin C is fat-soluble",
    "RNA contains thymine",
    "Denaturation breaks the peptide bonds of a protein",
    "Glucose is a ketohexose",
    "Fructose is an aldohexose",
    "Starch is a polymer of β-glucose",
    "Vitamin B12 is stored in large amounts in fat tissue",
], "biomolecules")

# ---------------------------------------------------------------- c12-pb p-Block Elements
table("c12-pb", [
    ("Contact process", "H2SO4 with V2O5 catalyst"), ("Ostwald process", "HNO3 from NH3 with Pt/Rh gauze"),
    ("Haber process", "NH3 with iron oxide catalyst"), ("Deacon's process", "Cl2 by oxidising HCl with CuCl2"),
    ("Bleaching powder", "Ca(OCl)2"), ("Laughing gas", "N2O"),
], "{}:", "What is: {}?")
facts("c12-pb", [
    "Among hydrides of group 15, NH3 is the most basic",
    "Bond angle decreases from NH3 to BiH3",
    "Fluorine is the strongest oxidising halogen",
    "HF is the weakest hydrohalic acid in water",
    "Ozone is a strong oxidising agent",
    "Xenon forms compounds such as XeF2, XeF4 and XeF6",
    "White phosphorus is more reactive than red phosphorus",
    "H3PO2 is a strong reducing agent because it has two P-H bonds",
], [
    "BiH3 is the most basic group 15 hydride",
    "HF is the strongest hydrohalic acid in water",
    "Red phosphorus is more reactive than white phosphorus",
    "Helium forms many stable compounds",
    "H3PO4 is a strong reducing agent",
    "Iodine is the strongest oxidising halogen",
    "Bond angle increases from NH3 to BiH3",
    "Nitrogen readily forms pentahalides like NCl5",
], "p-block elements")

# ---------------------------------------------------------------- c12-pr Principles Related to Practical Chemistry
table("c12-pr", [
    ("Pb2+ with KI", "Yellow precipitate"), ("Cu2+ with K4[Fe(CN)6]", "Chocolate-brown precipitate"),
    ("Fe3+ with K4[Fe(CN)6]", "Prussian blue colour"), ("Ni2+ with dimethylglyoxime", "Rosy red precipitate"),
    ("NH4+ with Nessler's reagent", "Brown precipitate"), ("Ba2+ in a flame", "Apple-green flame"),
    ("Ca2+ in a flame", "Brick-red flame"), ("Sr2+ in a flame", "Crimson-red flame"),
], "{} gives:", "Which ion or test gives a {}?")
facts("c12-pr", [
    "KMnO4 acts as its own indicator in redox titrations",
    "Phenolphthalein is used for titrating a strong base",
    "Group II cations are precipitated as sulphides in acidic medium",
    "Group III cations Fe3+ and Al3+ are precipitated as hydroxides with NH4Cl and NH4OH",
    "The brown ring test is used for nitrate ions",
    "Chromyl chloride test is used to detect chloride ions",
    "Carbonate gives effervescence of CO2 with dilute HCl",
    "Mohr's salt is ferrous ammonium sulphate",
], [
    "Group II cations are precipitated as hydroxides",
    "The brown ring test is used for sulphate ions",
    "Chromyl chloride test detects bromide",
    "Methyl orange is used for titrating a weak acid with a strong base",
    "KMnO4 titrations are done in strongly alkaline medium",
    "Barium gives a crimson flame",
    "Mohr's salt is ferric chloride",
    "Group IV cations are precipitated in strongly acidic H2S",
], "practical chemistry")

# ---------------------------------------------------------------- more for the thinner chapters
table("c11-03", [
    ("Group 1 elements", "Alkali metals"), ("Group 2 elements", "Alkaline earth metals"), ("Group 16 elements", "Chalcogens"),
    ("Group 17 elements", "Halogens"), ("Group 18 elements", "Noble gases"), ("f-block elements", "Inner transition elements"),
], "{} are called:", "{} belong to which group or block?")
table("c11-03", [
    ("first ionisation enthalpy of Na, Mg, Al and Si", "Na < Al < Mg < Si"), ("first ionisation enthalpy of B, C, N and O", "B < C < O < N"),
    ("negative electron gain enthalpy of F, Cl, Br and I", "I < Br < F < Cl"), ("atomic radius of Li, Na, K and Rb", "Li < Na < K < Rb"),
    ("ionic radius of N3-, O2-, F- and Na+", "Na+ < F- < O2- < N3-"),
], "The correct order of {} is:", None)

table("c11-07", [
    ("2H2O2 → 2H2O + O2", "Disproportionation"), ("Zn + CuSO4 → ZnSO4 + Cu", "Displacement"), ("2KClO3 → 2KCl + 3O2", "Decomposition"),
    ("C + O2 → CO2", "Combination"), ("Cl2 + 2OH- → Cl- + OCl- + H2O", "Disproportionation", ["Disproportionation"]),
], "The redox reaction {} is an example of:", None)


@gen("c11-07", weight=3)
def _eq_wt(rng):
    sp, nf, m = rng.choice([("KMnO4 in acidic medium", 5, 158), ("KMnO4 in neutral medium", 3, 158), ("K2Cr2O7 in acidic medium", 6, 294),
                            ("H2SO4 as an acid", 2, 98), ("Ca(OH)2 as a base", 2, 74), ("FeSO4 (Fe2+ to Fe3+)", 1, 152)])
    return num_q(rng, f"The equivalent weight of {sp} (molar mass {m}) is:", m / nf, "", f"E = M / n-factor = {m}/{nf}.",
                 wrongs=[m, m / (nf + 1), m * nf], form=lambda x: fmt(x, 1))


table("c11-09", [
    ("Ethene with cold dilute alkaline KMnO4", "Ethane-1,2-diol (Baeyer's test)"), ("Ethyne with water, HgSO4 and dilute H2SO4", "Ethanal"),
    ("Ethyne passed through red-hot iron tube", "Benzene"), ("Calcium carbide with water", "Ethyne"),
    ("Sodium acetate with soda lime on heating", "Methane"), ("Benzene with Cl2 and anhydrous AlCl3", "Chlorobenzene"),
], "{} gives:", "Which reaction gives {}?")

table("c12-06", [
    ("Chloroform with air and light", "Phosgene"), ("Chlorobenzene with NaOH at 623 K and 300 atm", "Phenol (Dow process)"),
    ("Ethyl bromide with alcoholic KOH", "Ethene"), ("Ethyl bromide with aqueous KOH", "Ethanol"), ("Ethyl bromide with KCN", "Propanenitrile"),
    ("Ethyl bromide with AgCN", "Ethyl isocyanide"), ("Chloroform with KOH and aniline", "Phenyl isocyanide"),
], "{} gives:", "Which reaction gives {}?")

table("c12-07", [
    ("Primary alcohol with PCC", "Aldehyde"), ("Secondary alcohol with CrO3", "Ketone"), ("Tertiary alcohol with Cu at 573 K", "Alkene"),
    ("Phenol with Zn dust", "Benzene"), ("Phenol with conc. HNO3", "Picric acid (2,4,6-trinitrophenol)"), ("Anisole with HI", "Phenol and methyl iodide"),
    ("Ethanol with conc. H2SO4 at 443 K", "Ethene"), ("Ethanol with conc. H2SO4 at 413 K", "Diethyl ether"),
], "{} gives:", "Which reaction gives {}?", weight=2)

table("c12-09", [
    ("Aniline with bromine water", "2,4,6-Tribromoaniline"), ("Aniline with acetic anhydride", "Acetanilide"),
    ("Benzenediazonium chloride with H3PO2", "Benzene"), ("Benzenediazonium chloride with KI", "Iodobenzene"),
    ("Benzenediazonium chloride with warm water", "Phenol"), ("Benzenediazonium chloride with CuCN", "Benzonitrile"),
    ("Nitrobenzene with Sn/HCl", "Aniline"),
], "{} gives:", "Which reaction gives {}?", weight=2)

table("c12-10", [
    ("Sucrose", "Glucose + fructose"), ("Maltose", "Glucose + glucose (α-1,4)"), ("Lactose", "Galactose + glucose"),
    ("Starch", "Amylose + amylopectin"), ("Cellulose", "Linear chains of β-D-glucose"), ("Glycogen", "Highly branched animal starch"),
], "{} is made of:", "Which carbohydrate is made of {}?")
table("c12-10", [
    ("Primary structure of a protein", "Sequence of amino acids"), ("α-helix", "Secondary structure held by hydrogen bonds"),
    ("Tertiary structure", "Overall folding of the polypeptide chain"), ("Quaternary structure", "Arrangement of two or more polypeptide subunits"),
], "{}:", "Which level of protein structure: {}?")

table("c12-pb", [
    ("H3PO2", "Monobasic"), ("H3PO3", "Dibasic"), ("H3PO4", "Tribasic"), ("H4P2O7", "Tetrabasic"),
], "{} is:", "Which oxoacid of phosphorus is {}?")
table("c12-pb", [
    ("XeF2", "Linear"), ("XeF4", "Square planar"), ("XeF6", "Distorted octahedral"), ("XeO3", "Pyramidal"), ("SF4", "See-saw"),
    ("ClF3", "Bent T-shape"), ("BrF5", "Square pyramidal"),
], "The shape of {} is:", "Which molecule is {}?", weight=2)

tag(None)
