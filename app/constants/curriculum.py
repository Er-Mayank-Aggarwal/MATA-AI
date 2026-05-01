"""
CBSE 2026-27 NEW Competency-Based Curriculum Chapter Maps (NCF-SE 2023)
Based on uploaded syllabus PDFs.
"""

CURRICULUM = {
    9: {
        "mathematics": {
            "subject_full": "Mathematics (Class 9)",
            "chapters": {
                1:  {"title": "Number System",                   "topics": ["Rational numbers", "Irrational numbers", "Proofs of irrationality of sqrt(2) and sqrt(3)", "Square root spiral", "Real numbers on number line"]},
                2:  {"title": "Introduction to Polynomials",      "topics": ["Algebraic expressions", "Definition of polynomial", "Degree", "Linear polynomials", "Linear growth and decay"]},
                3:  {"title": "Sequences and Progressions",      "topics": ["Arithmetic Progressions (AP)", "Geometric Progressions (GP)", "Sum of first n natural numbers", "Fractals", "Tower of Hanoi"]},
                4:  {"title": "Exploring Algebraic Identities",  "topics": ["Visualising identities using geometric models", "Factorisation using identities", "Algebra tiles", "Rational expressions"]},
                5:  {"title": "Linear Equations in Two Variables","topics": ["Graphical representation", "Slope-intercept form", "Substitution and elimination methods", "Practical applications"]},
                6:  {"title": "Coordinate Geometry",              "topics": ["Cartesian system", "Distance formula", "Midpoint of line segment", "Right-angled triangle verification"]},
                7:  {"title": "Introduction to Euclid’s Geometry", "topics": ["Baudhayana’s Sulbasutras", "Axioms and Postulates", "Constructing a square", "History of geometry"]},
                8:  {"title": "Lines and Angles",                 "topics": ["Rays and angles", "Intersecting and parallel lines", "Theorems on angles", "Linear pair theorem"]},
                9:  {"title": "Triangles – Congruence Theorems", "topics": ["Triangle rigidity", "Congruence criteria (SAS, SSS, ASA, RHS, AAS)", "Isosceles triangle properties", "SSA condition analysis"]},
                10: {"title": "4-gons (Quadrilaterals)",          "topics": ["Properties of parallelograms", "Midpoint theorem", "Central symmetry", "Tiling a plane"]},
                11: {"title": "Circles",                          "topics": ["Chords and subtended angles", "Perpendicular from centre", "Cyclic quadrilaterals", "Tangents basics"]},
                12: {"title": "Area and Perimeter",               "topics": ["Perimeter of circle", "Pi and its history", "Length of arc", "Heron’s formula", "Brahmagupta’s formula for cyclic 4-gon"]},
                13: {"title": "Surface Area and Volume",          "topics": ["Surface area and volume of spheres", "Hemispheres", "Right circular cones", "Pyramids"]},
                14: {"title": "Statistics",                       "topics": ["Graphical representation (stacked bar graphs)", "Measures of central tendency (mean, median, mode)", "Weighted average"]},
                15: {"title": "Introduction to Probability",      "topics": ["Randomness and probability scale", "Empirical vs Theoretical probability", "Tree diagrams and tables"]},
            },
        },
        "science": {
            "subject_full": "Science (Class 9)",
            "chapters": {
                1:  {"title": "Matter and its Properties",        "topics": ["Atomic level interactions", "Classification of elements", "Investigating nature of substances", "Chemical interactions and symbols"]},
                2:  {"title": "Cell - Unit of Life",               "topics": ["Discovery of cell", "Prokaryotic vs Eukaryotic", "Organelles (Nucleus, Mitochondria, etc.)", "Permeability", "Cell division (Mitosis/Meiosis)"]},
                3:  {"title": "Tissues",                           "topics": ["Plant vs Animal tissues", "Meristematic and Permanent", "Epithelial, Connective, Muscular, Nervous", "Musculoskeletal system care"]},
                4:  {"title": "Diversity in Living Organisms",    "topics": ["Classification importance", "Five kingdoms", "Binomial nomenclature", "Three domains of classification"]},
                5:  {"title": "Exploring Mixtures",               "topics": ["Homogeneous vs Heterogeneous", "Solutions, Suspensions, Colloids", "Separation techniques (Crystallisation, Distillation, Centrifugation)"]},
                6:  {"title": "Structure of an Atom",             "topics": ["Subatomic particles", "Atomic Models (Thomson, Rutherford, Bohr)", "Valency", "Isotopes and Isobars"]},
                7:  {"title": "Atoms and Molecules",               "topics": ["Laws of conservation of mass", "Dalton’s Atomic theory", "Molecules and Ions", "Writing chemical formulae"]},
                8:  {"title": "Earth as a System",                "topics": ["Interconnected spheres (Biosphere, Geosphere, etc.)", "Solar energy interaction", "Biogeochemical cycles (Water, Carbon, Nitrogen)"]},
                9:  {"title": "Motion",                            "topics": ["Displacement, Velocity, Acceleration", "Graphical representation", "Equations of motion", "Uniform circular motion"]},
                10: {"title": "Force and Laws of Motion",         "topics": ["Balanced/Unbalanced forces", "Newton’s Laws of Motion", "Inertia and Momentum", "Force of friction"]},
                11: {"title": "Work, Energy and Simple Machines", "topics": ["Work done", "Kinetic and Potential energy", "Power", "Simple machines (Pulley, Inclined plane, Lever)", "Mechanical advantage"]},
                12: {"title": "Sound",                            "topics": ["Production and propagation", "Wavelength, Frequency, Amplitude", "Human perception", "Reflection, Echo, SONAR"]},
            },
        },
        "social_science": {
            "subject_full": "Social Science (Class 9)",
            "chapters": {
                1:  {"title": "Understanding Social Science",     "topics": ["Meaning and scope", "Indian perspective", "Interconnections between disciplines"]},
                2:  {"title": "Shaping of Earth’s Surface",       "topics": ["Plate tectonics", "Weathering and Erosion", "Landforms and Disasters (GLOF, Landslides)"]},
                3:  {"title": "Atmosphere and Climate",           "topics": ["Atmospheric layers", "Monsoons", "Climate change and Carbon footprint"]},
                4:  {"title": "Early Humans and Civilisation",    "topics": ["Palaeolithic to Neolithic", "Harappan and Mesopotamian cultures", "Transition to food production"]},
                5:  {"title": "State and Society (upto 1000 CE)", "topics": ["Vedic Age", "Administrative structure of early empires", "Knowledge traditions of India"]},
                6:  {"title": "Democracy",                         "topics": ["Features and types", "Roots of democracy in India", "Challenges and Global systems"]},
                7:  {"title": "Elections",                         "topics": ["Electoral systems", "Election Commission of India", "Party system in India", "Coalition governments"]},
                8:  {"title": "Building Blocks in Economics",     "topics": ["Scarcity and choice", "Opportunity cost", "Economic systems (Market vs Planned)"]},
                9:  {"title": "The Price Puzzle",                 "topics": ["Laws of demand and supply", "Market failures", "Public goods", "Price ceilings"]},
                10: {"title": "Oceans and Life",                  "topics": ["Ocean relief and movement", "Marine resources", "Cyclones and Tsunamis"]},
                11: {"title": "Life on Earth",                    "topics": ["Biomes", "Biosphere reserves in India", "Forest conservation and Ecotourism"]},
                12: {"title": "Resistance and Resilience",        "topics": ["Regional kingdoms (1000-1700 CE)", "Bhakti tradition", "Forts and fortifications"]},
                13: {"title": "India and the World-I",            "topics": ["Early trade relations", "Cultural connections (Greece, Rome, SE Asia)", "Indian Knowledge Systems"]},
                14: {"title": "Roots of Authority",               "topics": ["Kautilya and Shukraniti", "Danda, Nyaya and Bala", "Post-independence justice concepts"]},
                15: {"title": "From Ideas to Startups",           "topics": ["Entrepreneurship meaning", "MSMEs and Startup India", "Creating a business plan"]},
                16: {"title": "Smart Ways to Manage Finances",     "topics": ["Personal financial management", "Budgeting", "Compound interest vs Simple interest", "Risk and Insurance"]},
            },
        }
    },
    10: {
        "mathematics": {
            "subject_full": "Mathematics (Class 10)",
            "chapters": {
                1:  {"title": "Real Numbers",                        "topics": ["Fundamental Theorem of Arithmetic", "Proofs of irrationality of sqrt(2), sqrt(3), sqrt(5)"]},
                2:  {"title": "Polynomials",                         "topics": ["Zeros of a polynomial", "Relationship between zeros and coefficients of quadratic polynomials"]},
                3:  {"title": "Pair of Linear Equations",            "topics": ["Graphical method of solution", "Consistency and Inconsistency", "Substitution and Elimination methods"]},
                4:  {"title": "Quadratic Equations",                 "topics": ["Standard form", "Solutions by factorisation and quadratic formula", "Nature of roots"]},
                5:  {"title": "Arithmetic Progressions",             "topics": ["nth term of an AP", "Sum of first n terms", "Applications in daily life"]},
                6:  {"title": "Coordinate Geometry",                 "topics": ["Distance formula", "Section formula (internal division)"]},
                7:  {"title": "Triangles",                           "topics": ["Similar figures", "Similarity criteria (AAA, SAS, SSS)", "Basic Proportionality Theorem"]},
                8:  {"title": "Circles",                             "topics": ["Tangent to a circle", "Point of contact", "Theorems on tangents"]},
                9:  {"title": "Introduction to Trigonometry",        "topics": ["Trigonometric ratios of acute angles", "Values at 30, 45, 60 degrees", "Relationships between ratios"]},
                10: {"title": "Trigonometric Identities",           "topics": ["Proof and application of sin^2 A + cos^2 A = 1"]},
                11: {"title": "Heights and Distances",               "topics": ["Angle of elevation and depression (30, 45, 60 degrees)"]},
                12: {"title": "Areas Related to Circles",            "topics": ["Area of sectors and segments of a circle"]},
                13: {"title": "Surface Areas and Volumes",           "topics": ["Surface area and volume of combinations of cubes, spheres, cylinders, cones"]},
                14: {"title": "Statistics",                          "topics": ["Mean, median and mode of grouped data", "Assumed mean and step deviation methods"]},
                15: {"title": "Probability",                         "topics": ["Classical definition of probability", "Simple problems on single events"]},
            },
        },
        "science": {
            "subject_full": "Science (Class 10)",
            "chapters": {
                1:  {"title": "Chemical Reactions and Equations",    "topics": ["Balanced chemical equations", "Combination reactions", "Decomposition reactions", "Displacement reactions", "Double Displacement reactions", "Oxidation and reduction (Redox)", "Exothermic and Endothermic reactions", "Effects of oxidation in everyday life (Corrosion and Rancidity)"]},
                2:  {"title": "Acids, Bases and Salts",              "topics": ["Indicators", "pH scale importance", "Neutralization", "Preparation of Sodium Hydroxide, Bleaching Powder, Baking Soda"]},
                3:  {"title": "Metals and Non-metals",               "topics": ["Physical/Chemical properties", "Reactivity series", "Metallurgy", "Corrosion and prevention"]},
                4:  {"title": "Carbon and its Compounds",            "topics": ["Covalent bonding", "Versatile nature of carbon", "Homologous series", "Ethanol and Ethanoic acid", "Soaps and detergents"]},
                5:  {"title": "Life Processes",                      "topics": ["Nutrition in plants/animals", "Respiration", "Transportation", "Excretion"]},
                6:  {"title": "Control and Co-ordination",            "topics": ["Nervous system", "Tropic movements in plants", "Plant hormones", "Animal hormones"]},
                7:  {"title": "Reproduction",                        "topics": ["Asexual and sexual reproduction", "Reproduction in flowering plants", "Reproduction in humans", "Reproductive health"]},
                8:  {"title": "Heredity",                            "topics": ["Mendel’s contribution", "Laws for inheritance of traits", "Sex determination"]},
                9:  {"title": "Light - Reflection and Refraction",   "topics": ["Spherical mirrors", "Mirror and Lens formulae", "Refractive index", "Power of a lens"]},
                10: {"title": "Human Eye and Colourful World",       "topics": ["Human eye structure", "Defects of vision", "Refraction through prism", "Atmospheric refraction", "Scattering of light"]},
                11: {"title": "Electricity",                         "topics": ["Ohm’s law", "Resistance and Resistivity", "Resistors in series/parallel", "Heating effect", "Electric power"]},
                12: {"title": "Magnetic Effects of Electric Current","topics": ["Magnetic field lines", "Force on current carrying conductor", "Fleming’s Left Hand Rule", "Domestic electric circuits"]},
                13: {"title": "Our Environment",                     "topics": ["Ecosystems", "Food chains and webs", "Ozone depletion", "Waste management"]},
            },
        },
        "social_science": {
            "subject_full": "Social Science (Class 10)",
            "chapters": {
                1:  {"title": "Rise of Nationalism in Europe",       "topics": ["French Revolution impact", "Unification of Germany and Italy", "Visualising the nation"]},
                2:  {"title": "Nationalism in India",                "topics": ["Non-Cooperation Movement", "Civil Disobedience Movement", "Sense of collective belonging"]},
                3:  {"title": "The Making of a Global World",        "topics": ["Pre-modern world", "19th century globalisation", "Conquest, disease and trade"]},
                4:  {"title": "Print Culture and the Modern World",  "topics": ["Print revolution in Europe", "Print in India", "Women and Print", "Dissent and Censorship"]},
                5:  {"title": "Resources and Development",           "topics": ["Types of resources", "Resource planning in India", "Land and Soil resources"]},
                6:  {"title": "Forest and Wildlife Resources",       "topics": ["Types of forests", "Conservation of biodiversity", "Community and conservation"]},
                7:  {"title": "Water Resources",                     "topics": ["Water scarcity", "Multi-purpose projects", "Rainwater harvesting"]},
                8:  {"title": "Agriculture",                         "topics": ["Types of farming", "Cropping patterns", "Major crops", "Contribution to national economy"]},
                9:  {"title": "Minerals and Energy Resources",       "topics": ["Minerals in India", "Conventional and Non-conventional energy", "Conservation"]},
                10: {"title": "Manufacturing Industries",            "topics": ["Agro-based industries", "Mineral-based industries", "Industrial pollution"]},
                11: {"title": "Lifelines of National Economy",       "topics": ["Roadways, Railways, Waterways", "Major ports and International airports", "Communication"]},
                12: {"title": "Power Sharing",                       "topics": ["Belgium and Sri Lanka case studies", "Why power sharing is desirable", "Forms of power sharing"]},
                13: {"title": "Federalism",                          "topics": ["What is federalism", "Federalism in India", "Decentralisation", "Panchayati Raj"]},
                14: {"title": "Gender, Religion and Caste",         "topics": ["Gender and politics", "Communalism", "Caste inequality"]},
                15: {"title": "Political Parties",                   "topics": ["Why do we need parties", "National and State parties", "Challenges and reforms"]},
                16: {"title": "Outcomes of Democracy",               "topics": ["Accountable and responsive government", "Economic growth", "Reduction of inequality"]},
                17: {"title": "Development",                         "topics": ["Development goals", "National income", "HDI", "Sustainability"]},
                18: {"title": "Sectors of the Indian Economy",       "topics": ["Primary, Secondary, Tertiary", "Comparing sectors", "Organised and Unorganised", "GDP contribution"]},
                19: {"title": "Money and Credit",                    "topics": ["Money as medium of exchange", "Sources of credit", "Self Help Groups (SHGs)"]},
                20: {"title": "Globalisation and the Indian Economy","topics": ["What is globalisation", "Factors enabling globalisation", "WTO", "Production across countries"]},
            },
        }
    }
}

VALID_CLASSES = [9, 10]
VALID_SUBJECTS = ["mathematics", "science", "social_science"]

QUESTION_TYPES = {
    "mcq": "Multiple Choice Questions (MCQ)",
    "assertion_reason": "Assertion-Reason Questions",
    "short_answer": "Short Answer Questions",
    "long_answer": "Long Answer Questions",
    "case_study": "Case Study Based Questions",
}