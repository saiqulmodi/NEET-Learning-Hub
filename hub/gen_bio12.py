"""NEET Biology, Class 12 (NCERT rationalised). Fact tables, statements and computed questions."""
import math

from .core import table, groups, facts, gen, num_q, Q, sig, sci

# ---------------------------------------------------------------- b12-01 Sexual Reproduction in Flowering Plants
table("b12-01", [
    ("Tapetum", "Innermost wall layer of the microsporangium that nourishes developing pollen"),
    ("Exine", "Outer pollen wall made of sporopollenin, the most resistant organic material known"),
    ("Germ pores", "Gaps in the exine where sporopollenin is absent"),
    ("Filiform apparatus", "Cellular thickenings at the micropylar tip of synergids that guide pollen tubes"),
    ("Funicle", "Stalk that attaches the ovule to the placenta"),
    ("Chalaza", "Basal part of the ovule, opposite the micropyle"),
    ("Scutellum", "The single cotyledon of a grass embryo"),
    ("Coleoptile", "Hollow foliar structure enclosing the plumule in monocots"),
    ("Coleorhiza", "Sheath enclosing the radicle in monocots"),
    ("Perisperm", "Persistent residual nucellus in some seeds"),
], "Which description fits {}?", "Which structure is: {}?", weight=2)
table("b12-01", [
    ("Coconut water", "Free-nuclear endosperm"), ("White kernel of coconut", "Cellular endosperm"),
    ("Pea, groundnut and beans", "Non-albuminous seeds"), ("Wheat, maize, barley and castor", "Albuminous seeds"),
    ("Black pepper and beet", "Seeds with perisperm"), ("Apple, strawberry and cashew", "False fruits developing from the thalamus"),
    ("Banana", "Parthenocarpic fruit"), ("Citrus and mango", "Polyembryony"),
    ("Viola, Oxalis and Commelina", "Cleistogamous flowers"), ("Vallisneria and Hydrilla", "Water pollination"),
    ("Zostera", "Marine water-pollinated sea grass"), ("Castor and maize", "Monoecious plants"),
    ("Papaya", "Dioecious plant"), ("Amorphophallus", "Very tall flower (about 6 feet)"),
], "{} is an example of:", "Which is an example of {}?", weight=3)
table("b12-01", [
    ("Autogamy", "Pollen transfer to the stigma of the same flower"),
    ("Geitonogamy", "Pollen transfer to another flower of the same plant"),
    ("Xenogamy", "Pollen transfer to a flower of a different plant"),
    ("Apomixis", "Seed formation without fertilisation"),
    ("Syngamy", "Fusion of a male gamete with the egg"),
    ("Triple fusion", "Fusion of a male gamete with the two polar nuclei"),
], "{} is:", "Which term means: {}?")
facts("b12-01", [
    "A typical angiosperm embryo sac is 7-celled and 8-nucleate",
    "The egg apparatus has two synergids and one egg cell",
    "The primary endosperm nucleus is triploid",
    "Pollen grains of rice and wheat lose viability within about 30 minutes",
    "Pollen can be stored for years in liquid nitrogen at -196 °C",
    "Most monocot and dicot ovules develop the embryo sac by the monosporic (Polygonum) method",
    "Emasculation and bagging are used in artificial hybridisation",
    "Seeds of a date palm about 2000 years old have germinated",
], [
    "The primary endosperm nucleus is diploid",
    "The embryo sac has three synergids",
    "Geitonogamy is genetically the same as cross-pollination",
    "Coconut water is cellular endosperm",
    "Pea seeds are albuminous",
    "Exine is made of cellulose and pectin",
], "Sexual Reproduction in Flowering Plants", weight=2)

# ---------------------------------------------------------------- b12-02 Human Reproduction
table("b12-02", [
    ("Sertoli cells", "Nourish developing sperm in the seminiferous tubules"),
    ("Leydig cells", "Secrete androgens such as testosterone"),
    ("Acrosome", "Cap on the sperm head with enzymes for fertilisation"),
    ("Middle piece of sperm", "Contains mitochondria that power sperm movement"),
    ("Graafian follicle", "Mature follicle that releases the secondary oocyte"),
    ("Corpus luteum", "Secretes progesterone after ovulation"),
    ("Zona pellucida", "Layer around the ovum that blocks extra sperm after fertilisation"),
    ("Trophoblast", "Outer layer of the blastocyst that attaches to the endometrium"),
    ("Inner cell mass", "Cells of the blastocyst that become the embryo"),
    ("Colostrum", "First milk, rich in IgA antibodies"),
], "The role of {} is:", "Which cell or structure: {}?", weight=2)
table("b12-02", [
    ("Fertilisation", "Ampullary region of the fallopian tube"), ("Implantation", "Endometrium of the uterus"),
    ("Spermatogenesis", "Seminiferous tubules"), ("Sperm storage and maturation", "Epididymis"),
], "Where does {} occur?", None)
table("b12-02", [
    ("Heart forms", "After one month of pregnancy"),
    ("Limbs and digits develop", "By the end of the second month"),
    ("Major organs form, external genitalia well developed", "By the end of the first trimester"),
    ("First movements of the foetus and hair on the head", "During the fifth month"),
    ("Body covered with fine hair, eyelids separate", "By the end of the second trimester (about 24 weeks)"),
], "{}:", None)
table("b12-02", [
    ("hCG", "Placenta"), ("hPL", "Placenta"), ("Relaxin", "Ovary in late pregnancy"),
    ("LH surge", "Anterior pituitary, causing ovulation"), ("Oxytocin during parturition", "Posterior pituitary"),
], "{} comes from:", None)
facts("b12-02", [
    "A human male ejaculates 200-300 million sperm",
    "At least 60 per cent of sperm should have normal shape and 40 per cent vigorous motility for normal fertility",
    "Oogonia are formed during foetal life; no new ones form after birth",
    "Primary oocytes are arrested in prophase I of meiosis",
    "About 60,000-80,000 primary follicles remain in each ovary at puberty",
    "The average menstrual cycle is 28-29 days",
    "Ovulation is triggered by an LH surge",
    "The embryo with 8-16 blastomeres is called a morula",
    "Parturition is triggered by the foetal ejection reflex",
], [
    "Oogonia are formed throughout a woman's life",
    "Fertilisation normally takes place in the uterus",
    "The corpus luteum secretes LH",
    "Sertoli cells secrete testosterone",
    "Menstruation occurs when the egg is fertilised",
    "The placenta does not secrete hormones",
], "Human Reproduction", weight=2)

# ---------------------------------------------------------------- b12-03 Reproductive Health
table("b12-03", [
    ("Lippes loop", "Non-medicated IUD"), ("CuT, Cu7 and Multiload 375", "Copper-releasing IUDs"),
    ("Progestasert and LNG-20", "Hormone-releasing IUDs"), ("Saheli", "Once-a-week non-steroidal oral pill"),
    ("Vasectomy", "Cutting and tying the vas deferens"), ("Tubectomy", "Cutting and tying the fallopian tubes"),
    ("Lactational amenorrhea", "Natural method effective up to six months after childbirth"),
    ("Diaphragms, cervical caps and vaults", "Barrier methods for females"),
], "{}:", "Which contraceptive or method is: {}?", weight=2)
table("b12-03", [
    ("ZIFT", "Zygote or early embryo (up to 8 blastomeres) placed in the fallopian tube"),
    ("IUT", "Embryo with more than 8 blastomeres placed in the uterus"),
    ("GIFT", "Ovum from a donor placed in the fallopian tube of a female who cannot produce ova"),
    ("ICSI", "Sperm injected directly into the ovum"),
    ("IUI (artificial insemination)", "Semen placed in the vagina or uterus"),
], "{} means:", "Which technique: {}?")
facts("b12-03", [
    "Saheli was developed at CDRI, Lucknow",
    "Emergency contraceptives are effective within 72 hours of unprotected intercourse",
    "MTPs are relatively safe during the first trimester (up to 12 weeks)",
    "Hepatitis B, genital herpes and HIV infections are not completely curable",
    "Amniocentesis is banned in India for sex determination",
    "India's population was about 350 million at the time of independence",
    "Copper ions suppress sperm motility and fertilising capacity",
], [
    "Vasectomy involves cutting the fallopian tubes",
    "Saheli has to be taken daily",
    "Lactational amenorrhea works for two years after childbirth",
    "All sexually transmitted infections can be completely cured",
    "MTP is safest in the third trimester",
    "Lippes loop releases hormones",
], "Reproductive Health", weight=2)

# ---------------------------------------------------------------- b12-04 Principles of Inheritance
table("b12-04", [
    ("Stem height", "Tall"), ("Flower colour", "Violet"), ("Flower position", "Axial"), ("Pod shape", "Inflated"),
    ("Pod colour", "Green"), ("Seed shape", "Round"), ("Seed colour", "Yellow"),
], "In Mendel's peas, the dominant form of {} is:", "Which trait has '{}' as its dominant form?")
table("b12-04", [
    ("Haemophilia", "X-linked recessive"), ("Colour blindness", "X-linked recessive"),
    ("Sickle cell anaemia", "Autosomal recessive"), ("Phenylketonuria", "Autosomal recessive"),
    ("Thalassemia", "Autosomal recessive"), ("Myotonic dystrophy", "Autosomal dominant"),
], "{} is inherited as:", None)
table("b12-04", [
    ("Down's syndrome", "Trisomy of chromosome 21"), ("Klinefelter's syndrome", "47, XXY"),
    ("Turner's syndrome", "45, XO"),
], "{} is due to:", "Which syndrome is due to {}?")
table("b12-04", [
    ("Grasshopper", "XX-XO type"), ("Humans and Drosophila", "XX-XY type"), ("Birds", "ZW-ZZ type (female heterogametic)"),
    ("Honey bee", "Haplodiploidy (males from unfertilised eggs)"),
], "Sex determination in {} is:", "Which organism shows {} sex determination?")
table("b12-04", [
    ("Incomplete dominance", "Flower colour in snapdragon (Antirrhinum)"), ("Codominance", "AB blood group"),
    ("Pleiotropy", "Phenylketonuria, where one gene causes many effects"), ("Polygenic inheritance", "Human skin colour"),
    ("Linkage", "Studied by Morgan in Drosophila"), ("Chromosomal theory of inheritance", "Sutton and Boveri"),
], "An example or name linked with {} is:", "Which concept is linked with: {}?")
facts("b12-04", [
    "In sickle cell anaemia glutamic acid is replaced by valine at the sixth position of the beta-globin chain",
    "Alpha thalassemia is controlled by genes on chromosome 16",
    "Beta thalassemia is controlled by a gene on chromosome 11",
    "The ABO blood group gene has three alleles: IA, IB and i",
    "A test cross is a cross with the homozygous recessive parent",
    "Sturtevant used recombination frequency to map genes on chromosomes",
], [
    "Haemophilia is autosomal dominant",
    "Turner's syndrome has an extra X chromosome",
    "In birds the male is the heterogametic sex",
    "Down's syndrome is due to trisomy of chromosome 18",
    "A test cross is made with the homozygous dominant parent",
    "Colour blindness is more common in females",
], "Principles of Inheritance and Variation", weight=2)


@gen("b12-04", weight=2)
def _ratio(rng):
    kind = rng.choice(["monohybrid F2 phenotypic", "monohybrid F2 genotypic", "dihybrid F2 phenotypic",
                       "monohybrid test cross", "dihybrid test cross", "incomplete dominance F2"])
    ans = {"monohybrid F2 phenotypic": "3 : 1", "monohybrid F2 genotypic": "1 : 2 : 1",
           "dihybrid F2 phenotypic": "9 : 3 : 3 : 1", "monohybrid test cross": "1 : 1",
           "dihybrid test cross": "1 : 1 : 1 : 1", "incomplete dominance F2": "1 : 2 : 1"}[kind]
    pool = ["3 : 1", "1 : 2 : 1", "9 : 3 : 3 : 1", "1 : 1", "1 : 1 : 1 : 1", "9 : 7", "15 : 1"]
    return Q(f"The {kind} ratio is:", ans, [p for p in pool if p != ans], f"{kind}: {ans}.")


# ---------------------------------------------------------------- b12-05 Molecular Basis of Inheritance
table("b12-05", [
    ("Transformation in Streptococcus pneumoniae using mice", "Frederick Griffith"),
    ("DNA is the transforming principle", "Avery, MacLeod and McCarty"),
    ("DNA is the genetic material, using radioactive bacteriophages", "Hershey and Chase"),
    ("Semiconservative DNA replication in E. coli using 15N", "Meselson and Stahl"),
    ("Semiconservative replication in Vicia faba using radioactive thymidine", "Taylor and colleagues"),
    ("Double helix model of DNA (1953)", "Watson and Crick"),
    ("X-ray diffraction data of DNA", "Wilkins and Franklin"),
    ("A = T and G = C in double-stranded DNA", "Erwin Chargaff"),
    ("Lac operon", "Jacob and Monod"),
    ("DNA fingerprinting", "Alec Jeffreys"),
    ("Chemical method to synthesise RNA with defined bases", "Har Gobind Khorana"),
], "{}:", "What is {} known for?", weight=2)
table("b12-05", [
    ("RNA polymerase I", "rRNAs (28S, 18S and 5.8S)"), ("RNA polymerase II", "hnRNA, the precursor of mRNA"),
    ("RNA polymerase III", "tRNA, 5S rRNA and snRNAs"),
], "In eukaryotes, {} transcribes:", "Which enzyme transcribes {}?")
table("b12-05", [
    ("i gene of lac operon", "Codes for the repressor"), ("z gene", "Codes for beta-galactosidase"),
    ("y gene", "Codes for permease"), ("a gene", "Codes for transacetylase"),
    ("Lactose (allolactose)", "Inducer of the lac operon"),
], "{}:", "Which part of the lac operon: {}?")
table("b12-05", [
    ("Start codon", "AUG (methionine)"), ("Stop codons", "UAA, UAG and UGA"),
    ("Number of codons", "64"), ("Codons that code for amino acids", "61"),
], "{}:", None)
facts("b12-05", [
    "DNA polymerase adds nucleotides only in the 5' to 3' direction",
    "Okazaki fragments are joined by DNA ligase",
    "Introns are removed by splicing",
    "Capping adds methyl guanosine triphosphate to the 5' end of hnRNA",
    "Tailing adds 200-300 adenylate residues to the 3' end",
    "Euchromatin is loosely packed and transcriptionally active",
    "A nucleosome contains about 200 bp of DNA wrapped around a histone octamer",
    "The genetic code is degenerate, unambiguous and nearly universal",
    "Less than 2 per cent of the human genome codes for proteins",
    "Chromosome 1 has the most genes and the Y chromosome the fewest",
], [
    "DNA polymerase adds nucleotides in the 3' to 5' direction",
    "Heterochromatin is transcriptionally active",
    "UAG codes for methionine",
    "Exons are removed by splicing",
    "In the lac operon, lactose acts as the repressor",
    "Histones are negatively charged proteins",
], "Molecular Basis of Inheritance", weight=2)


@gen("b12-05", weight=2)
def _dna_length(rng):
    bp = rng.choice([1e6, 4.6e6, 2e7, 6.6e9, 5e5, 48502, 3e8])
    length_m = bp * 0.34e-9
    return num_q(rng, f"A DNA double helix has {sig(bp)} base pairs. Its length (distance 0.34 nm between base pairs) is:",
                 length_m, " m", f"Length = {sig(bp)} × 0.34 × 10^-9 m.", form=sci)


@gen("b12-05", weight=2)
def _hbonds(rng):
    bp = rng.choice([100, 200, 500, 1000, 2000])
    at_pct = rng.choice([20, 30, 40, 60])
    at_pairs = bp * at_pct // 100
    gc_pairs = bp - at_pairs
    hb = 2 * at_pairs + 3 * gc_pairs
    return num_q(rng, f"A DNA segment has {bp} base pairs, and {at_pct}% of its base pairs are A-T. How many hydrogen bonds hold the strands together?",
                 hb, explanation=f"A-T pairs = {at_pairs} (2 bonds each), G-C pairs = {gc_pairs} (3 bonds each).",
                 form=lambda x: str(int(round(x))), wrongs=[2 * bp, 3 * bp, 3 * at_pairs + 2 * gc_pairs])


@gen("b12-05", weight=2)
def _mrna(rng):
    bases = "ATGC"
    seq = "".join(rng.choice(bases) for _ in range(9))
    comp = {"A": "U", "T": "A", "G": "C", "C": "G"}
    mrna = "".join(comp[b] for b in seq)
    wrong_dna = "".join({"A": "T", "T": "A", "G": "C", "C": "G"}[b] for b in seq)
    same = seq.replace("T", "U")
    rev = mrna[::-1]
    return Q(f"The template strand of DNA reads 3'-{seq}-5'. The mRNA transcribed from it reads 5'-...-3':",
             mrna, [wrong_dna, same, rev], "mRNA is complementary to the template, with U in place of T.")


@gen("b12-05")
def _codons(rng):
    aa = rng.choice([50, 100, 146, 200, 300])
    return num_q(rng, f"A protein has {aa} amino acids. How many nucleotides (excluding the stop codon) code for it?",
                 3 * aa, form=lambda x: str(int(x)), wrongs=[aa, 2 * aa, 3 * aa + 3],
                 explanation="Each amino acid is coded by a triplet codon.")


# ---------------------------------------------------------------- b12-06 Evolution
table("b12-06", [
    ("Homologous organs (divergent evolution)", "Forelimbs of whales, bats, cheetahs and humans"),
    ("Analogous organs (convergent evolution)", "Wings of a butterfly and a bird"),
    ("Homologous structures in plants", "Thorns of Bougainvillea and tendrils of Cucurbita"),
    ("Analogous structures in plants", "Sweet potato (root) and potato (stem)"),
    ("Adaptive radiation", "Darwin's finches of the Galapagos Islands"),
    ("Industrial melanism", "Dark peppered moths in polluted England"),
    ("Founder effect", "A small group that settles a new place changes allele frequencies"),
], "An example of {} is:", "{} is an example of:", weight=2)
table("b12-06", [
    ("Spontaneous generation disproved with flask experiments", "Louis Pasteur"),
    ("Simulated early Earth to make amino acids (1953)", "S.L. Miller"),
    ("Chemical origin of life proposed", "Oparin and Haldane"),
    ("Mutation theory using evening primrose (Oenothera)", "Hugo de Vries"),
    ("Inheritance of acquired characters (use and disuse)", "Lamarck"),
    ("Natural selection", "Charles Darwin and Alfred Wallace"),
], "{}:", "What is {} known for?")
table("b12-06", [
    ("Homo habilis", "Brain 650-800 cc; probably did not eat meat"),
    ("Homo erectus", "Brain about 900 cc; probably ate meat; about 1.5 million years ago"),
    ("Neanderthal man", "Brain 1400 cc; buried the dead; 100,000-40,000 years ago"),
    ("Australopithecines", "Lived in East African grasslands about 2 million years ago"),
    ("Dryopithecus and Ramapithecus", "Primates of about 15 million years ago"),
], "{}:", "Which human ancestor fits: {}?")
facts("b12-06", [
    "Miller used CH4, H2, NH3 and water vapour at 800 °C with electric discharge",
    "The coelacanth, thought extinct, was caught in South Africa in 1938",
    "Dinosaurs disappeared about 65 million years ago",
    "Gene flow, genetic drift, mutation, recombination and natural selection change allele frequencies",
    "Natural selection can be stabilising, directional or disruptive",
    "Agriculture began about 10,000 years ago",
    "Prehistoric cave art was made about 18,000 years ago",
], [
    "Analogous organs show common ancestry",
    "Hugo de Vries worked on Drosophila",
    "Homo erectus had a brain of about 1400 cc",
    "In Hardy-Weinberg equilibrium, allele frequencies change every generation",
    "Darwin's finches are an example of convergent evolution",
    "Miller's experiment produced complete living cells",
], "Evolution", weight=2)


@gen("b12-06", weight=2)
def _hw(rng):
    q = rng.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    p = round(1 - q, 2)
    ask = rng.choice(["heterozygotes (2pq)", "homozygous dominant (p²)", "homozygous recessive (q²)"])
    val = {"heterozygotes (2pq)": 2 * p * q, "homozygous dominant (p²)": p * p, "homozygous recessive (q²)": q * q}[ask]
    return num_q(rng, f"In a population in Hardy-Weinberg equilibrium, the recessive allele frequency q = {q}. The frequency of {ask} is:",
                 val, explanation=f"p = {p}; p² + 2pq + q² = 1.", form=lambda x: f"{x:.2f}",
                 wrongs=[p * q, 2 * p * q, p * p, q * q, p, q])


# ---------------------------------------------------------------- b12-07 Human Health and Disease
table("b12-07", [
    ("Typhoid", "Salmonella typhi"), ("Pneumonia", "Streptococcus pneumoniae and Haemophilus influenzae"),
    ("Common cold", "Rhinoviruses"), ("Malignant malaria", "Plasmodium falciparum"),
    ("Amoebiasis", "Entamoeba histolytica"), ("Ascariasis", "Ascaris"),
    ("Filariasis (elephantiasis)", "Wuchereria bancrofti and W. malayi"),
    ("Ringworm", "Microsporum, Trichophyton and Epidermophyton"), ("AIDS", "HIV, a retrovirus"),
], "{} is caused by:", "Which disease is caused by {}?", weight=3)
table("b12-07", [
    ("Malaria", "Female Anopheles mosquito"), ("Filariasis", "Female Culex mosquito"),
    ("Dengue and chikungunya", "Aedes mosquito"), ("Amoebiasis (mechanical carrier)", "Housefly"),
], "The vector of {} is:", "Which disease is spread by the {}?")
table("b12-07", [
    ("Typhoid", "Widal test"), ("AIDS", "ELISA"), ("Cancer", "Biopsy and histopathology"),
], "{} is confirmed by:", "Which disease is confirmed by {}?")
table("b12-07", [
    ("Haemozoin", "Toxin released by Plasmodium causing chills and high fever"),
    ("Sporozoites", "Infectious stage of Plasmodium injected by the mosquito"),
    ("Gametocytes", "Sexual stages of Plasmodium formed in human RBCs"),
    ("Interferons", "Proteins that protect uninfected cells from viral infection"),
    ("Macrophages in HIV infection", "Act as an HIV factory"),
    ("Helper T cells in HIV infection", "Steadily decrease in number"),
    ("Mast cells", "Release histamine and serotonin in allergy"),
    ("Proto-oncogenes (c-onc)", "Normal genes that can turn cancerous when activated"),
], "{}:", "What is described: {}?", weight=2)
table("b12-07", [
    ("Heroin (smack)", "Diacetylmorphine from the opium poppy, Papaver somniferum"),
    ("Cannabinoids (marijuana, hashish, charas, ganja)", "Cannabis sativa; affect the cardiovascular system"),
    ("Cocaine", "Erythroxylum coca; interferes with dopamine transport"),
    ("Hallucinogenic plants", "Atropa belladonna and Datura"),
    ("Nicotine", "Stimulates the adrenal gland to release adrenaline and noradrenaline"),
], "{}:", "Which drug or plant: {}?")
table("b12-07", [
    ("Primary lymphoid organs", "Bone marrow and thymus"),
    ("Secondary lymphoid organs", "Spleen, lymph nodes, tonsils and Peyer's patches"),
    ("Antibody passing through the placenta", "IgG"), ("Antibody in colostrum", "IgA"),
    ("Antibody involved in allergy", "IgE"),
], "{}:", None)
facts("b12-07", [
    "An antibody molecule has two heavy and two light chains (H2L2)",
    "B lymphocytes produce antibodies; T lymphocytes mediate cell-mediated immunity",
    "Graft rejection is due to cell-mediated immunity",
    "Edward Jenner developed the smallpox vaccine using cowpox",
    "Hepatitis B vaccine is made using recombinant yeast",
    "MALT forms about half of the lymphoid tissue of the body",
    "Rheumatoid arthritis is an autoimmune disease",
    "Common cold infects the nose and respiratory passages but not the lungs",
    "Cancer cells lose contact inhibition",
], [
    "Typhoid is caused by a virus",
    "Antibodies are produced by T lymphocytes",
    "Benign tumours spread by metastasis",
    "HIV is a DNA virus that does not use reverse transcriptase",
    "Malaria parasites reproduce sexually in human RBCs",
    "Interferons are produced by bacteria to kill viruses",
], "Human Health and Disease", weight=2)

# ---------------------------------------------------------------- b12-08 Microbes in Human Welfare
table("b12-08", [
    ("Citric acid", "Aspergillus niger"), ("Acetic acid", "Acetobacter aceti"),
    ("Butyric acid", "Clostridium butylicum"), ("Lactic acid", "Lactobacillus"),
    ("Streptokinase (clot buster)", "Streptococcus"), ("Cyclosporin A", "Trichoderma polysporum"),
    ("Statins", "Monascus purpureus"), ("Penicillin", "Penicillium notatum"),
    ("Baker's yeast for bread", "Saccharomyces cerevisiae"), ("Large holes in Swiss cheese", "Propionibacterium sharmanii"),
    ("Curd and extra vitamin B12", "Lactobacillus and other lactic acid bacteria"),
], "{} is produced by or comes from:", "What does {} produce?", weight=3)
table("b12-08", [
    ("Rhizobium", "Nitrogen-fixing bacteria in root nodules of legumes"),
    ("Azospirillum and Azotobacter", "Free-living nitrogen fixers in soil"),
    ("Glomus", "Mycorrhizal fungus that absorbs phosphorus for the plant"),
    ("Anabaena, Nostoc and Oscillatoria", "Cyanobacteria that fix nitrogen in paddy fields"),
    ("Bacillus thuringiensis", "Biocontrol of butterfly caterpillars"),
    ("Trichoderma", "Biocontrol of plant root pathogens"),
    ("Nucleopolyhedrovirus (baculovirus)", "Narrow-spectrum insecticide for specific insects"),
    ("Ladybird", "Biocontrol of aphids"), ("Dragonflies", "Biocontrol of mosquitoes"),
    ("Methanobacterium", "Methanogen that produces biogas"),
], "{}:", "Which organism is used as: {}?", weight=2)
facts("b12-08", [
    "Alexander Fleming discovered penicillin from Penicillium notatum",
    "Ernest Chain and Howard Florey established penicillin's full potential as an antibiotic",
    "Biogas is mostly methane with some CO2 and H2S",
    "The biogas technology in India was developed mainly by IARI and KVIC",
    "Primary sewage treatment is physical; secondary treatment is biological",
    "BOD measures the oxygen that microbes would use to oxidise organic matter in water",
    "Flocs are masses of bacteria and fungal filaments in secondary treatment",
    "Lipases are used in detergents to remove oily stains",
    "Pectinases and proteases are used to clarify bottled fruit juices",
], [
    "Primary sewage treatment is biological",
    "A high BOD means the water is clean",
    "Biogas is mostly oxygen",
    "Statins raise blood cholesterol",
    "Cyclosporin A is an antibiotic against bacteria",
    "Penicillin was discovered by Louis Pasteur",
], "Microbes in Human Welfare", weight=2)

# ---------------------------------------------------------------- b12-09 Biotechnology: Principles and Processes
table("b12-09", [
    ("First recombinant DNA (1972)", "Stanley Cohen and Herbert Boyer"),
    ("Molecular scissors", "Restriction endonucleases"), ("Molecular glue", "DNA ligase"),
    ("Heat-stable DNA polymerase for PCR", "Taq polymerase from Thermus aquaticus"),
    ("Natural genetic engineer of plants", "Agrobacterium tumefaciens (Ti plasmid)"),
    ("Agarose source", "Seaweed"), ("Stain for DNA in gels", "Ethidium bromide (orange under UV)"),
    ("First restriction endonuclease studied", "Hind II"),
], "{}:", "What is {}?", weight=2)
table("b12-09", [
    ("PCR step 1", "Denaturation of DNA at high temperature"), ("PCR step 2", "Annealing of primers"),
    ("PCR step 3", "Extension by DNA polymerase"),
    ("ori", "Sequence where replication starts and copy number is controlled"),
    ("Selectable marker", "Gene that helps pick out transformants, e.g. antibiotic resistance"),
    ("Insertional inactivation", "Recombinants lose a marker such as beta-galactosidase and give white colonies"),
    ("Elution", "Recovering DNA bands cut out of the gel"),
    ("Downstream processing", "Separation and purification of the product"),
], "{}:", "Which step or term: {}?", weight=2)
table("b12-09", [
    ("BamHI and SalI sites in pBR322", "Tetracycline resistance gene"),
    ("PvuI and PstI sites in pBR322", "Ampicillin resistance gene"),
], "{} lie in the:", None)
facts("b12-09", [
    "EcoRI gets its name from Escherichia coli strain RY13",
    "Restriction enzymes recognise palindromic sequences",
    "DNA is negatively charged and moves towards the anode in electrophoresis",
    "Bacterial cells are made competent with divalent cations such as calcium",
    "Heat shock at 42 °C helps bacteria take up recombinant DNA",
    "Biolistics uses gold or tungsten particles coated with DNA",
    "Stirred-tank bioreactors are commonly used for large-scale culture",
], [
    "DNA moves towards the cathode in electrophoresis",
    "DNA ligase cuts DNA at specific sites",
    "Taq polymerase is destroyed at high temperatures",
    "Recombinant colonies are blue when beta-galactosidase is inactivated",
    "Restriction enzymes cut only single-stranded DNA",
    "Agarose is obtained from bacteria",
], "Biotechnology: Principles and Processes", weight=2)


@gen("b12-09", weight=2)
def _pcr(rng):
    n = rng.choice([5, 10, 15, 20, 25, 30])
    start = rng.choice([1, 2, 5, 10])
    return num_q(rng, f"PCR starts with {start} copies of a DNA segment. After {n} cycles (perfect doubling) there are:",
                 start * 2 ** n, " copies", f"Copies = {start} × 2^{n}.", form=lambda x: f"{int(x):,}",
                 wrongs=[start * 2 ** (n - 1), start * 2 ** (n + 1), start * 2 * n])


@gen("b12-09")
def _fragments(rng):
    cuts = rng.choice([1, 2, 3, 4, 5])
    shape = rng.choice(["linear", "circular"])
    val = cuts + 1 if shape == "linear" else cuts
    return Q(f"A {shape} DNA molecule is cut at {cuts} site(s) by a restriction enzyme. How many fragments form?",
             str(val), [str(x) for x in {cuts - 1, cuts, cuts + 1, cuts + 2, 2 * cuts} - {val} if x > 0],
             "A linear molecule gives cuts + 1 fragments; a circular one gives as many fragments as cuts.")


# ---------------------------------------------------------------- b12-10 Biotechnology and its Applications
table("b12-10", [
    ("cryIAc and cryIIAb", "Control cotton bollworms"), ("cryIAb", "Controls corn borer"),
    ("RNA interference in tobacco", "Protects against the nematode Meloidogyne incognita"),
    ("Golden rice", "Rich in vitamin A (beta-carotene)"),
    ("Rosie (1997)", "Transgenic cow whose milk had human alpha-lactalbumin"),
    ("Alpha-1-antitrypsin from transgenic animals", "Treats emphysema"),
    ("First clinical gene therapy (1990)", "Adenosine deaminase (ADA) deficiency"),
    ("Eli Lilly (1983)", "Human insulin made by joining A and B chains produced in E. coli"),
    ("GEAC", "Indian body that judges the safety of genetic modification research"),
], "{}:", "What is described: {}?", weight=2)
facts("b12-10", [
    "Bt toxin exists as an inactive protoxin that becomes active in the alkaline insect gut",
    "Insulin consists of two peptide chains, A and B, joined by disulphide bridges",
    "Pro-insulin contains an extra C peptide that is removed in mature insulin",
    "More than 95 per cent of transgenic animals are mice",
    "Rosie's milk contained 2.4 grams of human protein per litre",
    "Biopiracy is the use of bio-resources without proper authorisation or payment",
], [
    "Bt toxin is active as soon as it is made in the bacterium",
    "Mature insulin contains the C peptide",
    "Gene therapy was first used for haemophilia in 1990",
    "Most transgenic animals are cows",
    "Golden rice is rich in vitamin C",
    "RNA interference makes plants produce more nematodes",
], "Biotechnology and its Applications")

# ---------------------------------------------------------------- b12-11 Organisms and Populations
table("b12-11", [
    ("Mutualism (+, +)", "Lichens, mycorrhizae, fig and fig wasp"),
    ("Competition (-, -)", "Abingdon tortoise and goats on the Galapagos"),
    ("Predation (+, -)", "Moth larvae controlling prickly pear cactus in Australia"),
    ("Parasitism (+, -)", "Cuscuta growing on hedge plants"),
    ("Commensalism (+, 0)", "Orchid growing as an epiphyte on a mango branch"),
    ("Brood parasitism", "Cuckoo laying eggs in a crow's nest"),
    ("Sexual deceit", "Ophrys orchid flower resembling a female bee"),
    ("Competitive exclusion", "Gause's principle"),
    ("Keystone predator", "Pisaster starfish studied by Paine"),
], "An example of {} is:", "{} is an example of:", weight=3)
table("b12-11", [
    ("Expanding population", "Triangular (broad-based) age pyramid"),
    ("Stable population", "Bell-shaped age pyramid"),
    ("Declining population", "Urn-shaped age pyramid"),
    ("Exponential growth", "dN/dt = rN"), ("Logistic growth", "dN/dt = rN(K - N)/K"),
], "{}:", "{} indicates:")
facts("b12-11", [
    "Monarch butterflies are distasteful because of chemicals from a weed they eat as caterpillars",
    "Barnacles on a whale's back are an example of commensalism",
    "Cattle egrets feeding near grazing cattle is commensalism",
    "The liver fluke needs two intermediate hosts, a snail and a fish",
    "Logistic growth is also called Verhulst-Pearl growth",
    "K is the carrying capacity of the environment",
], [
    "In commensalism both species are harmed",
    "Exponential growth is limited by carrying capacity",
    "The cuckoo is an example of mutualism",
    "Cuscuta makes its own food by photosynthesis",
    "A bell-shaped age pyramid shows a declining population",
    "In amensalism both species benefit",
], "Organisms and Populations", weight=2)


@gen("b12-11", weight=2)
def _birth_rate(rng):
    n0 = rng.choice([20, 40, 50, 80, 100, 200])
    new = rng.choice([2, 4, 5, 8, 10, 16])
    kind = rng.choice(["birth", "death"])
    return num_q(rng, f"A pond has {n0} lotus plants; during a year {new} {'new plants are added by reproduction' if kind == 'birth' else 'plants die'}. The {kind} rate per plant per year is:",
                 new / n0, explanation=f"{kind.capitalize()} rate = {new}/{n0}.", form=lambda x: f"{x:.2f}",
                 wrongs=[n0 / new / 100, new / n0 * 10, (new + 1) / n0])


@gen("b12-11")
def _logistic(rng):
    r, n, k = rng.choice([0.1, 0.2, 0.5]), rng.choice([100, 200, 500]), rng.choice([1000, 2000])
    val = r * n * (k - n) / k
    return num_q(rng, f"For logistic growth with r = {r}, N = {n} and K = {k}, dN/dt is:", val, " per unit time",
                 f"dN/dt = rN(K - N)/K = {r} × {n} × ({k} - {n})/{k}.", wrongs=[r * n, r * k, r * (k - n)])


# ---------------------------------------------------------------- b12-12 Ecosystem
table("b12-12", [
    ("Fragmentation", "Detritivores such as earthworms break detritus into smaller particles"),
    ("Leaching", "Water-soluble inorganic nutrients sink into the soil"),
    ("Catabolism", "Bacterial and fungal enzymes degrade detritus into simpler substances"),
    ("Humification", "Formation of dark, colloidal, slowly decomposing humus"),
    ("Mineralisation", "Release of inorganic nutrients from humus"),
], "In decomposition, {} is:", "Which step of decomposition: {}?")
table("b12-12", [
    ("Pyramid of energy", "Always upright"), ("Pyramid of biomass in the sea", "Inverted"),
    ("Pyramid of numbers for a single tree with insects", "Inverted"),
    ("Pioneer species on bare rock", "Lichens"),
    ("Primary succession", "Begins where no soil exists, such as bare rock"),
    ("Secondary succession", "Begins in abandoned farmland or burned forest"),
    ("Hydrarch succession", "Begins in water and moves toward mesic conditions"),
    ("Climax community", "Community in near equilibrium with the environment"),
], "{}:", None)
facts("b12-12", [
    "Net primary productivity = gross primary productivity minus respiration losses",
    "Annual NPP of the whole biosphere is about 170 billion tons of dry organic matter",
    "Oceans produce only about 55 billion tons of NPP a year despite covering 70 per cent of the surface",
    "Plants capture only 2-10 per cent of photosynthetically active radiation",
    "PAR is less than 50 per cent of incident solar radiation",
    "Lindeman's 10 per cent law describes energy transfer between trophic levels",
    "Humus is highly resistant to microbial action",
], [
    "The pyramid of energy can be inverted",
    "Oceans produce more NPP than land each year",
    "Plants capture about 50 per cent of PAR",
    "Secondary succession is slower than primary succession",
    "Humus decomposes very quickly",
    "Lichens are the climax community on rock",
], "Ecosystem", weight=2)


@gen("b12-12", weight=2)
def _ten_percent(rng):
    e = rng.choice([1000, 5000, 10000, 20000, 50000])
    lvl = rng.choice([2, 3, 4])
    names = {2: "primary consumers", 3: "secondary consumers", 4: "tertiary consumers"}
    val = e * 0.1 ** (lvl - 1)
    return num_q(rng, f"Producers trap {e} J. By the 10% law, energy available to {names[lvl]} is:", val, " J",
                 f"{e} × 0.1^{lvl - 1}.", wrongs=[e * 0.1 ** lvl, e * 0.1 ** (lvl - 2), e / lvl])


@gen("b12-12")
def _npp(rng):
    g = rng.choice([1000, 1500, 2000, 2500])
    r = rng.choice([200, 400, 500, 800])
    return num_q(rng, f"GPP of a field is {g} kcal/m²/yr and respiration loss is {r}. NPP is:", g - r, " kcal/m²/yr",
                 f"NPP = GPP - R = {g} - {r}.", form=lambda x: str(int(x)), wrongs=[g + r, r, g])


# ---------------------------------------------------------------- b12-13 Biodiversity and Conservation
table("b12-13", [
    ("Dodo", "Mauritius"), ("Quagga", "Africa"), ("Thylacine", "Australia"), ("Steller's sea cow", "Russia"),
], "The extinct {} lived in:", "Which extinct animal lived in {}?")
table("b12-13", [
    ("Habitat loss and fragmentation", "The most important cause of biodiversity loss"),
    ("Over-exploitation", "Extinction of Steller's sea cow and the passenger pigeon"),
    ("Alien species invasion", "Nile perch in Lake Victoria wiping out over 200 cichlid species"),
    ("Co-extinction", "A parasite dying out with its host"),
], "{} is linked with:", "Which cause of biodiversity loss: {}?")
table("b12-13", [
    ("Popularised the term biodiversity", "Edward Wilson"),
    ("Estimated about 7 million species on Earth", "Robert May"),
    ("Species-area relationship", "Alexander von Humboldt"),
    ("Rivet popper hypothesis", "Paul Ehrlich"),
    ("Long-term ecosystem experiments on species richness and productivity", "David Tilman"),
], "{}:", "What is {} known for?")
table("b12-13", [
    ("Khasi and Jaintia Hills", "Meghalaya"), ("Aravalli Hills", "Rajasthan"),
    ("Western Ghats sacred groves", "Karnataka and Maharashtra"), ("Sarguja, Chanda and Bastar", "Madhya Pradesh"),
], "Sacred groves of the {} are in:", None)
facts("b12-13", [
    "India has 2.4 per cent of the world's land area but about 8.1 per cent of its species diversity",
    "India is one of 12 megadiversity countries",
    "Insects make up more than 70 per cent of all recorded animal species",
    "The Amazon rain forest has the greatest biodiversity on Earth",
    "Biodiversity hotspots cover less than 2 per cent of the Earth's land area",
    "Western Ghats-Sri Lanka, Indo-Burma and the Himalaya are hotspots covering India",
    "The Earth Summit on biodiversity was held in Rio de Janeiro in 1992",
    "In the species-area curve, Z is usually 0.1-0.2 for small regions",
    "About 784 species became extinct in the last 500 years (IUCN 2004)",
], [
    "Plants make up more than 70 per cent of all recorded species",
    "Biodiversity decreases from the poles towards the equator",
    "Zoos are an example of in-situ conservation",
    "Hotspots cover about 20 per cent of the Earth's land area",
    "The Earth Summit was held in Johannesburg in 1992",
    "Over-exploitation is the most important cause of extinction",
], "Biodiversity and Conservation", weight=2)


@gen("b12-13")
def _species_area(rng):
    c, z, a = rng.choice([2, 5, 10]), rng.choice([0.1, 0.2, 0.25]), rng.choice([100, 1000, 10000])
    s = c * a ** z
    return num_q(rng, f"Using S = C·A^Z with C = {c}, Z = {z} and A = {a} km², the number of species S is about:",
                 s, explanation=f"S = {c} × {a}^{z}.", wrongs=[c * a * z, c + a ** z, c * a ** (2 * z)])
