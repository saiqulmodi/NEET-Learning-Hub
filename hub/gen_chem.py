"""NEET Chemistry, Classes 11-12: computed numericals, reaction/reagent tables and checked statements."""
import math

from .core import table, groups, facts, gen, num_q, Q, sig, sci, fmt


def R(rng, *xs):
    return rng.choice(xs)


# ---------------------------------------------------------------- c11-01 Some Basic Concepts
@gen("c11-01", weight=2)
def _limiting(rng):
    h, o = R(rng, 2, 4, 6, 8), R(rng, 1, 2, 3, 4, 5)
    water = min(h, 2 * o)
    lim = "H2" if h < 2 * o else ("O2" if h > 2 * o else "neither (exact ratio)")
    return Q(f"{h} mol H2 reacts with {o} mol O2 (2H2 + O2 → 2H2O). The limiting reagent and moles of water formed are:",
             f"{lim}; {water} mol", [f"{'O2' if lim == 'H2' else 'H2'}; {water} mol", f"{lim}; {2 * water} mol",
                                     f"{'O2' if lim == 'H2' else 'H2'}; {h + o} mol"], "Compare the 2 : 1 mole ratio.")


@gen("c11-01", weight=2)
def _molality(rng):
    g, m, w = R(rng, 18, 36, 90, 180), 180, R(rng, 250, 500, 1000)
    return num_q(rng, f"{g} g glucose (M = 180 g/mol) is dissolved in {w} g water. Molality is:", g / m / (w / 1000), " mol/kg",
                 "m = moles of solute / kg of solvent.", wrongs=[g / m / w, g / m, g / w])


facts("c11-01", [
    "One mole contains 6.022 × 10^23 particles",
    "Molality does not change with temperature",
    "Molarity changes with temperature",
    "The law of definite proportions was given by Proust",
    "Avogadro's law: equal volumes of gases at the same T and P have equal numbers of molecules",
], [
    "Molality changes with temperature",
    "One mole of any gas occupies 22.4 L at any temperature",
    "The law of multiple proportions was given by Lavoisier",
    "Molarity is moles of solute per kg of solvent",
    "Mass is not conserved in chemical reactions",
], "Some Basic Concepts of Chemistry")


# ---------------------------------------------------------------- c11-02 Structure of Atom
@gen("c11-02", weight=2)
def _nodes(rng):
    n, l, name = rng.choice([(2, 0, "2s"), (3, 0, "3s"), (3, 1, "3p"), (4, 1, "4p"), (3, 2, "3d"), (4, 2, "4d"), (4, 3, "4f"), (5, 2, "5d")])
    kind = rng.choice(["radial", "angular", "total"])
    val = {"radial": n - l - 1, "angular": l, "total": n - 1}[kind]
    return Q(f"Number of {kind} nodes in a {name} orbital:", str(val), [str(x) for x in {0, 1, 2, 3, 4} - {val}],
             "Radial = n - l - 1, angular = l, total = n - 1.")


@gen("c11-02", weight=2)
def _shell(rng):
    n = R(rng, 1, 2, 3, 4)
    kind = rng.choice(["electrons", "orbitals"])
    val = 2 * n * n if kind == "electrons" else n * n
    return Q(f"The maximum number of {kind} in the shell n = {n} is:", str(val),
             [str(x) for x in {2 * n * n, n * n, 2 * n, n + 1, 4 * n} - {val}], "Orbitals n², electrons 2n².")


table("c11-02", [
    ("Chromium (Z = 24)", "[Ar] 3d5 4s1"), ("Copper (Z = 29)", "[Ar] 3d10 4s1"), ("Iron (Z = 26)", "[Ar] 3d6 4s2"),
    ("Zinc (Z = 30)", "[Ar] 3d10 4s2"), ("Manganese (Z = 25)", "[Ar] 3d5 4s2"),
], "The ground-state electronic configuration of {} is:", "Which element has the configuration {}?")
table("c11-02", [
    ("Isotopes", "Same atomic number, different mass number"), ("Isobars", "Same mass number, different atomic number"),
    ("Isotones", "Same number of neutrons"), ("Isoelectronic species", "Same number of electrons"),
], "{} have:", "Atoms or ions with {} are called:")
facts("c11-02", [
    "Heisenberg's uncertainty principle applies to microscopic particles such as electrons",
    "Hund's rule: pairing begins only after each orbital of a subshell has one electron",
    "Pauli's principle: no two electrons in an atom have the same four quantum numbers",
    "The Aufbau order fills 4s before 3d",
    "Half-filled and completely filled subshells have extra stability",
], [
    "Two electrons in an atom can have the same four quantum numbers",
    "3d fills before 4s in the Aufbau order",
    "The azimuthal quantum number l can equal n",
    "Electrons pair up before each orbital is singly occupied",
    "Cathode rays are positively charged",
], "Structure of Atom")


# ---------------------------------------------------------------- c11-03 Classification of Elements
_ROOT = {0: "nil", 1: "un", 2: "bi", 3: "tri", 4: "quad", 5: "pent", 6: "hex", 7: "sept", 8: "oct", 9: "enn"}


def _iupac(z):
    s = "".join(_ROOT[int(d)] for d in str(z)) + "ium"
    s = s.replace("nnn", "nn").replace("iium", "ium")
    return s[0].upper() + s[1:]


@gen("c11-03", weight=2)
def _iupac_name(rng):
    z = rng.choice(list(range(101, 121)))
    ans = _iupac(z)
    wr = [_iupac(x) for x in (z + 1, z - 1, int(str(z)[::-1]) if int(str(z)[::-1]) > 100 else z + 10)]
    return Q(f"The IUPAC temporary name of the element with Z = {z} is:", ans, wr + [_iupac(z + 11)],
             "Roots: 0 nil, 1 un, 2 bi, 3 tri, 4 quad, 5 pent, 6 hex, 7 sept, 8 oct, 9 enn, + ium.")


table("c11-03", [
    ("ns1 or ns2 outer configuration", "s-block"), ("ns2 np1-6 outer configuration", "p-block"),
    ("(n-1)d1-10 ns0-2 outer configuration", "d-block"), ("(n-2)f1-14 (n-1)d0-1 ns2 outer configuration", "f-block"),
], "Elements with {} belong to the:", None)
table("c11-03", [
    ("highest electronegativity", "Fluorine"), ("highest first ionisation enthalpy", "Helium"),
    ("most negative electron gain enthalpy", "Chlorine"), ("largest atomic radius in period 3", "Sodium"),
    ("smallest atomic radius in group 1", "Lithium"),
], "The element with the {} is:", None)
facts("c11-03", [
    "Atomic radius decreases across a period",
    "Ionisation enthalpy generally increases across a period",
    "Chlorine has a more negative electron gain enthalpy than fluorine",
    "Isoelectronic ions get smaller as nuclear charge increases",
    "Mendeleev left gaps for undiscovered elements such as gallium (eka-aluminium)",
    "The modern periodic law is based on atomic number",
], [
    "Atomic radius increases across a period",
    "Noble gases have very negative electron gain enthalpies",
    "Fluorine has the most negative electron gain enthalpy",
    "The modern periodic law is based on atomic mass",
    "Cations are larger than their parent atoms",
], "Classification of Elements and Periodicity")


# ---------------------------------------------------------------- c11-04 Chemical Bonding
table("c11-04", [
    ("BeCl2", "Linear"), ("BF3", "Trigonal planar"), ("CH4", "Tetrahedral"), ("NH3", "Trigonal pyramidal"),
    ("H2O", "Bent (V-shaped)"), ("PCl5", "Trigonal bipyramidal"), ("SF6", "Octahedral"), ("ClF3", "T-shaped"),
    ("XeF4", "Square planar"), ("SF4", "See-saw"), ("BrF5", "Square pyramidal"), ("XeF2", "Linear"),
], "The shape of {} is:", "Which molecule is {}?", weight=3)
table("c11-04", [
    ("BeCl2", "sp"), ("BF3", "sp2"), ("CH4", "sp3"), ("PCl5", "sp3d"), ("SF6", "sp3d2"), ("C2H2", "sp"), ("C2H4", "sp2"),
], "The hybridisation of the central atom in {} is:", "Which molecule has {} hybridisation of its central atom?", weight=2)


@gen("c11-04", weight=2)
def _bondorder(rng):
    sp, nb, na = rng.choice([("O2", 10, 6), ("O2+", 10, 5), ("O2-", 10, 7), ("O2 2-", 10, 8), ("N2", 10, 4), ("N2+", 9, 4),
                             ("H2", 2, 0), ("H2+", 1, 0), ("He2", 2, 2), ("C2", 8, 4), ("F2", 10, 8)])
    bo = (nb - na) / 2
    return Q(f"According to molecular orbital theory, the bond order of {sp} is:", fmt(bo),
             [fmt(x) for x in {0, 0.5, 1, 1.5, 2, 2.5, 3} - {bo}][:6], "Bond order = (bonding - antibonding electrons)/2.")


facts("c11-04", [
    "O2 is paramagnetic",
    "CO2, BF3, CH4 and CCl4 have zero dipole moment",
    "NH3 has a larger dipole moment than NF3",
    "Lone pair-lone pair repulsion is greater than bond pair-bond pair repulsion",
    "Bond length decreases as bond order increases",
    "The H-O-H bond angle in water is about 104.5°",
], [
    "N2 is paramagnetic",
    "H2O has zero dipole moment",
    "Bond length increases with bond order",
    "Sigma bonds are weaker than pi bonds between the same atoms",
    "BF3 is pyramidal",
], "Chemical Bonding and Molecular Structure", weight=2)


# ---------------------------------------------------------------- c11-05 Thermodynamics
@gen("c11-05", weight=2)
def _gibbs(rng):
    dh, ds, t = R(rng, -100, -50, 40, 80), R(rng, -0.2, -0.1, 0.1, 0.2), R(rng, 298, 400, 500, 1000)
    dg = dh - t * ds
    return num_q(rng, f"For a reaction, ΔH = {dh} kJ/mol and ΔS = {ds} kJ/(mol K). ΔG at {t} K is:", dg, " kJ/mol",
                 "ΔG = ΔH - TΔS.", wrongs=[dh + t * ds, dh - ds, t * ds - dh])


@gen("c11-05", weight=2)
def _dh_du(rng):
    du, dn, t = R(rng, -100, -200, 50), R(rng, -2, -1, 1, 2), 298
    dh = du + dn * 8.314e-3 * t
    return num_q(rng, f"For a gas reaction at 298 K, ΔU = {du} kJ and Δng = {dn}. ΔH is (R = 8.314 J/mol K):", dh, " kJ",
                 "ΔH = ΔU + Δng RT.", form=lambda x: f"{x:.2f}", wrongs=[du - dn * 8.314e-3 * t, du + dn * 8.314 * t / 100, du])


table("c11-05", [
    ("ΔH negative, ΔS positive", "Spontaneous at all temperatures"),
    ("ΔH positive, ΔS negative", "Non-spontaneous at all temperatures"),
    ("ΔH negative, ΔS negative", "Spontaneous at low temperatures"),
    ("ΔH positive, ΔS positive", "Spontaneous at high temperatures"),
], "When {}, the reaction is:", None)
facts("c11-05", [
    "Enthalpy and entropy are state functions",
    "Work and heat are path functions",
    "ΔG is negative for a spontaneous process at constant T and P",
    "Entropy of a perfect crystal at 0 K is zero",
    "Hess's law follows from enthalpy being a state function",
], [
    "Work is a state function",
    "A spontaneous process always has negative ΔH",
    "Entropy decreases when a solid melts",
    "ΔG is positive for a spontaneous process",
    "Isolated systems exchange energy with the surroundings",
], "Thermodynamics")


# ---------------------------------------------------------------- c11-06 Equilibrium
@gen("c11-06", weight=2)
def _ksp(rng):
    s = R(rng, 1e-3, 2e-4, 1e-5, 3e-4)
    kind = rng.choice([("AgCl (AB)", 1), ("CaF2 (AB2)", 4), ("Ag2CrO4 (A2B)", 4)])
    val = s * s if kind[1] == 1 else 4 * s ** 3
    return num_q(rng, f"The molar solubility of {kind[0]} is {sci(s)} mol/L. Its Ksp is:", val, "", "AB: s²; AB2 or A2B: 4s³.",
                 form=sci, wrongs=[s * s if kind[1] == 4 else 4 * s ** 3, 2 * s * s, s ** 3])


@gen("c11-06", weight=2)
def _buffer(rng):
    pka, ratio = R(rng, 4.74, 4.76, 9.25), R(rng, 1, 10, 0.1)
    return num_q(rng, f"A buffer has pKa = {pka} and [salt]/[acid] = {ratio}. Its pH is:", pka + math.log10(ratio), "",
                 "pH = pKa + log([salt]/[acid]).", form=lambda x: f"{x:.2f}",
                 wrongs=[pka - math.log10(ratio) if ratio != 1 else pka + 1, pka + 2 * math.log10(ratio) + 0.5, 14 - pka])


@gen("c11-06", weight=2)
def _kpkc(rng):
    kc, dn, t = R(rng, 1, 2, 4), R(rng, 1, -1, 2), R(rng, 300, 500)
    kp = kc * (0.0821 * t) ** dn
    return num_q(rng, f"For a gas equilibrium with Kc = {kc} and Δn = {dn} at {t} K, Kp is (R = 0.0821 L atm/mol K):", kp, "",
                 "Kp = Kc(RT)^Δn.", form=sci, wrongs=[kc * (0.0821 * t) ** (-dn), kc * 0.0821 * t * 2, kc])


@gen("c11-06")
def _poh(rng):
    e = R(rng, 2, 3, 4, 5)
    return Q(f"A solution has [OH⁻] = 10^-{e} M at 25 °C. Its pH is:", str(14 - e), [str(e), str(14 + e), str(7 + e)],
             "pOH = -log[OH⁻]; pH = 14 - pOH.")


facts("c11-06", [
    "A catalyst does not change the equilibrium constant",
    "The equilibrium constant changes with temperature",
    "Adding an inert gas at constant volume does not shift equilibrium",
    "The conjugate base of a strong acid is weak",
    "The ionic product of water at 25 °C is 1 × 10^-14",
], [
    "A catalyst shifts equilibrium towards products",
    "Increasing pressure shifts equilibrium towards more moles of gas",
    "Kc depends on initial concentrations",
    "pH of a neutral solution is 7 at all temperatures",
    "Strong acids have strong conjugate bases",
], "Equilibrium")


# ---------------------------------------------------------------- c11-07 Redox Reactions
table("c11-07", [
    ("KMnO4 in acidic medium", "5"), ("KMnO4 in neutral medium", "3"), ("KMnO4 in strongly basic medium", "1"),
    ("K2Cr2O7 in acidic medium", "6"),
], "The number of electrons gained per formula unit (n-factor) by {} is:", None)
table("c11-07", [
    ("2H2O2 → 2H2O + O2", "Disproportionation"), ("Zn + CuSO4 → ZnSO4 + Cu", "Displacement"),
    ("2KClO3 → 2KCl + 3O2", "Decomposition"), ("C + O2 → CO2", "Combination"),
], "The redox reaction {} is an example of:", None)
facts("c11-07", [
    "Oxidation is the loss of electrons",
    "The oxidation number of oxygen in H2O2 is -1",
    "The oxidation number of oxygen in OF2 is +2",
    "In a disproportionation reaction the same element is both oxidised and reduced",
    "A reducing agent gets oxidised",
], [
    "Oxidation is the gain of electrons",
    "An oxidising agent gets oxidised",
    "The oxidation number of hydrogen in metal hydrides is +1",
    "Oxidation number of oxygen is always -2",
    "Reduction involves an increase in oxidation number",
], "Redox Reactions")


@gen("c11-07", weight=2)
def _ox(rng):
    sp, el, val = rng.choice([("K2Cr2O7", "Cr", 6), ("KMnO4", "Mn", 7), ("H2SO4", "S", 6), ("HNO3", "N", 5), ("NH3", "N", -3),
                              ("Na2S2O3", "S", 2), ("CrO5", "Cr", 6), ("Fe3O4", "Fe", "8/3"), ("H2O2", "O", -1), ("NaH", "H", -1)])
    pool = ["+7", "+6", "+5", "+4", "+3", "+2", "-1", "-3", "8/3", "+1"]
    ans = f"+{val}" if isinstance(val, int) and val > 0 else str(val)
    return Q(f"The oxidation number of {el} in {sp} is:", ans, [p for p in pool if p != ans], f"{el} in {sp}: {ans}.")


# ---------------------------------------------------------------- c11-08 Organic Chemistry: Basic Principles
table("c11-08", [
    ("Sublimation", "Camphor, naphthalene and anthracene"), ("Steam distillation", "Aniline from aniline-water mixture"),
    ("Fractional distillation", "Crude oil fractions"), ("Distillation under reduced pressure", "Glycerol from spent lye"),
    ("Chromatography", "Separating plant pigments"), ("Differential extraction", "Organic compound from water using ether"),
], "Which mixture or substance is purified by {}?", "{} is purified or separated by:")
table("c11-08", [
    ("Nitrogen (with FeSO4 and acid)", "Prussian blue colour"),
    ("Sulphur (with sodium nitroprusside)", "Violet colour"),
    ("Nitrogen and sulphur together", "Blood-red colour (thiocyanate)"),
    ("Halogens (with silver nitrate)", "White, pale yellow or yellow precipitate"),
], "In detection of {}, the result is:", "Which element gives {} in Lassaigne's test?")
table("c11-08", [
    ("Tertiary carbocation", "Most stable of the alkyl carbocations"), ("Methyl carbocation", "Least stable alkyl carbocation"),
    ("Electrophile", "Electron-seeking species such as NO2+"), ("Nucleophile", "Electron-rich species such as OH-"),
    ("Inductive effect", "Permanent polarisation through sigma bonds"),
    ("Resonance effect", "Delocalisation of pi electrons in a conjugated system"),
    ("Hyperconjugation", "Delocalisation of sigma electrons of C-H bonds next to an unsaturated system"),
], "{}:", "Which term describes: {}?")


@gen("c11-08", weight=2)
def _kjeldahl(rng):
    m, v = R(rng, 0.5, 0.25, 1), R(rng, 10, 20, 25)
    pct = 1.4 * 1 * v / m
    return num_q(rng, f"In Kjeldahl's method, ammonia from {m} g of a compound neutralised {v} mL of 1 M H2SO4. Percentage of nitrogen:",
                 1.4 * 2 * v / m, "%", "% N = 1.4 × M × 2 × V(H2SO4)/m for H2SO4.", wrongs=[pct, 1.4 * v * m, 14 * v / m])


facts("c11-08", [
    "Kjeldahl's method cannot be used for nitro and azo compounds",
    "Carbon in organic compounds is tetravalent",
    "Homolytic cleavage forms free radicals",
    "Heterolytic cleavage forms ions",
    "Tertiary carbocations are stabilised by hyperconjugation and +I effect",
], [
    "Kjeldahl's method works for pyridine",
    "Homolytic cleavage forms carbocations and carbanions",
    "Methyl carbocation is the most stable carbocation",
    "Nucleophiles are electron-deficient",
    "Steam distillation is used for substances miscible with water",
], "Organic Chemistry: Basic Principles")


# ---------------------------------------------------------------- c11-09 Hydrocarbons
table("c11-09", [
    ("Wurtz reaction", "Alkyl halide + sodium in dry ether gives a higher alkane"),
    ("Kolbe's electrolysis", "Electrolysis of sodium carboxylate gives an alkane"),
    ("Markovnikov's rule", "H adds to the carbon of the double bond that already has more hydrogens"),
    ("Peroxide (Kharasch) effect", "Anti-Markovnikov addition of HBr in the presence of peroxide"),
    ("Ozonolysis", "Cleavage of a C=C bond to give aldehydes or ketones"),
    ("Baeyer's reagent", "Cold dilute alkaline KMnO4; decolourised by unsaturation"),
    ("Lindlar's catalyst", "Partial hydrogenation of alkynes to cis-alkenes"),
    ("Friedel-Crafts alkylation", "Benzene + alkyl halide with anhydrous AlCl3"),
    ("Nitration of benzene", "Concentrated HNO3 and H2SO4 generate the nitronium ion"),
], "{}:", "Which named rule or reaction: {}?", weight=2)
table("c11-09", [
    ("C4H10 (butane)", "2"), ("C5H12 (pentane)", "3"), ("C6H14 (hexane)", "5"), ("C7H16 (heptane)", "9"),
], "Number of structural isomers of {}:", None)
groups("c11-09", {
    "ortho/para directing groups": ["-OH", "-NH2", "-CH3", "-OCH3"],
    "meta directing groups": ["-NO2", "-CHO", "-COOH", "-CN"],
}, "Which of these is NOT one of the {}?", "Which of these is one of the {}?")
facts("c11-09", [
    "Staggered ethane is more stable than eclipsed ethane",
    "Aromatic compounds follow Huckel's (4n + 2) pi electron rule",
    "Halogens are deactivating but ortho/para directing",
    "Alkanes undergo free-radical substitution with halogens in light",
    "Acetylene is more acidic than ethylene",
], [
    "Eclipsed ethane is more stable than staggered ethane",
    "Benzene readily undergoes addition reactions",
    "The -NO2 group is ortho/para directing",
    "Ethane is more acidic than acetylene",
    "Cyclooctatetraene is aromatic",
], "Hydrocarbons", weight=2)


# ---------------------------------------------------------------- c12-01 Solutions
table("c12-01", [
    ("NaCl (complete dissociation)", "2"), ("CaCl2 (complete dissociation)", "3"), ("K4[Fe(CN)6] (complete dissociation)", "5"),
    ("Glucose", "1"), ("Acetic acid dimerising fully in benzene", "0.5"), ("Al2(SO4)3 (complete dissociation)", "5"),
], "The van't Hoff factor (i) of {} is:", None)
table("c12-01", [
    ("Ethanol + acetone", "Positive deviation from Raoult's law"), ("Carbon disulphide + acetone", "Positive deviation from Raoult's law"),
    ("Chloroform + acetone", "Negative deviation from Raoult's law"), ("Nitric acid + water", "Negative deviation from Raoult's law"),
    ("n-hexane + n-heptane", "Nearly ideal solution"), ("Benzene + toluene", "Nearly ideal solution"),
], "The mixture {} shows:", "Which mixture shows {}?")


@gen("c12-01", weight=2)
def _henry(rng):
    kh, p = R(rng, 1.67e8, 76.48e3), R(rng, 1, 2, 5)
    return num_q(rng, f"A gas has Henry's constant KH = {sci(kh)} (pressure units) and partial pressure {p} in the same units. Its mole fraction in solution:",
                 p / kh, "", "p = KH x.", form=sci, wrongs=[kh / p, p * kh, p / kh * 10])


@gen("c12-01", weight=2)
def _osmotic(rng):
    c, t = R(rng, 0.1, 0.2, 0.05), R(rng, 300, 310)
    return num_q(rng, f"Osmotic pressure of a {c} M non-electrolyte solution at {t} K (R = 0.0821 L atm/mol K) is:", c * 0.0821 * t,
                 " atm", "π = CRT.", wrongs=[c * 8.314 * t / 100, c * 0.0821, 0.0821 * t / c])


facts("c12-01", [
    "Colligative properties depend on the number of solute particles",
    "Azeotropes boil at a constant temperature with unchanged composition",
    "Reverse osmosis is used for desalination",
    "Solubility of gases decreases with rising temperature",
    "Relative lowering of vapour pressure equals the mole fraction of the solute",
], [
    "Colligative properties depend on the chemical nature of the solute",
    "Solubility of gases increases with temperature",
    "Osmosis is the flow of solute through a semipermeable membrane",
    "Molality depends on temperature",
    "Freezing point rises when a non-volatile solute is added",
], "Solutions")


# ---------------------------------------------------------------- c12-02 Electrochemistry
@gen("c12-02", weight=2)
def _deposit(rng):
    i, t, metal = R(rng, 1, 2, 5), R(rng, 965, 1930, 9650), rng.choice([("Ag", 108, 1), ("Cu", 63.5, 2), ("Al", 27, 3)])
    mass = i * t / 96500 * metal[1] / metal[2]
    return num_q(rng, f"A current of {i} A passes for {t} s through a solution of {metal[0]}^{metal[2]}+ ions. Mass of {metal[0]} deposited:",
                 mass, " g", "m = (I t / F) × (M / n).", wrongs=[i * t / 96500 * metal[1], mass * 2, i * t * metal[1] / 96500 / 10])


@gen("c12-02", weight=2)
def _dg_cell(rng):
    n, e = R(rng, 1, 2, 3), R(rng, 0.34, 0.76, 1.1, 0.46)
    return num_q(rng, f"A cell with E° = {e} V transfers {n} electron(s). ΔG° is (F = 96500 C/mol):", -n * 96500 * e / 1000, " kJ/mol",
                 "ΔG° = -nFE°.", wrongs=[n * 96500 * e / 1000, -96500 * e / 1000, -n * 96500 * e])


@gen("c12-02")
def _kohl(rng):
    a, b = R(rng, 349.6, 50.1, 73.5), R(rng, 76.3, 199.1, 40.9)
    return num_q(rng, f"Limiting molar conductivities of the cation and anion are {a} and {b} S cm² mol⁻¹. Λ°m of the salt (1:1) is:",
                 a + b, " S cm² mol⁻¹", "Kohlrausch's law: Λ°m = λ°+ + λ°-.", wrongs=[a - b, a * b / 100, (a + b) / 2])


table("c12-02", [
    ("Dry (Leclanché) cell", "Zinc container anode and carbon rod cathode"),
    ("Mercury cell", "Gives a constant 1.35 V; used in hearing aids and watches"),
    ("Lead storage battery", "Lead anode, PbO2 cathode, 38% sulphuric acid"),
    ("H2-O2 fuel cell", "Used in the Apollo space programme"),
], "{}:", "Which cell: {}?")
facts("c12-02", [
    "Conductivity of an electrolyte decreases on dilution",
    "Molar conductivity increases on dilution",
    "Rusting of iron is an electrochemical process",
    "In a galvanic cell, oxidation occurs at the anode",
    "A cell reaction is spontaneous when E°cell is positive",
], [
    "Molar conductivity decreases on dilution",
    "In a galvanic cell the anode is positive",
    "Reduction occurs at the anode",
    "Galvanising means coating iron with tin",
    "A negative E°cell means a spontaneous reaction",
], "Electrochemistry")


# ---------------------------------------------------------------- c12-03 Chemical Kinetics
@gen("c12-03", weight=2)
def _t_half(rng):
    k = R(rng, 0.01, 0.0693, 0.231, 0.693, 0.1)
    return num_q(rng, f"A first-order reaction has k = {k} per minute. Its half-life is:", 0.693 / k, " min", "t½ = 0.693/k.",
                 wrongs=[k / 0.693, 0.693 * k, 1 / k])


@gen("c12-03", weight=2)
def _completion(rng):
    th = R(rng, 10, 20, 30, 69.3)
    pct, factor = rng.choice([(99, 2 * 3.32), (99.9, 3 * 3.32), (75, 2), (87.5, 3), (90, 3.32)])
    return num_q(rng, f"A first-order reaction has a half-life of {th} min. Time for {pct}% completion is about:", th * factor, " min",
                 "For first order, t = (2.303/k) log(a/(a - x)); 75% = 2 t½, 87.5% = 3 t½, 99% ≈ 6.64 t½.",
                 wrongs=[th * pct / 50, th * factor / 2, th * 2])


@gen("c12-03", weight=2)
def _temp10(rng):
    dt = R(rng, 10, 20, 30, 40)
    return num_q(rng, f"If the rate doubles for every 10 °C rise, by what factor does it increase for a {dt} °C rise?", 2 ** (dt / 10),
                 " times", "Factor = 2^(ΔT/10).", form=lambda x: fmt(x), wrongs=[2 * dt / 10, dt / 10, 2 ** (dt / 10) / 2])


table("c12-03", [
    ("Zero-order reaction", "mol L⁻¹ s⁻¹"), ("First-order reaction", "s⁻¹"), ("Second-order reaction", "L mol⁻¹ s⁻¹"),
], "Unit of the rate constant of a {}:", "A rate constant in {} indicates a:")
facts("c12-03", [
    "Half-life of a first-order reaction does not depend on initial concentration",
    "Half-life of a zero-order reaction is proportional to initial concentration",
    "A catalyst lowers the activation energy",
    "Order of a reaction can be fractional",
    "Molecularity cannot be zero or fractional",
    "Radioactive decay follows first-order kinetics",
], [
    "Molecularity can be fractional",
    "A catalyst changes the enthalpy of a reaction",
    "Half-life of a first-order reaction depends on initial concentration",
    "Rate constant does not depend on temperature",
    "Order is always equal to the stoichiometric coefficients",
], "Chemical Kinetics", weight=2)


# ---------------------------------------------------------------- c12-pb p-Block Elements
table("c12-pb", [
    ("H3PO4", "Tribasic"), ("H3PO3", "Dibasic"), ("H3PO2", "Monobasic"),
], "Basicity of {}:", "Which oxoacid of phosphorus is {}?")
table("c12-pb", [
    ("Inert pair effect", "Tl+ is more stable than Tl3+"), ("Catenation is strongest in", "Carbon"),
    ("Nitrogen cannot form NCl5 because", "It has no d orbitals"), ("Most reactive halogen", "Fluorine"),
    ("Noble gas compound first prepared", "Xe+PtF6- (by Neil Bartlett)"), ("Bleaching action of chlorine is due to", "Oxidation by nascent oxygen"),
    ("Structure of PCl5 in the solid state", "[PCl4]+[PCl6]-"), ("Contact process catalyst", "V2O5"),
    ("Ozone layer absorbs", "Ultraviolet radiation"), ("Shape of XeO3", "Pyramidal"),
], "{}:", None, weight=2)
groups("c12-pb", {
    "group 13 elements": ["Boron", "Aluminium", "Gallium", "Indium", "Thallium"],
    "group 15 elements": ["Nitrogen", "Phosphorus", "Arsenic", "Antimony", "Bismuth"],
    "group 16 elements": ["Oxygen", "Sulphur", "Selenium", "Tellurium"],
    "group 17 elements": ["Fluorine", "Chlorine", "Bromine", "Iodine"],
    "group 18 elements": ["Helium", "Neon", "Argon", "Krypton", "Xenon"],
}, "Which of these is NOT one of the {}?", "Which of these is one of the {}?")
facts("c12-pb", [
    "Fluorine shows only the -1 oxidation state",
    "Ammonia is more basic than phosphine",
    "Bond dissociation enthalpy of F2 is less than that of Cl2",
    "White phosphorus is more reactive than red phosphorus",
    "H2O is a liquid while H2S is a gas due to hydrogen bonding",
    "Thermal stability of hydrides decreases down group 15",
], [
    "Red phosphorus is more reactive than white phosphorus",
    "Fluorine shows +7 oxidation state",
    "Phosphine is more basic than ammonia",
    "H3PO3 is tribasic",
    "Noble gases form no compounds at all",
], "p-Block Elements", weight=2)


# ---------------------------------------------------------------- c12-04 d- and f-Block Elements
@gen("c12-04", weight=3)
def _moment(rng):
    ion, n = rng.choice([("Ti3+", 1), ("V3+", 2), ("Cr3+", 3), ("Mn2+", 5), ("Fe2+", 4), ("Fe3+", 5), ("Co2+", 3), ("Ni2+", 2),
                         ("Cu2+", 1), ("Zn2+", 0), ("Sc3+", 0), ("Mn3+", 4)])
    mu = math.sqrt(n * (n + 2))
    pool = {math.sqrt(k * (k + 2)) for k in range(0, 6)} - {mu}
    return Q(f"The spin-only magnetic moment of {ion} (in BM) is about:", f"{mu:.2f}", [f"{x:.2f}" for x in sorted(pool)],
             f"{ion} has {n} unpaired electrons; μ = √(n(n + 2)).")


table("c12-04", [
    ("Lanthanoid contraction", "Steady decrease in size of lanthanoid atoms/ions with atomic number"),
    ("Zn, Cd and Hg", "Not regarded as typical transition elements (full d10 in all states)"),
    ("Most common oxidation state of lanthanoids", "+3"), ("Highest oxidation state of manganese", "+7"),
    ("Colour of KMnO4", "Deep purple"), ("Colour of K2Cr2O7", "Orange"),
    ("Interstitial compounds", "Small atoms like H, C or N trapped in metal lattices"),
], "{}:", None)
facts("c12-04", [
    "Most transition metal ions are coloured due to d-d transitions",
    "Transition metals and their compounds are good catalysts",
    "Zr and Hf have almost identical radii due to lanthanoid contraction",
    "Actinoids show a wider range of oxidation states than lanthanoids",
    "Chromate turns to dichromate when acidified",
], [
    "Zn2+ salts are deeply coloured",
    "Lanthanoids commonly show +7 oxidation state",
    "Sc3+ is paramagnetic",
    "Lanthanoid contraction increases atomic size",
    "Dichromate turns to chromate in acid",
], "d- and f-Block Elements")


# ---------------------------------------------------------------- c12-05 Coordination Compounds
table("c12-05", [
    ("EDTA⁴⁻", "Hexadentate"), ("Ethylenediamine (en)", "Bidentate"), ("Oxalate", "Bidentate"), ("NH3", "Monodentate"),
    ("NO2⁻", "Ambidentate (binds through N or O)"), ("SCN⁻", "Ambidentate (binds through S or N)"),
], "The ligand {} is:", None)
table("c12-05", [
    ("[Ni(CO)4]", "sp3, tetrahedral, diamagnetic"), ("[Ni(CN)4]2-", "dsp2, square planar, diamagnetic"),
    ("[Co(NH3)6]3+", "d2sp3, inner-orbital octahedral, diamagnetic"), ("[CoF6]3-", "sp3d2, outer-orbital octahedral, paramagnetic"),
    ("[NiCl4]2-", "sp3, tetrahedral, paramagnetic"),
], "{} is:", "Which complex is {}?")


@gen("c12-05", weight=3)
def _ox_state(rng):
    cx, ox = rng.choice([("[Co(NH3)6]Cl3", 3), ("K4[Fe(CN)6]", 2), ("K3[Fe(CN)6]", 3), ("[Ni(CO)4]", 0), ("[Cu(NH3)4]SO4", 2),
                         ("K2[PtCl6]", 4), ("[Cr(H2O)6]Cl3", 3), ("[Co(NH3)5Cl]Cl2", 3), ("K3[Al(C2O4)3]", 3)])
    return Q(f"The oxidation state of the central metal in {cx} is:", f"{ox:+d}" if ox else "0",
             [f"{x:+d}" if x else "0" for x in {0, 1, 2, 3, 4, 6} - {ox}], "Sum of charges of ligands and counter ions balances.")


@gen("c12-05", weight=2)
def _cn(rng):
    cx, cn = rng.choice([("[Co(NH3)6]3+", 6), ("[Ni(CO)4]", 4), ("[Fe(C2O4)3]3-", 6), ("[Co(en)3]3+", 6), ("[Pt(NH3)2Cl2]", 4),
                         ("[Cu(NH3)4]2+", 4), ("[Co(EDTA)]-", 6), ("[Ag(NH3)2]+", 2)])
    return Q(f"The coordination number of the metal in {cx} is:", str(cn), [str(x) for x in {2, 3, 4, 6, 8} - {cn}],
             "Count donor atoms: bidentate ligands count twice; EDTA counts six.")


facts("c12-05", [
    "Werner proposed primary (ionisable) and secondary (non-ionisable) valencies",
    "Strong field ligands such as CN⁻ and CO cause pairing of electrons",
    "Square planar [Pt(NH3)2Cl2] shows cis-trans isomerism",
    "Chlorophyll contains magnesium and haemoglobin contains iron",
    "In the spectrochemical series, CO is a stronger field ligand than F⁻",
], [
    "Tetrahedral complexes show geometrical isomerism",
    "F⁻ is a strong field ligand",
    "Vitamin B12 contains iron",
    "Secondary valency of a metal is ionisable",
    "Chlorophyll contains iron",
], "Coordination Compounds")


# ---------------------------------------------------------------- c12-06 Haloalkanes and Haloarenes
table("c12-06", [
    ("Finkelstein reaction", "Alkyl chloride/bromide + NaI in dry acetone gives alkyl iodide"),
    ("Swarts reaction", "Alkyl chloride/bromide + metallic fluoride (AgF, Hg2F2) gives alkyl fluoride"),
    ("Sandmeyer reaction", "Benzene diazonium salt + CuCl or CuBr gives aryl halide"),
    ("Wurtz-Fittig reaction", "Alkyl halide + aryl halide + sodium gives alkylarene"),
    ("Fittig reaction", "Two aryl halides + sodium give a diphenyl"),
], "{}:", "Which named reaction: {}?", weight=2)
table("c12-06", [
    ("Chloroform", "Stored in dark coloured bottles as it forms poisonous phosgene in air and light"),
    ("Iodoform", "Used earlier as an antiseptic"), ("Freons", "Deplete the ozone layer"),
    ("DDT", "First chlorinated organic insecticide; not biodegradable"),
    ("Carbon tetrachloride", "Used earlier in fire extinguishers"),
], "{}:", "Which compound: {}?")
facts("c12-06", [
    "SN2 reactions proceed with inversion of configuration",
    "SN1 reactions go through a carbocation intermediate",
    "Tertiary halides react fastest by SN1",
    "Primary halides react fastest by SN2",
    "Haloarenes are less reactive towards nucleophilic substitution than haloalkanes",
    "Alcoholic KOH favours elimination; aqueous KOH favours substitution",
], [
    "SN2 reactions give racemisation",
    "Tertiary halides react fastest by SN2",
    "Haloarenes undergo nucleophilic substitution more easily than haloalkanes",
    "Aqueous KOH favours elimination",
    "SN1 reactions are one-step reactions",
], "Haloalkanes and Haloarenes")


# ---------------------------------------------------------------- c12-07 Alcohols, Phenols and Ethers
table("c12-07", [
    ("Reimer-Tiemann reaction", "Phenol + CHCl3 + NaOH gives salicylaldehyde"),
    ("Kolbe's reaction", "Sodium phenoxide + CO2 gives salicylic acid"),
    ("Williamson synthesis", "Alkyl halide + sodium alkoxide gives an ether"),
    ("Lucas test", "Tertiary alcohols give turbidity immediately with ZnCl2/HCl"),
    ("Hydroboration-oxidation", "Alkene gives anti-Markovnikov alcohol"),
], "{}:", "Which reaction or test: {}?")
facts("c12-07", [
    "Phenol is more acidic than ethanol",
    "o-nitrophenol is more volatile than p-nitrophenol due to intramolecular hydrogen bonding",
    "Phenol gives a violet colour with neutral FeCl3",
    "Primary alcohols are oxidised to aldehydes by PCC",
    "Methanol is poisonous and can cause blindness",
    "Electron-withdrawing groups increase the acidity of phenol",
], [
    "Ethanol is more acidic than phenol",
    "Tertiary alcohols react slowest in the Lucas test",
    "Electron-donating groups increase the acidity of phenol",
    "Ethers are highly reactive towards bases",
    "p-nitrophenol is more volatile than o-nitrophenol",
], "Alcohols, Phenols and Ethers")


# ---------------------------------------------------------------- c12-08 Aldehydes, Ketones and Carboxylic Acids
table("c12-08", [
    ("Clemmensen reduction", "Zn-Hg and HCl reduce C=O to CH2"),
    ("Wolff-Kishner reduction", "Hydrazine and KOH in ethylene glycol reduce C=O to CH2"),
    ("Rosenmund reduction", "Acyl chloride + H2 over Pd-BaSO4 gives an aldehyde"),
    ("Stephen reaction", "Nitrile + SnCl2/HCl, then hydrolysis, gives an aldehyde"),
    ("Etard reaction", "Chromyl chloride oxidises toluene to benzaldehyde"),
    ("Aldol condensation", "Aldehydes or ketones with an alpha-hydrogen in dilute alkali"),
    ("Cannizzaro reaction", "Aldehydes without an alpha-hydrogen in concentrated alkali disproportionate"),
    ("Hell-Volhard-Zelinsky reaction", "Alpha-halogenation of carboxylic acids with Cl2/Br2 and red phosphorus"),
], "{}:", "Which named reaction: {}?", weight=2)
table("c12-08", [
    ("Tollens' test", "Silver mirror with aldehydes"), ("Fehling's test", "Red-brown precipitate with aliphatic aldehydes"),
    ("Iodoform test", "Yellow precipitate with methyl ketones and ethanol"),
    ("Sodium bicarbonate test", "Brisk effervescence with carboxylic acids"),
], "{} gives:", "Which test gives {}?")
facts("c12-08", [
    "Aldehydes are generally more reactive than ketones in nucleophilic addition",
    "Formic acid gives a positive Tollens' test",
    "Electron-withdrawing groups increase the acidity of carboxylic acids",
    "Benzaldehyde undergoes the Cannizzaro reaction",
    "Carboxylic acids have higher boiling points than alcohols of similar mass",
], [
    "Ketones give a positive Tollens' test",
    "Electron-donating groups increase acidity of carboxylic acids",
    "Benzaldehyde undergoes aldol condensation by itself",
    "Acetone gives a red precipitate with Fehling's solution",
    "Formaldehyde has an alpha-hydrogen",
], "Aldehydes, Ketones and Carboxylic Acids")


# ---------------------------------------------------------------- c12-09 Amines
table("c12-09", [
    ("Gabriel phthalimide synthesis", "Makes only primary aliphatic amines"),
    ("Hofmann bromamide degradation", "Amide gives a primary amine with one carbon less"),
    ("Carbylamine test", "Primary amines give foul-smelling isocyanides with CHCl3 and KOH"),
    ("Hinsberg's reagent", "Benzenesulphonyl chloride used to distinguish 1°, 2° and 3° amines"),
    ("Diazotisation", "Aniline + NaNO2/HCl at 273-278 K gives benzene diazonium chloride"),
    ("Coupling reaction", "Diazonium salt + phenol gives an orange azo dye"),
], "{}:", "Which reaction or test: {}?", weight=2)
facts("c12-09", [
    "Aniline is a weaker base than methylamine",
    "In water, dimethylamine is more basic than methylamine",
    "Primary amine sulphonamides dissolve in alkali in the Hinsberg test",
    "Tertiary amines do not react with Hinsberg's reagent",
    "Aniline cannot be made by Gabriel synthesis",
], [
    "Aniline is a stronger base than ammonia",
    "Tertiary amines give the carbylamine test",
    "Gabriel synthesis gives aromatic primary amines",
    "Secondary amine sulphonamides dissolve in alkali",
    "Hofmann bromamide reaction gives an amine with one carbon more",
], "Amines")


# ---------------------------------------------------------------- c12-10 Biomolecules
table("c12-10", [
    ("Vitamin A", "Night blindness and xerophthalmia"), ("Vitamin B1 (thiamine)", "Beriberi"),
    ("Vitamin B2 (riboflavin)", "Cheilosis"), ("Vitamin B6 (pyridoxine)", "Convulsions"),
    ("Vitamin B12", "Pernicious anaemia"), ("Vitamin C", "Scurvy"), ("Vitamin D", "Rickets and osteomalacia"),
    ("Vitamin E", "Increased fragility of RBCs and muscular weakness"), ("Vitamin K", "Increased blood clotting time"),
], "Deficiency of {} causes:", "Deficiency of which vitamin causes {}?", weight=2)
table("c12-10", [
    ("Sucrose", "Glucose + fructose; non-reducing sugar"), ("Maltose", "Two glucose units joined by an α-1,4 link; reducing"),
    ("Lactose", "Galactose + glucose joined by a β-1,4 link; reducing"), ("Starch", "Amylose and amylopectin"),
    ("Cellulose", "β-D-glucose units; main component of plant cell walls"),
], "{}:", "Which carbohydrate: {}?")
groups("c12-10", {
    "essential amino acids": ["Valine", "Leucine", "Lysine", "Threonine", "Tryptophan", "Phenylalanine"],
    "non-essential amino acids": ["Glycine", "Alanine", "Serine", "Glutamic acid", "Aspartic acid"],
}, "Which of these is NOT one of the {}?", "Which of these is one of the {}?")
facts("c12-10", [
    "Vitamins B and C are water-soluble",
    "Vitamins A, D, E and K are fat-soluble",
    "DNA contains deoxyribose and thymine; RNA contains ribose and uracil",
    "Denaturation destroys secondary and tertiary structure but not primary structure",
    "The alpha-helix is a secondary structure of proteins",
    "Sucrose is called invert sugar after hydrolysis because the sign of rotation changes",
], [
    "Vitamin C is fat-soluble",
    "Sucrose is a reducing sugar",
    "Denaturation breaks peptide bonds",
    "RNA contains thymine",
    "Cellulose is made of alpha-D-glucose",
], "Biomolecules", weight=2)


# ---------------------------------------------------------------- c12-pr Principles Related to Practical Chemistry
table("c12-pr", [
    ("Fe3+", "Blood-red colour with potassium thiocyanate"), ("Cu2+", "Deep blue solution with excess ammonia"),
    ("NH4+", "Brown precipitate with Nessler's reagent"), ("Cl⁻", "White precipitate with AgNO3, soluble in ammonia"),
    ("Br⁻", "Pale yellow precipitate with AgNO3, partly soluble in ammonia"),
    ("I⁻", "Yellow precipitate with AgNO3, insoluble in ammonia"), ("SO4 2-", "White precipitate with BaCl2, insoluble in HCl"),
    ("NO3⁻", "Brown ring test"), ("CO3 2-", "Effervescence of CO2 that turns lime water milky with dilute acid"),
    ("Pb2+", "Yellow precipitate with potassium iodide"),
], "The confirmatory test for {} is:", "Which ion gives: {}?", weight=3)
table("c12-pr", [
    ("Unsaturation", "Decolourises bromine water"), ("Phenolic -OH", "Violet colour with neutral FeCl3"),
    ("Aldehyde group", "Silver mirror with Tollens' reagent"), ("Carboxylic acid group", "Effervescence with NaHCO3"),
    ("Primary amino group", "Foul smell in the carbylamine test"),
], "Test for {}:", "Which functional group shows: {}?")
table("c12-pr", [
    ("Strong acid vs strong base", "Phenolphthalein or methyl orange"), ("Weak acid vs strong base", "Phenolphthalein"),
    ("Strong acid vs weak base", "Methyl orange"), ("KMnO4 titrations", "KMnO4 itself (self-indicator)"),
], "Indicator for {} titration:", None)
facts("c12-pr", [
    "Oxalic acid and Mohr's salt are titrated against KMnO4 in acidic medium",
    "Group I cations are precipitated with dilute HCl",
    "Group V cations are precipitated as carbonates",
    "Dilute H2SO4, not HCl, is used to acidify KMnO4 titrations",
], [
    "KMnO4 titrations are acidified with HCl",
    "Phenolphthalein is used for strong acid vs weak base titrations",
    "Group I cations are precipitated with H2S in basic medium",
    "Brown ring test detects sulphate ions",
], "Practical Chemistry")
