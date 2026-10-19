"""High-yield NEET Biology, second batch (Classes 11-12): more original questions on repeatedly asked NCERT topics.

Tagged "hy2" so it is generated after the first high-yield batch and existing question ids never move.
"""
from .core import table, facts, groups, tag

tag("hy2")

# ---------------------------------------------------------------- Class 11
table("b11-01", [
    ("Housefly", "Musca domestica"), ("Mango", "Mangifera indica"), ("Wheat", "Triticum aestivum"), ("Human", "Homo sapiens"),
    ("Potato", "Solanum tuberosum"), ("Lion", "Panthera leo"), ("Tiger", "Panthera tigris"), ("Leopard", "Panthera pardus"),
    ("Brinjal", "Solanum melongena"),
], "The scientific name of {} is:", "{} is the scientific name of:")
table("b11-02", [
    ("Bacteriophage", "Usually double-stranded DNA"), ("Tobacco mosaic virus", "Single-stranded RNA"),
    ("Potato spindle tuber disease", "Caused by a viroid"), ("Mad cow disease (BSE)", "Caused by a prion"),
    ("Albugo", "Parasitic fungus on mustard"), ("Puccinia", "Fungus causing wheat rust"), ("Ustilago", "Fungus causing smut"),
    ("Trichoderma", "Fungus used as a biocontrol agent"),
], "{}:", "Which agent or organism: {}?")
facts("b11-02", [
    "Methanogens are archaebacteria",
    "Cyanobacteria have chlorophyll a like plants",
    "Chemosynthetic bacteria oxidise inorganic substances to get energy",
    "Rhizopus and Mucor are phycomycetes",
    "Penicillium and Aspergillus are ascomycetes",
    "Agaricus (mushroom) is a basidiomycete",
    "Alternaria and Colletotrichum are deuteromycetes",
    "Yeast is a unicellular ascomycete",
], [
    "Agaricus is an ascomycete",
    "Penicillium is a basidiomycete",
    "Cyanobacteria lack chlorophyll",
    "Archaebacteria have peptidoglycan cell walls like eubacteria",
    "Rhizopus is a basidiomycete",
    "Yeast is a multicellular basidiomycete",
    "Puccinia is a deuteromycete",
    "Chemosynthetic bacteria use sunlight for energy",
], "fungi and monerans")
facts("b11-03", [
    "In bryophytes the sporophyte depends on the gametophyte",
    "In pteridophytes the main plant body is the sporophyte",
    "The prothallus of a fern is the gametophyte",
    "Gemmae help liverworts reproduce asexually",
    "Pinus has mycorrhizal roots",
    "In gymnosperms the male and female gametophytes do not live free",
], [
    "In bryophytes the gametophyte depends on the sporophyte",
    "The prothallus of a fern is the sporophyte",
    "Gemmae are sexual structures",
    "Pinus has coralloid roots",
    "Fern sporophytes are short-lived",
    "Bryophytes have vascular tissue",
], "plant groups")
table("b11-04", [
    ("Radial symmetry", "Cnidarians, ctenophores and adult echinoderms"), ("Bilateral symmetry", "Annelids, arthropods and chordates"),
    ("Asymmetry", "Most sponges"), ("Diploblastic", "Cnidarians and ctenophores"),
    ("Pseudocoelomate", "Aschelminthes (roundworms)"), ("Acoelomate", "Platyhelminthes (flatworms)"),
], "{} is seen in:", "Which body plan is seen in {}?")
facts("b11-04", [
    "Notochord is replaced by a vertebral column in vertebrates",
    "Urochordates have a notochord only in the larval tail",
    "In cephalochordates the notochord runs from head to tail throughout life",
    "Mammals have external ears (pinnae)",
    "Cyclostomes are marine but migrate to fresh water to spawn",
    "Arthropoda is the largest animal phylum",
    "Aves have a four-chambered heart and are warm-blooded",
    "Torpedo can give electric shocks",
], [
    "All chordates have a vertebral column",
    "Mollusca is the largest animal phylum",
    "Reptiles are warm-blooded",
    "Cyclostomes have jaws",
    "Urochordates have a notochord throughout life",
    "Birds have a three-chambered heart",
    "Sharks have a bony endoskeleton",
    "Mammals lack hair",
], "chordates and animal diversity")
table("b11-05", [
    ("Fabaceae", "Pea family: vexillary corolla, diadelphous stamens, marginal placentation"),
    ("Solanaceae", "Potato family: fused petals, swollen placenta, oblique ovary"),
    ("Liliaceae", "Lily family: trimerous flowers, perianth of 6 tepals, axile placentation"),
    ("Brassicaceae", "Mustard family: tetradynamous stamens, parietal placentation"),
], "Which description fits family {}?", "Which family: {}?")
facts("b11-05", [
    "Reticulate venation is typical of dicots",
    "Parallel venation is typical of monocots",
    "Opuntia has a flattened stem called a phylloclade",
    "Pea leaves have tendrils formed from leaflets",
    "Ginger and turmeric have underground stems (rhizomes)",
    "Pitcher plant leaves trap insects",
], [
    "Reticulate venation is typical of monocots",
    "Ginger is a modified root",
    "Opuntia leaves are broad and green",
    "Pitcher plant leaves are modified for climbing",
    "Onion bulb is a modified root",
    "Carrot is a modified stem",
], "plant morphology")
table("b11-08", [
    ("Robert Hooke", "First described cells in cork"), ("Leeuwenhoek", "First saw and described a live cell"),
    ("Robert Brown", "Discovered the nucleus"), ("Camillo Golgi", "Observed the Golgi apparatus"),
    ("George Palade", "Observed ribosomes under the electron microscope"), ("Christian de Duve", "Discovered lysosomes"),
], "{}:", "Who is known for: {}?")
table("b11-09", [
    ("Simple lipid", "Fatty acids esterified with glycerol"), ("Phospholipid", "Lipid with phosphorus and a phosphorylated organic compound"),
    ("Nucleoside", "Nitrogen base + sugar"), ("Nucleotide", "Nitrogen base + sugar + phosphate"),
    ("Essential amino acid", "Must come from food"), ("Holoenzyme", "Apoenzyme + cofactor"),
], "{}:", "Which term: {}?")
table("b11-10", [
    ("Leptotene", "Chromosomes become gradually visible"), ("Zygotene", "Homologous chromosomes pair (synapsis)"),
    ("Pachytene", "Bivalents clear; crossing over"), ("Diplotene", "Synaptonemal complex dissolves; chiasmata visible"),
    ("Diakinesis", "Terminalisation of chiasmata; nuclear envelope breaks"),
], "In {} of meiosis I:", "Which substage of prophase I: {}?")
table("b11-11", [
    ("Chlorophyll a", "Bright or blue-green on chromatography"), ("Chlorophyll b", "Yellow-green"),
    ("Xanthophylls", "Yellow"), ("Carotenoids (carotene)", "Yellow to yellow-orange"),
], "On chromatography, {} appears:", "Which pigment appears {}?")
facts("b11-11", [
    "Jan Ingenhousz showed that sunlight is needed to purify air",
    "Priestley showed that plants restore air spoilt by a burning candle",
    "Van Niel showed that oxygen in photosynthesis comes from water",
    "Melvin Calvin worked out the C3 pathway using radioactive 14C",
    "Hatch and Slack described the C4 pathway",
    "Engelmann used a split spectrum and aerobic bacteria to show the action spectrum",
], [
    "Calvin used 18O to show oxygen comes from water",
    "Priestley discovered the C4 pathway",
    "Hatch and Slack worked out the C3 cycle",
    "Ingenhousz showed plants need darkness to purify air",
    "Engelmann used anaerobic bacteria",
    "Van Niel showed oxygen comes from CO2",
], "history of photosynthesis")
table("b11-12", [
    ("Hexokinase", "Glucose to glucose-6-phosphate"), ("Phosphofructokinase", "Fructose-6-phosphate to fructose-1,6-bisphosphate"),
    ("Pyruvate dehydrogenase", "Pyruvate to acetyl CoA"), ("Citrate synthase", "Acetyl CoA + oxaloacetate to citrate"),
    ("Succinate dehydrogenase", "Succinate to fumarate"), ("Alcohol dehydrogenase", "Acetaldehyde to ethanol in yeast"),
], "The enzyme {} catalyses:", "Which enzyme catalyses: {}?")
table("b11-13", [
    ("Long day plants", "Flower when day length exceeds a critical period"), ("Short day plants", "Flower when day length is below a critical period"),
    ("Day neutral plants", "Flowering not linked to day length"), ("Vernalisation", "Low temperature treatment promotes flowering"),
], "{}:", "Which term: {}?")
facts("b11-13", [
    "IAA and IBA are natural auxins; NAA and 2,4-D are synthetic",
    "Gibberellins increase the length of grape stalks",
    "Spraying sugarcane with gibberellins increases stem length and yield",
    "Cytokinins promote lateral shoot growth and nutrient mobilisation",
    "Ethylene promotes root growth and root hair formation",
    "ABA is an antagonist to gibberellins",
], [
    "NAA is a natural auxin",
    "Gibberellins reduce sugarcane stem length",
    "Cytokinins promote apical dominance",
    "ABA promotes growth and seed germination",
    "Ethylene is a liquid hormone",
    "Auxins promote leaf abscission in young leaves",
], "plant hormones")
facts("b11-14", [
    "Asthma is difficulty in breathing caused by inflammation of bronchi and bronchioles",
    "Occupational respiratory disorders cause fibrosis of the lungs",
    "Each lung is covered by a double-layered pleura",
    "The trachea divides into right and left primary bronchi at the 5th thoracic vertebra",
    "Cartilaginous rings support the trachea and bronchi",
    "Exchange of gases happens by simple diffusion",
], [
    "The pleura is a single layer around both lungs",
    "Gas exchange in alveoli happens by active transport",
    "Asthma is caused by loss of alveolar walls",
    "The trachea has no cartilage",
    "The diaphragm relaxes during normal inspiration",
    "Emphysema is mainly caused by vitamin deficiency",
], "the respiratory system")
table("b11-15", [
    ("Erythrocytes in an adult", "5 to 5.5 million per mm³"), ("Leucocytes in an adult", "6000 to 8000 per mm³"),
    ("Platelets in an adult", "1.5 to 3.5 lakh per mm³"), ("Haemoglobin in an adult", "12 to 16 g per 100 mL"),
    ("Life span of red blood cells", "About 120 days"),
], "{}:", "Which value is: {}?")
facts("b11-15", [
    "Hypertension is blood pressure of 140/90 mm Hg or higher",
    "Coronary artery disease is often due to deposits of calcium, fat and cholesterol",
    "Angina is chest pain from too little oxygen reaching the heart muscle",
    "Heart failure means the heart is not pumping blood effectively enough",
    "The lub sound is caused by closure of the AV valves",
    "The dub sound is caused by closure of the semilunar valves",
], [
    "Heart failure is the same as cardiac arrest",
    "The lub sound is due to closure of semilunar valves",
    "Angina is caused by too much oxygen in the heart",
    "Hypertension means blood pressure below 120/80",
    "The dub sound comes from opening of AV valves",
    "Atherosclerosis widens the coronary arteries",
], "disorders of circulation")
table("b11-16", [
    ("Liver", "Excretes bilirubin, cholesterol and drugs in bile"), ("Lungs", "Remove about 200 mL of CO2 per minute"),
    ("Sweat glands", "Remove NaCl, small amounts of urea and lactic acid"), ("Sebaceous glands", "Remove sterols and waxes in sebum"),
], "As an accessory excretory organ, the {}:", "Which organ: {}?")
facts("b11-17", [
    "Arthritis is inflammation of joints",
    "Osteoporosis is a decrease in bone mass with age",
    "Low estrogen is a common cause of osteoporosis",
    "Muscular dystrophy is a genetic progressive degeneration of skeletal muscle",
    "Tetany is rapid spasms due to low calcium in body fluid",
    "The pectoral girdle has a clavicle and a scapula",
], [
    "Muscular dystrophy is caused by infection",
    "Arthritis is a disorder of the neuromuscular junction",
    "The pelvic girdle has a clavicle and a scapula",
    "Osteoporosis increases bone mass",
    "Tetany is due to excess calcium",
    "Gout is due to calcium deficiency",
], "skeletal and muscular disorders")
table("b11-18", [
    ("Cerebrum", "Thinking, memory, voluntary actions"), ("Thalamus", "Major relay centre for sensory and motor signals"),
    ("Limbic system", "Emotions, sexual behaviour and motivation"), ("Midbrain", "Corpora quadrigemina; vision and hearing reflexes"),
    ("Pons", "Fibre tracts linking brain regions; regulates breathing"),
], "{}:", "Which part of the brain: {}?")
table("b11-19", [
    ("Growth hormone", "Anterior pituitary"), ("Prolactin", "Anterior pituitary", ["Anterior pituitary"]), ("TSH", "Anterior pituitary", ["Anterior pituitary"]),
    ("Melatonin", "Pineal gland"), ("Thyroxine", "Thyroid"), ("Cortisol", "Adrenal cortex"), ("Adrenaline", "Adrenal medulla"),
    ("Insulin", "Beta cells of the islets of Langerhans"), ("Glucagon", "Alpha cells of the islets of Langerhans"),
    ("Testosterone", "Leydig cells of the testis"), ("Progesterone", "Corpus luteum"),
], "{} is secreted by the:", None, weight=2)

# ---------------------------------------------------------------- Class 12
table("b12-01", [
    ("Wind pollination", "Light, non-sticky pollen; feathery stigma; e.g. maize"), ("Water pollination", "Vallisneria, Hydrilla and Zostera"),
    ("Insect pollination", "Large, colourful, fragrant flowers with nectar"), ("Bird pollination", "Bright red or orange flowers with lots of nectar"),
], "{}:", "Which kind of pollination: {}?")
facts("b12-01", [
    "Pollen grains can be stored for years in liquid nitrogen at -196 °C",
    "Pollen allergy is caused by pollen of plants such as Parthenium",
    "A typical anther is bilobed and tetrasporangiate",
    "The microspore mother cell divides by meiosis to form a pollen tetrad",
    "The ovule is attached to the placenta by the funicle",
    "The hilum is the point where the body of the ovule joins the funicle",
], [
    "A typical anther is monothecous",
    "Pollen grains cannot be stored",
    "The microspore mother cell divides by mitosis",
    "The micropyle is where the ovule joins the funicle",
    "Parthenium pollen never causes allergy",
    "The chalaza lies at the micropylar end",
], "pollen and ovules")
table("b12-02", [
    ("Spermatogonia", "2n germ cells in seminiferous tubules"), ("Primary spermatocyte", "2n; undergoes meiosis I"),
    ("Secondary spermatocyte", "n; undergoes meiosis II"), ("Spermatid", "n; becomes a sperm by spermiogenesis"),
], "{}:", "Which cell: {}?")
table("b12-02", [
    ("Menstrual phase", "Days 1-5; endometrium breaks down"), ("Follicular (proliferative) phase", "Follicles grow; endometrium regenerates"),
    ("Ovulatory phase", "LH surge releases the ovum around day 14"), ("Luteal (secretory) phase", "Corpus luteum makes progesterone"),
], "{} of the menstrual cycle:", "Which phase: {}?")
groups("b12-03", {
    "bacterial sexually transmitted infections": ["Gonorrhoea", "Syphilis", "Chlamydiasis"],
    "viral sexually transmitted infections": ["Genital herpes", "Hepatitis B", "Genital warts", "HIV infection"],
    "protozoan sexually transmitted infections": ["Trichomoniasis"],
}, "Which is NOT one of the {}?", "Which is one of the {}?")
table("b12-04", [
    ("Point mutation", "Change in a single base pair, e.g. sickle cell anaemia"), ("Frameshift mutation", "Insertion or deletion that shifts the reading frame"),
    ("Aneuploidy", "Gain or loss of a chromosome"), ("Polyploidy", "Increase in whole sets of chromosomes"),
], "{}:", "Which type of mutation: {}?")
facts("b12-04", [
    "Turner's syndrome females are sterile with rudimentary ovaries",
    "Klinefelter's syndrome males have gynaecomastia and are sterile",
    "In haemophilia a single protein of the clotting cascade is affected",
    "A colour-blind son gets the defective gene from his mother",
    "A haemophilic father cannot pass haemophilia to his son",
    "Queen Victoria was a carrier of haemophilia",
], [
    "A colour-blind son gets the gene from his father",
    "Turner's syndrome is seen in males",
    "Klinefelter's syndrome has the karyotype 45 XO",
    "A haemophilic father always has haemophilic sons",
    "Down's syndrome is sex-linked",
    "Haemophilia is caused by a missing chromosome",
], "chromosomal and sex-linked disorders")
table("b12-05", [
    ("Transcription unit", "Promoter, structural gene and terminator"), ("Template strand", "Strand with 3' to 5' polarity read by RNA polymerase"),
    ("Coding strand", "Strand with the same sequence as RNA (T for U)"), ("Exons", "Coding sequences in the mature RNA"),
    ("Introns", "Intervening sequences removed by splicing"), ("Cistron", "Segment of DNA coding for one polypeptide"),
], "{}:", "Which term: {}?")
facts("b12-05", [
    "DNA fingerprinting uses VNTRs (satellite DNA)",
    "Alec Jeffreys developed DNA fingerprinting",
    "The Human Genome Project was completed in 2003",
    "Expressed sequence tags identify genes expressed as RNA",
    "The genetic code is degenerate",
    "The genetic code is nearly universal",
    "In the lac operon, the y gene codes for permease",
    "The lac operon is under negative regulation",
], [
    "The genetic code is ambiguous",
    "The Human Genome Project was completed in 1990",
    "In the lac operon, the y gene codes for β-galactosidase",
    "DNA fingerprinting uses only coding exons",
    "Repetitive DNA is absent from the human genome",
    "The lac operon is switched on by glucose",
    "One codon codes for several amino acids",
    "The a gene codes for permease",
], "molecular genetics")
table("b12-06", [
    ("Dryopithecus", "Ape-like; about 15 mya"), ("Ramapithecus", "More man-like; about 15 mya"),
    ("Homo habilis", "First human-like being; 650-800 cc brain"), ("Homo erectus", "About 1.5 mya; 900 cc brain"),
    ("Neanderthal man", "1400 cc brain; lived 1,00,000-40,000 years ago"), ("Homo sapiens", "Arose in Africa; modern humans"),
], "{}:", "Which hominid: {}?")
table("b12-07", [
    ("Plasmodium vivax", "Benign tertian malaria"), ("Plasmodium falciparum", "Malignant malaria, the most serious kind"),
    ("Aedes mosquito", "Spreads dengue and chikungunya"), ("Female Anopheles", "Spreads malaria"),
    ("Culex mosquito", "Spreads filariasis"), ("Houseflies", "Mechanical carriers of amoebiasis"),
], "{}:", "Which organism: {}?")
facts("b12-07", [
    "Cancer cells lose the property of contact inhibition",
    "Benign tumours stay at their original location",
    "Metastasis is the spread of malignant tumour cells to new sites",
    "Alpha-interferon helps the immune system destroy tumours",
    "Opioids bind to receptors in the central nervous system and gastrointestinal tract",
    "Barbiturates and benzodiazepines are used to treat depression and insomnia",
    "HIV is a retrovirus with reverse transcriptase",
    "AIDS is diagnosed by ELISA",
], [
    "Benign tumours spread to distant organs",
    "Cancer cells show contact inhibition",
    "HIV is a DNA virus without reverse transcriptase",
    "Opioids act mainly on the kidneys",
    "Metastasis is the shrinking of a tumour",
    "AIDS is diagnosed by the Widal test",
    "Interferons are produced by bacteria to kill viruses",
    "Antibiotics cure viral infections like AIDS",
], "cancer, drugs and AIDS")
table("b12-08", [
    ("Rhizobium", "Symbiotic nitrogen fixation in legume root nodules"), ("Azospirillum", "Free-living nitrogen fixer in soil"),
    ("Azotobacter", "Free-living nitrogen fixer in soil", ["Free-living nitrogen fixer in soil"]), ("Anabaena and Nostoc", "Cyanobacterial biofertilisers in paddy fields"),
    ("Glomus", "Mycorrhizal fungus that absorbs phosphorus"), ("Trichoderma", "Free-living fungus used against plant pathogens"),
    ("Ladybird", "Controls aphids"), ("Dragonflies", "Control mosquitoes"),
], "{}:", None)
table("b12-09", [
    ("Restriction enzyme naming: E in EcoRI", "Genus Escherichia"), ("Restriction enzyme naming: co in EcoRI", "Species coli"),
    ("Restriction enzyme naming: R in EcoRI", "Strain RY13"), ("Restriction enzyme naming: I in EcoRI", "First enzyme isolated from that strain"),
], "{}:", None)
facts("b12-09", [
    "Hind II was the first restriction endonuclease isolated",
    "EcoRI cuts DNA to leave sticky ends",
    "Exonucleases remove nucleotides from the ends of DNA",
    "Endonucleases cut at specific positions within DNA",
    "Elution is the recovery of DNA bands from the gel",
    "Spooling is the collection of precipitated DNA threads with chilled ethanol",
], [
    "EcoRI was the first restriction endonuclease isolated",
    "Exonucleases cut in the middle of DNA",
    "Spooling uses hot water to precipitate DNA",
    "Elution adds DNA to the gel",
    "All restriction enzymes leave blunt ends",
    "Endonucleases remove nucleotides only from the ends",
], "recombinant DNA technology")
table("b12-10", [
    ("Bt cotton", "Insect resistance"), ("Flavr Savr tomato", "Delayed ripening; longer shelf life"),
    ("Golden rice", "Vitamin A enrichment"), ("Transgenic mice", "Testing vaccine safety, e.g. polio"),
], "{} was developed for:", "Which GM organism: {}?")
table("b12-11", [
    ("Population density", "Number of individuals per unit area"), ("Natality", "Number of births in a population in a period"),
    ("Mortality", "Number of deaths in a population in a period"), ("Immigration", "Individuals entering from elsewhere"),
    ("Emigration", "Individuals leaving the habitat"),
], "{}:", "Which term: {}?")
facts("b12-11", [
    "Bergmann's rule: animals of the same species are larger in colder climates",
    "Some organisms such as many zooplankton enter diapause",
    "Bears hibernate in winter",
    "Snails and fish aestivate in summer",
    "Birds migrate to avoid harsh conditions",
    "The logistic model is dN/dt = rN((K - N)/K)",
], [
    "Hibernation is summer sleep",
    "Aestivation is winter sleep",
    "The exponential model includes K",
    "Diapause is found only in plants",
    "Animals in hot climates are always larger",
    "Migration is a physiological response by plants",
], "adaptations and population growth")
table("b12-12", [
    ("Producers", "First trophic level"), ("Primary consumers (herbivores)", "Second trophic level"),
    ("Secondary consumers", "Third trophic level"), ("Top carnivores", "Fourth trophic level"),
], "{} occupy the:", "Which group occupies the {}?")
table("b12-13", [
    ("Western Ghats and Sri Lanka", "One of the biodiversity hot spots in India"), ("Indo-Burma", "Hot spot covering north-east India"),
    ("Himalaya", "Hot spot of the Himalayan region"), ("Silent Valley", "Protected tropical evergreen forest in Kerala"),
], "{}:", None)
facts("b12-13", [
    "India has about 50,000 strains of rice",
    "India has about 1,000 varieties of mango",
    "Alien species invasions cause loss of native species",
    "Co-extinction can happen when a host and its parasite are linked",
    "The IUCN Red List records threatened species",
    "Tropical rain forests are the richest in species",
], [
    "India has about 500 strains of rice",
    "Alien species always increase native biodiversity",
    "Polar regions are richest in species",
    "Co-extinction happens only to plants",
    "The IUCN Red List records only extinct species",
    "Mango has only a dozen varieties in India",
], "biodiversity")

tag(None)
