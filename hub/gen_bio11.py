"""NEET Biology, Class 11 (NCERT rationalised). Fact tables and checked statements."""
from .core import table, groups, facts, gen, num_q, Q

# ---------------------------------------------------------------- b11-01 The Living World
table("b11-01", [
    ("Herbarium", "A store of pressed, dried and preserved plant specimens on sheets"),
    ("Botanical garden", "Collections of living plants grown for identification"),
    ("Museum", "Preserved plant and animal specimens in jars or as skeletons"),
    ("Key", "A tool based on contrasting characters in pairs (couplets) for identification"),
    ("Monograph", "Information on any one taxon"),
    ("Flora", "An account of the habitat and distribution of the plants of an area"),
    ("Manual", "Information for identifying the names of species found in an area"),
    ("Catalogue", "An alphabetical listing of species"),
], "Which description fits the taxonomic aid '{}'?", "Which taxonomic aid is '{}'?")
table("b11-01", [
    ("Mango", "Mangifera indica"), ("Potato", "Solanum tuberosum"), ("Brinjal", "Solanum melongena"),
    ("Wheat", "Triticum aestivum"), ("Housefly", "Musca domestica"), ("Human", "Homo sapiens"),
    ("Lion", "Panthera leo"), ("Tiger", "Panthera tigris"), ("Leopard", "Panthera pardus"),
], "The scientific name of {} is:", "Which organism has the scientific name {}?")
table("b11-01", [
    ("Human", "Hominidae"), ("Housefly", "Muscidae"), ("Mango", "Anacardiaceae"), ("Wheat", "Poaceae"),
    ("Potato and brinjal", "Solanaceae"), ("Cat, tiger and leopard", "Felidae"), ("Dog", "Canidae"),
], "{} belong(s) to the family:", "Which organism(s) belong to the family {}?")
table("b11-01", [
    ("Human", "Primata"), ("Housefly", "Diptera"), ("Mango", "Sapindales"), ("Wheat", "Poales"),
    ("Dog", "Carnivora"),
], "{} belongs to the order:", "Which organism belongs to the order {}?")
facts("b11-01", [
    "Biological names are printed in italics when typed",
    "The generic name starts with a capital letter and the specific epithet with a small letter",
    "Binomial nomenclature was introduced by Carolus Linnaeus",
    "ICBN provides the rules for naming plants",
    "Species is the lowest category in the taxonomic hierarchy",
    "Kingdom is the highest category in the taxonomic hierarchy used by NCERT",
    "A genus is a group of related species",
    "Metabolism is a defining property of living organisms",
], [
    "The specific epithet always starts with a capital letter",
    "A genus is a group of related families",
    "A family includes several orders",
    "Binomial nomenclature was introduced by Charles Darwin",
    "ICZN provides the rules for naming plants",
    "Growth is a defining property of living organisms, since non-living things never grow",
    "Order is a lower category than family",
], "The Living World")

# ---------------------------------------------------------------- b11-02 Biological Classification
table("b11-02", [
    ("Gave the five kingdom classification (1969)", "R.H. Whittaker"),
    ("Proposed the two kingdom classification", "Carolus Linnaeus"),
    ("Called the infectious fluid of tobacco mosaic 'Contagium vivum fluidum'", "M.W. Beijerinck"),
    ("First recognised a tiny agent causing tobacco mosaic disease", "D.J. Ivanowsky"),
    ("Showed that viruses could be crystallised", "W.M. Stanley"),
    ("Discovered viroids (1971)", "T.O. Diener"),
], "{}:", "What is {} known for?")
table("b11-02", [
    ("Bacteria", "Monera"), ("Nostoc", "Monera"), ("Mycoplasma", "Monera"), ("Methanogens", "Monera"),
    ("Amoeba", "Protista"), ("Paramoecium", "Protista"), ("Diatoms", "Protista"), ("Euglena", "Protista"),
    ("Plasmodium", "Protista"), ("Slime moulds", "Protista"), ("Yeast", "Fungi"), ("Agaricus", "Fungi"),
    ("Penicillium", "Fungi"), ("Moss", "Plantae"), ("Fern", "Plantae"), ("Earthworm", "Animalia"),
], "In the five kingdom system, {} belongs to kingdom:", "Which of these belongs to kingdom {}?")
groups("b11-02", {
    "Phycomycetes": ["Mucor", "Rhizopus", "Albugo"],
    "Ascomycetes": ["Aspergillus", "Claviceps", "Neurospora"],
    "Basidiomycetes": ["Agaricus", "Ustilago", "Puccinia"],
    "Deuteromycetes": ["Alternaria", "Colletotrichum", "Trichoderma"],
}, "Which of these is NOT one of the {}?", "Which of these belongs to the {}?")
table("b11-02", [
    ("Ascomycetes", "Sac fungi"), ("Basidiomycetes", "Club fungi (mushrooms, bracket fungi, puffballs)"),
    ("Deuteromycetes", "Imperfect fungi (only asexual stage known)"),
    ("Phycomycetes", "Aseptate coenocytic mycelium; zoospores or aplanospores"),
], "Which description fits {}?", "Which class of fungi is described as: {}?")
table("b11-02", [
    ("Chrysophytes", "Diatoms and desmids with silica walls that form diatomaceous earth"),
    ("Dinoflagellates", "Red tides, e.g. Gonyaulax"),
    ("Euglenoids", "A protein-rich pellicle instead of a cell wall"),
    ("Slime moulds", "Saprophytic protists forming a plasmodium"),
    ("Sporozoans", "Infectious spore-like stage, e.g. Plasmodium"),
    ("Flagellated protozoans", "Trypanosoma, which causes sleeping sickness"),
    ("Ciliated protozoans", "Paramoecium, with a gullet and thousands of cilia"),
    ("Amoeboid protozoans", "Pseudopodia for movement and capturing prey"),
], "Which feature or example belongs to {}?", "Which protist group shows: {}?")
table("b11-02", [
    ("Archaebacteria", "Live in extreme habitats such as hot springs and salty areas"),
    ("Methanogens", "Produce methane (biogas) in the gut of ruminants"),
    ("Cyanobacteria", "Fix nitrogen in heterocysts, e.g. Nostoc and Anabaena"),
    ("Mycoplasma", "Lack a cell wall; the smallest living cells"),
    ("Viroids", "Free RNA without a protein coat; cause potato spindle tuber disease"),
    ("Prions", "Abnormally folded proteins; cause mad cow disease (BSE)"),
    ("Lichens", "Algae and fungi in symbiosis; indicators of air pollution"),
], "{}:", "Which of these is described as: {}?")
facts("b11-02", [
    "Tobacco mosaic virus contains RNA",
    "Bacteriophages usually have double-stranded DNA",
    "The fungal partner of a lichen is the mycobiont",
    "Diatoms are chief producers in the oceans",
    "Fungal cell walls are made of chitin and polysaccharides",
    "Heterocysts are found in some cyanobacteria",
    "Mycoplasma can survive without oxygen",
], [
    "Viruses have their own cell membrane",
    "Prions are made only of RNA",
    "Lichens grow well in heavily polluted areas",
    "Euglenoids have a cellulose cell wall",
    "Deuteromycetes reproduce mainly by sexual spores",
    "Viroids have a protein coat",
    "All bacteria are autotrophs",
], "Biological Classification")

# ---------------------------------------------------------------- b11-03 Plant Kingdom
table("b11-03", [
    ("Chlorophyceae", "Starch"), ("Phaeophyceae", "Mannitol and laminarin"), ("Rhodophyceae", "Floridean starch"),
], "The stored food of {} is:", "Which class of algae stores {}?")
table("b11-03", [
    ("Chlorophyceae", "Chlorophyll a and b"), ("Phaeophyceae", "Chlorophyll a, c and fucoxanthin"),
    ("Rhodophyceae", "Chlorophyll a, d and phycoerythrin"),
], "The main pigments of {} are:", "Which class of algae has {}?")
groups("b11-03", {
    "green algae": ["Chlamydomonas", "Volvox", "Spirogyra", "Ulothrix", "Chara"],
    "brown algae": ["Ectocarpus", "Dictyota", "Laminaria", "Sargassum", "Fucus"],
    "red algae": ["Polysiphonia", "Porphyra", "Gracilaria", "Gelidium"],
    "bryophytes": ["Marchantia", "Funaria", "Sphagnum", "Polytrichum"],
    "pteridophytes": ["Selaginella", "Equisetum", "Dryopteris", "Adiantum", "Salvinia"],
    "gymnosperms": ["Cycas", "Pinus", "Ginkgo", "Sequoia"],
}, "Which of these is NOT one of the {}?", "Which of these is one of the {}?", weight=2)
table("b11-03", [
    ("Haplontic life cycle", "Volvox and Spirogyra"),
    ("Diplontic life cycle", "Gymnosperms, angiosperms and Fucus"),
    ("Haplo-diplontic life cycle", "Bryophytes, pteridophytes, Ectocarpus and Polysiphonia"),
], "Which organisms show a {}?", "{} show which life cycle pattern?")
table("b11-03", [
    ("Agar used in microbiology", "Gelidium and Gracilaria"),
    ("Single-cell protein food supplement", "Chlorella"),
    ("Algin", "Brown algae"),
    ("Carrageen", "Red algae"),
    ("Peat used as fuel and packing", "Sphagnum"),
    ("Coralloid roots with cyanobacteria", "Cycas"),
    ("Tallest tree species", "Sequoia"),
    ("Gemmae for vegetative reproduction", "Marchantia"),
], "{} comes from or is seen in:", "What is associated with {}?")
facts("b11-03", [
    "Bryophytes are called the amphibians of the plant kingdom",
    "In bryophytes the main plant body is the haploid gametophyte",
    "Pteridophytes are the first terrestrial plants with xylem and phloem",
    "The gametophyte of pteridophytes is called the prothallus",
    "Selaginella and Salvinia are heterosporous",
    "Gymnosperm seeds are not covered by a fruit wall",
    "In angiosperms the endosperm is triploid",
    "Pinus roots form mycorrhiza with fungi",
    "The first stage of a moss gametophyte is the protonema",
], [
    "In bryophytes the main plant body is the diploid sporophyte",
    "Gymnosperms show double fertilisation",
    "Pteridophytes produce seeds",
    "Red algae store mannitol",
    "In angiosperms the endosperm is diploid",
    "Bryophytes have true xylem and phloem",
    "Sphagnum is a liverwort",
], "Plant Kingdom")

# ---------------------------------------------------------------- b11-04 Animal Kingdom
_ANIMALS = [
    ("Physalia", "Portuguese man-of-war"), ("Adamsia", "Sea anemone"), ("Pennatula", "Sea-pen"),
    ("Gorgonia", "Sea-fan"), ("Meandrina", "Brain coral"), ("Pleurobrachia", "Comb jelly"),
    ("Hirudinaria", "Blood-sucking leech"), ("Laccifer", "Lac insect"), ("Bombyx", "Silkworm"),
    ("Limulus", "King crab (living fossil)"), ("Pinctada", "Pearl oyster"), ("Sepia", "Cuttlefish"),
    ("Loligo", "Squid"), ("Octopus", "Devil fish"), ("Aplysia", "Sea-hare"), ("Dentalium", "Tusk shell"),
    ("Chaetopleura", "Chiton"), ("Asterias", "Star fish"), ("Echinus", "Sea urchin"), ("Antedon", "Sea lily"),
    ("Cucumaria", "Sea cucumber"), ("Ophiura", "Brittle star"), ("Exocoetus", "Flying fish"),
    ("Hippocampus", "Sea horse"), ("Labeo", "Rohu"), ("Catla", "Katla"), ("Clarias", "Magur"),
    ("Betta", "Fighting fish"), ("Pterophyllum", "Angel fish"), ("Scoliodon", "Dog fish"), ("Pristis", "Saw fish"),
    ("Carcharodon", "Great white shark"), ("Trygon", "Sting ray"), ("Torpedo", "Electric ray"),
    ("Petromyzon", "Lamprey"), ("Myxine", "Hagfish"), ("Bufo", "Toad"), ("Rana", "Frog"), ("Hyla", "Tree frog"),
    ("Salamandra", "Salamander"), ("Ichthyophis", "Limbless amphibian"), ("Chelone", "Turtle"),
    ("Testudo", "Tortoise"), ("Calotes", "Garden lizard"), ("Hemidactylus", "Wall lizard"), ("Naja", "Cobra"),
    ("Bangarus", "Krait"), ("Corvus", "Crow"), ("Columba", "Pigeon"), ("Psittacula", "Parrot"),
    ("Struthio", "Ostrich"), ("Pavo", "Peacock"), ("Aptenodytes", "Penguin"), ("Neophron", "Vulture"),
    ("Ornithorhynchus", "Platypus"), ("Macropus", "Kangaroo"), ("Pteropus", "Flying fox"),
    ("Balaenoptera", "Blue whale"), ("Delphinus", "Common dolphin"),
]
table("b11-04", _ANIMALS, "The common name of {} is:", "{} is the common name of which genus?", weight=3)
groups("b11-04", {
    "Porifera": ["Sycon", "Spongilla", "Euspongia"],
    "Cnidaria": ["Physalia", "Adamsia", "Pennatula", "Meandrina", "Aurelia"],
    "Ctenophora": ["Pleurobrachia", "Ctenoplana", "Beroe"],
    "Platyhelminthes": ["Taenia", "Fasciola", "Planaria"],
    "Aschelminthes": ["Ascaris", "Wuchereria", "Ancylostoma"],
    "Annelida": ["Nereis", "Pheretima", "Hirudinaria"],
    "Arthropoda": ["Apis", "Bombyx", "Anopheles", "Locusta", "Limulus"],
    "Mollusca": ["Pila", "Pinctada", "Sepia", "Octopus", "Aplysia"],
    "Echinodermata": ["Asterias", "Echinus", "Antedon", "Cucumaria", "Ophiura"],
    "Hemichordata": ["Balanoglossus", "Saccoglossus", "Ptychodera"],
}, "Which of these does NOT belong to phylum {}?", "Which of these belongs to phylum {}?", weight=3)
groups("b11-04", {
    "Cyclostomata": ["Petromyzon", "Myxine", "Lampetra"],
    "Chondrichthyes": ["Scoliodon", "Pristis", "Carcharodon", "Trygon", "Torpedo"],
    "Osteichthyes": ["Exocoetus", "Hippocampus", "Labeo", "Catla", "Betta"],
    "Amphibia": ["Bufo", "Rana", "Hyla", "Salamandra", "Ichthyophis"],
    "Reptilia": ["Chelone", "Testudo", "Calotes", "Naja", "Hemidactylus"],
    "Aves": ["Corvus", "Columba", "Struthio", "Pavo", "Neophron"],
    "Mammalia": ["Ornithorhynchus", "Macropus", "Pteropus", "Balaenoptera", "Delphinus"],
}, "Which of these is NOT a member of class {}?", "Which of these belongs to class {}?", weight=2)
table("b11-04", [
    ("Porifera", "Canal system with ostia, osculum and choanocytes"),
    ("Cnidaria", "Cnidoblasts (stinging cells) on tentacles"),
    ("Ctenophora", "Eight external rows of ciliated comb plates"),
    ("Platyhelminthes", "Flame cells for excretion; dorsoventrally flattened body"),
    ("Aschelminthes", "Pseudocoelom; body circular in cross-section"),
    ("Annelida", "Metameric segmentation and nephridia"),
    ("Arthropoda", "Jointed appendages and chitinous exoskeleton; the largest phylum"),
    ("Mollusca", "Mantle, and a rasping radula in the mouth"),
    ("Echinodermata", "Water vascular system; radially symmetrical adults"),
    ("Hemichordata", "Body of proboscis, collar and trunk"),
], "A key feature of phylum {} is:", "Which phylum has this feature: {}?", weight=2)
facts("b11-04", [
    "Cnidarians such as Obelia show metagenesis (alternation of polyp and medusa)",
    "Ctenophores show bioluminescence",
    "Platypus is an egg-laying mammal",
    "Crocodiles have a four-chambered heart",
    "Birds have pneumatic bones",
    "Torpedo has electric organs",
    "Cartilaginous fishes lack an air bladder",
    "Echinoderm larvae are bilaterally symmetrical",
    "Arthropods excrete through Malpighian tubules",
], [
    "Annelids have a pseudocoelom",
    "Sponges have true tissues",
    "Amphibians have a four-chambered heart",
    "Bony fishes have a placoid scale covering",
    "Flatworms are triploblastic coelomates",
    "Mammals are cold-blooded",
    "Hemichordates have a notochord along the whole body",
], "Animal Kingdom")

# ---------------------------------------------------------------- b11-05 Morphology of Flowering Plants
table("b11-05", [
    ("Prop roots", "Banyan tree"), ("Stilt roots", "Maize and sugarcane"),
    ("Pneumatophores", "Rhizophora (mangroves)"), ("Storage tap roots", "Carrot and turnip"),
    ("Storage adventitious roots", "Sweet potato"), ("Stem tendrils", "Cucumber, pumpkin and grapevine"),
    ("Stem thorns", "Citrus and Bougainvillea"), ("Phylloclade (flattened green stem)", "Opuntia"),
    ("Underground storage stems", "Potato, ginger and turmeric"), ("Offset", "Pistia and Eichhornia"),
    ("Sucker", "Banana, pineapple and Chrysanthemum"), ("Leaf tendrils", "Pea"),
    ("Leaf spines", "Cacti"), ("Fleshy storage leaves", "Onion and garlic"),
    ("Insect-trapping leaves", "Pitcher plant and Venus fly trap"), ("Phyllode", "Australian Acacia"),
], "Which plant shows {}?", "{} shows which modification?", weight=2)
table("b11-05", [
    ("Alternate phyllotaxy", "China rose, mustard and sunflower"),
    ("Opposite phyllotaxy", "Calotropis and guava"),
    ("Whorled phyllotaxy", "Alstonia"),
    ("Marginal placentation", "Pea"),
    ("Axile placentation", "China rose, tomato and lemon"),
    ("Parietal placentation", "Mustard and Argemone"),
    ("Free central placentation", "Dianthus and Primrose"),
    ("Basal placentation", "Sunflower and marigold"),
    ("Valvate aestivation", "Calotropis"),
    ("Twisted aestivation", "China rose, lady's finger and cotton"),
    ("Imbricate aestivation", "Cassia and gulmohur"),
    ("Vexillary aestivation", "Pea and bean"),
    ("Hypogynous flower", "Mustard, china rose and brinjal"),
    ("Perigynous flower", "Plum, rose and peach"),
    ("Epigynous flower", "Guava, cucumber and ray florets of sunflower"),
], "Which plants show {}?", "{} show(s) which arrangement?", weight=3)
table("b11-05", [
    ("Fabaceae", "Pea: vexillary aestivation and diadelphous stamens"),
    ("Solanaceae", "Brinjal: swollen axile placenta and persistent calyx"),
    ("Liliaceae", "Onion: trimerous perianth (tepals) and superior trilocular ovary"),
], "Which description fits family {}?", "Which family is described as: {}?")
facts("b11-05", [
    "Dicotyledonous plants usually have a tap root system",
    "Monocots usually show parallel venation",
    "Neem has pinnately compound leaves",
    "Silk cotton has palmately compound leaves",
    "A parthenocarpic fruit develops without fertilisation",
    "Mango and coconut fruits are drupes",
    "In racemose inflorescence the main axis keeps growing",
], [
    "Monocots usually have a tap root system",
    "Dicots usually show parallel venation",
    "In cymose inflorescence the main axis keeps growing",
    "Potato tuber is a modified root",
    "Sweet potato is a modified stem",
    "Ginger is a modified root",
    "Mustard flowers are epigynous",
], "Morphology of Flowering Plants")

# ---------------------------------------------------------------- b11-06 Anatomy of Flowering Plants
table("b11-06", [
    ("Intercalary meristem", "Grasses, regenerating parts removed by grazers"),
    ("Collenchyma", "Cells thickened at the corners with cellulose, hemicellulose and pectin"),
    ("Sclereids", "Hard cells in the pulp of guava, pear and sapota"),
    ("Companion cells", "Linked to sieve tubes by pit fields"),
    ("Bulliform cells", "Large empty cells in grass leaves that roll the leaf when water is short"),
    ("Casparian strips", "Suberin bands on the walls of endodermal cells"),
    ("Pericycle", "Gives rise to lateral roots"),
    ("Phellogen", "Cork cambium"),
    ("Lenticels", "Lens-shaped openings in the bark for gas exchange"),
    ("Heartwood (duramen)", "Dark, non-conducting central wood filled with tannins and resins"),
    ("Sapwood (alburnum)", "Light, peripheral wood that conducts water"),
    ("Annual ring", "One spring wood plus one autumn wood layer"),
], "Which description fits {}?", "Which tissue or structure is described as: {}?", weight=2)
table("b11-06", [
    ("Radial vascular bundles", "Roots"), ("Conjoint closed vascular bundles", "Monocot stems"),
    ("Conjoint open vascular bundles", "Dicot stems"), ("Exarch xylem", "Roots"), ("Endarch xylem", "Stems"),
    ("Dumb-bell shaped guard cells", "Grasses"), ("Bean-shaped guard cells", "Dicots"),
], "{} are found in:", None)
facts("b11-06", [
    "Phloem parenchyma is absent in most monocots",
    "Vascular cambium is present in dicot stems",
    "Monocot stems have scattered vascular bundles",
    "Periderm consists of phellem, phellogen and phelloderm",
    "Spring wood has wider vessels than autumn wood",
    "Tracheids and vessels are the main water-conducting elements",
], [
    "Monocot stems have a ring of open vascular bundles",
    "Sieve tubes have a large nucleus at maturity",
    "Roots show endarch xylem",
    "Heartwood conducts most of the water",
    "Collenchyma cells are dead at maturity",
    "Sclereids are living cells with thin walls",
], "Anatomy of Flowering Plants")

# ---------------------------------------------------------------- b11-07 Structural Organisation in Animals
table("b11-07", [
    ("Squamous epithelium", "Walls of blood vessels and air sacs of lungs"),
    ("Cuboidal epithelium", "Ducts of glands and tubular parts of nephrons"),
    ("Columnar epithelium", "Lining of the stomach and intestine"),
    ("Ciliated epithelium", "Bronchioles and fallopian tubes"),
    ("Compound epithelium", "Moist surface of buccal cavity and pharynx"),
    ("Areolar tissue", "Beneath the skin"),
    ("Dense regular tissue (tendon)", "Attaches skeletal muscle to bone"),
    ("Dense regular tissue (ligament)", "Attaches one bone to another"),
    ("Cartilage", "Tip of the nose and the outer ear"),
    ("Cardiac muscle", "Heart wall, with intercalated discs"),
    ("Smooth muscle", "Walls of internal organs such as blood vessels and intestine"),
], "Where is {} found (or what does it do)?", "Which tissue is found in or does: {}?", weight=2)
table("b11-07", [
    ("Tight junctions", "Stop substances leaking across a tissue"),
    ("Adhering junctions", "Cement neighbouring cells together"),
    ("Gap junctions", "Connect the cytoplasm of adjoining cells for rapid transfer of ions and molecules"),
], "The role of {} is to:", "Which junctions {}?")
table("b11-07", [
    ("Hepatic caeca of cockroach", "At the junction of foregut and midgut"),
    ("Malpighian tubules of cockroach", "At the junction of midgut and hindgut"),
    ("Mushroom-shaped gland of cockroach", "6th and 7th abdominal segments of the male"),
    ("Spermatheca of cockroach", "6th abdominal segment of the female"),
    ("Gizzard (proventriculus) of cockroach", "Grinds food with chitinous teeth"),
    ("Anal styles of cockroach", "Present only in males"),
], "Location or feature of {}:", "Which part of the cockroach is described: {}?")
facts("b11-07", [
    "Cockroach has an open circulatory system",
    "The heart of cockroach has 13 chambers",
    "Cockroach has 10 pairs of spiracles",
    "Each compound eye of cockroach has about 2000 ommatidia",
    "Cockroach nymphs moult about 13 times",
    "Neuroglia make up more than half the volume of neural tissue",
    "Bone has a hard matrix of calcium salts and collagen",
], [
    "Cockroach has a closed circulatory system",
    "Cockroach development is holometabolous with a pupa",
    "Cardiac muscle is voluntary",
    "Tendons attach bone to bone",
    "Smooth muscle fibres are striated",
    "Blood is an epithelial tissue",
], "Structural Organisation in Animals")

# ---------------------------------------------------------------- b11-08 Cell: The Unit of Life
table("b11-08", [
    ("Cell theory (plants and animals)", "Schleiden and Schwann"),
    ("Omnis cellula-e cellula (cells arise from pre-existing cells)", "Rudolf Virchow"),
    ("Discovered the nucleus", "Robert Brown"),
    ("Fluid mosaic model of the membrane (1972)", "Singer and Nicolson"),
    ("Described the Golgi apparatus (1898)", "Camillo Golgi"),
], "{}:", "What is {} known for?")
table("b11-08", [
    ("Rough endoplasmic reticulum", "Protein synthesis and secretion"),
    ("Smooth endoplasmic reticulum", "Lipid synthesis, including steroidal hormones in animals"),
    ("Golgi apparatus", "Packaging materials and forming glycoproteins and glycolipids"),
    ("Lysosomes", "Hydrolytic enzymes active at acidic pH"),
    ("Mitochondria", "Aerobic respiration; the cell's powerhouse"),
    ("Chloroplasts", "Photosynthesis"),
    ("Ribosomes", "Sites of protein synthesis"),
    ("Nucleolus", "Active ribosomal RNA synthesis"),
    ("Centrioles", "Form basal bodies of cilia and the spindle in animal cells"),
    ("Mesosomes", "Infoldings of the bacterial membrane that help in respiration and DNA replication"),
    ("Vacuole membrane (tonoplast)", "Transports ions into the vacuole against a concentration gradient"),
], "The main role of {} is:", "Which organelle is responsible for: {}?", weight=2)
table("b11-08", [
    ("Metacentric chromosome", "Centromere in the middle, two equal arms"),
    ("Sub-metacentric chromosome", "Centromere slightly away from the middle"),
    ("Acrocentric chromosome", "Centromere very close to one end"),
    ("Telocentric chromosome", "Centromere at the very end"),
], "Which description fits a {}?", "Which chromosome type has: {}?")
facts("b11-08", [
    "Prokaryotic ribosomes are 70S, made of 50S and 30S subunits",
    "Eukaryotic ribosomes are 80S, made of 60S and 40S subunits",
    "Mitochondria and chloroplasts contain their own DNA",
    "Cilia and flagella have a 9+2 arrangement of microtubules",
    "Centrioles have a 9+0 cartwheel arrangement of triplets",
    "Mycoplasma is the smallest known cell (about 0.3 micrometre)",
    "Plasmids give some bacteria resistance to antibiotics",
    "The inner mitochondrial membrane forms cristae",
], [
    "Prokaryotic cells have a membrane-bound nucleus",
    "Lysosomes are formed by mitochondria",
    "Ribosomes are surrounded by a double membrane",
    "Centrioles are present in most higher plant cells",
    "The nuclear envelope is a single membrane",
    "Chloroplasts are found in animal cells",
    "Eukaryotic ribosomes are 70S",
], "Cell: The Unit of Life", weight=2)

# ---------------------------------------------------------------- b11-09 Biomolecules
table("b11-09", [
    ("Collagen", "Intercellular ground substance; most abundant animal protein"),
    ("Trypsin", "Enzyme"), ("Insulin", "Hormone"), ("Antibody", "Fights infectious agents"),
    ("Receptor", "Sensory reception (smell, taste, hormones)"), ("GLUT-4", "Enables glucose transport into cells"),
    ("RuBisCO", "Most abundant protein in the whole biosphere"),
], "The role of {} is:", "Which protein: {}?")
table("b11-09", [
    ("Cellulose", "Homopolymer of glucose that cannot hold iodine"),
    ("Starch", "Plant storage polysaccharide that gives blue colour with iodine"),
    ("Glycogen", "Animal storage polysaccharide"),
    ("Inulin", "Polymer of fructose"),
    ("Chitin", "Complex polysaccharide of amino sugars in arthropod exoskeletons"),
], "Which description fits {}?", "Which polysaccharide is: {}?")
table("b11-09", [
    ("Oxidoreductases", "Catalyse oxidation-reduction between two substrates"),
    ("Transferases", "Transfer a group (other than hydrogen) between substrates"),
    ("Hydrolases", "Break bonds by adding water"),
    ("Lyases", "Remove groups from substrates by mechanisms other than hydrolysis, leaving double bonds"),
    ("Isomerases", "Inter-convert optical, geometric or positional isomers"),
    ("Ligases", "Join two compounds, e.g. C-O, C-S, C-N bonds"),
], "Enzymes of the class {}:", "Which enzyme class does this: {}?")
table("b11-09", [
    ("Glycine", "R group is hydrogen"), ("Alanine", "R group is a methyl group"),
    ("Serine", "R group is a hydroxymethyl group"),
], "In {}, the:", "Which amino acid has: {}?")
table("b11-09", [
    ("Haem in peroxidase and catalase", "Prosthetic group"), ("NAD and NADP", "Coenzymes"),
    ("Zinc in carboxypeptidase", "Metal ion cofactor"),
], "{} is an example of a:", None)
facts("b11-09", [
    "Malonate inhibits succinic dehydrogenase by competing with succinate",
    "Amino acids are joined by peptide bonds",
    "Monosaccharides are joined by glycosidic bonds",
    "Nucleotides in a nucleic acid are joined by phosphodiester bonds",
    "Lipids are not strictly macromolecules",
    "Enzymes lower the activation energy of a reaction",
    "Uridine is a nucleoside found in RNA",
], [
    "Cellulose gives a blue colour with iodine",
    "Inulin is a polymer of glucose",
    "Enzymes raise the activation energy of a reaction",
    "Competitive inhibitors bind to a site far from the active site",
    "Thymidine is found mainly in RNA",
    "Glycine has a methyl R group",
], "Biomolecules")

# ---------------------------------------------------------------- b11-10 Cell Cycle and Cell Division
table("b11-10", [
    ("G1 phase", "Cell grows and is metabolically active, but DNA does not replicate"),
    ("S phase", "DNA is replicated and centrioles duplicate in animal cells"),
    ("G2 phase", "Proteins needed for mitosis are made"),
    ("G0 phase", "Quiescent stage; cell stays inactive"),
    ("Prophase", "Chromatin condenses and the spindle begins to form"),
    ("Metaphase", "Chromosomes line up at the equatorial plate; best stage to study chromosome shape"),
    ("Anaphase", "Centromeres split and chromatids move to opposite poles"),
    ("Telophase", "Nuclear envelope, nucleolus, Golgi and ER re-form"),
], "What happens in {}?", "In which phase does this happen: {}?", weight=2)
table("b11-10", [
    ("Leptotene", "Chromosomes become gradually visible"),
    ("Zygotene", "Synapsis of homologous chromosomes; synaptonemal complex forms"),
    ("Pachytene", "Crossing over between non-sister chromatids; recombination nodules appear"),
    ("Diplotene", "Synaptonemal complex dissolves and chiasmata are seen"),
    ("Diakinesis", "Terminalisation of chiasmata"),
], "In {} of meiosis I:", "Which substage of prophase I: {}?", weight=2)
facts("b11-10", [
    "A typical human cell divides about once every 24 hours",
    "Yeast completes its cell cycle in about 90 minutes",
    "Mitosis in a human cell lasts only about an hour",
    "In plant cells, cytokinesis occurs by cell plate formation",
    "Meiosis reduces the chromosome number by half",
    "Crossing over is catalysed by the enzyme recombinase",
    "Diplotene can last for months or years in the oocytes of some vertebrates",
], [
    "DNA replicates during G2 phase",
    "Interphase is the shortest phase of the cell cycle",
    "Crossing over occurs in zygotene",
    "Mitosis happens only in diploid cells",
    "Chromosome number doubles in S phase",
    "Plant cells divide by furrowing of the membrane",
], "Cell Cycle", weight=2)


@gen("b11-10", weight=2)
def _chromatids(rng):
    n = rng.choice([8, 10, 12, 14, 16, 20, 24, 46])
    stage = rng.choice(["chromosomes at metaphase of mitosis", "chromatids at metaphase of mitosis",
                        "chromosomes in each daughter cell after mitosis", "chromosomes in each cell after meiosis II",
                        "chromatids at metaphase I of meiosis"])
    val = {"chromosomes at metaphase of mitosis": n, "chromatids at metaphase of mitosis": 2 * n,
           "chromosomes in each daughter cell after mitosis": n, "chromosomes in each cell after meiosis II": n // 2,
           "chromatids at metaphase I of meiosis": 2 * n}[stage]
    wrong = {n, 2 * n, n // 2, 4 * n} - {val}
    return Q(f"A diploid cell has {n} chromosomes in G1. How many {stage}?", str(val), [str(x) for x in wrong],
             f"G1 has {n} chromosomes; after S phase each has two chromatids. Answer: {val}.")


# ---------------------------------------------------------------- b11-11 Photosynthesis
table("b11-11", [
    ("Showed plants restore 'bad air' using a candle and mouse in a bell jar (1770)", "Joseph Priestley"),
    ("Showed sunlight is needed and only green parts release oxygen", "Jan Ingenhousz"),
    ("Showed glucose is made and stored as starch in green parts", "Julius von Sachs"),
    ("Described the first action spectrum using Cladophora and aerobic bacteria", "T.W. Engelmann"),
    ("Showed oxygen in photosynthesis comes from water, using sulphur bacteria", "Cornelius van Niel"),
    ("Traced the C3 pathway (Calvin cycle)", "Melvin Calvin"),
    ("Worked out the C4 pathway", "Hatch and Slack"),
], "{}:", "What is {} known for?", weight=2)
table("b11-11", [
    ("Chlorophyll a", "Bright or blue-green; the chief pigment"), ("Chlorophyll b", "Yellow-green"),
    ("Xanthophylls", "Yellow"), ("Carotenoids", "Yellow to yellow-orange"),
], "On chromatography, {} appears:", "Which pigment appears {}?")
table("b11-11", [
    ("Reaction centre of photosystem I", "P700"), ("Reaction centre of photosystem II", "P680"),
    ("First stable product in C3 plants", "3-phosphoglyceric acid (PGA)"),
    ("First stable product in C4 plants", "Oxaloacetic acid (OAA)"),
    ("Primary CO2 acceptor in C4 mesophyll cells", "Phosphoenol pyruvate (PEP)"),
    ("Primary CO2 acceptor in the Calvin cycle", "Ribulose bisphosphate (RuBP)"),
    ("Enzyme fixing CO2 in C4 mesophyll", "PEP carboxylase"),
    ("Enzyme fixing CO2 in the Calvin cycle", "RuBisCO"),
    ("Splitting of water", "Photosystem II side, releasing oxygen"),
    ("ATP synthase part in the thylakoid membrane", "CF0"),
], "{}:", "What is: {}?", weight=2)
facts("b11-11", [
    "Cyclic photophosphorylation involves only PS I and makes ATP but no NADPH",
    "Cyclic photophosphorylation occurs in the stroma lamellae",
    "Non-cyclic photophosphorylation makes both ATP and NADPH",
    "Kranz anatomy is seen in C4 plants such as maize and sorghum",
    "Photorespiration occurs in C3 plants, not in C4 plants",
    "Six turns of the Calvin cycle make one glucose molecule",
    "Making one glucose in the Calvin cycle needs 18 ATP and 12 NADPH",
    "Blackman's law of limiting factors applies to photosynthesis",
], [
    "Photolysis of water occurs on the PS I side",
    "C4 plants show high photorespiration",
    "The Calvin cycle occurs in the thylakoid lumen",
    "The light reaction produces glucose directly",
    "RuBisCO has no oxygenase activity",
    "PEP carboxylase is found in the bundle sheath of C4 plants",
], "Photosynthesis in Higher Plants", weight=2)

# ---------------------------------------------------------------- b11-12 Respiration in Plants
table("b11-12", [
    ("Glycolysis", "Cytoplasm"), ("Krebs cycle", "Mitochondrial matrix"),
    ("Oxidative decarboxylation of pyruvate", "Mitochondrial matrix (pyruvate dehydrogenase)"),
    ("Electron transport system", "Inner mitochondrial membrane"),
    ("Alcoholic fermentation", "Yeast cytoplasm"),
], "Where does {} take place?", None)
table("b11-12", [
    ("Complex I", "NADH dehydrogenase"), ("Complex III", "Cytochrome bc1 complex"),
    ("Complex IV", "Cytochrome c oxidase (cytochromes a and a3 with two copper centres)"),
    ("Complex V", "ATP synthase"),
], "{} of the electron transport chain is:", "Which complex is {}?")
table("b11-12", [
    ("Carbohydrates", "1"), ("Fats such as tripalmitin", "0.7"), ("Proteins", "about 0.9"),
], "The respiratory quotient (RQ) of {} is:", "Which substrate has an RQ of {}?")
facts("b11-12", [
    "Glycolysis is also called the EMP pathway",
    "Pyruvate is the end product of glycolysis",
    "Oxygen is the final electron acceptor in aerobic respiration",
    "Ubiquinone carries electrons from complexes I and II to complex III",
    "In muscles, lack of oxygen converts pyruvate to lactic acid",
    "The respiratory pathway is amphibolic",
    "Citric acid is the first product of the Krebs cycle",
    "Complete aerobic respiration of one glucose gives a net 38 ATP (theoretical)",
], [
    "Glycolysis occurs in the mitochondria",
    "The Krebs cycle occurs on the outer mitochondrial membrane",
    "Fermentation produces more ATP than aerobic respiration",
    "Fats have an RQ greater than 1",
    "Carbon dioxide is the final electron acceptor",
    "Yeast fermentation gives lactic acid",
], "Respiration in Plants", weight=2)


@gen("b11-12")
def _rq(rng):
    co2, o2 = rng.choice([(6, 6), (102, 145), (12, 12), (16, 23), (4, 4)])
    rq = co2 / o2
    return num_q(rng, f"A substrate releases {co2} molecules of CO2 while consuming {o2} molecules of O2. Its RQ is:",
                 rq, explanation=f"RQ = CO2 released / O2 consumed = {co2}/{o2}.", form=lambda x: f"{x:.2f}")


# ---------------------------------------------------------------- b11-13 Plant Growth and Development
table("b11-13", [
    ("Auxins", "Apical dominance, rooting of stem cuttings and preventing fruit drop"),
    ("Gibberellins", "Bolting in beet and cabbage, and longer sugarcane stems"),
    ("Cytokinins", "Cell division, overcoming apical dominance and delaying leaf senescence"),
    ("Ethylene", "Fruit ripening and more female flowers in cucumber"),
    ("Abscisic acid", "Stomatal closure and seed dormancy under stress"),
], "A typical effect of {} is:", "Which plant hormone causes: {}?", weight=2)
table("b11-13", [
    ("Auxin first isolated", "From human urine"),
    ("Gibberellin discovered", "From bakanae (foolish seedling) disease of rice caused by Gibberella fujikuroi"),
    ("Kinetin discovered", "From autoclaved herring sperm DNA"),
    ("Zeatin isolated", "From corn kernels and coconut milk"),
    ("Abscisic acid also called", "Inhibitor-B, abscission II and dormin"),
    ("Coleoptile phototropism observed", "By Charles and Francis Darwin in canary grass"),
    ("Auxin isolated from coleoptile tips", "By F.W. Went using oat seedlings"),
], "{}:", None)
facts("b11-13", [
    "2,4-D is used to kill dicotyledonous weeds",
    "Ethephon releases ethylene and hastens fruit ripening",
    "Ethylene is a gaseous plant hormone",
    "Gibberellins speed up malting in the brewing industry",
    "Heterophylly in buttercup is caused by the environment",
    "Plant growth is generally indeterminate",
    "Growth in plants follows a sigmoid curve under natural conditions",
], [
    "Abscisic acid promotes seed germination",
    "Cytokinins promote apical dominance",
    "Ethylene delays fruit ripening",
    "Auxins are gases",
    "Gibberellins cause stomatal closure",
    "2,4-D is used to kill monocot weeds such as grasses",
], "Plant Growth and Development")

# ---------------------------------------------------------------- b11-14 Breathing and Exchange of Gases
table("b11-14", [
    ("Tidal volume", "About 500 mL"), ("Inspiratory reserve volume", "About 2500-3000 mL"),
    ("Expiratory reserve volume", "About 1000-1100 mL"), ("Residual volume", "About 1100-1200 mL"),
], "In a healthy adult, the {} is:", "Which lung volume is {}?")
table("b11-14", [
    ("Inspiratory capacity", "TV + IRV"), ("Expiratory capacity", "TV + ERV"),
    ("Functional residual capacity", "ERV + RV"), ("Vital capacity", "ERV + TV + IRV"),
    ("Total lung capacity", "VC + RV"),
], "{} equals:", "Which capacity equals {}?")
table("b11-14", [
    ("pO2 in alveoli", "104 mm Hg"), ("pCO2 in alveoli", "40 mm Hg"),
    ("pO2 in deoxygenated blood", "40 mm Hg"), ("pCO2 in deoxygenated blood", "45 mm Hg"),
    ("pO2 in oxygenated blood", "95 mm Hg"), ("pO2 in atmospheric air", "159 mm Hg"),
], "{} is about:", None)
table("b11-14", [
    ("Sponges, coelenterates and flatworms", "Simple diffusion over the body surface"),
    ("Earthworm", "Moist cuticle"), ("Insects", "Tracheal tubes"),
    ("Aquatic arthropods and molluscs", "Gills"), ("Frogs (in addition to lungs)", "Moist skin"),
], "Breathing in {} is through:", None)
facts("b11-14", [
    "About 97 per cent of oxygen is transported by RBCs as oxyhaemoglobin",
    "About 70 per cent of CO2 is carried as bicarbonate",
    "About 20-25 per cent of CO2 is carried as carbamino-haemoglobin",
    "CO2 is 20-25 times more soluble than O2",
    "The respiratory rhythm centre is in the medulla",
    "The pneumotaxic centre is in the pons",
    "Every 100 mL of oxygenated blood delivers about 5 mL of O2 to tissues",
    "Emphysema damages the alveolar walls",
], [
    "Most CO2 is carried dissolved in plasma",
    "The pneumotaxic centre is in the cerebellum",
    "Asthma is caused by damage to alveolar walls",
    "Oxygen is more soluble than CO2 in blood",
    "Inspiration happens when intrapulmonary pressure is above atmospheric pressure",
    "Carbonic anhydrase is absent from RBCs",
], "Breathing and Exchange of Gases", weight=2)


@gen("b11-14", weight=2)
def _capacity(rng):
    tv, irv, erv, rv = rng.choice([450, 500, 550]), rng.choice([2500, 2800, 3000]), rng.choice([1000, 1100]), rng.choice([1100, 1200])
    kind = rng.choice(["vital capacity", "inspiratory capacity", "functional residual capacity", "total lung capacity"])
    val = {"vital capacity": tv + irv + erv, "inspiratory capacity": tv + irv,
           "functional residual capacity": erv + rv, "total lung capacity": tv + irv + erv + rv}[kind]
    wrong = [tv + irv + erv + rv, tv + irv, erv + rv, tv + erv, tv + irv + erv]
    return num_q(rng, f"TV = {tv} mL, IRV = {irv} mL, ERV = {erv} mL and RV = {rv} mL. Find the {kind}.", val, " mL",
                 f"{kind.capitalize()} = {val} mL.", form=lambda x: str(int(x)), wrongs=wrong)


# ---------------------------------------------------------------- b11-15 Body Fluids and Circulation
table("b11-15", [
    ("Neutrophils", "60-65 per cent of WBCs; the most abundant"), ("Lymphocytes", "20-25 per cent of WBCs"),
    ("Monocytes", "6-8 per cent of WBCs"), ("Eosinophils", "2-3 per cent of WBCs; linked to allergic reactions"),
    ("Basophils", "0.5-1 per cent of WBCs; secrete histamine, serotonin and heparin"),
], "{}:", "Which white blood cells are {}?")
table("b11-15", [
    ("Fibrinogen", "Blood clotting"), ("Globulins", "Defence mechanisms of the body"),
    ("Albumins", "Osmotic balance"),
], "The plasma protein {} mainly helps in:", "Which plasma protein helps in {}?")
table("b11-15", [
    ("P wave", "Depolarisation of the atria"), ("QRS complex", "Depolarisation of the ventricles"),
    ("T wave", "Return of the ventricles from excited to normal state (repolarisation)"),
    ("First heart sound 'lub'", "Closure of the tricuspid and bicuspid valves"),
    ("Second heart sound 'dub'", "Closure of the semilunar valves"),
], "{} represents:", "Which ECG feature or heart sound represents: {}?")
table("b11-15", [
    ("Pacemaker of the heart", "Sino-atrial node (SAN)"), ("Valve between right atrium and right ventricle", "Tricuspid valve"),
    ("Valve between left atrium and left ventricle", "Bicuspid (mitral) valve"),
    ("Graveyard of RBCs", "Spleen"), ("Platelets come from", "Megakaryocytes"),
    ("Normal blood pressure", "120/80 mm Hg"), ("Hypertension", "Blood pressure of 140/90 mm Hg or higher"),
], "{}:", None)
table("b11-15", [
    ("Blood group A", "Antigen A on RBCs, anti-B antibodies in plasma"),
    ("Blood group B", "Antigen B on RBCs, anti-A antibodies in plasma"),
    ("Blood group AB", "Antigens A and B, no antibodies; universal recipient"),
    ("Blood group O", "No antigens, both antibodies; universal donor"),
], "{} has:", "Which blood group has: {}?")
facts("b11-15", [
    "RBCs live for about 120 days",
    "A healthy adult has 5-5.5 million RBCs per cubic mm of blood",
    "Each cardiac cycle takes about 0.8 seconds",
    "Stroke volume is about 70 mL and cardiac output about 5 litres per minute",
    "The SAN generates 70-75 action potentials per minute",
    "Erythroblastosis foetalis can occur when an Rh-negative mother carries an Rh-positive foetus",
    "Calcium ions play an important role in clotting",
    "Thrombin converts fibrinogen to fibrin",
], [
    "Mammalian RBCs have a nucleus",
    "Basophils are the most abundant WBCs",
    "The AV node is the pacemaker of the heart",
    "The T wave shows atrial depolarisation",
    "Lymph contains as many RBCs as blood",
    "Fishes have a four-chambered heart",
], "Body Fluids and Circulation", weight=2)


@gen("b11-15")
def _cardiac(rng):
    hr, sv = rng.choice([60, 70, 72, 75, 80, 90]), rng.choice([60, 65, 70, 75, 80])
    return num_q(rng, f"Heart rate {hr} beats/min and stroke volume {sv} mL. Cardiac output in litres per minute is:",
                 hr * sv / 1000, " L/min", f"Cardiac output = {hr} × {sv} mL = {hr * sv} mL/min.")


# ---------------------------------------------------------------- b11-16 Excretory Products
table("b11-16", [
    ("Bony fishes, aquatic amphibians and aquatic insects", "Ammonotelic"),
    ("Mammals, terrestrial amphibians and marine fishes", "Ureotelic"),
    ("Reptiles, birds, land snails and insects", "Uricotelic"),
], "{} are:", "Which animals are {}?")
table("b11-16", [
    ("Flatworms such as Planaria", "Protonephridia (flame cells)"), ("Earthworm", "Nephridia"),
    ("Insects including cockroach", "Malpighian tubules"), ("Crustaceans such as prawns", "Antennal (green) glands"),
], "The excretory structures of {} are:", "Which animals excrete through {}?")
table("b11-16", [
    ("Proximal convoluted tubule", "Reabsorbs nearly all nutrients and 70-80 per cent of electrolytes and water"),
    ("Descending limb of Henle's loop", "Permeable to water but almost impermeable to electrolytes"),
    ("Ascending limb of Henle's loop", "Impermeable to water but allows transport of electrolytes"),
    ("Collecting duct", "Reabsorbs large amounts of water to concentrate urine"),
    ("Juxtaglomerular apparatus", "Releases renin when GFR falls"),
    ("Vasa recta", "Capillaries running parallel to Henle's loop in the medulla"),
], "The role of the {} is:", "Which part of the nephron: {}?", weight=2)
table("b11-16", [
    ("ADH (vasopressin)", "Increases water reabsorption from the distal tubule"),
    ("Aldosterone", "Increases Na+ and water reabsorption"),
    ("Atrial natriuretic factor (ANF)", "Causes vasodilation and lowers blood pressure, checking the renin-angiotensin mechanism"),
    ("Angiotensin II", "Powerful vasoconstrictor that raises glomerular blood pressure"),
], "The action of {} is:", "Which substance: {}?")
facts("b11-16", [
    "The glomerular filtration rate is about 125 mL per minute (180 litres per day)",
    "A healthy adult passes 1 to 1.5 litres of urine a day",
    "Each kidney has about one million nephrons",
    "Urea is made in the liver",
    "Lungs remove about 200 mL of CO2 per minute",
    "Haemodialysis is used to treat uremia",
], [
    "Urea is made in the kidney",
    "Henle's loop is in the renal pelvis",
    "ANF raises blood pressure",
    "Most of the filtrate is excreted as urine",
    "Birds are ammonotelic",
    "The ascending limb of Henle's loop is permeable to water",
], "Excretory Products and their Elimination", weight=2)

# ---------------------------------------------------------------- b11-17 Locomotion and Movement
table("b11-17", [
    ("Cervical vertebrae", "7"), ("Thoracic vertebrae", "12"), ("Lumbar vertebrae", "5"),
    ("Bones in the skull", "22"), ("Ear ossicles (both ears)", "6"), ("Bones in the adult human skeleton", "206"),
    ("Pairs of ribs", "12"), ("Cranial bones", "8"), ("Facial bones", "14"),
], "Number of {}:", None)
table("b11-17", [
    ("Ball and socket joint", "Between the humerus and the pectoral girdle"), ("Hinge joint", "Knee joint"),
    ("Pivot joint", "Between atlas and axis"), ("Gliding joint", "Between the carpals"),
    ("Saddle joint", "Between the carpal and metacarpal of the thumb"),
    ("Fibrous joint", "Sutures of the skull"), ("Cartilaginous joint", "Between adjacent vertebrae"),
], "An example of a {} is:", "Which joint is found {}?", weight=2)
table("b11-17", [
    ("Myasthenia gravis", "Autoimmune disorder of the neuromuscular junction"),
    ("Muscular dystrophy", "Progressive genetic degeneration of skeletal muscle"),
    ("Tetany", "Rapid spasms due to low Ca2+ in body fluid"),
    ("Osteoporosis", "Age-related loss of bone mass; low oestrogen is a common cause"),
    ("Gout", "Inflammation of joints due to uric acid crystals"),
    ("Arthritis", "Inflammation of joints"),
], "{} is:", "Which disorder: {}?")
table("b11-17", [
    ("Actin", "Thin filaments of the I band"), ("Myosin", "Thick filaments of the A band"),
    ("Troponin", "Binds Ca2+ and moves tropomyosin to expose active sites"),
    ("Sarcomere", "The part of a myofibril between two Z lines"),
    ("Myoglobin", "Red pigment storing oxygen in red muscle fibres"),
], "{}:", "Which protein or structure: {}?")
facts("b11-17", [
    "Muscle contraction is explained by the sliding filament theory",
    "Ribs 8, 9 and 10 are false (vertebrochondral) ribs",
    "Ribs 11 and 12 are floating ribs",
    "Red muscle fibres have many mitochondria and much myoglobin",
    "Macrophages and leucocytes show amoeboid movement",
    "The I band shortens during muscle contraction",
], [
    "The A band shortens during muscle contraction",
    "White muscle fibres have plenty of myoglobin",
    "Ribs 11 and 12 are true ribs",
    "There are 7 thoracic vertebrae",
    "The knee is a pivot joint",
    "Gout is caused by low calcium",
], "Locomotion and Movement")

# ---------------------------------------------------------------- b11-18 Neural Control and Coordination
table("b11-18", [
    ("Cerebrum", "Memory, intelligence, language and voluntary actions"),
    ("Corpus callosum", "Connects the two cerebral hemispheres"),
    ("Thalamus", "Major coordinating centre for sensory and motor signals"),
    ("Hypothalamus", "Controls body temperature, hunger and thirst, and releases hypothalamic hormones"),
    ("Cerebellum", "Very convoluted; integrates information for balance and coordination"),
    ("Medulla oblongata", "Controls respiration, cardiovascular reflexes and gastric secretion"),
    ("Pons", "Fibre tracts connecting different regions of the brain"),
    ("Corpora quadrigemina", "Four round swellings on the dorsal midbrain"),
], "The function of the {} is:", "Which part of the brain: {}?", weight=2)
table("b11-18", [
    ("Multipolar neuron", "Cerebral cortex"), ("Bipolar neuron", "Retina of the eye"),
    ("Unipolar neuron", "Embryonic stage"),
], "A {} is found in the:", "Which neuron type is found in the {}?")
facts("b11-18", [
    "The resting membrane potential of a neuron is about -70 mV",
    "The sodium-potassium pump moves 3 Na+ out for every 2 K+ in",
    "Myelinated fibres have nodes of Ranvier between Schwann cell sheaths",
    "At rest the axon membrane is more permeable to K+ than to Na+",
    "Neurotransmitters cross the synaptic cleft at a chemical synapse",
    "Electrical synapses are rare in the human body",
    "The hindbrain consists of pons, cerebellum and medulla",
], [
    "At rest the inside of the axon is positive",
    "Myelinated fibres conduct impulses more slowly than unmyelinated ones",
    "The sodium-potassium pump moves 2 Na+ out for every 3 K+ in",
    "The thalamus controls body temperature",
    "The cerebellum controls breathing",
    "Electrical synapses are the most common synapses in humans",
], "Neural Control and Coordination")

# ---------------------------------------------------------------- b11-19 Chemical Coordination
table("b11-19", [
    ("Melatonin", "Pineal gland"), ("Thymosins", "Thymus"), ("Parathyroid hormone (PTH)", "Parathyroid glands"),
    ("Thyroxine (T4)", "Thyroid gland"), ("Thyrocalcitonin (TCT)", "Thyroid gland"),
    ("Adrenaline", "Adrenal medulla"), ("Cortisol", "Adrenal cortex"), ("Aldosterone", "Adrenal cortex"),
    ("Insulin", "Beta cells of the islets of Langerhans"), ("Glucagon", "Alpha cells of the islets of Langerhans"),
    ("Testosterone", "Leydig cells of the testis"), ("Progesterone", "Corpus luteum"),
    ("Oestrogen", "Growing ovarian follicles"), ("Atrial natriuretic factor", "Atrial wall of the heart"),
    ("Erythropoietin", "Juxtaglomerular cells of the kidney"), ("Prolactin", "Anterior pituitary"),
    ("Oxytocin (stored and released)", "Posterior pituitary"), ("Gonadotrophin-releasing hormone", "Hypothalamus"),
], "{} is secreted by the:", "Which hormone is secreted by the {}?", weight=3)
table("b11-19", [
    ("Dwarfism", "Too little growth hormone in childhood"), ("Gigantism", "Too much growth hormone in childhood"),
    ("Acromegaly", "Too much growth hormone in adults"), ("Cretinism", "Hypothyroidism during pregnancy or infancy"),
    ("Exophthalmic goitre (Graves' disease)", "Hyperthyroidism"),
    ("Addison's disease", "Too little hormone from the adrenal cortex"),
    ("Diabetes mellitus", "Lack of insulin action"), ("Diabetes insipidus", "Lack of ADH"),
], "{} is caused by:", "Which disorder is caused by {}?", weight=2)
table("b11-19", [
    ("Gastrin", "Stimulates gastric glands to secrete HCl and pepsinogen"),
    ("Secretin", "Stimulates secretion of water and bicarbonate from the pancreas"),
    ("Cholecystokinin (CCK)", "Stimulates pancreatic enzymes and bile juice"),
    ("Gastric inhibitory peptide (GIP)", "Inhibits gastric secretion and motility"),
], "{}:", "Which gut hormone: {}?")
facts("b11-19", [
    "Steroid hormones bind to intracellular receptors",
    "Protein hormones bind to membrane-bound receptors and use second messengers such as cAMP",
    "Oxytocin and vasopressin are made in the hypothalamus",
    "PTH raises blood calcium levels",
    "Thyrocalcitonin lowers blood calcium levels",
    "Adrenaline and noradrenaline are emergency (fight or flight) hormones",
    "Glucagon is hyperglycaemic and insulin is hypoglycaemic",
], [
    "Insulin raises blood glucose",
    "Oxytocin is made in the posterior pituitary",
    "PTH lowers blood calcium",
    "Steroid hormones need cAMP as a second messenger",
    "Aldosterone is made in the adrenal medulla",
    "Melatonin is secreted by the thymus",
], "Chemical Coordination and Integration", weight=2)
