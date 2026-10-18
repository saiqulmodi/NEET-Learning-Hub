"""High-yield NEET Biology, Class 12: original questions on the topics NEET (and AIPMT before it) asks again and again.

Facts follow the NCERT Class 12 Biology textbook. Nothing is copied from past papers. Ratios and probabilities are computed.
"""
from fractions import Fraction

from .core import table, facts, groups, gen, Q, tag

tag("hy")

# ---------------------------------------------------------------- b12-01 Sexual Reproduction in Flowering Plants
table("b12-01", [
    ("Tapetum", "Nourishes the developing pollen grains"), ("Exine of pollen", "Made of sporopollenin"),
    ("Germ pore", "Region of the pollen wall without sporopollenin"), ("Filiform apparatus", "Guides the pollen tube into the synergid"),
    ("Scutellum", "Single cotyledon of a grass embryo"), ("Coleoptile", "Sheath that covers the plumule in monocots"),
    ("Perisperm", "Persistent nucellus in seeds such as black pepper"), ("Pericarp", "Wall of the fruit formed from the ovary wall"),
], "{}:", "Which structure: {}?")
groups("b12-01", {
    "haploid (n)": ["Synergid", "Egg cell", "Antipodal cell", "Pollen grain", "Megaspore"],
    "diploid (2n)": ["Zygote", "Nucellus", "Integument cell", "Megaspore mother cell", "Microspore mother cell"],
    "triploid (3n)": ["Primary endosperm nucleus", "Endosperm cell of wheat", "Coconut kernel cell"],
}, "Which of these is NOT {}?", "Which of these is {}?")
table("b12-01", [
    ("Apomixis", "Seeds formed without fertilisation"), ("Polyembryony", "More than one embryo in a seed, e.g. citrus"),
    ("Parthenocarpy", "Fruit formed without fertilisation, e.g. banana"), ("Geitonogamy", "Pollen to another flower of the same plant"),
    ("Xenogamy", "Pollen to a flower of a different plant"), ("Cleistogamy", "Flowers that never open, e.g. Commelina"),
], "{}:", "Which term: {}?")
facts("b12-01", [
    "A typical angiosperm embryo sac is 7-celled and 8-nucleate",
    "The Polygonum type embryo sac develops from one functional megaspore",
    "Pollen grains of many species stay viable for months, while rice and wheat pollen lose viability in about 30 minutes",
    "Vallisneria and Hydrilla are water-pollinated",
    "Most aquatic plants such as water hyacinth and water lily are pollinated by insects or wind",
    "In coconut the endosperm is free-nuclear (coconut water) and cellular (white kernel)",
    "Bagging and emasculation are used in artificial hybridisation",
    "The micropylar end of the embryo sac has the egg apparatus",
], [
    "A typical angiosperm embryo sac is 8-celled and 7-nucleate",
    "The endosperm of angiosperms is diploid",
    "Water hyacinth is pollinated by water",
    "Emasculation is removal of the gynoecium",
    "Antipodal cells lie at the micropylar end",
    "Cleistogamous flowers ensure cross-pollination",
    "Apomixis involves fusion of male and female gametes",
    "The tapetum lies on the outside of the anther wall",
], "reproduction in flowering plants")

# ---------------------------------------------------------------- b12-02 Human Reproduction
table("b12-02", [
    ("Sertoli cells", "Nourish developing sperm"), ("Leydig cells", "Secrete androgens"),
    ("Graafian follicle", "Mature follicle that releases the ovum"), ("Corpus luteum", "Secretes progesterone after ovulation"),
    ("Acrosome", "Contains enzymes that help sperm enter the ovum"), ("Zona pellucida", "Layer around the secondary oocyte"),
], "The role or feature of {} is:", "Which structure: {}?")
table("b12-02", [
    ("Ovulation", "About day 14 of a 28-day cycle"), ("Fertilisation", "Ampullary-isthmic junction of the oviduct"),
    ("Implantation", "Blastocyst embeds in the endometrium"), ("First heartbeat of the foetus", "End of the first month"),
    ("Limbs and digits form", "By the end of the second month"), ("Eyelids separate and eyelashes form", "By the end of the 24th week"),
], "{}:", "Which event: {}?")
facts("b12-02", [
    "Human chorionic gonadotropin, human placental lactogen and relaxin are made only during pregnancy",
    "An LH surge causes ovulation",
    "The secondary oocyte completes meiosis II only after a sperm enters it",
    "Spermiogenesis turns spermatids into sperm",
    "Spermatogenesis begins at puberty",
    "Cleavage of the zygote produces a morula of 8 to 16 cells",
    "The inner cell mass gives rise to the embryo",
    "Colostrum contains IgA antibodies",
], [
    "Oogenesis starts at puberty",
    "Fertilisation normally occurs in the uterus",
    "The trophoblast gives rise to the embryo",
    "Progesterone is secreted mainly by the Graafian follicle before ovulation",
    "Leydig cells nourish developing sperm",
    "An FSH surge causes ovulation",
    "One primary oocyte gives four functional ova",
    "Menstruation is caused by a rise in progesterone",
], "human reproduction")

# ---------------------------------------------------------------- b12-03 Reproductive Health
table("b12-03", [
    ("Lippes loop", "Non-medicated IUD"), ("Multiload 375", "Copper-releasing IUD"), ("LNG-20", "Hormone-releasing IUD"),
    ("Saheli", "Once-a-week oral contraceptive pill"), ("Vasectomy", "Surgical method in males"), ("Tubectomy", "Surgical method in females"),
], "{} is a:", "Which is a {}?")
table("b12-03", [
    ("GIFT", "Ovum placed in the fallopian tube of a female who cannot make ova"),
    ("ZIFT", "Embryo up to 8 blastomeres transferred to the fallopian tube"),
    ("IUT", "Embryo with more than 8 blastomeres transferred to the uterus"),
    ("ICSI", "Sperm injected directly into the ovum"), ("AI (IUI)", "Semen placed in the vagina or uterus"),
], "{}:", "Which assisted reproductive technology: {}?")
facts("b12-03", [
    "Amniocentesis is banned in India for sex determination",
    "MTP is relatively safe during the first trimester",
    "Lactational amenorrhoea is effective for up to six months after childbirth",
    "Barrier methods also protect against sexually transmitted infections",
    "Hepatitis B, genital herpes and HIV infections are not completely curable",
    "Saheli was developed at CDRI, Lucknow",
    "Copper IUDs suppress sperm motility and fertilising capacity",
    "Population in India was about 350 million at independence",
], [
    "MTP is safest in the third trimester",
    "Saheli is taken once a day",
    "Lactational amenorrhoea is effective for up to two years",
    "Copper IUDs work by releasing progesterone",
    "Vasectomy involves cutting the fallopian tubes",
    "Oral pills prevent STIs",
    "Amniocentesis is encouraged in India for sex determination",
    "ZIFT transfers embryos with more than 8 blastomeres to the uterus",
], "reproductive health")

# ---------------------------------------------------------------- b12-04 Principles of Inheritance and Variation
CROSSES = [
    ("Tt × Tt", "tall to dwarf", "3:1"), ("Tt × tt", "tall to dwarf", "1:1"), ("TT × tt", "tall to dwarf", "1:0 (all tall)"),
    ("RrYy × RrYy", "phenotypes", "9:3:3:1"), ("RrYy × rryy", "phenotypes", "1:1:1:1"),
    ("Rr × Rr in snapdragon (incomplete dominance)", "red : pink : white", "1:2:1"),
]


@gen("b12-04", weight=3)
def _cross(rng):
    cross, what, ratio = rng.choice(CROSSES)
    wrong = [r for _, _, r in CROSSES if r != ratio] + ["2:1", "1:2:1", "3:1"]
    return Q(f"The expected ratio of {what} in the cross {cross} is:", ratio, wrong, f"{cross} gives {ratio}.")


@gen("b12-04", weight=3)
def _prob(rng):
    """Probability of a genotype class in a multi-gene heterozygous cross (product rule)."""
    n = rng.choice([1, 2, 3, 4])
    kind = rng.choice(["recessive", "dominant", "hetero"])
    p1 = {"recessive": Fraction(1, 4), "dominant": Fraction(3, 4), "hetero": Fraction(1, 2)}[kind]
    p = p1 ** n
    genes = "".join(f"{c}{c.lower()}" for c in "ABCD"[:n])
    tgt = {"recessive": "with genotype " + "".join(c.lower() * 2 for c in "ABCD"[:n]),
           "hetero": "with genotype " + genes,
           "dominant": "showing the dominant trait for every gene"}[kind]
    pool = [Fraction(1, 4) ** n, Fraction(3, 4) ** n, Fraction(1, 2) ** n, p1 ** (n + 1), Fraction(1, 2 ** (n + 1)), Fraction(1, 16), Fraction(9, 16)]
    wrongs = [str(x) for x in dict.fromkeys(pool) if x != p]
    return Q(f"In the cross {genes} × {genes} (genes assort independently), the probability of an offspring {tgt} is:",
             str(p), wrongs, f"Each gene gives {p1}; multiply for {n} gene(s): {p}.")


table("b12-04", [
    ("Haemophilia", "Sex-linked recessive"), ("Colour blindness", "Sex-linked recessive", ["Sex-linked recessive"]),
    ("Sickle cell anaemia", "Autosomal recessive"), ("Phenylketonuria", "Autosomal recessive", ["Autosomal recessive"]),
    ("Thalassemia", "Autosomal recessive", ["Autosomal recessive"]), ("Myotonic dystrophy", "Autosomal dominant"),
    ("Down's syndrome", "Trisomy of chromosome 21"), ("Klinefelter's syndrome", "44 + XXY"), ("Turner's syndrome", "44 + XO"),
], "{} is due to / inherited as:", None, weight=2)
table("b12-04", [
    ("Grasshopper", "XO type; males have one sex chromosome"), ("Humans and Drosophila", "XY type; male heterogametic"),
    ("Birds", "ZW type; female heterogametic"), ("Honey bee", "Haplodiploid; males develop from unfertilised eggs"),
], "Sex determination in {}:", "Which organism shows: {}?")
facts("b12-04", [
    "Mendel worked with 7 pairs of contrasting characters in pea",
    "The ABO blood group gene shows multiple alleles and co-dominance",
    "Starch grain size in pea is an example of incomplete dominance at the level of the grain",
    "Morgan worked with Drosophila and showed linkage",
    "Sturtevant used recombination frequency to map genes",
    "Human skin colour is an example of polygenic inheritance",
    "Phenylketonuria is an inborn error of metabolism",
    "Sickle cell anaemia is caused by GAG changing to GUG in the beta-globin gene",
], [
    "Mendel worked with 14 pairs of contrasting characters",
    "Haemophilia is an autosomal dominant disorder",
    "In birds the male is heterogametic",
    "Down's syndrome is caused by trisomy of chromosome 18",
    "A test cross is made with the homozygous dominant parent",
    "Tightly linked genes show high recombination frequency",
    "Klinefelter's syndrome has the karyotype 44 + XO",
    "Sickle cell anaemia changes valine to glutamic acid at position 6",
], "inheritance")

# ---------------------------------------------------------------- b12-05 Molecular Basis of Inheritance
table("b12-05", [
    ("Griffith", "Transforming principle in Streptococcus pneumoniae"), ("Avery, MacLeod and McCarty", "Showed the transforming principle is DNA"),
    ("Hershey and Chase", "Showed DNA is the genetic material using bacteriophages"), ("Meselson and Stahl", "Proved semi-conservative replication using 15N"),
    ("Watson and Crick", "Double helix model of DNA"), ("Jacob and Monod", "Lac operon"), ("Chargaff", "A = T and G = C rule"),
    ("Taylor", "Semi-conservative replication in Vicia faba chromosomes"),
], "{} is known for:", "Who is known for: {}?")
facts("b12-05", [
    "The human genome has about 3 × 10^9 base pairs",
    "Less than 2% of the human genome codes for proteins",
    "Chromosome 1 has the most genes (2968) and the Y chromosome the fewest (231)",
    "DNA polymerase works only in the 5' to 3' direction",
    "Okazaki fragments are joined by DNA ligase",
    "In eukaryotes RNA polymerase II transcribes hnRNA",
    "AUG codes for methionine and is the start codon",
    "Lactose is the inducer of the lac operon",
], [
    "DNA polymerase works in the 3' to 5' direction",
    "RNA polymerase I transcribes tRNA",
    "Okazaki fragments form on the leading strand",
    "UAA codes for tryptophan",
    "The lac operon repressor is made by the z gene",
    "Over 50% of the human genome codes for proteins",
    "The Y chromosome has the most genes",
    "Hershey and Chase used 15N to label DNA",
], "molecular genetics")

# ---------------------------------------------------------------- b12-06 Evolution
table("b12-06", [
    ("Big Bang theory", "Origin of the universe"), ("Miller's experiment", "Amino acids formed from CH4, NH3, H2 and water vapour"),
    ("Industrial melanism", "Dark peppered moths increased in polluted England"), ("Darwin's finches", "Adaptive radiation on the Galapagos"),
    ("Hugo de Vries", "Mutation theory using Oenothera"), ("Lamarck", "Use and disuse of organs; giraffe neck"),
], "{}:", "What is associated with: {}?")
groups("b12-06", {
    "homologous organs (divergent evolution)": ["Thorns of Bougainvillea and tendrils of Cucurbita", "Forelimbs of whale, bat and cheetah",
                                                "Vertebrate hearts", "Vertebrate brains"],
    "analogous organs (convergent evolution)": ["Wings of butterfly and bird", "Eye of octopus and mammal", "Sweet potato and potato",
                                                "Flippers of penguin and dolphin"],
}, "Which pair is NOT an example of {}?", "Which pair is an example of {}?")
facts("b12-06", [
    "Homologous organs show divergent evolution",
    "Analogous organs show convergent evolution",
    "Australian marsupials show adaptive radiation",
    "Homo habilis was probably the first human-like being and did not eat meat",
    "Homo erectus had a brain of about 900 cc",
    "Neanderthal man had a brain of about 1400 cc and buried the dead",
    "Hardy-Weinberg equilibrium gives p² + 2pq + q² = 1",
    "Genetic drift changes allele frequencies by chance, especially in small populations",
], [
    "Homologous organs show convergent evolution",
    "Wings of birds and butterflies are homologous",
    "Homo habilis had a brain of about 1400 cc",
    "Gene flow keeps a population in Hardy-Weinberg equilibrium",
    "Darwin proposed the mutation theory",
    "Industrial melanism shows inheritance of acquired characters",
    "Natural selection acts only on acquired characters",
    "Miller used oxygen in his experimental atmosphere",
], "evolution")


@gen("b12-06", weight=2)
def _hardy(rng):
    q = rng.choice([0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9])
    p = round(1 - q, 2)
    ask = rng.choice(["het", "rec", "dom"])
    val = {"het": 2 * p * q, "rec": q * q, "dom": p * p}[ask]
    name = {"het": "heterozygotes (2pq)", "rec": "homozygous recessives (q²)", "dom": "homozygous dominants (p²)"}[ask]
    wr = [round(x, 4) for x in (2 * p * q, q * q, p * p, p * q, q, p, 2 * q) if round(x, 4) != round(val, 4)]
    return Q(f"In a population in Hardy-Weinberg equilibrium the frequency of the recessive allele is {q}. The frequency of {name} is:",
             f"{round(val, 4):g}", [f"{x:g}" for x in wr], f"p = {p}, q = {q}; {name} = {round(val, 4):g}.")


# ---------------------------------------------------------------- b12-07 Human Health and Disease
table("b12-07", [
    ("Typhoid", "Salmonella typhi"), ("Pneumonia", "Streptococcus pneumoniae"), ("Common cold", "Rhinoviruses"),
    ("Malaria", "Plasmodium"), ("Amoebiasis", "Entamoeba histolytica"), ("Ascariasis", "Ascaris"),
    ("Filariasis (elephantiasis)", "Wuchereria"), ("Ringworm", "Microsporum, Trichophyton and Epidermophyton"),
], "{} is caused by:", "{} causes which disease?")
table("b12-07", [
    ("Widal test", "Typhoid"), ("ELISA", "HIV infection"), ("Haemozoin", "Malaria chills and high fever"),
    ("Smack (brown sugar)", "Diacetylmorphine"), ("Cannabinoids", "Act on the cardiovascular system"),
    ("Cocaine", "Interferes with dopamine transport"),
], "{} is associated with:", "What is associated with {}?")
facts("b12-07", [
    "Antibodies are made by B-lymphocytes",
    "Cell-mediated immunity is due to T-lymphocytes",
    "Each antibody has two light and two heavy chains (H2L2)",
    "IgE is the antibody involved in allergy",
    "Vaccination gives active immunity",
    "Injecting preformed antibodies gives passive immunity",
    "HIV infects helper T-lymphocytes",
    "Sporozoites are the infective stage of Plasmodium injected by the female Anopheles",
], [
    "Antibodies are made by T-lymphocytes",
    "Colostrum gives active immunity",
    "Each antibody has four heavy chains and no light chains",
    "IgG is the main antibody in allergy",
    "HIV infects red blood cells",
    "Malaria is spread by the male Anopheles mosquito",
    "Typhoid is caused by a virus",
    "Thymus and bone marrow are secondary lymphoid organs",
], "health and immunity")

# ---------------------------------------------------------------- b12-08 Microbes in Human Welfare
table("b12-08", [
    ("Citric acid", "Aspergillus niger"), ("Acetic acid", "Acetobacter aceti"), ("Butyric acid", "Clostridium butylicum"),
    ("Lactic acid", "Lactobacillus"), ("Streptokinase (clot buster)", "Streptococcus"), ("Cyclosporin A", "Trichoderma polysporum"),
    ("Statins", "Monascus purpureus"), ("Penicillin", "Penicillium notatum"),
], "{} is obtained from:", "{} gives which product?")
table("b12-08", [
    ("Swiss cheese holes", "CO2 from Propionibacterium sharmanii"), ("Roquefort cheese", "Ripened by fungi"),
    ("Toddy", "Fermented palm sap"), ("Dosa and idli batter", "Fermented by bacteria"),
], "{}:", None)
facts("b12-08", [
    "Lactobacillus raises the vitamin B12 content of curd",
    "Methanogens such as Methanobacterium produce biogas",
    "Biogas is mainly methane",
    "Primary sewage treatment is physical removal of particles",
    "BOD falls as sewage is treated by aerobic microbes",
    "Bacillus thuringiensis is used to control butterfly caterpillars",
    "Glomus forms mycorrhiza and helps phosphorus uptake",
    "Baculoviruses of the genus Nucleopolyhedrovirus are species-specific biocontrol agents",
], [
    "Biogas is mainly carbon dioxide",
    "Penicillin was discovered by Waksman",
    "Activated sludge contains mainly algae",
    "High BOD means water is clean",
    "Streptokinase is made by Trichoderma",
    "Swiss cheese holes come from oxygen",
    "Statins raise blood cholesterol",
    "Cyclosporin A is an antibiotic used against tuberculosis",
], "microbes in human welfare")

# ---------------------------------------------------------------- b12-09 Biotechnology: Principles and Processes
table("b12-09", [
    ("EcoRI", "Restriction endonuclease from Escherichia coli RY13"), ("DNA ligase", "Joins DNA fragments"),
    ("Taq polymerase", "Heat-stable polymerase from Thermus aquaticus"), ("Lysozyme", "Breaks bacterial cell walls"),
    ("Chitinase", "Breaks fungal cell walls"), ("Cellulase", "Breaks plant cell walls"),
], "{}:", "Which enzyme: {}?")
table("b12-09", [
    ("ori", "Where replication starts"), ("rop", "Codes for proteins in plasmid replication"),
    ("ampR and tetR", "Selectable markers"), ("BamHI site in tetR", "Insertional inactivation of tetracycline resistance"),
], "In pBR322, {}:", "Which part of pBR322: {}?")
facts("b12-09", [
    "Restriction enzymes cut DNA at palindromic sequences",
    "The first recombinant DNA was made by Cohen and Boyer in 1972",
    "DNA is separated by gel electrophoresis according to size",
    "DNA fragments move towards the anode in gel electrophoresis",
    "Ethidium bromide makes DNA glow orange under UV light",
    "PCR needs denaturation, annealing and extension",
    "Blue-white selection uses insertional inactivation of beta-galactosidase",
    "Agrobacterium tumefaciens transfers T-DNA into plant cells",
], [
    "Smaller DNA fragments move more slowly in a gel",
    "DNA moves towards the cathode in gel electrophoresis",
    "In blue-white screening, blue colonies carry the insert",
    "Taq polymerase is from Escherichia coli",
    "Restriction enzymes join DNA fragments",
    "PCR is used to cut DNA at specific sites",
    "Lysozyme is used to break fungal cell walls",
    "The Ti plasmid comes from Agrobacterium rhizogenes",
], "biotechnology tools")

# ---------------------------------------------------------------- b12-10 Biotechnology and its Applications
table("b12-10", [
    ("cryIAc and cryIIAb", "Control the cotton bollworm"), ("cryIAb", "Controls the corn borer"),
    ("RNA interference", "Protects tobacco from Meloidogyne incognita"), ("Golden rice", "Rich in beta-carotene (vitamin A)"),
    ("Rosie the cow", "Milk with human alpha-lactalbumin"), ("ADA deficiency", "First clinical gene therapy, 1990"),
], "{}:", "Which application: {}?")
facts("b12-10", [
    "Bt toxin is an inactive protoxin that becomes active in the alkaline insect gut",
    "Eli Lilly made human insulin by producing chains A and B separately in E. coli",
    "Human insulin has two polypeptide chains linked by disulphide bridges",
    "GEAC is the Indian body that decides on GM research and release",
    "Biopiracy includes use of bio-resources without authorisation or compensation",
    "Basmati rice is an example of a patent dispute over Indian varieties",
    "The first transgenic cow was Rosie",
    "ELISA detects an infection by antigen-antibody interaction",
], [
    "Bt toxin is active inside the bacterium",
    "Human insulin is a single polypeptide chain",
    "Golden rice is rich in vitamin C",
    "RNAi protects plants by adding more mRNA",
    "Insulin is made from the proinsulin of cows only",
    "Gene therapy was first used for haemophilia",
    "GEAC regulates only drug prices",
    "Bt cotton resists all insects including aphids",
], "biotechnology applications")

# ---------------------------------------------------------------- b12-11 Organisms and Populations
table("b12-11", [
    ("Mutualism", "+ / +"), ("Competition", "- / -"), ("Predation", "+ / -"), ("Commensalism", "+ / 0"), ("Amensalism", "- / 0"),
], "The sign of interaction in {} is:", "Which interaction is {}?")
table("b12-11", [
    ("Orchid on a mango branch", "Commensalism"), ("Barnacles on a whale", "Commensalism", ["Commensalism"]),
    ("Lichen", "Mutualism"), ("Fig and fig wasp", "Mutualism", ["Mutualism"]), ("Cuscuta on a host plant", "Parasitism"),
    ("Abingdon tortoise and goats on Galapagos", "Competition"), ("Cuckoo laying eggs in a crow's nest", "Brood parasitism"),
], "{} is an example of:", None)
facts("b12-11", [
    "Exponential growth gives a J-shaped curve",
    "Logistic growth gives an S-shaped (sigmoid) curve",
    "The carrying capacity is K",
    "Gause's principle says two closely related species competing for the same resource cannot co-exist indefinitely",
    "Mediterranean orchid Ophrys uses sexual deceit to get pollinated",
    "An expanding population has a triangular age pyramid",
    "Natality and immigration increase population density",
    "Allen's rule says mammals from colder climates have shorter ears and limbs",
], [
    "Logistic growth gives a J-shaped curve",
    "Mortality and immigration decrease population density",
    "An expanding population has an urn-shaped age pyramid",
    "Mutualism harms both species",
    "Commensalism benefits both species",
    "Allen's rule says mammals from colder climates have longer ears",
    "The intrinsic rate of increase is K",
    "Predators always drive their prey to extinction",
], "populations and interactions")

# ---------------------------------------------------------------- b12-12 Ecosystem
facts("b12-12", [
    "Only about 10% of energy passes from one trophic level to the next (Lindeman)",
    "Plants capture only 2-10% of photosynthetically active radiation",
    "PAR is about 50% of incident solar radiation",
    "Net primary productivity = gross primary productivity - respiration losses",
    "Detritus food chains carry more energy than grazing food chains in a terrestrial ecosystem",
    "Hydrarch succession starts in water and ends in a mesic forest",
    "The phosphorus cycle has no significant atmospheric phase",
    "Lichens are pioneer species on bare rock",
], [
    "About 50% of energy passes from one trophic level to the next",
    "The pyramid of energy can be inverted",
    "The phosphorus cycle has a large gaseous reservoir in the atmosphere",
    "Decomposers occupy the first trophic level",
    "Gross primary productivity is lower than net primary productivity",
    "Mosses are pioneer species on bare rock",
    "Climax communities change faster than pioneer communities",
    "Humification increases the rate of decomposition",
], "ecosystems")

# ---------------------------------------------------------------- b12-13 Biodiversity and Conservation
table("b12-13", [
    ("Dodo", "Mauritius"), ("Quagga", "Africa"), ("Steller's sea cow", "Russia"), ("Thylacine", "Australia"),
], "The extinct {} lived in:", "Which extinct animal lived in {}?")
table("b12-13", [
    ("Species-area relationship", "Alexander von Humboldt"), ("Rivet popper hypothesis", "Paul Ehrlich"),
    ("Long-term ecosystem experiments on biodiversity and productivity", "David Tilman"), ("Estimate of 7 million species", "Robert May"),
], "{}:", "Who is associated with: {}?")
facts("b12-13", [
    "India has about 8.1% of the world's species with 2.4% of the land area",
    "The Amazon rain forest is called the lungs of the planet",
    "Habitat loss is the main cause of biodiversity loss",
    "Nile perch in Lake Victoria led to the extinction of many cichlid fish",
    "Sacred groves are an in situ form of conservation",
    "Zoos, botanical gardens and seed banks are ex situ conservation",
    "Biodiversity hot spots cover less than 2% of Earth's land area",
    "The Earth Summit was held in Rio de Janeiro in 1992",
], [
    "Seed banks are an in situ form of conservation",
    "Sacred groves are ex situ conservation",
    "Biodiversity decreases from the poles towards the equator",
    "Over-exploitation is the main cause of biodiversity loss",
    "India has about 25% of the world's species",
    "The Earth Summit was held in Johannesburg in 1992",
    "Lantana and water hyacinth are endemic Indian species",
    "In the species-area relation, Z is much larger for small areas than for whole continents",
], "biodiversity")

groups("b12-13", {
    "in situ conservation": ["Sacred groves", "Wildlife sanctuaries", "Biosphere reserves", "National parks"],
    "ex situ conservation": ["Zoological parks", "Botanical gardens", "Seed banks", "Cryopreservation of gametes"],
}, "Which is NOT an example of {}?", "Which is an example of {}?")

# ---------------------------------------------------------------- more for the thinner chapters
table("b12-12", [
    ("Pioneer species of xerarch succession", "Lichens"), ("Pioneer species of hydrarch succession", "Phytoplankton"),
    ("Final stable community", "Climax community"), ("Series of communities at one place", "Sere"),
    ("Remains of dead plants and animals", "Detritus"), ("Dark amorphous substance resistant to microbes", "Humus"),
], "{}:", "What is {}?")
table("b12-12", [
    ("Fragmentation", "Detritivores break detritus into smaller particles"), ("Leaching", "Water-soluble nutrients move down into the soil"),
    ("Catabolism", "Bacterial and fungal enzymes degrade detritus"), ("Humification", "Formation of humus"),
    ("Mineralisation", "Release of inorganic nutrients from humus"),
], "In decomposition, {} is:", "Which step of decomposition: {}?")
facts("b12-12", [
    "Decomposition is faster in warm, moist conditions",
    "Decomposition slows down in detritus rich in lignin and chitin",
    "The standing crop is the mass of living material at a time",
    "Productivity of the oceans is low per unit area",
    "Primary productivity depends on the plant species and environmental factors",
    "Ecological pyramids do not include saprophytes",
], [
    "Decomposition is faster in cold, dry conditions",
    "Detritus rich in nitrogen decomposes slowly",
    "Ecological pyramids include saprophytes",
    "Standing crop is the energy lost as heat",
    "Oceans have the highest productivity per unit area",
    "Secondary productivity is the rate of photosynthesis",
], "decomposition and productivity")

table("b12-10", [
    ("Bt", "Bacillus thuringiensis"), ("ADA", "Adenosine deaminase"), ("GEAC", "Genetic Engineering Appraisal Committee"),
    ("ELISA", "Enzyme Linked Immuno-Sorbent Assay"), ("PCR", "Polymerase Chain Reaction"), ("RNAi", "RNA interference"),
], "{} stands for:", "What is the short form of {}?")

table("b12-05", [
    ("UAA, UAG and UGA", "Stop codons"), ("AUG", "Start codon for methionine"), ("Sigma factor", "Helps RNA polymerase start transcription"),
    ("Rho factor", "Helps end transcription in bacteria"), ("Capping and tailing", "Processing of hnRNA in eukaryotes"),
    ("Splicing", "Removes introns and joins exons"), ("Histone octamer with DNA", "Nucleosome"),
], "{}:", "What is: {}?")

table("b12-07", [
    ("Primary lymphoid organs", "Bone marrow and thymus"), ("Secondary lymphoid organs", "Spleen, lymph nodes, tonsils, Peyer's patches"),
    ("Physical barrier of innate immunity", "Skin and mucus coating"), ("Cytokine barrier", "Interferons from virus-infected cells"),
    ("Cellular barrier", "Neutrophils, monocytes, natural killer cells and macrophages"), ("Physiological barrier", "Stomach acid, saliva and tears"),
], "{}:", "Which is: {}?")

table("b12-08", [
    ("Sewage treatment primary sludge", "Settles out during primary treatment"), ("Floc", "Bacteria held together with fungal filaments"),
    ("Activated sludge", "Sediment of flocs used as inoculum"), ("Anaerobic sludge digester", "Bacteria digest sludge and make biogas"),
], "{}:", "Which term: {}?")

table("b12-09", [
    ("Bacterial transformation using calcium", "Makes cells competent to take up DNA"), ("Microinjection", "DNA injected directly into the nucleus of an animal cell"),
    ("Biolistics (gene gun)", "Gold or tungsten particles coated with DNA fired into plant cells"), ("Disarmed pathogen vector", "Delivers genes without causing disease"),
    ("Downstream processing", "Separation and purification of the product"), ("Bioreactor", "Large vessel for growing cells to make products"),
], "{}:", "Which method or term: {}?")

facts("b12-11", [
    "Kangaroo rat can meet its water needs through metabolic water",
    "Desert plants often have CAM photosynthesis",
    "Altitude sickness is due to low partial pressure of oxygen",
    "Nearly all plants and about 99% of animals are conformers",
    "Prickly pear cactus in Australia was controlled by a moth that feeds on it",
    "Monarch butterflies are distasteful to predators because of a chemical from their food plant",
], [
    "Kangaroo rats drink large amounts of water daily",
    "Altitude sickness is due to high oxygen pressure",
    "All animals regulate their body temperature",
    "Cacti have broad leaves to reduce water loss",
    "Monarch butterflies make their toxin from scratch",
    "Prickly pear in Australia was controlled by a virus",
], "organisms and the environment")

tag(None)
