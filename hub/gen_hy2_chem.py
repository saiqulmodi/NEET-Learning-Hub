"""High-yield NEET Chemistry, second batch (Classes 11-12): more original questions on repeatedly asked topics.

Tagged "hy2" so it is generated after the first high-yield batch and existing question ids never move. Numericals are computed.
"""
import math

from .core import table, facts, gen, num_q, Q, fmt, sci, tag

tag("hy2")


def R(rng, *xs):
    return rng.choice(xs)


# ---------------------------------------------------------------- Class 11
@gen("c11-01", weight=3)
def _dilution(rng):
    m1, v1, v2 = R(rng, 0.5, 1, 2, 5), R(rng, 50, 100, 200), R(rng, 250, 500, 1000)
    return num_q(rng, f"{v1} mL of {m1} M HCl is diluted to {v2} mL. The new molarity is:", m1 * v1 / v2, " M", "M1V1 = M2V2.",
                 wrongs=[m1 * v2 / v1, m1 * (v2 - v1) / v2, m1 / 2])


@gen("c11-01", weight=2)
def _gas_volume(rng):
    sp, m = rng.choice([("O2", 32), ("N2", 28), ("CO2", 44), ("CH4", 16), ("NH3", 17)])
    g = R(rng, 8, 16, 32, 44, 64, 88)
    return num_q(rng, f"The volume of {g} g of {sp} at STP (22.4 L/mol) is:", g / m * 22.4, " L", "V = (mass/M) × 22.4 L.",
                 wrongs=[g * 22.4, m / g * 22.4, g / m])


@gen("c11-01", weight=2)
def _molality(rng):
    sp, m = rng.choice([("NaOH", 40), ("glucose", 180), ("urea", 60), ("NaCl", 58.5)])
    g, w = R(rng, 4, 6, 9, 18, 20), R(rng, 100, 200, 500)
    return num_q(rng, f"{g} g of {sp} (M = {m}) is dissolved in {w} g of water. The molality is:", g / m / (w / 1000), " m",
                 "m = moles of solute / kg of solvent.", wrongs=[g / m, g / m / w, g / m / (w / 1000) / 2])


@gen("c11-02", weight=2)
def _photon(rng):
    lam = R(rng, 200, 300, 400, 500, 600, 662)
    e = 6.626e-34 * 3e8 / (lam * 1e-9)
    return num_q(rng, f"The energy of a photon of wavelength {lam} nm (h = 6.626 × 10^-34 J s) is:", e, " J", "E = hc/λ.",
                 wrongs=[e * 10, e / 10, 6.626e-34 * lam], form=lambda x: sci(x))


@gen("c11-02", weight=2)
def _quantum(rng):
    name, n, l = rng.choice([("3d", 3, 2), ("4f", 4, 3), ("2p", 2, 1), ("5s", 5, 0), ("4d", 4, 2), ("3p", 3, 1)])
    ask = rng.choice(["l", "orbitals", "electrons"])
    if ask == "l":
        return Q(f"The azimuthal quantum number l for a {name} orbital is:", str(l), [str(x) for x in range(5) if x != l], "s = 0, p = 1, d = 2, f = 3.")
    if ask == "orbitals":
        return Q(f"The number of orbitals in a {name[1]} subshell is:", str(2 * l + 1), [str(x) for x in (1, 3, 5, 7, 9) if x != 2 * l + 1], "Orbitals = 2l + 1.")
    return Q(f"The maximum number of electrons in shell n = {n} is:", str(2 * n * n), [str(x) for x in (2 * n, n * n, 4 * n, 2 * n * n + 2) if x != 2 * n * n],
             "Maximum electrons = 2n².")


table("c11-03", [
    ("Element with Z = 101", "Mendelevium (Unnilunium)"), ("Element with Z = 104", "Rutherfordium (Unnilquadium)"),
    ("Element with Z = 109", "Meitnerium (Unnilennium)"), ("Element with Z = 110", "Darmstadtium (Ununnilium)"),
], "{}:", None)
facts("c11-03", [
    "Ionisation enthalpy decreases down a group",
    "Metallic character increases down a group",
    "Oxides become more basic down a group",
    "Diagonal relationship exists between Li and Mg",
    "Be and Al show a diagonal relationship",
    "Noble gases have positive electron gain enthalpy",
], [
    "Metallic character decreases down a group",
    "Oxides become more acidic down a group",
    "Na and Mg show a diagonal relationship",
    "Ionisation enthalpy increases down a group",
    "Li and Be show a diagonal relationship",
    "Halogens have positive electron gain enthalpies",
], "periodic trends")


@gen("c11-04", weight=2)
def _bond_count(rng):
    mol, s, p = rng.choice([("C2H4 (ethene)", 5, 1), ("C2H2 (ethyne)", 3, 2), ("CO2", 2, 2), ("N2", 1, 2), ("HCN", 2, 2), ("C2H6 (ethane)", 7, 0),
                            ("benzene", 12, 3)])
    ask = rng.choice(["σ", "π"])
    val = s if ask == "σ" else p
    return Q(f"The number of {ask} bonds in {mol} is:", str(val), [str(x) for x in range(0, 13) if x != val][:6], f"{mol}: {s} σ and {p} π bonds.")


table("c11-04", [
    ("H2O", "Has lone pairs and a dipole moment; bent"), ("CO2", "Linear; zero dipole moment"),
    ("NH3", "Pyramidal; dipole moment 1.47 D"), ("CCl4", "Tetrahedral; zero dipole moment"),
], "Which description fits {}?", None)

table("c11-05", [
    ("Isothermal process", "Temperature constant"), ("Adiabatic process", "No heat exchange"), ("Isobaric process", "Pressure constant"),
    ("Isochoric process", "Volume constant"), ("Cyclic process", "System returns to its initial state"),
], "{}:", "Which process: {}?")


@gen("c11-05", weight=2)
def _hess(rng):
    a, b = R(rng, -394, -286, -110, -242), R(rng, -283, -394, -46, -92)
    return num_q(rng, f"If reaction 1 has ΔH = {a} kJ and reaction 2 has ΔH = {b} kJ, the ΔH of (reaction 1 - reaction 2) is:", a - b, " kJ",
                 "Hess's law: subtract the equations and their ΔH.", wrongs=[a + b, b - a, a * b / 100])


@gen("c11-06", weight=2)
def _kc(rng):
    a, b, c = R(rng, 0.1, 0.2, 0.5), R(rng, 0.1, 0.2, 0.4), R(rng, 0.2, 0.4, 0.6, 1)
    return num_q(rng, f"For A + B ⇌ C at equilibrium, [A] = {a} M, [B] = {b} M and [C] = {c} M. Kc is:", c / (a * b), "",
                 "Kc = [C]/([A][B]).", wrongs=[a * b / c, c / (a + b), c * a * b])


@gen("c11-06", weight=2)
def _buffer(rng):
    pka, ratio = R(rng, 4.74, 4.76, 9.25, 3.75), R(rng, 1, 10, 0.1, 2)
    return num_q(rng, f"A buffer has pKa = {pka} and [salt]/[acid] = {fmt(ratio)}. Its pH is:", pka + math.log10(ratio), "",
                 "Henderson equation: pH = pKa + log([salt]/[acid]).", wrongs=[pka - math.log10(ratio), pka * ratio, pka + ratio], form=lambda x: fmt(x, 2))


facts("c11-06", [
    "The ionic product of water at 25 °C is 1 × 10^-14",
    "pH + pOH = 14 at 25 °C",
    "Salts of a strong acid and weak base give acidic solutions",
    "Salts of a weak acid and strong base give basic solutions",
    "A Lewis base donates an electron pair",
    "Le Chatelier's principle predicts the effect of changing conditions on equilibrium",
], [
    "Salts of a strong acid and weak base give basic solutions",
    "A Lewis acid donates an electron pair",
    "pH + pOH = 7 at 25 °C",
    "Sodium acetate solution is acidic",
    "Ammonium chloride solution is basic",
    "The ionic product of water does not change with temperature",
], "ionic equilibrium")

table("c11-07", [
    ("Cr in CrO5", "+6"), ("S in H2S2O8", "+6", ["+6"]), ("Mn in K2MnO4", "+6", ["+6"]), ("Fe in K4[Fe(CN)6]", "+2"),
    ("Os in OsO4", "+8"), ("C in C3O2", "+4/3"), ("Cl in ClO2", "+4"), ("N in N2O", "+1"),
], "The oxidation state of {} is:", None, weight=2)

table("c11-08", [
    ("CH3-CH2-OH", "Ethanol"), ("CH3-CO-CH3", "Propanone"), ("CH3-CHO", "Ethanal"), ("CH3-COOH", "Ethanoic acid"),
    ("CH3-O-CH3", "Methoxymethane"), ("CH3-CH2-NH2", "Ethanamine"), ("CH3-CN", "Ethanenitrile"), ("CH3-COO-CH3", "Methyl ethanoate"),
], "The IUPAC name of {} is:", "Which structure is {}?", weight=2)
table("c11-08", [
    ("Structural isomers differing in chain", "Chain isomerism"), ("Isomers differing in the position of a group", "Position isomerism"),
    ("Isomers with different functional groups", "Functional isomerism"), ("Isomers differing in groups on either side of a functional group", "Metamerism"),
], "{} show:", "{} means:")

facts("c11-09", [
    "Alkanes are also called paraffins",
    "Ethene has a planar structure",
    "Ethyne has a linear structure",
    "cis-But-2-ene has a higher boiling point than trans-but-2-ene",
    "trans-But-2-ene has a higher melting point than cis-but-2-ene",
    "Free radical halogenation of alkanes needs light or heat",
], [
    "Alkanes are highly reactive at room temperature",
    "Ethyne is a bent molecule",
    "Ethene is non-planar",
    "trans-But-2-ene has a higher dipole moment than cis",
    "Halogenation of alkanes happens in the dark at 0 °C",
    "Benzene readily decolourises bromine water",
], "hydrocarbons")

# ---------------------------------------------------------------- Class 12
@gen("c12-01", weight=2)
def _mass_from_fp(rng):
    g, w, dt = R(rng, 1, 2, 5, 10), R(rng, 50, 100, 200), R(rng, 0.186, 0.372, 0.93, 0.5)
    m = 1.86 * g * 1000 / (dt * w)
    return num_q(rng, f"{g} g of a non-electrolyte in {w} g of water lowers the freezing point by {dt} K (Kf = 1.86). Its molar mass is:", m, " g/mol",
                 "M = Kf × w × 1000/(ΔTf × W).", wrongs=[m / 2, m * 2, 1.86 * g / (dt * w)])


@gen("c12-01", weight=2)
def _rlvp(rng):
    n2, n1 = R(rng, 0.1, 0.2, 0.5, 1), R(rng, 5, 9.9, 10, 20)
    x = n2 / (n1 + n2)
    return num_q(rng, f"{n2} mol of a non-volatile solute is dissolved in {n1} mol of solvent. The relative lowering of vapour pressure is:", x, "",
                 "ΔP/P° = mole fraction of solute.", wrongs=[n2 / n1, n1 / (n1 + n2), x * 2], form=lambda v: fmt(v, 4))


@gen("c12-02", weight=2)
def _nernst(rng):
    e0, n = R(rng, 1.1, 0.46, 0.34), R(rng, 1, 2)
    q = R(rng, 10, 100, 0.1, 0.01)
    e = e0 - 0.059 / n * math.log10(q)
    return num_q(rng, f"For a cell with E° = {e0} V, n = {n} and reaction quotient Q = {fmt(q)}, the cell potential at 298 K is:", e, " V",
                 "E = E° - (0.059/n) log Q.", wrongs=[e0 + 0.059 / n * math.log10(q), e0, e0 - 0.059 * math.log10(q) * n], form=lambda x: fmt(x, 3))


@gen("c12-02", weight=2)
def _lambda_m(rng):
    k, c = R(rng, 0.01, 0.02, 0.0125, 0.005), R(rng, 0.1, 0.05, 0.01, 0.2)
    lm = k * 1000 / c
    return num_q(rng, f"A solution of concentration {c} mol/L has conductivity {k} S/cm. Its molar conductivity is:", lm, " S cm² mol⁻¹",
                 "Λm = κ × 1000 / C.", wrongs=[k / c, k * c * 1000, lm / 10])


@gen("c12-03", weight=2)
def _first_order_time(rng):
    k = R(rng, 0.01, 0.02, 0.05, 0.1, 0.2303)
    f = R(rng, 90, 99, 99.9, 75, 50)
    t = 2.303 / k * math.log10(100 / (100 - f))
    return num_q(rng, f"For a first-order reaction with k = {k} per min, the time for {f}% completion is:", t, " min", "t = (2.303/k) log([A]₀/[A]).",
                 wrongs=[t / 2, t * 2, 1 / k])


@gen("c12-03", weight=2)
def _zero_order(rng):
    a0, k = R(rng, 0.5, 1, 2), R(rng, 0.01, 0.02, 0.05)
    return num_q(rng, f"A zero-order reaction has [A]₀ = {a0} M and k = {k} M/s. Its half-life is:", a0 / (2 * k), " s", "t½ = [A]₀/2k.",
                 wrongs=[0.693 / k, a0 / k, 2 * a0 * k])


table("c12-04", [
    ("[Ar] 3d5 4s1", "Chromium"), ("[Ar] 3d10 4s1", "Copper"), ("[Ar] 3d5 4s2", "Manganese"), ("[Ar] 3d6 4s2", "Iron"),
    ("[Ar] 3d10 4s2", "Zinc"), ("[Ar] 3d1 4s2", "Scandium"), ("[Ar] 3d8 4s2", "Nickel"),
], "The element with configuration {} is:", "The electron configuration of {} is:", weight=2)
table("c12-04", [
    ("KMnO4 in acid", "MnO4- is reduced to Mn2+"), ("KMnO4 in neutral or faintly alkaline medium", "MnO4- is reduced to MnO2"),
    ("K2Cr2O7 in acid", "Cr2O7 2- is reduced to Cr3+"), ("Acidified K2Cr2O7 with H2S", "Sulphur is precipitated"),
], "{}:", "Which reaction: {}?")

table("c12-05", [
    ("K3[Fe(CN)6]", "Potassium hexacyanidoferrate(III)"), ("K4[Fe(CN)6]", "Potassium hexacyanidoferrate(II)"),
    ("[Co(NH3)6]Cl3", "Hexaamminecobalt(III) chloride"), ("[Pt(NH3)2Cl2]", "Diamminedichloridoplatinum(II)"),
    ("[Ni(CO)4]", "Tetracarbonylnickel(0)"), ("[Cu(NH3)4]SO4", "Tetraamminecopper(II) sulphate"),
], "The IUPAC name of {} is:", "Which complex is {}?", weight=2)


@gen("c12-05", weight=2)
def _ox_coord(rng):
    cx, ox, cn = rng.choice([("[Co(NH3)5Cl]Cl2", 3, 6), ("K3[Fe(C2O4)3]", 3, 6), ("[Pt(en)2Cl2]2+", 4, 6), ("[Ni(CN)4]2-", 2, 4),
                             ("[Fe(CO)5]", 0, 5), ("K2[PtCl6]", 4, 6), ("[Cr(H2O)6]Cl3", 3, 6)])
    if rng.random() < 0.5:
        return Q(f"The oxidation state of the metal in {cx} is:", f"{ox:+d}" if ox else "0", ["0", "+1", "+2", "+3", "+4", "+6"], "Sum of charges of ligands and ions.")
    return Q(f"The coordination number of the metal in {cx} is:", str(cn), ["2", "4", "5", "6", "8"], "Count donor atoms; en and oxalate are bidentate.")


table("c12-06", [
    ("CHCl3", "Chloroform; once an anaesthetic"), ("CHI3", "Iodoform; antiseptic"), ("CCl4", "Carbon tetrachloride; once in fire extinguishers"),
    ("CF2Cl2", "Freon-12; refrigerant that damages ozone"), ("DDT", "p,p'-Dichlorodiphenyltrichloroethane; insecticide"),
], "{}:", "Which compound: {}?")

table("c12-07", [
    ("Ethanol with Na", "Sodium ethoxide and H2"), ("Phenol with NaOH", "Sodium phenoxide"), ("Ethanol with SOCl2", "Chloroethane"),
    ("Phenol with Br2 in CS2 at low temperature", "o- and p-Bromophenol"), ("Salicylic acid with acetic anhydride", "Aspirin"),
], "{} gives:", "Which reaction gives {}?")

table("c12-08", [
    ("Benzaldehyde with conc. NaOH", "Benzyl alcohol and sodium benzoate"), ("Acetaldehyde with dilute NaOH", "3-Hydroxybutanal (aldol)"),
    ("Acetone with NH2OH", "Acetone oxime"), ("Aldehyde with HCN", "Cyanohydrin"), ("Acetic acid with PCl5", "Acetyl chloride"),
    ("Sodium benzoate with soda lime", "Benzene"),
], "{} gives:", "Which reaction gives {}?", weight=2)
facts("c12-08", [
    "The order of acidity is HCOOH > CH3COOH",
    "Chloroacetic acid is stronger than acetic acid",
    "Trifluoroacetic acid is stronger than trichloroacetic acid",
    "Aldehydes are generally more reactive than ketones towards nucleophilic addition",
    "The carbonyl carbon is electrophilic",
    "2,4-DNP gives orange-red precipitates with aldehydes and ketones",
], [
    "Acetic acid is stronger than formic acid",
    "Ketones are more reactive than aldehydes towards nucleophiles",
    "The carbonyl oxygen is electrophilic",
    "Trichloroacetic acid is stronger than trifluoroacetic acid",
    "2,4-DNP reacts only with carboxylic acids",
    "Benzoic acid is weaker than phenol",
], "carbonyl compounds and acids")

table("c12-09", [
    ("C6H5NH2", "Aniline (benzenamine)"), ("CH3NHCH3", "N-Methylmethanamine"), ("(CH3)3N", "N,N-Dimethylmethanamine"),
    ("C6H5N2+Cl-", "Benzenediazonium chloride"), ("C6H5NHCOCH3", "N-Phenylethanamide (acetanilide)"),
], "{} is:", "Which formula is {}?")

table("c12-10", [
    ("Glucose with HI", "n-Hexane"), ("Glucose with Br2 water", "Gluconic acid"), ("Glucose with HNO3", "Saccharic acid"),
    ("Glucose with acetic anhydride", "Glucose pentaacetate"), ("Glucose with NH2OH", "Glucose oxime"),
], "{} gives:", "Which reaction gives {}?")

table("c12-pb", [
    ("Oxoacid with S in +4 state", "H2SO3"), ("Peroxodisulphuric acid", "H2S2O8"), ("Pyrosulphuric acid (oleum)", "H2S2O7"),
    ("Hypochlorous acid", "HOCl"), ("Perchloric acid", "HClO4"), ("Chloric acid", "HClO3"),
], "{} is:", "{} is called:")
facts("c12-pb", [
    "Ozone is thermodynamically unstable with respect to oxygen",
    "Sulphuric acid is dibasic",
    "Nitrogen exists as a diatomic molecule with a triple bond",
    "PCl5 is trigonal bipyramidal in the gas phase",
    "Interhalogen compounds are more reactive than halogens (except F2)",
    "Helium is used in diving apparatus as a diluent for oxygen",
    "Neon is used in discharge tubes for advertisement signs",
    "Argon provides an inert atmosphere in metallurgy",
], [
    "Ozone is more stable than oxygen",
    "PCl5 is square planar",
    "Sulphuric acid is monobasic",
    "Interhalogens are less reactive than all halogens",
    "Helium is used in neon signs as the main gas",
    "Nitrogen is a strong oxidising agent at room temperature",
    "Argon is very reactive",
    "Phosphorus forms stable Pπ-Pπ multiple bonds like nitrogen",
], "p-block elements")

table("c12-pr", [
    ("Group I", "Pb2+ as chlorides with dilute HCl"), ("Group II", "Cu2+, Pb2+ as sulphides with H2S in dilute HCl"),
    ("Group III", "Fe3+, Al3+ as hydroxides with NH4OH and NH4Cl"), ("Group IV", "Zn2+, Ni2+, Co2+ as sulphides with H2S in ammoniacal medium"),
    ("Group V", "Ba2+, Ca2+, Sr2+ as carbonates with (NH4)2CO3"), ("Group zero", "NH4+ detected with NaOH (ammonia smell)"),
], "In cation analysis, {}:", "Which group: {}?")

tag(None)
