"""High-yield NEET Biology, Class 11: original questions on the topics NEET (and AIPMT before it) asks again and again.

Facts follow the NCERT Class 11 Biology textbook. Nothing is copied from past papers.
"""
from .core import table, facts, groups, tag

tag("hy")

# ---------------------------------------------------------------- b11-01 The Living World
table("b11-01", [
    ("Species", "Genus"), ("Genus", "Family"), ("Family", "Order"), ("Order", "Class"),
    ("Class", "Phylum or Division"), ("Phylum or Division", "Kingdom"),
], "In the taxonomic hierarchy, the category just above {} is:", "{} lies just above which category?")
facts("b11-01", [
    "Binomial nomenclature was introduced by Carolus Linnaeus",
    "In a scientific name the generic name starts with a capital letter and the specific epithet with a small letter",
    "Scientific names are Latinised and printed in italics",
    "Species is the basic unit of classification",
    "Common characters decrease as we go higher in the taxonomic hierarchy",
    "Metabolism is a defining feature of all living organisms",
    "Plants are named under the International Code of Botanical Nomenclature (ICBN)",
    "Systematics deals with the diversity of organisms and their evolutionary relationships",
], [
    "Binomial nomenclature was introduced by Aristotle",
    "Both words of a scientific name start with capital letters",
    "Genus is the lowest category in the taxonomic hierarchy",
    "Family is a higher category than order",
    "Common characters increase as we go higher in the taxonomic hierarchy",
    "Growth is a defining property of life because non-living things never grow",
    "Plants are named under the International Code of Zoological Nomenclature (ICZN)",
    "Reproduction is a defining property of life because every living individual reproduces",
], "taxonomy and the living world")

# ---------------------------------------------------------------- b11-02 Biological Classification
table("b11-02", [
    ("Two kingdom classification", "Carolus Linnaeus"), ("Five kingdom classification", "R.H. Whittaker"),
    ("Discovery of viruses (tobacco mosaic disease)", "Dmitri Ivanowsky"), ("The name 'virus' (contagium vivum fluidum)", "M.W. Beijerinck"),
    ("Crystallising a virus (TMV)", "W.M. Stanley"), ("Discovery of viroids", "T.O. Diener"),
], "{} is credited to:", "Which contribution belongs to {}?")
table("b11-02", [
    ("Chrysophytes (diatoms)", "Cell walls of silica forming diatomaceous earth"), ("Dinoflagellates", "Red tides and two flagella in grooves"),
    ("Euglenoids", "A protein-rich pellicle instead of a cell wall"), ("Slime moulds", "Plasmodium and spores with true walls"),
    ("Sporozoans", "Infectious spore-like stage, e.g. Plasmodium"), ("Ciliates", "Cilia and a gullet, e.g. Paramoecium"),
], "Which feature belongs to {}?", "Which protist group has: {}?")
facts("b11-02", [
    "Mycoplasma lacks a cell wall and is the smallest known living cell",
    "Archaebacteria such as methanogens live in the guts of ruminants and produce methane",
    "Heterocysts of Nostoc and Anabaena fix nitrogen",
    "Lichens are associations of algae and fungi",
    "Viroids are free RNA without a protein coat",
    "The cell wall of most fungi is made of chitin",
    "Neurospora is used extensively in biochemical and genetic work",
    "Deuteromycetes are called imperfect fungi because only asexual or vegetative phases are known",
], [
    "Mycoplasma has a thick peptidoglycan cell wall",
    "Viroids have a protein coat but no nucleic acid",
    "Lichens are associations of bacteria and protozoa",
    "Euglenoids have a cellulose cell wall",
    "The cell wall of most fungi is made of cellulose",
    "Five kingdom classification was proposed by Linnaeus",
    "Phycomycetes have septate mycelium and form ascospores",
    "Viruses contain both DNA and RNA in the same particle",
], "kingdoms, monerans, protists and fungi")

# ---------------------------------------------------------------- b11-03 Plant Kingdom
groups("b11-03", {
    "Chlorophyceae (green algae)": ["Volvox", "Ulothrix", "Spirogyra", "Chara", "Chlamydomonas"],
    "Phaeophyceae (brown algae)": ["Ectocarpus", "Laminaria", "Fucus", "Dictyota", "Sargassum"],
    "Rhodophyceae (red algae)": ["Polysiphonia", "Porphyra", "Gelidium", "Gracilaria"],
}, "Which alga does NOT belong to {}?", "Which alga belongs to {}?")
groups("b11-03", {
    "bryophytes": ["Funaria", "Marchantia", "Sphagnum", "Polytrichum"],
    "pteridophytes": ["Selaginella", "Equisetum", "Pteris", "Dryopteris", "Adiantum"],
    "gymnosperms": ["Cycas", "Pinus", "Ginkgo", "Cedrus"],
}, "Which plant is NOT one of the {}?", "Which plant is one of the {}?")
table("b11-03", [
    ("Agar", "Gelidium and Gracilaria"), ("Carrageen", "Red algae"), ("Algin", "Brown algae"),
    ("Single-cell protein for space travellers", "Chlorella"), ("Peat used as fuel", "Sphagnum"),
], "{} is obtained from:", "What is obtained from {}?")
facts("b11-03", [
    "Bryophytes are called the amphibians of the plant kingdom",
    "Pteridophytes are the first terrestrial plants with vascular tissues",
    "Selaginella and Salvinia are heterosporous",
    "In gymnosperms the ovules are not enclosed in an ovary",
    "Cycas has coralloid roots associated with nitrogen-fixing cyanobacteria",
    "In angiosperms the endosperm is triploid",
    "Double fertilisation is a characteristic of angiosperms",
    "The protonema is the first stage of the moss gametophyte",
], [
    "Bryophytes have true xylem and phloem",
    "Gymnosperms have ovules enclosed in an ovary",
    "Ferns are the first plants with flowers",
    "The endosperm of gymnosperms is triploid",
    "Double fertilisation occurs in all gymnosperms",
    "In mosses the sporophyte is free-living and dominant",
    "Pinus is homosporous",
    "Fucus is a red alga",
], "the plant kingdom")

# ---------------------------------------------------------------- b11-04 Animal Kingdom
table("b11-04", [
    ("Sycon", "Porifera"), ("Spongilla", "Porifera"), ("Obelia", "Cnidaria"), ("Physalia", "Cnidaria"),
    ("Pleurobrachia", "Ctenophora"), ("Taenia", "Platyhelminthes"), ("Fasciola", "Platyhelminthes"),
    ("Ascaris", "Aschelminthes"), ("Wuchereria", "Aschelminthes"), ("Nereis", "Annelida"), ("Hirudinaria", "Annelida"),
    ("Limulus", "Arthropoda"), ("Pila", "Mollusca"), ("Octopus", "Mollusca"), ("Asterias", "Echinodermata"),
    ("Antedon", "Echinodermata"), ("Balanoglossus", "Hemichordata"),
], "{} belongs to phylum:", None, weight=2)
table("b11-04", [
    ("Petromyzon", "Cyclostomata"), ("Scoliodon", "Chondrichthyes"), ("Pristis", "Chondrichthyes"),
    ("Hippocampus", "Osteichthyes"), ("Labeo", "Osteichthyes"), ("Ichthyophis", "Amphibia"), ("Salamandra", "Amphibia"),
    ("Chelone", "Reptilia"), ("Hemidactylus", "Reptilia"), ("Columba", "Aves"), ("Neophron", "Aves"),
    ("Ornithorhynchus", "Mammalia"), ("Pteropus", "Mammalia"), ("Macropus", "Mammalia"),
], "{} belongs to the class:", None, weight=2)
table("b11-04", [
    ("Ctenophores", "Comb plates for locomotion"), ("Sponges", "Canal system and choanocytes"), ("Cnidarians", "Cnidoblasts"),
    ("Flatworms", "Flame cells"), ("Annelids", "Nephridia and metameres"), ("Echinoderms", "Water vascular system"),
    ("Molluscs", "Radula and mantle"), ("Hemichordates", "Proboscis gland"),
], "A key feature of {} is:", "Which group has {}?")
facts("b11-04", [
    "Ctenophores show bioluminescence",
    "Cnidarians show two body forms, polyp and medusa",
    "Aschelminthes have a pseudocoelom",
    "Echinoderm adults are radially symmetrical but their larvae are bilateral",
    "Birds have pneumatic bones",
    "Crocodiles have a four-chambered heart",
    "Cartilaginous fishes lack an air bladder",
    "Ornithorhynchus is an egg-laying mammal",
], [
    "Sponges have a true coelom",
    "Annelids have a pseudocoelom",
    "Cyclostomes have paired fins and jaws",
    "Bony fishes have placoid scales",
    "All reptiles have a four-chambered heart",
    "Amphibians have scales and lay shelled eggs on land",
    "Platyhelminthes are triploblastic and coelomate",
    "Birds have teeth in their jaws",
], "the animal kingdom")

# ---------------------------------------------------------------- b11-05 Morphology of Flowering Plants
table("b11-05", [
    ("Racemose inflorescence", "Main axis keeps growing and flowers open from base to apex"),
    ("Cymose inflorescence", "Main axis ends in a flower"),
    ("Hypogynous flower", "Superior ovary, e.g. mustard and brinjal"),
    ("Epigynous flower", "Inferior ovary, e.g. guava and cucumber"),
    ("Perigynous flower", "Half-inferior ovary, e.g. plum and rose"),
], "{}:", "Which term means: {}?")
table("b11-05", [
    ("Mustard", "Parietal placentation"), ("Pea", "Marginal placentation"), ("Tomato", "Axile placentation"),
    ("Dianthus", "Free central placentation"), ("Sunflower", "Basal placentation"), ("China rose", "Axile placentation"),
], "{} shows:", None)
table("b11-05", [
    ("Valvate aestivation", "Calotropis"), ("Twisted aestivation", "China rose"), ("Imbricate aestivation", "Cassia"),
    ("Vexillary aestivation", "Pea"),
], "An example of {} is:", "{} shows which aestivation?")
facts("b11-05", [
    "The edible part of the coconut is the endosperm",
    "Mango and coconut are drupes",
    "The fruit of mango develops from a monocarpellary superior ovary",
    "Pea flowers have vexillary aestivation",
    "In Fabaceae the stamens are diadelphous",
    "Liliaceae flowers are trimerous with a perianth",
    "Pneumatophores of Rhizophora help in respiration",
    "Tendrils of grapevine are stem modifications",
], [
    "The edible part of the coconut is the mesocarp",
    "In Solanaceae the ovary is inferior",
    "Pneumatophores are found in desert plants",
    "Tendrils of grapevine are leaf modifications",
    "Liliaceae flowers are pentamerous",
    "In Fabaceae the placentation is axile",
    "Potato tuber is a modified root",
    "Sweet potato is a modified stem",
], "flowering plant morphology")

# ---------------------------------------------------------------- b11-06 Anatomy of Flowering Plants
table("b11-06", [
    ("Dicot root", "Xylem and phloem on different radii; 2 to 4 xylem bundles"),
    ("Monocot root", "More than six xylem bundles and a large pith"),
    ("Dicot stem", "Vascular bundles in a ring, conjoint and open"),
    ("Monocot stem", "Scattered vascular bundles with bundle sheath, closed"),
    ("Dicot leaf", "Dorsiventral with palisade and spongy mesophyll"),
    ("Monocot (isobilateral) leaf", "Undifferentiated mesophyll and bulliform cells"),
], "Which feature identifies a {}?", "This feature identifies which organ: {}?")
facts("b11-06", [
    "Casparian strips of the endodermis contain suberin",
    "Lateral roots arise from the pericycle",
    "Bulliform cells help grass leaves roll up when water is short",
    "Heartwood is darker and does not conduct water",
    "Cork cambium is also called phellogen",
    "Interfascicular cambium arises from medullary ray cells",
    "In roots the protoxylem lies towards the outside (exarch)",
    "Spring wood has wide vessels and light colour",
], [
    "Lateral roots arise from the endodermis",
    "Heartwood conducts most of the water in an old tree",
    "Monocot stems show regular secondary growth",
    "Casparian strips contain lignin and cutin only",
    "In stems the protoxylem lies towards the outside (exarch)",
    "Autumn wood has wide vessels and light colour",
    "Bulliform cells are found in the lower epidermis of dicot leaves",
    "Phelloderm is formed towards the outside of the cork cambium",
], "plant anatomy")

# ---------------------------------------------------------------- b11-07 Structural Organisation in Animals
table("b11-07", [
    ("Cockroach heart", "13 chambers"), ("Malpighian tubules of cockroach", "Excretion of uric acid"),
    ("Cockroach mouthparts", "Biting and chewing"), ("Cockroach spiracles", "10 pairs"),
    ("Cockroach ovarioles", "8 in each ovary"), ("Mushroom gland of cockroach", "Part of the male reproductive system"),
], "{}:", "Which cockroach structure fits: {}?")
facts("b11-07", [
    "Squamous epithelium lines blood vessels and lung air sacs",
    "Ciliated epithelium lines the bronchioles and fallopian tubes",
    "Tight junctions stop substances leaking across a tissue",
    "Gap junctions let ions and small molecules pass between neighbouring cells",
    "Cardiac muscle cells are joined by intercalated discs",
    "Tendons attach skeletal muscles to bones",
    "Adipose tissue stores fat and lies below the skin",
    "The cockroach has an open circulatory system",
], [
    "Tendons attach one bone to another",
    "Smooth muscle fibres are striated and voluntary",
    "Cardiac muscle is voluntary",
    "The cockroach has a closed circulatory system",
    "Cockroach blood carries haemoglobin to its tissues",
    "Cartilage is a loose connective tissue",
    "Neuroglia conduct nerve impulses over long distances",
    "Ligaments attach muscles to bones",
], "animal tissues and the cockroach")

# ---------------------------------------------------------------- b11-08 Cell: The Unit of Life
table("b11-08", [
    ("Lysosomes", "Suicidal bags with hydrolytic enzymes"), ("Ribosomes", "Protein synthesis, not membrane-bound"),
    ("Smooth ER", "Lipid and steroid synthesis"), ("Golgi apparatus", "Packaging and glycoprotein formation"),
    ("Mitochondria", "Aerobic respiration and ATP"), ("Centrioles", "Basal bodies and spindle in animal cells"),
    ("Vacuole", "Up to 90% of plant cell volume, bounded by tonoplast"), ("Nucleolus", "Site of rRNA synthesis"),
], "{}:", "Which cell part is described: {}?")
facts("b11-08", [
    "The cell theory was proposed by Schleiden and Schwann",
    "Virchow said that new cells arise from pre-existing cells",
    "The fluid mosaic model was proposed by Singer and Nicolson",
    "Prokaryotic ribosomes are 70S",
    "Mitochondria and chloroplasts have their own DNA",
    "Mesosomes are infoldings of the bacterial plasma membrane",
    "Cilia and flagella show a 9 + 2 arrangement of microtubules",
    "In a metacentric chromosome the centromere is in the middle",
], [
    "Eukaryotic cytoplasmic ribosomes are 70S",
    "Lysosomes are formed directly by mitochondria",
    "Ribosomes are bounded by a double membrane",
    "Centrioles show a 9 + 2 arrangement",
    "The fluid mosaic model was proposed by Robert Hooke",
    "Prokaryotes have a well-defined nucleus with a nuclear membrane",
    "In an acrocentric chromosome the centromere is exactly in the middle",
    "Golgi bodies are the sites of protein synthesis",
], "the cell")

# ---------------------------------------------------------------- b11-09 Biomolecules
table("b11-09", [
    ("Collagen", "Most abundant protein in animals"), ("RuBisCO", "Most abundant protein in the biosphere"),
    ("Cellulose", "Most abundant organic compound on Earth"), ("Inulin", "Polymer of fructose"),
    ("Glycogen", "Storage polysaccharide in animals"), ("Chitin", "Exoskeleton of arthropods"),
], "{}:", "Which biomolecule is: {}?")
table("b11-09", [
    ("Competitive inhibition", "Inhibitor resembles the substrate, e.g. malonate on succinic dehydrogenase"),
    ("Cofactor (prosthetic group)", "Tightly bound non-protein part, e.g. haem in peroxidase"),
    ("Coenzyme", "Loosely bound organic cofactor, e.g. NAD"), ("Km", "Substrate concentration at half Vmax"),
], "{}:", "Which term fits: {}?")
facts("b11-09", [
    "Lipids are not strictly macromolecules",
    "The acid-insoluble fraction contains proteins, nucleic acids and polysaccharides",
    "In nucleotides a sugar is linked to a base by an N-glycosidic bond",
    "Amino acids are joined by peptide bonds",
    "Enzymes lower the activation energy of a reaction",
    "Adenine and guanine are purines",
    "Starch gives a blue-black colour with iodine",
    "Lecithin is a phospholipid",
], [
    "Lipids are true polymers of high molecular weight",
    "Enzymes raise the activation energy of a reaction",
    "Cytosine is a purine",
    "Cellulose gives a blue-black colour with iodine",
    "Amino acids are joined by glycosidic bonds",
    "All enzymes are lipids",
    "Inulin is a polymer of glucose",
    "Competitive inhibitors change the shape of the active site permanently",
], "biomolecules and enzymes")

# ---------------------------------------------------------------- b11-10 Cell Cycle and Cell Division
table("b11-10", [
    ("G1 phase", "Cell grows; no DNA replication"), ("S phase", "DNA replicates; chromosome number stays the same"),
    ("G2 phase", "Proteins for mitosis are made"), ("G0 phase", "Quiescent stage; cells stop dividing"),
    ("Anaphase", "Centromeres split and chromatids move to opposite poles"), ("Metaphase", "Chromosomes line up at the equator"),
    ("Telophase", "Nuclear envelope and nucleolus reappear"),
], "What happens in {}?", "Which stage: {}?")
facts("b11-10", [
    "In a human cell the cell cycle takes about 24 hours",
    "Crossing over occurs in pachytene",
    "Synaptonemal complex forms in zygotene and dissolves in diplotene",
    "Chiasmata are seen in diplotene",
    "Terminalisation of chiasmata occurs in diakinesis",
    "Meiosis halves the chromosome number",
    "Metaphase is the best stage to study chromosome morphology",
    "In meiosis I homologous chromosomes separate",
], [
    "Crossing over occurs in leptotene",
    "DNA replication occurs in G2 phase",
    "In meiosis I sister chromatids separate",
    "Mitosis halves the chromosome number",
    "Chiasmata first appear in zygotene",
    "Interphase is the shortest stage of the cell cycle",
    "Cytokinesis in plant cells happens by furrow formation",
    "Anaphase is the best stage to count chromosomes",
], "the cell cycle")

# ---------------------------------------------------------------- b11-11 Photosynthesis in Higher Plants
table("b11-11", [
    ("Calvin cycle", "Stroma of chloroplast"), ("Light reaction", "Thylakoid membranes"),
    ("Photorespiration", "Chloroplast, peroxisome and mitochondrion"), ("C4 carbon fixation by PEP carboxylase", "Mesophyll cells"),
    ("Calvin cycle in C4 plants", "Bundle sheath cells"),
], "Where does {} happen?", None)
table("b11-11", [
    ("Primary CO2 acceptor in C3 plants", "RuBP"), ("Primary CO2 acceptor in C4 plants", "PEP"),
    ("First stable product in C3 plants", "3-phosphoglyceric acid (PGA)"), ("First stable product in C4 plants", "Oxaloacetic acid (OAA)"),
    ("Enzyme of C3 carbon fixation", "RuBisCO"), ("Reaction centre of PS I", "P700"), ("Reaction centre of PS II", "P680"),
], "{}:", "Which is {}?")
facts("b11-11", [
    "To fix one CO2 the Calvin cycle uses 3 ATP and 2 NADPH",
    "Making one glucose needs 18 ATP and 12 NADPH",
    "Splitting of water is linked to PS II",
    "Cyclic photophosphorylation produces ATP but no NADPH",
    "C4 plants show Kranz anatomy",
    "Photorespiration does not occur in C4 plants",
    "Chlorophyll a is the chief pigment of photosynthesis",
    "Blackman gave the law of limiting factors",
], [
    "Cyclic photophosphorylation produces both ATP and NADPH",
    "Splitting of water is linked to PS I",
    "Photorespiration produces ATP and sugar",
    "C3 plants show Kranz anatomy",
    "RuBisCO has a higher affinity for O2 than for CO2 at all times",
    "The Calvin cycle needs 2 ATP and 3 NADPH per CO2",
    "Oxygen in photosynthesis comes from CO2",
    "PS II absorbs best at 700 nm",
], "photosynthesis")

# ---------------------------------------------------------------- b11-12 Respiration in Plants
table("b11-12", [
    ("Final electron acceptor of aerobic respiration", "Oxygen"), ("First product of the Krebs cycle", "Citric acid"),
    ("End product of glycolysis", "Pyruvic acid"), ("Product of fermentation in muscle", "Lactic acid"),
    ("Product of fermentation in yeast", "Ethanol and CO2"), ("Complex V of the ETC", "ATP synthase"),
], "{}:", "Which is {}?")
facts("b11-12", [
    "Glycolysis is also called the EMP pathway",
    "Glycolysis gives a net gain of 2 ATP per glucose",
    "One NADH yields about 3 ATP in the textbook balance sheet",
    "Aerobic respiration of one glucose gives a net 38 ATP in the textbook balance sheet",
    "The RQ of carbohydrates is 1",
    "The RQ of fats is less than 1",
    "Respiration is an amphibolic pathway",
    "Cytochrome c is a small mobile carrier between complex III and IV",
], [
    "Glycolysis needs oxygen",
    "The Krebs cycle takes place in the cytoplasm",
    "The RQ of fats is more than 1",
    "Fermentation gives 38 ATP per glucose",
    "The final electron acceptor of aerobic respiration is NAD",
    "Respiration is a purely catabolic pathway",
    "One FADH2 yields 3 ATP in the textbook balance sheet",
    "Pyruvate is converted to acetyl CoA in the cytoplasm",
], "respiration")

# ---------------------------------------------------------------- b11-13 Plant Growth and Development
table("b11-13", [
    ("Auxin", "Apical dominance and rooting of cuttings"), ("Gibberellin", "Bolting and stem elongation in rosette plants"),
    ("Cytokinin", "Delays leaf senescence and promotes cell division"), ("Ethylene", "Fruit ripening and triple response"),
    ("Abscisic acid", "Stomatal closure and seed dormancy"),
], "A typical effect of {} is:", "Which hormone: {}?")
table("b11-13", [
    ("First isolated from human urine", "Auxin"), ("First discovered in the fungus Gibberella fujikuroi", "Gibberellin"),
    ("First found as kinetin in autoclaved herring sperm DNA", "Cytokinin"), ("The only gaseous plant hormone", "Ethylene"),
    ("Called the stress hormone", "Abscisic acid"),
], "{}:", None)
facts("b11-13", [
    "Short day plants flower when the night is longer than a critical length",
    "The site of photoperception in flowering is the leaf",
    "Vernalisation is promotion of flowering by a period of low temperature",
    "Phytochrome perceives red and far-red light",
    "2,4-D is a synthetic auxin used as a weedicide",
    "Ethephon releases ethylene",
    "Plant growth is generally indeterminate",
    "Dedifferentiation lets permanent tissues regain the ability to divide",
], [
    "The site of photoperception in flowering is the shoot apex",
    "Abscisic acid promotes seed germination",
    "Cytokinins speed up leaf senescence",
    "Gibberellins cause stomatal closure",
    "Ethylene delays fruit ripening",
    "Vernalisation is promotion of flowering by high temperature",
    "Short day plants flower only under continuous light",
    "Auxin was first isolated from Gibberella fujikuroi",
], "plant growth regulators")

# ---------------------------------------------------------------- b11-14 Breathing and Exchange of Gases
table("b11-14", [
    ("Tidal volume", "About 500 mL"), ("Inspiratory reserve volume", "2500 to 3000 mL"), ("Expiratory reserve volume", "1000 to 1100 mL"),
    ("Residual volume", "1100 to 1200 mL"), ("pO2 in alveoli", "104 mm Hg"), ("pCO2 in alveoli", "40 mm Hg"),
], "{} is:", "Which value is {}?")
facts("b11-14", [
    "About 97% of O2 is carried by haemoglobin as oxyhaemoglobin",
    "About 20-25% of CO2 is carried as carbaminohaemoglobin",
    "About 70% of CO2 is carried as bicarbonate",
    "The respiratory rhythm centre is in the medulla",
    "The pneumotaxic centre is in the pons",
    "Every 100 mL of oxygenated blood delivers about 5 mL of O2 to the tissues",
    "The diffusing capacity for CO2 is about 20-25 times that of O2",
    "Emphysema damages alveolar walls and reduces the respiratory surface",
], [
    "Most O2 is carried dissolved in plasma",
    "Most CO2 is carried as carbaminohaemoglobin",
    "The respiratory rhythm centre is in the cerebellum",
    "Low pCO2 favours dissociation of O2 from haemoglobin",
    "Residual volume can be exhaled by forceful expiration",
    "The diffusing capacity for O2 is higher than for CO2",
    "Inspiration is a passive process in normal breathing",
    "Carbonic anhydrase is found mainly in plasma, not in red cells",
], "breathing and gas exchange")

# ---------------------------------------------------------------- b11-15 Body Fluids and Circulation
table("b11-15", [
    ("SA node", "Pacemaker of the heart"), ("AV node", "Delays the impulse before it spreads to the ventricles"),
    ("Bundle of His", "Carries the impulse through the interventricular septum"), ("Purkinje fibres", "Spread the impulse through the ventricular walls"),
    ("Tricuspid valve", "Between right atrium and right ventricle"), ("Bicuspid (mitral) valve", "Between left atrium and left ventricle"),
], "{}:", "Which part of the heart: {}?")
table("b11-15", [
    ("Duration of one cardiac cycle", "0.8 seconds"), ("Stroke volume", "About 70 mL"), ("Cardiac output", "About 5000 mL per minute"),
    ("Normal heart rate", "About 72 beats per minute"), ("Normal blood pressure", "120/80 mm Hg"),
], "{} in a healthy adult:", "{} is the normal value of what?")
facts("b11-15", [
    "Erythroblastosis foetalis can occur when an Rh-negative mother carries an Rh-positive foetus",
    "Group O is called the universal donor",
    "Group AB is called the universal recipient",
    "Neutrophils are the most abundant white blood cells",
    "Lymph returns tissue fluid to the venous blood",
    "The hepatic portal vein carries blood from the intestine to the liver",
    "Fish have a two-chambered heart and single circulation",
    "The QRS complex shows depolarisation of the ventricles",
], [
    "Group AB is called the universal donor",
    "Basophils are the most abundant white blood cells",
    "The P wave shows ventricular depolarisation",
    "The T wave shows atrial depolarisation",
    "The AV node is the pacemaker of the heart",
    "Mammalian red blood cells have a nucleus",
    "Amphibians have a four-chambered heart",
    "The pulmonary vein carries deoxygenated blood",
], "blood and circulation")

# ---------------------------------------------------------------- b11-16 Excretory Products and their Elimination
table("b11-16", [
    ("Glomerular filtration rate", "About 125 mL per minute"), ("Filtrate formed per day", "About 180 litres"),
    ("Urine passed per day", "1 to 1.5 litres"), ("Urea excreted per day", "25 to 30 g"),
], "{} in a healthy adult:", "{} is the normal value of what?")
facts("b11-16", [
    "Nearly 99% of the filtrate is reabsorbed by the renal tubules",
    "The PCT reabsorbs nearly all glucose and amino acids",
    "The descending limb of Henle's loop is permeable to water but almost impermeable to electrolytes",
    "The ascending limb of Henle's loop is impermeable to water",
    "ADH increases water reabsorption in the distal tubule and collecting duct",
    "Aldosterone increases Na+ and water reabsorption",
    "ANF opposes the renin-angiotensin mechanism",
    "Juxtamedullary nephrons have long loops of Henle",
], [
    "The ascending limb of Henle's loop is freely permeable to water",
    "ADH decreases water reabsorption",
    "Most of the filtrate leaves the body as urine",
    "Glucose is mainly reabsorbed in the collecting duct",
    "ANF raises blood pressure",
    "Cortical nephrons have the longest loops of Henle",
    "Urea is made in the kidney",
    "Diabetes insipidus is caused by too much ADH",
], "kidney function")

# ---------------------------------------------------------------- b11-17 Locomotion and Movement
table("b11-17", [
    ("A band", "Dark band; length stays the same during contraction"), ("I band", "Light band; shortens during contraction"),
    ("H zone", "Central part of the A band without thin filaments"), ("Z line", "Bisects the I band and marks the sarcomere ends"),
    ("Sarcomere", "Functional unit of contraction between two Z lines"),
], "{}:", "Which part of a muscle fibre: {}?")
table("b11-17", [
    ("Bones in the human skeleton", "206"), ("Bones in the skull", "22"), ("Vertebrae", "26"),
    ("Pairs of ribs", "12"), ("Bones in each limb", "30"),
], "Number of {}:", None)
facts("b11-17", [
    "Calcium ions bind troponin and expose active sites on actin",
    "Myosin heads have ATPase activity",
    "Red muscle fibres have plenty of myoglobin and mitochondria",
    "Gout is caused by accumulation of uric acid crystals in joints",
    "Myasthenia gravis is an autoimmune disorder of the neuromuscular junction",
    "The 8th, 9th and 10th pairs of ribs are vertebrochondral (false) ribs",
    "The 11th and 12th pairs of ribs are floating ribs",
    "Pivot joint is found between the atlas and axis",
], [
    "Calcium ions bind myosin and expose sites on tropomyosin",
    "The A band shortens during contraction",
    "White muscle fibres have plenty of myoglobin",
    "Tetany is caused by a high level of calcium",
    "The 11th and 12th pairs of ribs join the sternum",
    "The knee joint is a ball and socket joint",
    "Osteoporosis is caused by excess bone formation",
    "Actin filaments have ATPase activity",
], "muscles and skeleton")

# ---------------------------------------------------------------- b11-18 Neural Control and Coordination
table("b11-18", [
    ("Resting membrane", "Outside positive, inside negative"), ("Depolarised membrane", "Outside negative, inside positive"),
    ("Na+/K+ pump", "Moves 3 Na+ out and 2 K+ in"), ("Myelinated fibre", "Saltatory conduction from node to node"),
], "In a nerve fibre, the {}:", "Which fits: {}?")
table("b11-18", [
    ("Rods", "Twilight (scotopic) vision"), ("Cones", "Daylight and colour (photopic) vision"), ("Fovea", "Point of greatest visual acuity"),
    ("Blind spot", "No photoreceptors"), ("Organ of Corti", "Hearing receptor on the basilar membrane"),
    ("Crista and macula", "Balance receptors of the vestibular apparatus"),
], "{}:", "Which part of the eye or ear: {}?")
facts("b11-18", [
    "The corpus callosum connects the two cerebral hemispheres",
    "The hypothalamus controls body temperature, hunger and thirst",
    "The cerebellum maintains posture and balance",
    "The medulla controls respiration and cardiovascular reflexes",
    "Rhodopsin is made of opsin and retinal, a derivative of vitamin A",
    "The ear ossicles are malleus, incus and stapes",
    "The eustachian tube equalises pressure on either side of the eardrum",
    "Chemical synapses use neurotransmitters such as acetylcholine",
], [
    "The cerebellum controls body temperature",
    "The fovea has only rods",
    "The blind spot has the most cones",
    "The stapes is attached to the tympanic membrane",
    "A resting neuron is negative outside and positive inside",
    "Electrical synapses are slower than chemical synapses",
    "The medulla connects the two cerebral hemispheres",
    "The cochlea maintains balance",
], "the nervous system and senses")

# ---------------------------------------------------------------- b11-19 Chemical Coordination and Integration
table("b11-19", [
    ("Oxytocin", "Contraction of uterus and milk ejection"), ("Vasopressin (ADH)", "Water reabsorption in kidney tubules"),
    ("Melatonin", "Day-night (diurnal) rhythm"), ("Thymosins", "Differentiation of T-lymphocytes"),
    ("Calcitonin", "Lowers blood calcium"), ("Parathyroid hormone", "Raises blood calcium"),
    ("Glucagon", "Raises blood glucose"), ("Insulin", "Lowers blood glucose"),
], "The main action of {} is:", "Which hormone: {}?")
facts("b11-19", [
    "The posterior pituitary stores and releases oxytocin and vasopressin made by the hypothalamus",
    "Adrenaline and noradrenaline are called the emergency (3F) hormones",
    "Cortisol is a glucocorticoid",
    "Aldosterone is the main mineralocorticoid",
    "Steroid hormones act through intracellular receptors",
    "Hypothyroidism in pregnancy can cause cretinism in the child",
    "Addison's disease is due to too little adrenal cortex hormone",
    "Cushing's syndrome is due to too much cortisol",
], [
    "Oxytocin is made by the posterior pituitary itself",
    "Protein hormones act through receptors inside the nucleus",
    "Insulin raises blood glucose",
    "Calcitonin raises blood calcium",
    "Diabetes insipidus is caused by lack of insulin",
    "Acromegaly is caused by too little growth hormone in adults",
    "Melatonin is secreted by the thymus",
    "Thyroxine is a steroid hormone",
], "hormones")

# ---------------------------------------------------------------- more for the thinner chapters
table("b11-01", [
    ("Herbarium", "Dried, pressed and preserved plant specimens on sheets"), ("Botanical garden", "Living plants grown for reference"),
    ("Museum", "Preserved animals and plants, often in jars or as skeletons"), ("Key", "Taxonomic aid based on contrasting couplets"),
    ("Monograph", "Information on any one taxon"), ("Flora", "Habitat and distribution of plants of an area"),
], "The taxonomic aid '{}' is:", "Which taxonomic aid: {}?")
facts("b11-01", [
    "Taxonomic keys are generally analytical in nature",
    "Each statement in a key is called a lead",
    "Kew in England has one of the largest botanical gardens",
    "The Indian Botanical Garden is at Howrah",
    "The National Botanical Research Institute is at Lucknow",
    "Mangifera indica belongs to the family Anacardiaceae",
], [
    "Each statement in a key is called a couplet",
    "The Indian Botanical Garden is at Lucknow",
    "Herbaria keep living plants",
    "A monograph covers all plants of an area",
    "Keys are based on similar, not contrasting, characters",
    "Mangifera indica belongs to the family Poaceae",
], "taxonomic aids")

table("b11-06", [
    ("Collenchyma", "Thickened corners with cellulose, hemicellulose and pectin"), ("Sclerenchyma", "Dead cells with lignified walls"),
    ("Parenchyma", "Living thin-walled cells for storage and photosynthesis"), ("Tracheids", "Elongated dead xylem cells with tapering ends"),
    ("Companion cells", "Living cells that help sieve tubes"), ("Phloem fibres (bast fibres)", "Used for jute, flax and hemp"),
    ("Vessels", "Characteristic xylem element of angiosperms"),
], "{}:", "Which tissue or cell: {}?")
facts("b11-06", [
    "Gymnosperms lack vessels in their xylem",
    "Gymnosperms lack companion cells in their phloem",
    "Apical and intercalary meristems are primary meristems",
    "Intercalary meristems occur in grasses at the base of internodes",
    "The vascular bundles of dicot stems are open",
    "Radial vascular bundles occur in roots",
], [
    "Gymnosperms have vessels in their xylem",
    "Collenchyma cells are dead at maturity",
    "Phloem parenchyma is absent in most dicots",
    "Monocot stem vascular bundles are open",
    "Conjoint vascular bundles occur in roots",
    "Sclerenchyma cells are living and thin-walled",
], "plant tissues")

table("b11-07", [
    ("Simple squamous epithelium", "Walls of blood vessels and lung air sacs"), ("Simple cuboidal epithelium", "Ducts of glands and tubular parts of nephrons"),
    ("Simple columnar epithelium", "Lining of the stomach and intestine"), ("Compound (stratified) epithelium", "Dry surface of the skin and moist buccal cavity"),
    ("Dense regular connective tissue", "Tendons and ligaments"), ("Specialised connective tissue", "Cartilage, bone and blood"),
], "{} is found in:", "Which tissue is found in: {}?")

facts("b11-10", [
    "In animal cells cytokinesis takes place by a furrow in the plasma membrane",
    "In plant cells a cell plate forms during cytokinesis",
    "Meiosis II resembles mitosis",
    "The two cells formed after meiosis I have half the chromosome number",
    "Mitosis is an equational division",
    "Centriole duplication happens during S phase in animal cells",
], [
    "Meiosis I is an equational division",
    "In plant cells cytokinesis takes place by a furrow",
    "Meiosis II halves the chromosome number",
    "DNA replicates before meiosis II",
    "Mitosis produces genetically different daughter cells",
    "Chromosome number doubles in S phase",
], "cell division")

table("b11-12", [
    ("Carbohydrate (glucose)", "RQ = 1"), ("Fat (tripalmitin)", "RQ = 0.7"), ("Protein", "RQ = 0.9"), ("Organic acid (malic acid)", "RQ = 1.33"),
], "The respiratory quotient of {} is about:", "Which substrate has {}?")

table("b11-14", [
    ("Vital capacity", "ERV + TV + IRV"), ("Inspiratory capacity", "TV + IRV"), ("Expiratory capacity", "TV + ERV"),
    ("Functional residual capacity", "ERV + RV"), ("Total lung capacity", "RV + ERV + TV + IRV"),
], "{} equals:", "Which capacity equals {}?")

table("b11-16", [
    ("Ammonotelic", "Bony fishes, aquatic amphibians and aquatic insects"), ("Ureotelic", "Mammals, many terrestrial amphibians and marine fishes"),
    ("Uricotelic", "Reptiles, birds, land snails and insects"),
    ("Protonephridia (flame cells)", "Flatworms such as Planaria"), ("Nephridia", "Earthworms and other annelids"),
    ("Malpighian tubules", "Most insects including cockroaches"), ("Antennal (green) glands", "Crustaceans such as prawns"),
], "{}:", "Which excretory type or organ belongs to: {}?")
facts("b11-16", [
    "The counter-current mechanism helps make concentrated urine",
    "The vasa recta runs parallel to the loop of Henle",
    "Micturition is a reflex",
    "Haemodialysis removes urea from blood when the kidneys fail",
    "Renal calculi are stones of crystallised salts in the kidney",
    "Glomerulonephritis is inflammation of the glomeruli",
], [
    "Uricotelic animals excrete mostly ammonia",
    "Mammals are ammonotelic",
    "Birds are ureotelic",
    "The counter-current mechanism dilutes the urine",
    "Flame cells are found in earthworms",
    "Insects excrete through nephridia",
], "excretion")

table("b11-17", [
    ("Ball and socket joint", "Between humerus and pectoral girdle"), ("Hinge joint", "Knee joint"), ("Pivot joint", "Between atlas and axis"),
    ("Gliding joint", "Between the carpals"), ("Saddle joint", "Between the carpal and metacarpal of the thumb"),
    ("Fibrous joint", "Sutures between flat skull bones"), ("Cartilaginous joint", "Between adjacent vertebrae"),
], "An example of a {} is:", "{} is an example of which joint?")

facts("b11-19", [
    "The pineal gland is located on the dorsal side of the forebrain",
    "The thymus degenerates in old individuals",
    "Atrial natriuretic factor is secreted by the heart's atrial wall",
    "Erythropoietin is secreted by the kidney",
    "Gastrin acts on gastric glands to secrete HCl and pepsinogen",
    "Secretin acts on the pancreas to release water and bicarbonate",
], [
    "The pineal gland lies in the neck",
    "The thymus grows larger in old age",
    "Erythropoietin is secreted by the liver",
    "Secretin stimulates HCl release from the stomach",
    "ANF is secreted by the pancreas",
    "Gastrin lowers acid secretion",
], "hormones of other organs")

tag(None)
