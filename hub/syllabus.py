"""NEET-UG syllabus map.

Units follow the NMC NEET-UG syllabus (20 Physics, 20 Chemistry, 10 Biology units).
Chapters follow the NCERT Class 11-12 books (rationalised). Chapters the NMC
removed from NEET are kept as "Beyond NEET" so no school question is lost.
Classes 1-10 form the foundation path; their chapters are the School MCQ Bank topics.
"""
import re

NEET_UNITS = {
    "Physics": [
        "Units and Measurements", "Kinematics", "Laws of Motion", "Work, Energy and Power", "Rotational Motion",
        "Gravitation", "Properties of Solids and Liquids", "Thermodynamics", "Kinetic Theory of Gases",
        "Oscillations and Waves", "Electrostatics", "Current Electricity", "Magnetic Effects of Current and Magnetism",
        "Electromagnetic Induction and Alternating Currents", "Electromagnetic Waves", "Optics",
        "Dual Nature of Matter and Radiation", "Atoms and Nuclei", "Electronic Devices", "Experimental Skills",
    ],
    "Chemistry": [
        "Some Basic Concepts in Chemistry", "Atomic Structure", "Chemical Bonding and Molecular Structure",
        "Chemical Thermodynamics", "Solutions", "Equilibrium", "Redox Reactions and Electrochemistry",
        "Chemical Kinetics", "Classification of Elements and Periodicity in Properties", "p-Block Elements",
        "d- and f-Block Elements", "Coordination Compounds", "Purification and Characterisation of Organic Compounds",
        "Some Basic Principles of Organic Chemistry", "Hydrocarbons", "Organic Compounds Containing Halogens",
        "Organic Compounds Containing Oxygen", "Organic Compounds Containing Nitrogen", "Biomolecules",
        "Principles Related to Practical Chemistry",
    ],
    "Biology": [
        "Diversity in Living World", "Structural Organisation in Animals and Plants", "Cell Structure and Function",
        "Plant Physiology", "Human Physiology", "Reproduction", "Genetics and Evolution", "Biology and Human Welfare",
        "Biotechnology and Its Applications", "Ecology and Environment",
    ],
}

# (id, class, subject, NEET unit number, NCERT chapter title, branch)
_CH = [
    ("p11-01", 11, "Physics", 1, "Units and Measurement", ""),
    ("p11-02", 11, "Physics", 2, "Motion in a Straight Line", ""),
    ("p11-03", 11, "Physics", 2, "Motion in a Plane", ""),
    ("p11-04", 11, "Physics", 3, "Laws of Motion", ""),
    ("p11-05", 11, "Physics", 4, "Work, Energy and Power", ""),
    ("p11-06", 11, "Physics", 5, "System of Particles and Rotational Motion", ""),
    ("p11-07", 11, "Physics", 6, "Gravitation", ""),
    ("p11-08", 11, "Physics", 7, "Mechanical Properties of Solids", ""),
    ("p11-09", 11, "Physics", 7, "Mechanical Properties of Fluids", ""),
    ("p11-10", 11, "Physics", 7, "Thermal Properties of Matter", ""),
    ("p11-11", 11, "Physics", 8, "Thermodynamics", ""),
    ("p11-12", 11, "Physics", 9, "Kinetic Theory", ""),
    ("p11-13", 11, "Physics", 10, "Oscillations", ""),
    ("p11-14", 11, "Physics", 10, "Waves", ""),
    ("p12-01", 12, "Physics", 11, "Electric Charges and Fields", ""),
    ("p12-02", 12, "Physics", 11, "Electrostatic Potential and Capacitance", ""),
    ("p12-03", 12, "Physics", 12, "Current Electricity", ""),
    ("p12-04", 12, "Physics", 13, "Moving Charges and Magnetism", ""),
    ("p12-05", 12, "Physics", 13, "Magnetism and Matter", ""),
    ("p12-06", 12, "Physics", 14, "Electromagnetic Induction", ""),
    ("p12-07", 12, "Physics", 14, "Alternating Current", ""),
    ("p12-08", 12, "Physics", 15, "Electromagnetic Waves", ""),
    ("p12-09", 12, "Physics", 16, "Ray Optics and Optical Instruments", ""),
    ("p12-10", 12, "Physics", 16, "Wave Optics", ""),
    ("p12-11", 12, "Physics", 17, "Dual Nature of Radiation and Matter", ""),
    ("p12-12", 12, "Physics", 18, "Atoms", ""),
    ("p12-13", 12, "Physics", 18, "Nuclei", ""),
    ("p12-14", 12, "Physics", 19, "Semiconductor Electronics", ""),
    ("p12-15", 12, "Physics", 20, "Experimental Skills", ""),

    ("c11-01", 11, "Chemistry", 1, "Some Basic Concepts of Chemistry", ""),
    ("c11-02", 11, "Chemistry", 2, "Structure of Atom", ""),
    ("c11-03", 11, "Chemistry", 9, "Classification of Elements and Periodicity in Properties", ""),
    ("c11-04", 11, "Chemistry", 3, "Chemical Bonding and Molecular Structure", ""),
    ("c11-05", 11, "Chemistry", 4, "Thermodynamics", ""),
    ("c11-06", 11, "Chemistry", 6, "Equilibrium", ""),
    ("c11-07", 11, "Chemistry", 7, "Redox Reactions", ""),
    ("c11-08", 11, "Chemistry", 14, "Organic Chemistry: Some Basic Principles and Techniques", ""),
    ("c11-09", 11, "Chemistry", 15, "Hydrocarbons", ""),
    ("c12-01", 12, "Chemistry", 5, "Solutions", ""),
    ("c12-02", 12, "Chemistry", 7, "Electrochemistry", ""),
    ("c12-03", 12, "Chemistry", 8, "Chemical Kinetics", ""),
    ("c12-pb", 12, "Chemistry", 10, "p-Block Elements (Groups 13-18)", ""),
    ("c12-04", 12, "Chemistry", 11, "The d- and f-Block Elements", ""),
    ("c12-05", 12, "Chemistry", 12, "Coordination Compounds", ""),
    ("c12-06", 12, "Chemistry", 16, "Haloalkanes and Haloarenes", ""),
    ("c12-07", 12, "Chemistry", 17, "Alcohols, Phenols and Ethers", ""),
    ("c12-08", 12, "Chemistry", 17, "Aldehydes, Ketones and Carboxylic Acids", ""),
    ("c12-09", 12, "Chemistry", 18, "Amines", ""),
    ("c12-10", 12, "Chemistry", 19, "Biomolecules", ""),
    ("c12-pr", 12, "Chemistry", 20, "Principles Related to Practical Chemistry", ""),

    ("b11-01", 11, "Biology", 1, "The Living World", "Botany"),
    ("b11-02", 11, "Biology", 1, "Biological Classification", "Botany"),
    ("b11-03", 11, "Biology", 1, "Plant Kingdom", "Botany"),
    ("b11-04", 11, "Biology", 1, "Animal Kingdom", "Zoology"),
    ("b11-05", 11, "Biology", 2, "Morphology of Flowering Plants", "Botany"),
    ("b11-06", 11, "Biology", 2, "Anatomy of Flowering Plants", "Botany"),
    ("b11-07", 11, "Biology", 2, "Structural Organisation in Animals", "Zoology"),
    ("b11-08", 11, "Biology", 3, "Cell: The Unit of Life", "Botany"),
    ("b11-09", 11, "Biology", 3, "Biomolecules", "Zoology"),
    ("b11-10", 11, "Biology", 3, "Cell Cycle and Cell Division", "Botany"),
    ("b11-11", 11, "Biology", 4, "Photosynthesis in Higher Plants", "Botany"),
    ("b11-12", 11, "Biology", 4, "Respiration in Plants", "Botany"),
    ("b11-13", 11, "Biology", 4, "Plant Growth and Development", "Botany"),
    ("b11-14", 11, "Biology", 5, "Breathing and Exchange of Gases", "Zoology"),
    ("b11-15", 11, "Biology", 5, "Body Fluids and Circulation", "Zoology"),
    ("b11-16", 11, "Biology", 5, "Excretory Products and their Elimination", "Zoology"),
    ("b11-17", 11, "Biology", 5, "Locomotion and Movement", "Zoology"),
    ("b11-18", 11, "Biology", 5, "Neural Control and Coordination", "Zoology"),
    ("b11-19", 11, "Biology", 5, "Chemical Coordination and Integration", "Zoology"),
    ("b12-01", 12, "Biology", 6, "Sexual Reproduction in Flowering Plants", "Botany"),
    ("b12-02", 12, "Biology", 6, "Human Reproduction", "Zoology"),
    ("b12-03", 12, "Biology", 6, "Reproductive Health", "Zoology"),
    ("b12-04", 12, "Biology", 7, "Principles of Inheritance and Variation", "Botany"),
    ("b12-05", 12, "Biology", 7, "Molecular Basis of Inheritance", "Botany"),
    ("b12-06", 12, "Biology", 7, "Evolution", "Zoology"),
    ("b12-07", 12, "Biology", 8, "Human Health and Disease", "Zoology"),
    ("b12-08", 12, "Biology", 8, "Microbes in Human Welfare", "Botany"),
    ("b12-09", 12, "Biology", 9, "Biotechnology: Principles and Processes", "Zoology"),
    ("b12-10", 12, "Biology", 9, "Biotechnology and its Applications", "Zoology"),
    ("b12-11", 12, "Biology", 10, "Organisms and Populations", "Botany"),
    ("b12-12", 12, "Biology", 10, "Ecosystem", "Botany"),
    ("b12-13", 12, "Biology", 10, "Biodiversity and Conservation", "Botany"),
]

# Kept for school learners; NMC removed these from NEET-UG.
_BEYOND = [
    ("c12-x1", 12, "Chemistry", "Solid State (beyond NEET)"),
    ("c12-x2", 12, "Chemistry", "Surface Chemistry (beyond NEET)"),
    ("c12-x3", 12, "Chemistry", "Isolation of Metals (beyond NEET)"),
    ("c12-x4", 12, "Chemistry", "Polymers and Chemistry in Everyday Life (beyond NEET)"),
    ("x-sci", 11, "Physics", "Scientists and Discoveries (general)"),
]

# Ecos-Synthetica creatures that teach a chapter (shown as "Play it" links).
ECOS_LINKS = {
    "b11-02": "Phages, TMV, bacteria, fungi, lichen, diatom, malaria parasite",
    "b11-04": "Honey bee, locust, aphid, mosquito, earthworm, termite, Varroa mite",
    "b11-11": "Diatom (the start of water food chains)",
    "b12-05": "CRISPR against the dairy phage",
    "b12-07": "Malaria parasite, flu, TB, strep throat, Candida, house fly",
    "b12-08": "Streptomyces, Rhizobium, mycorrhiza, Trichoderma, Bacillus",
    "b12-09": "Restriction enzymes against phage lambda",
    "b12-11": "Lichen, mycorrhiza, ladybird and aphid, Rhizobium partnerships",
    "b12-12": "Energy flow through every creature",
}

CHAPTERS = {}
for cid, cls, subj, unit, title, branch in _CH:
    CHAPTERS[cid] = dict(id=cid, cls=cls, subject=subj, unit=unit, unit_title=NEET_UNITS[subj][unit - 1],
                         title=title, branch=branch, neet=True, ecos=ECOS_LINKS.get(cid, ""))
for cid, cls, subj, title in _BEYOND:
    CHAPTERS[cid] = dict(id=cid, cls=cls, subject=subj, unit=0, unit_title="Beyond NEET", title=title,
                         branch="", neet=False, ecos="")

# ---------------------------------------------------------------- School MCQ Bank -> chapters

# Class 11-12 bank topics: a chapter id, or a list of (regex, chapter id) rules with the last entry as default.
BANK_11_12 = {
    "Heredity: Mendelian crosses": "b12-04",
    "Heredity: ratios and sex determination": "b12-04",
    "Principles of inheritance and variation": "b12-04",
    "Diversity in living organisms": [(r"bryophyt|pteridophyt|gymnosperm|angiosperm|alga|thallophyt", "b11-03"),
                                      (r"phylum|chordat|arthropod|mollus|annelid|amphibian|reptil|mammal|fish|bird|poriferan|cnidarian|platyhelminth|nematod|echinoderm|aves", "b11-04"),
                                      (r"", "b11-01")],
    "Human physiology": [(r"heart|blood|pacemaker|cardiac|lymph|donor|recipient|stroke volume", "b11-15"),
                         (r"breath|tidal|lung|emphysema|oxygen is|co2 is|alveol|respirat", "b11-14"),
                         (r"urea|excret|kidney|nephron|gout|uric", "b11-16"),
                         (r"bone|muscle|myasthenia|sarcomere|actin|myosin|joint|contractile|fibril", "b11-17"),
                         (r"neuron|nerve|membrane potential|reflex|brain|synap", "b11-18"),
                         (r"hormone|gland|diabetes|goitre|graves|addison|dwarfism|thyroid|insulin|cretin|acromegal|gigantism", "b11-19"),
                         (r"", "b11-15")],
    "Hormones and glands": "b11-19",
    "Photosynthesis and respiration in plants": [(r"glycoly|krebs|respirat|electron transport|rq|atp are produced|fermentation", "b11-12"),
                                                 (r"", "b11-11")],
    "Life processes": [(r"yeast|anaerob", "b11-12"), (r"", "b11-09")],
    "Cell division (counting cells and chromosomes)": "b11-10",
    "Cell cycle and cell division": "b11-10",
    "Chromosome numbers": "b11-10",
    "Our environment: food chains and energy flow": "b12-12",
    "Molecular basis of inheritance": "b12-05",
    "Organisms and populations": "b12-11",
    "Human health and disease": "b12-07",
    "Evolution (Hardy–Weinberg)": "b12-06",
    "Evolution": "b12-06",
    "Microbes in human welfare": "b12-08",
    "Reproduction (plants and humans)": [(r"pollinat|embryo sac|endosperm|coconut|seed|fruit|polar nuclei|apomix|parthenocarp", "b12-01"),
                                         (r"iud|contracept|test-tube|amniocent|ivf|steril", "b12-03"),
                                         (r"", "b12-02")],
    "Biotechnology: principles and applications": [(r"bt |cry|insulin|gene therapy|transgenic|rnai|elisa|biopiracy|golden rice", "b12-10"),
                                                   (r"", "b12-09")],

    "Mole concept": "c11-01", "Molarity and solution stoichiometry": "c11-01",
    "Empirical formula and percentage composition": "c11-01",
    "Gas laws": "c11-01",
    "Thermodynamics": [(r"", "c11-05")],
    "Equilibrium and pH": "c11-06",
    "Chemical bonding (hybridisation and shape)": "c11-04",
    "Redox reactions (oxidation number)": "c11-07",
    "Structure of atom (quantum numbers)": "c11-02",
    "Periodic trends and s-block": [(r"flame|plaster|washing soda|baking|sodium hydroxide|solvay|lime", "c11-03"), (r"", "c11-03")],
    "Carbon compounds: homologous series and naming": "c11-08",
    "Solutions: Raoult's law and electrochemistry calculations": [(r"cell|e°|conductiv|faraday|electrolys|nernst", "c12-02"), (r"", "c12-01")],
    "Solutions (molality and colligative properties)": "c12-01",
    "Electrochemistry": "c12-02",
    "Chemical kinetics": "c12-03",
    "Solid state: density of unit cell": "c12-x1", "Solid state (unit cells)": "c12-x1",
    "Surface chemistry": "c12-x2",
    "General principles of isolation of metals": "c12-x3",
    "Chemistry in everyday life": "c12-x4",
    "Biomolecules and polymers": [(r"polymer|polystyrene|nylon|butadiene|bakelite|teflon|pvc|rubber|terylene|dacron|monomer", "c12-x4"), (r"", "c12-10")],
    "Organic chemistry: named reactions": [(r"halide|swarts|finkelstein|wurtz|sandmeyer|haloarene|fittig", "c12-06"),
                                            (r"ether|williamson|reimer|kolbe|phenol|alcohol", "c12-07"),
                                            (r"aldehyde|ketone|cannizzaro|aldol|clemmensen|wolff|rosenmund|stephen|etard|hell", "c12-08"),
                                            (r"amine|gabriel|hofmann|carbylamine|diazo|coupling", "c12-09"),
                                            (r"", "c11-09")],
    "Haloalkanes, alcohols, aldehydes and amines": [(r"sn1|sn2|alkyl halide|ddt|chloroform|haloalk", "c12-06"),
                                                    (r"lucas|phenol|alcohol|methanol|ether", "c12-07"),
                                                    (r"fehling|tollens|iodoform|aldehyde|ketone|carboxyl", "c12-08"),
                                                    (r"hinsberg|aniline|amine", "c12-09"),
                                                    (r"", "c12-07")],
    "Coordination compounds": "c12-05",
    "p-block elements": "c12-pb",
    "d- and f-block elements": "c12-04",

    "Units and dimensions": "p11-01",
    "Vectors and projectile motion": "p11-03",
    "Circular motion and friction": [(r"friction", "p11-04"), (r"", "p11-03")],
    "Collisions and conservation of momentum": "p11-05",
    "Rotational motion": "p11-06",
    "Gravitation (orbits and escape velocity)": "p11-07",
    "Mechanical properties of solids and fluids": [(r"young|stretch|stress|strain|modulus|wire", "p11-08"), (r"", "p11-09")],
    "Thermal properties and kinetic theory": [(r"rms|ideal gas|mol of|molecul|mean free", "p11-12"), (r"", "p11-10")],
    "Oscillations and waves": [(r"wave|string|sound|beat|organ pipe|resonance column", "p11-14"), (r"", "p11-13")],
    "Electric charges and fields": "p12-01",
    "Capacitance": "p12-02",
    "Current electricity (EMF and internal resistance)": "p12-03",
    "Moving charges and magnetism": "p12-04",
    "Electromagnetic induction and AC": [(r"rms|peak|transformer|lc circuit|reactance|impedance|ac |resonan", "p12-07"), (r"", "p12-06")],
    "Electromagnetic waves": "p12-08",
    "Ray and wave optics": [(r"young|fringe|diffract|polari|slit|interfer|brewster|huygens", "p12-10"), (r"", "p12-09")],
    "Dual nature of radiation and matter": "p12-11",
    "Atoms and nuclei": [(r"orbit|bohr|hydrogen|spectral|rydberg", "p12-12"), (r"", "p12-13")],
    "Semiconductor electronics": "p12-14",
    "Scientists and discoveries": "x-sci",
}

# Classes 1-5 EVS topics -> NEET subject strand (None = not a science strand, left out of the hub).
EVS_STRAND = {
    "Animals": "Biology", "Plants": "Biology", "body": "Biology", "Food": "Biology", "Birds": "Biology",
    "Insects": "Biology", "Honeybees": "Biology", "Snakes": "Biology", "inherited": "Biology", "Seeds": "Biology",
    "Roots": "Biology", "Fruits": "Biology", "tasting": "Biology", "habits": "Biology", "Spices": "Biology",
    "senses": "Biology", "Mangoes": "Biology", "Materials": "Chemistry", "Water": "Chemistry",
    "Fuels": "Physics", "Rainbow": "Physics", "Sun, Moon": "Physics", "Earth from space": "Physics",
    "pollution": "Biology", "Natural resources": "Biology", "Amazing animals": "Biology", "Every drop": "Chemistry",
}


def evs_strand(topic):
    for key, subj in EVS_STRAND.items():
        if key.lower() in topic.lower():
            return subj
    return None


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]


def chapter_for_bank(cls, subject, topic, question):
    """Hub chapter for one School MCQ Bank question, creating foundation chapters (classes 1-10) as needed.

    Returns (chapter dict) or None when the question is not part of the science path.
    """
    if cls >= 11:
        rule = BANK_11_12.get(topic)
        if rule is None:
            return None
        if isinstance(rule, list):
            q = question.lower()
            cid = next(c for rx, c in rule if re.search(rx, q))
        else:
            cid = rule
        return CHAPTERS[cid]
    subj = subject if subject in ("Physics", "Chemistry", "Biology") else (evs_strand(topic) if subject == "EVS" else None)
    if subj is None:
        return None
    cid = f"f{cls:02d}-{subj[0].lower()}-{slug(topic)}"
    if cid not in CHAPTERS:
        CHAPTERS[cid] = dict(id=cid, cls=cls, subject=subj, unit=0, unit_title="Foundation", title=topic,
                             branch="", neet=False, ecos="")
    return CHAPTERS[cid]
