"""Extra content for chapters that were thin after the first build."""
import math

from .core import table, facts, gen, num_q, Q, sig, sci, fmt


def R(rng, *xs):
    return rng.choice(xs)


# ---------------------------------------------------------------- p11-12 Kinetic Theory
@gen("p11-12", weight=2)
def _pv(rng):
    n, t, v = R(rng, 1, 2, 0.5), R(rng, 273, 300, 400, 500), R(rng, 0.01, 0.02, 0.0224, 0.05)
    return num_q(rng, f"Pressure of {n} mol of an ideal gas at {t} K in {v} m³ is (R = 8.314 J/mol K):", n * 8.314 * t / v, " Pa",
                 "PV = nRT.", form=sci, wrongs=[n * 8.314 * v / t, 8.314 * t / v, n * 0.0821 * t / v])


@gen("p11-12", weight=2)
def _cpcv(rng):
    gas, cv = rng.choice([("monatomic", 1.5), ("rigid diatomic", 2.5), ("rigid non-linear polyatomic", 3)])
    kind = rng.choice(["Cv", "Cp"])
    val = cv if kind == "Cv" else cv + 1
    pool = ["(3/2)R", "(5/2)R", "(7/2)R", "3R", "4R", "R"]
    ans = {1.5: "(3/2)R", 2.5: "(5/2)R", 3.5: "(7/2)R", 3: "3R", 4: "4R"}[val]
    return Q(f"Molar specific heat {kind} of a {gas} ideal gas is:", ans, [p for p in pool if p != ans],
             "Cv = (f/2)R and Cp = Cv + R.")


facts("p11-12", [
    "Pressure of an ideal gas is (1/3)ρv²rms",
    "Average kinetic energy of a molecule depends only on temperature",
    "Each degree of freedom has an average energy of (1/2)kT (law of equipartition)",
    "Mean free path decreases as the number density of molecules increases",
    "Cp - Cv = R for one mole of an ideal gas",
], [
    "Average kinetic energy of molecules depends on the nature of the gas",
    "Mean free path increases with pressure",
    "Cp is less than Cv for an ideal gas",
    "Each degree of freedom has energy kT",
    "Real gases obey PV = nRT exactly at high pressures",
], "Kinetic Theory", weight=2)

# ---------------------------------------------------------------- p12-05 Magnetism and Matter
table("p12-05", [
    ("Magnetic declination", "Angle between geographic and magnetic meridians"),
    ("Angle of dip (inclination)", "Angle the Earth's field makes with the horizontal"),
    ("Retentivity", "Magnetisation left when the magnetising field is removed"),
    ("Coercivity", "Reverse field needed to bring magnetisation to zero"),
    ("Magnetic susceptibility", "Ratio of magnetisation to magnetising field intensity"),
    ("Hysteresis", "Lag of magnetisation behind the magnetising field"),
], "{} is the:", "Which term means: {}?", weight=2)


@gen("p12-05", weight=2)
def _barmag(rng):
    m, b, th = R(rng, 0.5, 1, 2, 5), R(rng, 0.1, 0.2, 0.5), R(rng, 30, 60, 90)
    return num_q(rng, f"A bar magnet of moment {m} A m² is at {th}° to a uniform field of {b} T. Torque on it is:",
                 m * b * math.sin(math.radians(th)), " N m", "τ = mB sin θ.", wrongs=[m * b * math.cos(math.radians(th)) or m * b / 4, m / b, m * b * 2])


@gen("p12-05")
def _curie(rng):
    t1, t2 = R(rng, 200, 300), R(rng, 400, 600)
    return num_q(rng, f"A paramagnet has susceptibility χ at {t1} K. By Curie's law, its susceptibility at {t2} K is:", t1 / t2, " χ",
                 "χ ∝ 1/T.", form=lambda x: fmt(x, 3), wrongs=[t2 / t1, (t1 / t2) ** 2, 1])


# ---------------------------------------------------------------- p12-10 Wave Optics
@gen("p12-10", weight=2)
def _ydse(rng):
    lam, d, D = R(rng, 500, 600, 400, 700), R(rng, 0.5, 1, 0.2), R(rng, 1, 1.5, 2)
    beta = lam * 1e-9 * D / (d * 1e-3) * 1e3
    return num_q(rng, f"In Young's experiment λ = {lam} nm, slit separation {d} mm and screen distance {D} m. Fringe width is:", beta, " mm",
                 "β = λD/d.", wrongs=[beta * 10, beta / 2, lam * 1e-9 * d / D * 1e3 * 1e6 / 1e3])


@gen("p12-10", weight=2)
def _medium(rng):
    n = R(rng, 1.33, 1.5)
    return num_q(rng, f"The whole Young's double-slit set-up is immersed in a liquid of refractive index {n}. Fringe width becomes:", 1 / n,
                 " times", "Wavelength in the medium is λ/n.", form=lambda x: f"{x:.2f}", wrongs=[n, n * n, 1 / n ** 2])


@gen("p12-10")
def _singleslit(rng):
    lam, a = R(rng, 500, 600), R(rng, 0.1, 0.2, 0.5)
    theta = lam * 1e-9 / (a * 1e-3)
    return num_q(rng, f"Light of {lam} nm falls on a slit {a} mm wide. Angle of the first minimum (small angle) is:", theta, " rad",
                 "a sin θ = λ.", form=sci, wrongs=[theta * 2, theta / 2, a * 1e-3 / (lam * 1e-9)])


table("p12-10", [
    ("Constructive interference", "Path difference = nλ"), ("Destructive interference", "Path difference = (2n + 1)λ/2"),
    ("Brewster's law", "tan θB = n"), ("Malus's law", "I = I0 cos²θ"), ("Fringe width", "β = λD/d"),
], "{}:", "Which law or condition is: {}?")

# ---------------------------------------------------------------- p12-12 Atoms
@gen("p12-12", weight=2)
def _ion_energy(rng):
    z, n = rng.choice([(1, 1), (2, 1), (3, 1), (1, 2), (2, 2)])
    e = 13.6 * z * z / (n * n)
    sp = {1: "H", 2: "He+", 3: "Li2+"}[z]
    return num_q(rng, f"Energy needed to remove the electron from {sp} in the n = {n} state is:", e, " eV", "E = 13.6 Z²/n² eV.",
                 wrongs=[13.6 * z / n, 13.6 / n ** 2, 13.6 * z * z / n])


@gen("p12-12")
def _lines(rng):
    n = R(rng, 3, 4, 5, 6)
    return num_q(rng, f"Number of spectral lines possible when hydrogen electrons fall from n = {n} to the ground state:", n * (n - 1) / 2, "",
                 "Lines = n(n - 1)/2.", form=lambda x: str(int(x)), wrongs=[n - 1, n * n, n])


facts("p12-12", [
    "The Balmer series of hydrogen lies in the visible region",
    "Bohr's model applies to hydrogen-like (one-electron) atoms",
    "The size of an atom is about 10^-10 m and a nucleus about 10^-15 m",
    "Electron speed in the first Bohr orbit is about c/137",
], [
    "Bohr's model explains spectra of all many-electron atoms",
    "Electrons in Bohr orbits radiate energy continuously",
    "The Lyman series lies in the infrared region",
    "Nucleus size is about 10^-10 m",
], "Atoms")

# ---------------------------------------------------------------- c12-04 d- and f-Block
table("c12-04", [
    ("Potassium dichromate preparation", "Fusion of chromite ore (FeCr2O4) with Na2CO3 in air"),
    ("Potassium permanganate preparation", "Fusion of MnO2 with KOH and an oxidant, then oxidation of manganate"),
    ("Misch metal", "Alloy of a lanthanoid metal (about 95%) with iron and traces of S, C, Ca and Al"),
    ("Brass", "Copper-zinc alloy"), ("Bronze", "Copper-tin alloy"),
    ("Haber process catalyst", "Iron"), ("Ziegler-Natta catalyst", "TiCl4 with Al(CH3)3"),
], "{}:", "What is described: {}?")
table("c12-04", [
    ("Sc", "+3 only"), ("Mn", "+2 to +7"), ("Cr", "+3 and +6 most common"), ("Ce (lanthanoid)", "+3 and +4"),
], "Common oxidation states of {}:", None)
facts("c12-04", [
    "Transition metals have high melting points due to strong metallic bonding",
    "Cu+ compounds are colourless while Cu2+ compounds are coloured",
    "Mn2+ has a half-filled d5 configuration and is particularly stable",
    "KMnO4 oxidises iodide to iodine in acidic medium",
    "Actinoids are radioactive",
], [
    "Transition metals have low melting points",
    "Cu+ compounds are always blue",
    "All lanthanoids are radioactive",
    "Zn has partly filled d orbitals in its ground state",
], "d- and f-Block Elements")

# ---------------------------------------------------------------- c12-07 Alcohols, Phenols and Ethers
table("c12-07", [
    ("Primary alcohol + PCC", "Aldehyde"), ("Primary alcohol + acidified KMnO4", "Carboxylic acid"),
    ("Secondary alcohol + CrO3", "Ketone"), ("Tertiary alcohol + Cu at 573 K", "Alkene (dehydration)"),
    ("Phenol + bromine water", "2,4,6-tribromophenol (white precipitate)"), ("Phenol + Zn dust", "Benzene"),
    ("Phenol + conc. HNO3", "2,4,6-trinitrophenol (picric acid)"), ("Anisole + HI", "Phenol and methyl iodide"),
    ("Ethanol + conc. H2SO4 at 443 K", "Ethene"), ("Ethanol + conc. H2SO4 at 413 K", "Diethyl ether"),
], "{} gives:", None, weight=2)
facts("c12-07", [
    "Alcohols have higher boiling points than ethers of similar mass because of hydrogen bonding",
    "Order of acidity: phenol > water > ethanol",
    "Ethers are cleaved by HI",
    "Dehydration of alcohols follows the order tertiary > secondary > primary",
    "Commercial alcohol is made unfit for drinking by adding copper sulphate and pyridine (denaturation)",
], [
    "Ethers have higher boiling points than alcohols of similar mass",
    "Ethanol is more acidic than water",
    "Primary alcohols dehydrate most easily",
    "Phenol does not react with bromine water",
], "Alcohols, Phenols and Ethers")

# ---------------------------------------------------------------- c12-09 Amines
table("c12-09", [
    ("Aniline + Br2 water", "2,4,6-tribromoaniline (white precipitate)"),
    ("Benzene diazonium chloride + H2O (warm)", "Phenol"), ("Benzene diazonium chloride + H3PO2", "Benzene"),
    ("Benzene diazonium chloride + CuCN/KCN", "Benzonitrile"), ("Benzene diazonium chloride + KI", "Iodobenzene"),
    ("Nitrobenzene + Sn/HCl", "Aniline"), ("Acetamide + Br2 and NaOH", "Methylamine"),
    ("Aniline + acetic anhydride", "Acetanilide"),
], "{} gives:", None, weight=2)
facts("c12-09", [
    "Acetylation of aniline reduces the activating effect of -NH2",
    "Aniline gives a mixture with meta product on nitration because it is protonated in acid",
    "Amines are more basic than amides",
    "Aromatic diazonium salts are more stable than aliphatic ones",
    "Primary amines form intermolecular hydrogen bonds",
], [
    "Aniline does not react with bromine water",
    "Tertiary amines have higher boiling points than primary amines of similar mass",
    "Aliphatic diazonium salts are very stable",
    "Amides are more basic than amines",
], "Amines")

# ---------------------------------------------------------------- b11-13 Plant Growth and Development
table("b11-13", [
    ("Meristematic phase", "Cells with large nuclei and thin walls that keep dividing"),
    ("Elongation phase", "Increased vacuolation, cell enlargement and new wall deposition"),
    ("Maturation phase", "Cells reach maximal size and thicken their walls"),
    ("Dedifferentiation", "Differentiated cells regain the ability to divide"),
    ("Redifferentiation", "Cells from dedifferentiated tissue lose the ability to divide again"),
    ("Arithmetic growth", "Only one daughter cell keeps dividing; e.g. a root elongating at a constant rate"),
    ("Geometric growth", "Both daughter cells keep dividing, giving an exponential phase"),
], "{}:", "Which term describes: {}?", weight=2)
table("b11-13", [
    ("IAA and IBA", "Natural auxins"), ("NAA and 2,4-D", "Synthetic auxins"), ("GA3", "Most studied gibberellin"),
    ("Zeatin", "Natural cytokinin"), ("Kinetin", "Modified adenine cytokinin (not found in plants naturally)"),
    ("Ethephon", "Releases ethylene"),
], "{} is/are:", None)

# ---------------------------------------------------------------- b11-18 Neural Control
table("b11-18", [
    ("Central nervous system", "Brain and spinal cord"),
    ("Peripheral nervous system", "All nerves associated with the brain and spinal cord"),
    ("Afferent fibres", "Carry impulses from tissues or organs to the CNS"),
    ("Efferent fibres", "Carry impulses from the CNS to peripheral tissues or organs"),
    ("Somatic neural system", "Carries impulses from the CNS to skeletal muscles"),
    ("Autonomic neural system", "Carries impulses from the CNS to involuntary organs and smooth muscles"),
    ("Visceral nervous system", "Connects the CNS with the viscera"),
    ("Reflex arc", "Afferent neuron, integration in the CNS and efferent neuron"),
], "{}:", "Which part of the neural system: {}?", weight=2)
table("b11-18", [
    ("Depolarisation of the axon", "Rapid inflow of Na+ makes the inside positive"),
    ("Repolarisation", "K+ flows out and restores the resting potential"),
    ("Synaptic vesicles", "Release neurotransmitters into the synaptic cleft"),
    ("Dura mater, arachnoid and pia mater", "Cranial meninges covering the brain"),
    ("Grey matter of the cerebral cortex", "Folded layer with association areas"),
], "{}:", None)

# ---------------------------------------------------------------- b12-10 Biotechnology and its Applications
table("b12-10", [
    ("PCR in molecular diagnosis", "Detects very low amounts of a pathogen's nucleic acid"),
    ("ELISA", "Detects antigens or antibodies by an antigen-antibody reaction"),
    ("Recombinant DNA probe with autoradiography", "Detects a mutated gene"),
    ("Transgenic animals in vaccine safety", "Test polio vaccine safety before human use"),
    ("Transgenic animals in chemical safety", "Toxicity testing with more sensitive animals"),
    ("Bt cotton", "Resistant to bollworms"),
], "{}:", "Which use or technique: {}?", weight=2)
facts("b12-10", [
    "Gene therapy for ADA deficiency used lymphocytes from the patient's blood",
    "A permanent cure for ADA deficiency would involve gene transfer into early embryonic cells",
    "Bt toxin binds the insect midgut epithelial cells and creates pores",
    "Nematode-specific genes were introduced into tobacco using Agrobacterium vectors",
    "Biotechnology in agriculture includes agrochemical, organic and GM-crop approaches",
], [
    "Bt toxin kills the bacterium that produces it",
    "Gene therapy for ADA deficiency is a permanent cure in a single treatment",
    "ELISA is based on DNA hybridisation only",
    "RNA interference increases expression of the target gene",
], "Biotechnology and its Applications", weight=2)
