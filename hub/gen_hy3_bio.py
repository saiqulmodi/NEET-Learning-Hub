"""High-yield NEET Biology, third batch (Classes 11-12): more original questions on repeatedly asked NCERT facts.

Tagged "hy3" so it is generated after the earlier batches and existing question ids never move.
"""
from .core import table, facts, groups, tag

tag("hy3")

# ---------------------------------------------------------------- Class 11
table("b11-01", [
    ("ICBN", "Code for naming plants"), ("ICZN", "Code for naming animals"), ("Taxon", "A unit of any rank in classification"),
    ("Systematics", "Study of diversity and relationships of organisms"), ("Nomenclature", "Giving a standard name to an organism"),
    ("Identification", "Finding the correct place of an organism in the system"),
], "{} means:", "Which term means: {}?")
groups("b11-02", {
    "archaebacteria": ["Halophiles", "Thermoacidophiles", "Methanogens"],
    "protozoans": ["Amoeba", "Paramoecium", "Trypanosoma", "Plasmodium"],
    "fungi": ["Yeast", "Penicillium", "Agaricus", "Rhizopus"],
    "cyanobacteria": ["Nostoc", "Anabaena", "Oscillatoria"],
}, "Which organism is NOT one of the {}?", "Which organism is one of the {}?")
table("b11-02", [
    ("Amoeboid protozoans", "Pseudopodia; e.g. Amoeba, Entamoeba"), ("Flagellated protozoans", "Flagella; e.g. Trypanosoma (sleeping sickness)"),
    ("Ciliated protozoans", "Many cilia; e.g. Paramoecium"), ("Sporozoans", "Infectious spore-like stage; e.g. Plasmodium"),
], "{}:", "Which protozoan group: {}?")
table("b11-03", [
    ("Chlorophyceae", "Chlorophyll a and b; starch; cellulose wall"), ("Phaeophyceae", "Chlorophyll a, c and fucoxanthin; laminarin and mannitol"),
    ("Rhodophyceae", "Chlorophyll a, d and phycoerythrin; floridean starch"),
    ("Bryophytes", "No vascular tissue; gametophyte dominant"), ("Pteridophytes", "Vascular tissue; no seeds; sporophyte dominant"),
    ("Gymnosperms", "Naked seeds; no fruits"), ("Angiosperms", "Seeds enclosed in fruits"),
], "{}:", "Which group: {}?")
facts("b11-03", [
    "Sphagnum is used for packing living material because it holds water",
    "Mosses with lichens are the first organisms to colonise rocks",
    "Equisetum is commonly called horsetail",
    "Cycas has motile (flagellated) male gametes",
    "Sequoia is one of the tallest tree species",
    "Ginkgo is called a living fossil",
], [
    "Equisetum is a moss",
    "Pinus has motile male gametes",
    "Sphagnum is a red alga",
    "Ginkgo is an angiosperm",
    "Ferns produce seeds",
    "Sequoia is a moss",
], "plant diversity")
table("b11-04", [
    ("Earthworm (Pheretima)", "Annelida; clitellum; nephridia"), ("Cockroach (Periplaneta)", "Arthropoda; jointed legs; Malpighian tubules"),
    ("Snail (Pila)", "Mollusca; shell; radula"), ("Starfish (Asterias)", "Echinodermata; tube feet"),
    ("Tapeworm (Taenia)", "Platyhelminthes; flat body; hooks and suckers"), ("Roundworm (Ascaris)", "Aschelminthes; pseudocoelom; sexes separate"),
    ("Jellyfish (Aurelia)", "Cnidaria; medusa form"), ("Sea anemone (Adamsia)", "Cnidaria; polyp form", ["Cnidaria; polyp form"]),
], "{} is:", None, weight=2)
facts("b11-04", [
    "Spongilla is a freshwater sponge",
    "Pila is the apple snail",
    "Pinctada is the pearl oyster",
    "Sepia is the cuttlefish",
    "Loligo is the squid",
    "Ophiura is the brittle star",
    "Cucumaria is the sea cucumber",
    "Exocoetus is the flying fish",
], [
    "Sepia is the squid",
    "Pinctada is the apple snail",
    "Ophiura is the sea cucumber",
    "Exocoetus is the sea horse",
    "Loligo is the octopus",
    "Spongilla is a marine coral",
    "Cucumaria is the starfish",
    "Pila is the pearl oyster",
], "common names of animals")
table("b11-05", [
    ("Racemose inflorescence", "Mustard"), ("Cymose inflorescence", "Jasmine"), ("Epipetalous stamens", "Brinjal"),
    ("Epiphyllous stamens", "Lily"), ("Polyadelphous stamens", "Citrus"), ("Diadelphous stamens", "Pea"),
    ("Monoadelphous stamens", "China rose"),
], "An example of {} is:", "{} shows:", weight=2)
table("b11-06", [
    ("Guard cells in grasses", "Dumb-bell shaped"), ("Guard cells in dicots", "Bean shaped"), ("Root hairs", "Unicellular outgrowths of the epidermis"),
    ("Trichomes", "Multicellular hairs on the shoot"), ("Cuticle", "Waxy layer on the epidermis that reduces water loss"),
], "{}:", "Which structure: {}?")
facts("b11-07", [
    "Exocrine glands release their secretions through ducts",
    "Endocrine glands release hormones directly into blood",
    "Areolar tissue is found under the skin",
    "Bone has a hard matrix of calcium salts and collagen fibres",
    "Blood is a fluid connective tissue",
    "Neurons are excitable cells",
], [
    "Endocrine glands release secretions through ducts",
    "Cartilage has a matrix rich in calcium salts like bone",
    "Blood is an epithelial tissue",
    "Neuroglia make up a small part of neural tissue",
    "Exocrine glands release hormones into blood",
    "Smooth muscles are found in limb muscles",
], "animal tissues")
table("b11-08", [
    ("Cell wall of fungi", "Chitin"), ("Cell wall of plants", "Cellulose"), ("Cell wall of bacteria", "Peptidoglycan"),
    ("Middle lamella", "Calcium pectate"), ("Plasma membrane", "Lipid bilayer with proteins"),
], "{} is mainly made of:", "Which structure is mainly made of {}?")
facts("b11-08", [
    "Erythrocytes have about 40% lipids and 52% proteins in their membrane",
    "Quasi-fluid nature of the membrane helps cell growth and division",
    "Active transport uses ATP, e.g. the Na+/K+ pump",
    "Plasmodesmata connect neighbouring plant cells",
    "Chromoplasts give colour to flowers and fruits",
    "Leucoplasts store food: amyloplasts starch, elaioplasts oils, aleuroplasts proteins",
], [
    "Amyloplasts store oils",
    "Elaioplasts store proteins",
    "Plasmodesmata are found in animal cells",
    "Chromoplasts store starch",
    "Diffusion through the membrane always uses ATP",
    "The membrane has no proteins",
], "the cell membrane and plastids")
table("b11-09", [
    ("Glycine", "Simplest amino acid; R = H"), ("Alanine", "R = methyl group"), ("Serine", "R = hydroxymethyl group"),
    ("Lysine", "Basic amino acid"), ("Glutamic acid", "Acidic amino acid"), ("Tryptophan", "Aromatic amino acid"),
], "{}:", "Which amino acid: {}?")
facts("b11-10", [
    "Kinetochores are disc-shaped structures at the centromere",
    "Spindle fibres attach to the kinetochores",
    "A cell in G1 has 2C DNA content after mitosis (diploid)",
    "After S phase the DNA content becomes 4C",
    "Meiosis increases genetic variation",
    "Mitosis helps repair and growth of tissues",
], [
    "DNA content halves in S phase",
    "Meiosis produces identical cells",
    "Kinetochores are found on centrioles",
    "Mitosis occurs only in gametes",
    "Spindle fibres attach to the nucleolus",
    "Interphase is the dividing phase",
], "cell division")
groups("b11-11", {
    "C4 plants": ["Maize", "Sugarcane", "Sorghum", "Amaranthus"],
    "C3 plants": ["Wheat", "Rice", "Potato", "Spinach"],
    "CAM plants": ["Pineapple", "Opuntia", "Bryophyllum"],
}, "Which plant is NOT one of the {}?", "Which plant is one of the {}?")
facts("b11-12", [
    "Glycolysis gives 2 NADH per glucose",
    "The Krebs cycle gives 3 NADH, 1 FADH2 and 1 GTP per acetyl CoA",
    "Two turns of the Krebs cycle happen per glucose",
    "Oxidative phosphorylation is driven by a proton gradient",
    "Oxygen is reduced to water at complex IV",
    "Ubiquinone carries electrons from complexes I and II to III",
], [
    "The Krebs cycle runs once per glucose",
    "Glycolysis gives 4 NADH per glucose",
    "Oxygen is reduced at complex I",
    "ATP synthase is in the outer mitochondrial membrane",
    "FADH2 enters at complex I",
    "The Krebs cycle gives 2 FADH2 per acetyl CoA",
], "respiration")
table("b11-13", [
    ("Apical dominance", "Auxin"), ("Bolting in cabbage", "Gibberellin"), ("Breaking seed dormancy", "Gibberellin", ["Gibberellin"]),
    ("Richmond-Lang effect (delay of senescence)", "Cytokinin"), ("Ripening of fruits", "Ethylene"), ("Closing of stomata", "Abscisic acid"),
    ("Parthenocarpy in tomato", "Auxin", ["Auxin"]), ("Horizontal growth of seedlings and swelling of axis", "Ethylene", ["Ethylene"]),
], "{} is caused by:", None, weight=2)
table("b11-14", [
    ("Insects", "Tracheal tubes"), ("Earthworms", "Moist cuticle (skin)"), ("Fishes", "Gills"), ("Frogs", "Lungs and moist skin"),
    ("Reptiles, birds and mammals", "Lungs"), ("Sponges and coelenterates", "Simple diffusion over the body surface"),
], "Breathing in {} is through:", "Which animals breathe through {}?")
table("b11-15", [
    ("Neutrophils", "60-65% of WBCs; phagocytic"), ("Eosinophils", "2-3%; allergic reactions"), ("Basophils", "0.5-1%; secrete histamine, heparin"),
    ("Lymphocytes", "20-25%; B and T cells"), ("Monocytes", "6-8%; phagocytic, become macrophages"),
], "{}:", "Which white blood cells: {}?")
table("b11-16", [
    ("Bowman's capsule", "Cup that encloses the glomerulus"), ("PCT", "Lined by brush-border cuboidal epithelium; most reabsorption"),
    ("DCT", "Conditional reabsorption of Na+ and water; secretion of H+ and K+"), ("Collecting duct", "Joins many nephrons; concentrates urine"),
    ("Juxtaglomerular apparatus", "Releases renin when GFR falls"),
], "{}:", "Which part of the kidney: {}?")
table("b11-17", [
    ("Actin", "Thin filament protein"), ("Myosin", "Thick filament protein with heads"), ("Troponin", "Binds calcium in thin filaments"),
    ("Tropomyosin", "Covers active sites of actin at rest"), ("Myoglobin", "Red, oxygen-storing pigment in red muscle"),
], "{}:", "Which protein: {}?")
table("b11-18", [
    ("Reflex arc", "Receptor, sensory neuron, interneuron, motor neuron, effector"), ("Knee-jerk reflex", "Monosynaptic reflex arc"),
    ("Synaptic cleft", "Gap between pre- and post-synaptic neurons"), ("Neurotransmitter", "Chemical that crosses the synaptic cleft"),
], "{}:", "Which term: {}?")
facts("b11-18", [
    "The retina has three layers of cells: ganglion, bipolar and photoreceptor cells",
    "Light is focused on the retina by the cornea and the lens",
    "The aqueous humour fills the space between cornea and lens",
    "The vitreous humour fills the space between lens and retina",
    "The cochlea is a coiled part of the inner ear",
    "The external ear has a pinna and an external auditory meatus",
], [
    "The vitreous humour lies between cornea and lens",
    "The iris is the light-sensitive layer",
    "The cochlea is in the middle ear",
    "Ganglion cells are the photoreceptors",
    "The pinna is part of the inner ear",
    "The ossicles are in the inner ear",
], "the eye and the ear")
facts("b11-19", [
    "Hypothalamus releases releasing and inhibiting hormones for the pituitary",
    "The adrenal medulla secretes catecholamines",
    "The thyroid is made of follicles and stromal tissue",
    "Parathyroid glands are four in number on the back of the thyroid",
    "The pancreas is both exocrine and endocrine",
    "Graves' disease is due to hyperthyroidism",
], [
    "Parathyroid glands are two in number on the adrenal",
    "The pancreas is only an exocrine gland",
    "Graves' disease is due to hypothyroidism",
    "The adrenal cortex secretes adrenaline",
    "The hypothalamus is part of the hindbrain",
    "Thyroid follicles secrete insulin",
], "endocrine glands")

# ---------------------------------------------------------------- Class 12
table("b12-01", [
    ("Integuments", "Seed coat"), ("Ovary", "Fruit"), ("Ovule", "Seed"), ("Zygote", "Embryo"), ("Primary endosperm nucleus", "Endosperm"),
    ("Outer integument", "Testa"), ("Inner integument", "Tegmen"),
], "After fertilisation, the {} becomes the:", "The {} develops from the:", weight=2)
facts("b12-01", [
    "Seeds of lupine found in Arctic tundra germinated after about 10,000 years",
    "A 2000-year-old date palm seed from King Herod's palace germinated",
    "Dicot embryos have an epicotyl and a hypocotyl",
    "Most ripe seeds have 10-15% moisture",
    "Orchid fruits contain thousands of tiny seeds",
    "False fruits like apple develop from the thalamus as well",
], [
    "Apple is a true fruit formed only from the ovary",
    "Ripe seeds have about 90% moisture",
    "Seeds always lose viability within a year",
    "Orchid fruits contain a single large seed",
    "Monocot embryos have two cotyledons",
    "Dicot embryos lack a radicle",
], "seeds and fruits")
table("b12-02", [
    ("Seminiferous tubules", "Site of spermatogenesis"), ("Epididymis", "Stores and matures sperm"), ("Vas deferens", "Carries sperm towards the urethra"),
    ("Seminal vesicles", "Add fructose-rich fluid to semen"), ("Prostate gland", "Adds fluid to semen"), ("Bulbourethral glands", "Lubricate the penis"),
], "The role of the {} is:", "Which structure: {}?")
table("b12-02", [
    ("Oviduct (fallopian tube)", "Infundibulum, ampulla and isthmus"), ("Uterus wall", "Perimetrium, myometrium and endometrium"),
    ("Mammary gland", "Alveoli, tubules, ducts and lactiferous duct"), ("External genitalia", "Mons pubis, labia and clitoris"),
], "The parts of the {} are:", "These parts form the: {}?")
facts("b12-03", [
    "The Government of India started family planning programmes in 1951",
    "RCH stands for Reproductive and Child Health Care",
    "Statutory raising of marriageable age of females is 18 and males 21 years",
    "Infertility can be due to physical, congenital, drug, immunological or psychological causes",
    "Coitus interruptus is a natural method of contraception",
    "Diaphragms, cervical caps and vaults are barrier methods made of rubber",
], [
    "Family planning started in India in 1991",
    "The marriageable age for females is 21 years",
    "Coitus interruptus is a surgical method",
    "Diaphragms release hormones",
    "RCH stands for Rural Child Hospital",
    "Infertility is always due to the female partner",
], "reproductive health")
table("b12-04", [
    ("Monohybrid F2 genotypic ratio", "1:2:1"), ("Monohybrid F2 phenotypic ratio", "3:1"), ("Dihybrid F2 phenotypic ratio", "9:3:3:1"),
    ("Monohybrid test cross ratio", "1:1"), ("Dihybrid test cross ratio", "1:1:1:1"),
], "The {} is:", "Which ratio is {}?")
table("b12-04", [
    ("Blood group A", "IAIA or IAi"), ("Blood group B", "IBIB or IBi"), ("Blood group AB", "IAIB"), ("Blood group O", "ii"),
], "The possible genotypes for {} are:", "Which blood group has genotype {}?")
facts("b12-04", [
    "Mendel published his work in 1865",
    "Mendel's work was rediscovered in 1900 by de Vries, Correns and von Tschermak",
    "Sutton and Boveri proposed the chromosomal theory of inheritance",
    "Henking observed the X body in insects",
    "In Drosophila, white eye and yellow body genes are tightly linked",
    "Pleiotropy: one gene affects several traits, e.g. phenylketonuria",
], [
    "Mendel's work was rediscovered in 1950",
    "Morgan proposed the chromosomal theory of inheritance alone in 1850",
    "Henking observed the Y chromosome in humans",
    "Pleiotropy means many genes control one trait",
    "Mendel worked on Drosophila",
    "Mendel published his work in 1900",
], "history of genetics")
table("b12-05", [
    ("DNA polymerase", "Adds nucleotides during replication"), ("Helicase", "Unwinds the DNA double helix"), ("DNA ligase", "Joins Okazaki fragments"),
    ("RNA polymerase", "Makes RNA from a DNA template"), ("Reverse transcriptase", "Makes DNA from an RNA template"),
    ("Aminoacyl tRNA synthetase", "Charges tRNA with its amino acid"),
], "The enzyme {}:", "Which enzyme: {}?")
facts("b12-05", [
    "The ribosome's 23S rRNA acts as a ribozyme in bacteria",
    "tRNA has an anticodon loop and an amino acid acceptor end",
    "The untranslated regions (UTRs) are needed for efficient translation",
    "In bacteria transcription and translation can happen together",
    "RNA was probably the first genetic material",
    "DNA is more stable than RNA because of deoxyribose and thymine",
], [
    "In eukaryotes translation happens in the nucleus",
    "RNA is more stable than DNA",
    "tRNA has no anticodon",
    "UTRs are translated into protein",
    "The ribosome's rRNA has no catalytic role",
    "DNA has uracil in place of thymine",
], "gene expression")
table("b12-06", [
    ("Archaeopteryx", "Link between reptiles and birds"), ("Coelacanth", "Lobefin fish once thought extinct; ancestor of amphibians"),
    ("Thecodonts", "Reptiles that gave rise to dinosaurs"), ("Ichthyosaurs", "Fish-like reptiles about 200 mya"),
    ("Sauropsids", "Gave rise to reptiles and birds"), ("Synapsids", "Gave rise to mammals"),
], "{}:", "Which is: {}?")
facts("b12-06", [
    "Oparin and Haldane proposed that life arose from non-living organic molecules",
    "Life appeared about 4 billion years ago",
    "The Earth formed about 4.5 billion years ago",
    "Darwin travelled on HMS Beagle",
    "Alfred Wallace worked in the Malay Archipelago",
    "Founder effect is a kind of genetic drift",
], [
    "Life appeared about 400 years ago",
    "Darwin travelled on the Titanic",
    "Oparin proposed the theory of special creation",
    "The Earth formed 500 million years ago",
    "Founder effect is a kind of gene flow",
    "Wallace worked in the Arctic",
], "origin of life and evolution")
table("b12-07", [
    ("Salmonella typhi", "Typhoid; enters through contaminated food and water"), ("Streptococcus pneumoniae", "Pneumonia; droplets"),
    ("Rhinovirus", "Common cold; nose and respiratory passage"), ("Microsporum", "Ringworm; skin, nails, scalp"),
    ("Wuchereria bancrofti", "Filariasis; lymphatic vessels of lower limbs"), ("Entamoeba histolytica", "Amoebic dysentery; large intestine"),
], "{} causes:", "Which pathogen causes: {}?")
facts("b12-07", [
    "Edward Jenner developed the smallpox vaccine using cowpox",
    "Hepatitis B vaccine is made using yeast (recombinant DNA)",
    "Antihistamines, adrenaline and steroids reduce allergy symptoms",
    "Rheumatoid arthritis is an autoimmune disease",
    "Tobacco contains nicotine which raises blood pressure and heart rate",
    "Morphine is a very effective sedative and painkiller",
], [
    "Jenner developed the polio vaccine",
    "Hepatitis B vaccine is made from cowpox",
    "Rheumatoid arthritis is caused by a virus",
    "Nicotine lowers blood pressure",
    "Antihistamines increase allergy",
    "Morphine is a stimulant",
], "health and disease")
table("b12-08", [
    ("Saccharomyces cerevisiae", "Baker's and brewer's yeast; bread, beer, wine"), ("Lactobacillus", "Converts milk to curd"),
    ("Propionibacterium sharmanii", "Swiss cheese"), ("Aspergillus niger", "Citric acid"), ("Streptococcus", "Streptokinase"),
    ("Penicillium notatum", "Penicillin"),
], "{} is used for:", "Which microbe is used for: {}?")
table("b12-09", [
    ("Plasmid", "Extrachromosomal circular DNA that replicates on its own"), ("Vector", "Carries foreign DNA into a host"),
    ("Recombinant DNA", "DNA joined from two different sources"), ("Competent cell", "Cell able to take up DNA"),
    ("Selectable marker", "Gene that helps pick out transformants"), ("Cloning site", "Place in a vector where DNA is inserted"),
], "{}:", "Which term: {}?")
facts("b12-10", [
    "Bt cotton has cry genes from Bacillus thuringiensis",
    "Rosie produced milk with 2.4 grams of human protein per litre",
    "Transgenic animals are used to study diseases such as cancer and Alzheimer's",
    "Insulin was earlier extracted from the pancreas of cattle and pigs",
    "Gene therapy corrects a defective gene",
    "Molecular diagnosis can use PCR to detect low amounts of pathogens",
], [
    "Bt cotton has genes from Agrobacterium only",
    "Insulin was earlier extracted from human urine",
    "Gene therapy removes all genes from a cell",
    "PCR cannot detect pathogens",
    "Transgenic animals cannot be used to study diseases",
    "Rosie produced milk without any human protein",
], "biotechnology applications")
table("b12-11", [
    ("Regulate", "Maintain homeostasis, e.g. birds and mammals"), ("Conform", "Body temperature changes with the surroundings"),
    ("Migrate", "Move to a better area temporarily"), ("Suspend", "Reduce activity, e.g. hibernation or spores"),
], "Organisms that {}:", "Which response: {}?")
facts("b12-12", [
    "An ecosystem has biotic and abiotic components",
    "Stratification is vertical layering of plants in a forest",
    "Gross primary productivity is the rate of production of organic matter in photosynthesis",
    "The annual net primary productivity of the biosphere is about 170 billion tons (dry weight)",
    "Oceans contribute only about 55 billion tons despite covering 70% of the surface",
    "Grazing food chains start with producers",
], [
    "Oceans produce most of the biosphere's net primary productivity",
    "Stratification is horizontal zoning of soil",
    "An ecosystem has only biotic components",
    "Detritus food chains start with herbivores",
    "Gross primary productivity excludes photosynthesis",
    "Biosphere NPP is about 1 million tons a year",
], "ecosystem structure and productivity")
facts("b12-13", [
    "Biosphere reserves in India number 14 (as listed in NCERT)",
    "India has 90 national parks and 448 wildlife sanctuaries (NCERT figures)",
    "Over 1.5 million species have been described",
    "Over 70% of recorded species are animals",
    "Among animals, insects are the most species-rich group",
    "Fungi have more species than fishes, amphibians, reptiles and mammals combined",
], [
    "Plants make up over 70% of recorded species",
    "Mammals are the most species-rich animal group",
    "Fewer than 10,000 species have been described",
    "India has 5 national parks",
    "Fungi are less diverse than mammals",
    "Biosphere reserves are ex situ conservation",
], "biodiversity numbers")

tag(None)
