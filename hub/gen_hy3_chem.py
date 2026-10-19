"""High-yield NEET Chemistry, third batch (Classes 11-12): more original questions on repeatedly asked topics.

Tagged "hy3" so it is generated after the earlier batches and existing question ids never move. Numericals are computed.
"""
import math

from .core import table, facts, groups, gen, num_q, Q, fmt, sci, tag

tag("hy3")


def R(rng, *xs):
    return rng.choice(xs)


# ---------------------------------------------------------------- Class 11
@gen("c11-01", weight=3)
def _mole_fraction(rng):
    n1, n2 = R(rng, 1, 2, 3, 4), R(rng, 1, 2, 5, 6)
    return num_q(rng, f"A solution has {n1} mol of solute and {n2} mol of solvent. The mole fraction of the solute is:", n1 / (n1 + n2), "",
                 "x = n(solute)/(n(solute) + n(solvent)).", wrongs=[n1 / n2, n2 / (n1 + n2), n1 / (n1 + n2) * 2], form=lambda x: fmt(x, 3))


@gen("c11-01", weight=2)
def _atoms_in(rng):
    sp, m, at = rng.choice([("H2O", 18, 3), ("CO2", 44, 3), ("NH3", 17, 4), ("CH4", 16, 5), ("C6H12O6", 180, 24), ("O3", 48, 3)])
    g = R(rng, 1, 2, 3, 5) * m
    n = g / m * at
    return Q(f"The total number of atoms in {g} g of {sp} (M = {m}) is:", f"{fmt(n)} NA", [f"{fmt(x)} NA" for x in (g / m, n * 2, g / m * (at - 1), n / 2)],
             f"{fmt(g / m)} mol × {at} atoms per molecule.")


@gen("c11-01", weight=2)
def _percent_w(rng):
    s, w = R(rng, 5, 10, 20, 25), R(rng, 95, 90, 80, 75, 100)
    return num_q(rng, f"{s} g of solute is dissolved in {w} g of solvent. The mass percent of the solute is:", 100 * s / (s + w), "%",
                 "Mass % = solute/(solute + solvent) × 100.", wrongs=[100 * s / w, s, 100 * w / (s + w)])


@gen("c11-02", weight=2)
def _de_broglie_electron(rng):
    v = R(rng, 1e6, 2e6, 5e5, 3e6)
    lam = 6.626e-34 / (9.11e-31 * v)
    return num_q(rng, f"The de Broglie wavelength of an electron moving at {sci(v)} m/s is (h = 6.626 × 10^-34, m = 9.11 × 10^-31 kg):", lam * 1e9, " nm",
                 "λ = h/mv.", wrongs=[lam * 1e10, lam * 1e6, lam * 2e9], form=lambda x: sci(x))


@gen("c11-02", weight=2)
def _rydberg(rng):
    n1, n2 = rng.choice([(1, 2), (2, 3), (1, 3), (2, 4), (3, 4)])
    inv = 109677 * (1 / n1 ** 2 - 1 / n2 ** 2)
    return num_q(rng, f"For hydrogen, the wavenumber of the line from n = {n2} to n = {n1} is (R = 109677 cm⁻¹):", inv, " cm⁻¹",
                 "ν̄ = R(1/n1² - 1/n2²).", wrongs=[109677 * (1 / n1 - 1 / n2), 109677 / n2 ** 2, 109677 * (1 / n1 ** 2 + 1 / n2 ** 2)])


table("c11-02", [
    ("J.J. Thomson", "Discovered the electron with cathode rays; plum pudding model"), ("Rutherford", "Nuclear model from alpha scattering"),
    ("Chadwick", "Discovered the neutron"), ("Millikan", "Measured the charge of the electron (oil drop)"),
    ("Bohr", "Quantised orbits of hydrogen"), ("de Broglie", "Wave nature of matter"), ("Heisenberg", "Uncertainty principle"),
], "{}:", "Who is known for: {}?")
table("c11-03", [
    ("Na", "s-block"), ("Ca", "s-block", ["s-block"]), ("Fe", "d-block"), ("Cu", "d-block", ["d-block"]), ("Cl", "p-block"),
    ("Ne", "p-block", ["p-block"]), ("Ce", "f-block"), ("U", "f-block", ["f-block"]),
], "{} belongs to the:", None)
facts("c11-03", [
    "The modern periodic table has 18 groups and 7 periods",
    "Lanthanoids and actinoids are placed at the bottom of the table",
    "Isoelectronic species have the same number of electrons",
    "Electronegativity is not a measurable quantity like ionisation enthalpy",
    "The first ionisation enthalpy of Be is higher than that of B",
    "Atomic size of noble gases is given as van der Waals radius",
], [
    "The modern periodic table has 8 groups",
    "Isoelectronic species have the same number of protons",
    "The first ionisation enthalpy of B is higher than that of Be",
    "Lanthanoids are in period 2",
    "Electronegativity is measured directly in kJ/mol",
    "Mendeleev arranged elements by atomic number",
], "the periodic table")
table("c11-04", [
    ("NH4+", "Tetrahedral"), ("SO4 2-", "Tetrahedral", ["Tetrahedral"]), ("NO3-", "Trigonal planar"), ("CO3 2-", "Trigonal planar", ["Trigonal planar"]),
    ("I3-", "Linear"), ("ClO3-", "Pyramidal"), ("H3O+", "Pyramidal", ["Pyramidal"]), ("SF6", "Octahedral"),
], "The shape of {} is:", None, weight=2)
facts("c11-04", [
    "Ionic bonds form more easily with low ionisation enthalpy and high electron gain enthalpy",
    "Lattice enthalpy helps stabilise ionic compounds",
    "Fajans' rules predict covalent character in ionic bonds",
    "Hydrogen bonding makes the boiling point of water high",
    "A coordinate bond forms when one atom donates both electrons",
    "Resonance in benzene gives all C-C bonds the same length",
], [
    "Benzene has alternating short and long C-C bonds",
    "Hydrogen bonding lowers the boiling point of water",
    "A coordinate bond needs both atoms to give one electron",
    "Large cations favour covalent character (Fajans)",
    "Lattice enthalpy makes ionic compounds less stable",
    "Ionic bonds form between two non-metals",
], "chemical bonding")
table("c11-05", [
    ("Enthalpy of combustion", "Heat released when 1 mol burns completely in oxygen"), ("Enthalpy of formation", "Heat change when 1 mol forms from elements in standard states"),
    ("Enthalpy of neutralisation", "Heat released when acid and base form 1 mol of water"), ("Bond enthalpy", "Energy to break 1 mol of a bond in the gas phase"),
    ("Lattice enthalpy", "Energy to separate 1 mol of an ionic solid into gaseous ions"), ("Enthalpy of atomisation", "Energy to break 1 mol of a substance into gaseous atoms"),
], "{} is:", "Which enthalpy: {}?")


@gen("c11-05", weight=2)
def _bond_enthalpy(rng):
    hh, xx, hx, name = rng.choice([(436, 242, 431, "HCl"), (436, 158, 565, "HF"), (436, 193, 366, "HBr")])
    dh = hh + xx - 2 * hx
    return num_q(rng, f"Using bond enthalpies H-H = {hh}, X-X = {xx} and H-X = {hx} kJ/mol, ΔH for H2 + X2 → 2{name} is:", dh, " kJ",
                 "ΔH = bonds broken - bonds formed.", wrongs=[hh + xx - hx, 2 * hx - hh - xx, hh + xx + 2 * hx])


@gen("c11-06", weight=2)
def _degree(rng):
    ka, c = R(rng, 1.8e-5, 1e-5, 4e-4, 2e-6), R(rng, 0.1, 0.01, 0.05)
    a = math.sqrt(ka / c)
    return num_q(rng, f"The degree of ionisation of a {c} M weak acid with Ka = {sci(ka)} is about:", a, "", "α = √(Ka/C).",
                 wrongs=[ka / c, math.sqrt(ka * c), a * 10], form=lambda x: sci(x))


@gen("c11-06", weight=2)
def _poh(rng):
    e = R(rng, 1, 2, 3, 4, 5)
    c = R(rng, 1, 2, 5)
    oh = c * 10 ** -e
    return num_q(rng, f"The pOH of a solution with [OH-] = {c} × 10^-{e} M is:", -math.log10(oh), "", "pOH = -log[OH-].",
                 wrongs=[14 + math.log10(oh), e, -math.log10(oh) + 1], form=lambda x: fmt(x, 2))


table("c11-06", [
    ("CH3COONa", "Basic (salt of weak acid and strong base)"), ("NH4Cl", "Acidic (salt of strong acid and weak base)"),
    ("NaCl", "Neutral (salt of strong acid and strong base)"), ("CH3COONH4", "Nearly neutral (both weak)"),
    ("Na2CO3", "Basic (salt of weak acid and strong base)", ["Basic (salt of weak acid and strong base)"]),
], "An aqueous solution of {} is:", None)
facts("c11-07", [
    "In the reaction 2Na + Cl2 → 2NaCl, sodium is oxidised",
    "Balancing by the half-reaction method balances electrons separately",
    "In a galvanic cell oxidation occurs at the anode",
    "MnO4- is purple and Mn2+ is nearly colourless",
    "Hydrogen peroxide can act as both oxidant and reductant",
    "In NaH, hydrogen is in the -1 state",
], [
    "In 2Na + Cl2 → 2NaCl chlorine is oxidised",
    "Oxidation occurs at the cathode of a galvanic cell",
    "H2O2 can act only as an oxidant",
    "MnO4- is colourless",
    "The oxidation number of an element in its free state is +1",
    "Reduction is loss of electrons",
], "redox reactions")
table("c11-08", [
    ("-I effect", "Electron-withdrawing through sigma bonds, e.g. -NO2, -Cl"), ("+I effect", "Electron-donating through sigma bonds, e.g. -CH3"),
    ("Electromeric effect", "Temporary shift of π electrons when a reagent attacks"), ("Hyperconjugation", "Delocalisation of σ C-H electrons into an adjacent p orbital"),
    ("Resonance (+R) effect", "Donation of lone pair into a π system, e.g. -OH, -NH2"),
], "{}:", "Which electronic effect: {}?")
table("c11-08", [
    ("Crystallisation", "Purifies a solid using a suitable solvent"), ("Distillation", "Separates liquids with very different boiling points"),
    ("Fractional distillation", "Separates liquids with close boiling points"), ("Distillation under reduced pressure", "Purifies liquids that decompose below their boiling point"),
    ("Differential extraction", "Uses a solvent in which the compound is more soluble"), ("Sublimation", "Purifies solids that turn directly into vapour"),
], "{}:", "Which method: {}?")
table("c11-09", [
    ("Ethane", "C2H6"), ("Ethene", "C2H4"), ("Ethyne", "C2H2"), ("Propane", "C3H8"), ("Butane", "C4H10"), ("Benzene", "C6H6"),
    ("Toluene", "C7H8"), ("Cyclohexane", "C6H12"),
], "The molecular formula of {} is:", "{} is the formula of:")
facts("c11-09", [
    "Aromatic compounds have (4n + 2) π electrons in a planar ring",
    "Benzene is carcinogenic",
    "Polynuclear hydrocarbons in tobacco smoke can cause cancer",
    "Addition of HBr to propene gives 2-bromopropane",
    "Alkynes give a white precipitate with ammoniacal AgNO3 only if they are terminal",
    "Combustion of alkanes releases CO2, water and heat",
], [
    "Addition of HBr to propene (no peroxide) gives 1-bromopropane",
    "All alkynes give a precipitate with ammoniacal AgNO3",
    "Benzene has 4n π electrons",
    "Alkanes undergo addition reactions easily",
    "Tobacco smoke has no carcinogens",
    "Benzene is a saturated hydrocarbon",
], "hydrocarbons")

# ---------------------------------------------------------------- Class 12
@gen("c12-01", weight=2)
def _henry(rng):
    kh, p = R(rng, 1.67e8, 7.6e4, 1e5), R(rng, 1, 2, 0.5)
    x = p * 1.013e5 / kh
    return num_q(rng, f"Henry's law constant of a gas in water is {sci(kh)} Pa. At a partial pressure of {p} atm (1 atm = 1.013 × 10^5 Pa), its mole fraction in water is:",
                 x, "", "x = p/KH.", wrongs=[kh / (p * 1.013e5), p / kh, x * 10], form=lambda v: sci(v))


@gen("c12-01", weight=2)
def _ppm(rng):
    g, mass = R(rng, 1, 2, 5, 10), R(rng, 1000, 10000, 100000)
    return num_q(rng, f"{g} g of a substance is present in {mass} g of solution. Its concentration in ppm is:", g / mass * 1e6, " ppm",
                 "ppm = parts per 10^6 parts.", wrongs=[g / mass * 100, g / mass * 1e3, g / mass * 1e9], form=lambda v: sci(v))


table("c12-01", [
    ("Positive deviation from Raoult's law", "A-B attractions weaker than A-A and B-B; ΔHmix > 0"),
    ("Negative deviation from Raoult's law", "A-B attractions stronger; ΔHmix < 0"),
    ("Ideal solution", "ΔHmix = 0 and ΔVmix = 0"), ("Azeotrope", "Boils at constant temperature with the same composition in liquid and vapour"),
], "{}:", "Which term: {}?")


@gen("c12-02", weight=2)
def _kc_cell(rng):
    n, e = R(rng, 1, 2), R(rng, 0.059, 0.118, 0.236, 0.295)
    logk = n * e / 0.059
    return num_q(rng, f"A cell has n = {n} and E° = {e} V at 298 K. log K for the reaction is:", logk, "", "log K = nE°/0.059.",
                 wrongs=[e / (0.059 * n), n * e, logk * 2.303], form=lambda x: fmt(x, 2))


table("c12-02", [
    ("Dry cell (Leclanché)", "Zinc anode, carbon cathode with MnO2; about 1.5 V"), ("Mercury cell", "Zn-Hg anode, HgO paste; about 1.35 V"),
    ("Lead storage battery", "Pb anode, PbO2 cathode, 38% H2SO4"), ("Nickel-cadmium cell", "Rechargeable; Cd anode, nickel hydroxide cathode"),
    ("H2-O2 fuel cell", "Converts combustion energy directly into electricity"),
], "{}:", "Which cell: {}?")
facts("c12-02", [
    "Corrosion of iron needs oxygen and water",
    "Sacrificial protection uses a more reactive metal such as zinc or magnesium",
    "In electrolysis of aqueous NaCl, H2 is formed at the cathode",
    "In electrolysis of aqueous NaCl, Cl2 is formed at the anode",
    "Strong electrolytes have nearly complete ionisation",
    "The cell constant is l/A",
], [
    "Corrosion of iron happens in dry air without water",
    "In electrolysis of aqueous NaCl, sodium metal forms at the cathode",
    "The cell constant is A/l",
    "Sacrificial protection uses a less reactive metal like copper",
    "Weak electrolytes ionise completely",
    "Rust is pure iron(II) oxide",
], "electrochemistry")


@gen("c12-03", weight=2)
def _arrhenius(rng):
    ea, t1, t2 = R(rng, 50, 80, 100), R(rng, 300, 298), R(rng, 310, 320, 350)
    ratio = 10 ** (ea * 1000 / (2.303 * 8.314) * (1 / t1 - 1 / t2))
    return num_q(rng, f"A reaction has Ea = {ea} kJ/mol. The ratio k({t2} K)/k({t1} K) is about:", ratio, "",
                 "log(k2/k1) = Ea/(2.303R)(1/T1 - 1/T2).", wrongs=[ratio / 2, ratio * 2, math.log10(ratio)], form=lambda x: fmt(x, 2))


table("c12-03", [
    ("Rate law", "Experimentally determined rate expression"), ("Molecularity", "Number of species colliding in an elementary step"),
    ("Rate-determining step", "Slowest step of a mechanism"), ("Activation energy", "Minimum extra energy for effective collisions"),
    ("Arrhenius factor A", "Frequency factor"), ("Pseudo first-order reaction", "Higher order behaves as first order because one reactant is in excess"),
], "{}:", "Which term: {}?")
table("c12-04", [
    ("Brass", "Copper and zinc"), ("Bronze", "Copper and tin"), ("Misch metal", "Lanthanoid metal (about 95%) with iron and traces"),
    ("Stainless steel", "Iron with chromium and nickel"), ("German silver", "Copper, zinc and nickel"),
], "{} is an alloy of:", "Which alloy contains {}?")
facts("c12-04", [
    "Transition metals form interstitial compounds",
    "Most transition metal ions are paramagnetic",
    "The enthalpy of atomisation of transition metals is high",
    "Zn, Cd and Hg have low melting points among the d-block",
    "Actinoid contraction is greater than lanthanoid contraction",
    "Ce shows +4 and Eu shows +2 apart from +3",
], [
    "Zn has the highest melting point in the 3d series",
    "Transition metals never form complexes",
    "Lanthanoid contraction is greater than actinoid contraction",
    "Most transition metal ions are diamagnetic",
    "Mercury is a solid at room temperature",
    "Interstitial compounds are less hard than the pure metals",
], "d- and f-block elements")
table("c12-05", [
    ("Werner's primary valency", "Oxidation state; ionisable"), ("Werner's secondary valency", "Coordination number; non-ionisable"),
    ("Chelate", "Ring formed by a polydentate ligand"), ("Ambidentate ligand", "Can bind through two different atoms, e.g. NO2-"),
    ("Homoleptic complex", "Only one kind of ligand"), ("Heteroleptic complex", "More than one kind of ligand"),
], "{}:", "Which term: {}?")
table("c12-05", [
    ("Linkage isomerism", "[Co(NH3)5(NO2)]Cl2 and [Co(NH3)5(ONO)]Cl2"), ("Ionisation isomerism", "[Co(NH3)5SO4]Br and [Co(NH3)5Br]SO4"),
    ("Hydrate isomerism", "[Cr(H2O)6]Cl3 and [Cr(H2O)5Cl]Cl2·H2O"), ("Coordination isomerism", "[Co(NH3)6][Cr(CN)6] and [Cr(NH3)6][Co(CN)6]"),
], "An example of {} is:", "{} is an example of:")


@gen("c12-05", weight=2)
def _cfse(rng):
    n, name = rng.choice([(1, "d1"), (2, "d2"), (3, "d3"), (4, "d4 (high spin)"), (6, "d6 (low spin)")])
    t2g, eg = {1: (1, 0), 2: (2, 0), 3: (3, 0), 4: (3, 1), 6: (6, 0)}[n]
    cfse = -0.4 * t2g + 0.6 * eg
    return Q(f"The crystal field stabilisation energy of an octahedral {name} ion (ignoring pairing energy) is:", f"{fmt(cfse, 1)} Δo",
             [f"{fmt(x, 1)} Δo" for x in (-0.4, -0.8, -1.2, -0.6, -2.4, -1.6, 0) if round(x, 1) != round(cfse, 1)],
             f"t2g^{t2g} eg^{eg}: CFSE = -0.4 × {t2g} + 0.6 × {eg} Δo.")


table("c12-06", [
    ("Ethyl chloride", "Chloroethane"), ("Isopropyl bromide", "2-Bromopropane"), ("Benzyl chloride", "Chloromethylbenzene"),
    ("Chloroform", "Trichloromethane"), ("Allyl chloride", "3-Chloroprop-1-ene"), ("Vinyl chloride", "Chloroethene"),
], "The IUPAC name of {} is:", "{} is commonly called:")
facts("c12-06", [
    "The C-X bond is polar because X is more electronegative than carbon",
    "Haloalkanes are only slightly soluble in water",
    "Boiling points of haloalkanes rise from fluoride to iodide",
    "Among isomeric haloalkanes, boiling point falls with branching",
    "p-Dichlorobenzene has a higher melting point than o- and m-isomers",
    "Optically active haloalkanes racemise in SN1 reactions",
], [
    "The C-X bond is non-polar",
    "Haloalkanes are freely soluble in water",
    "Boiling points fall from fluoride to iodide",
    "Branching raises the boiling point of isomeric haloalkanes",
    "o-Dichlorobenzene has the highest melting point of the three isomers",
    "SN2 reactions give racemic mixtures",
], "haloalkanes and haloarenes")
table("c12-07", [
    ("Ethanol", "CH3CH2OH; grain alcohol"), ("Methanol", "CH3OH; wood spirit"), ("Glycerol", "Propane-1,2,3-triol"),
    ("Ethylene glycol", "Ethane-1,2-diol; antifreeze"), ("Catechol", "Benzene-1,2-diol"), ("Resorcinol", "Benzene-1,3-diol"),
    ("Hydroquinone (quinol)", "Benzene-1,4-diol"),
], "{}:", "Which compound: {}?")
table("c12-08", [
    ("Formaldehyde", "Methanal"), ("Acetaldehyde", "Ethanal"), ("Acetone", "Propanone"), ("Acetophenone", "1-Phenylethanone"),
    ("Benzophenone", "Diphenylmethanone"), ("Formic acid", "Methanoic acid"), ("Acetic acid", "Ethanoic acid"), ("Oxalic acid", "Ethanedioic acid"),
], "The IUPAC name of {} is:", "{} is commonly called:", weight=2)
facts("c12-09", [
    "Amines are basic because nitrogen has a lone pair",
    "Primary and secondary amines form hydrogen bonds with each other",
    "Tertiary amines have the lowest boiling points among isomeric amines",
    "Aniline is less basic than ammonia",
    "Electron-donating groups increase the basic strength of aniline",
    "Arenediazonium salts are made at low temperature (273-278 K)",
], [
    "Tertiary amines have the highest boiling points among isomeric amines",
    "Aniline is more basic than ammonia",
    "Electron-withdrawing groups increase the basic strength of aniline",
    "Diazotisation is done at 373 K",
    "Amines are acidic because nitrogen has a lone pair",
    "Tertiary amines form hydrogen bonds with each other",
], "amines")
table("c12-10", [
    ("DNA bases", "A, G, C and T"), ("RNA bases", "A, G, C and U"), ("Nucleoside", "Base + sugar"), ("Nucleotide", "Base + sugar + phosphate"),
    ("Phosphodiester linkage", "Joins nucleotides in nucleic acids"), ("Peptide linkage", "Joins amino acids in proteins"),
    ("Glycosidic linkage", "Joins monosaccharides"),
], "{}:", "Which is: {}?")
groups("c12-10", {
    "fat-soluble vitamins": ["Vitamin A", "Vitamin D", "Vitamin E", "Vitamin K"],
    "water-soluble vitamins": ["Vitamin B1", "Vitamin B2", "Vitamin B6", "Vitamin C"],
}, "Which is NOT one of the {}?", "Which is one of the {}?")
table("c12-pb", [
    ("Oxygen allotrope", "Ozone"), ("Sulphur allotropes", "Rhombic and monoclinic sulphur"), ("Phosphorus allotropes", "White, red and black phosphorus"),
    ("Brown ring", "[Fe(H2O)5NO]2+"), ("Hypo", "Na2S2O3·5H2O"), ("Oleum", "H2S2O7"),
], "{}:", None)
facts("c12-pb", [
    "HNO3 is a strong oxidising agent",
    "Concentrated H2SO4 is a strong dehydrating agent",
    "Chlorine bleaches by oxidation in the presence of moisture",
    "Fluorine shows only the -1 oxidation state",
    "Hydrogen fluoride is a liquid at room temperature because of hydrogen bonding",
    "Xenon fluorides are made by direct reaction of xenon and fluorine",
], [
    "Chlorine bleaches by reduction",
    "Fluorine shows +7 in its compounds",
    "HF is a gas at room temperature with no hydrogen bonding",
    "Concentrated H2SO4 is a reducing agent only",
    "Xenon does not react with fluorine",
    "Nitric acid is a weak oxidising agent",
], "p-block chemistry")
table("c12-pr", [
    ("Oxalic acid vs KMnO4 titration", "Done at 333 K in dilute H2SO4"), ("Mohr's salt vs KMnO4 titration", "Done at room temperature in dilute H2SO4"),
    ("Iodine test", "Blue colour with starch"), ("Lassaigne's extract", "Sodium fusion extract"),
    ("Biuret test", "Violet colour for proteins"), ("Molisch's test", "Violet ring for carbohydrates"),
], "{}:", "Which test or method: {}?")

tag(None)
