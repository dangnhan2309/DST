import json

# Define the labels and their meanings
labels_data = {
    "econ.EM": "Econometric Theory, Micro-Econometrics, Macro-Econometrics, Empirical Content of Economic Relations discovered via New Methods, Methodological Aspects of the Application of Statistical Inference to Economic Data.",
    "econ.GN": "General methodological, applied, and empirical contributions to economics.",
    "econ.TH": "Includes theoretical contributions to Contract Theory, Decision Theory, Game Theory, General Equilibrium, Growth, Learning and Evolution, Macroeconomics, Market and Mechanism Design, and Social Choice.",
    "eess.AS": "Theory and methods for processing signals representing audio, speech, and language, and their applications.",
    "eess.IV": "Theory, algorithms, and architectures for the formation, capture, processing, communication, analysis, and display of images, video, and multidimensional signals in a wide variety of applications.",
    "eess.SP": "Theory, algorithms, performance analysis and applications of signal and data analysis.",
    "eess.SY": "Theoretical and experimental research covering all facets of automatic control systems.",
    "math.AC": "Commutative rings, modules, ideals, homological algebra, computational aspects, invariant theory, connections to algebraic geometry and combinatorics.",
    "math.AG": "Algebraic varieties, stacks, sheaves, schemes, moduli spaces, complex geometry, quantum cohomology.",
    "math.AP": "Existence and uniqueness, boundary conditions, linear and non-linear operators, stability, soliton theory, integrable PDEs, conservation laws, qualitative dynamics.",
    "math.AT": "Homotopy theory, homological algebra, algebraic treatments of manifolds.",
    "math.CA": "Special functions, orthogonal polynomials, harmonic analysis, ODEs, differential relations, calculus of variations, approximations, expansions, asymptotics.",
    "math.CO": "Discrete mathematics, graph theory, enumeration, combinatorial optimization, Ramsey theory, combinatorial game theory.",
    "math.CT": "Enriched categories, topoi, abelian categories, monoidal categories, homological algebra.",
    "math.CV": "Holomorphic functions, automorphic group actions and forms, pseudoconvexity, complex geometry, analytic spaces, analytic sheaves.",
    "math.DG": "Complex, contact, Riemannian, pseudo-Riemannian and Finsler geometry, relativity, gauge theory, global analysis.",
    "math.DS": "Dynamics of differential equations and flows, mechanics, classical few-body problems, iterations, complex dynamics, delayed differential equations.",
    "math.FA": "Banach spaces, function spaces, real functions, integral transforms, theory of distributions, measure theory.",
    "math.GM": "Mathematical material of general interest, topics not covered elsewhere.",
    "math.GN": "Continuum theory, point-set topology, spaces with algebraic structure, foundations, dimension theory, local and global properties.",
    "math.GR": "Finite groups, topological groups, representation theory, cohomology, classification and structure.",
    "math.GT": "Manifolds, orbifolds, polyhedra, cell complexes, foliations, geometric structures.",
    "math.HO": "Biographies, philosophy of mathematics, mathematics education, recreational mathematics, communication of mathematics, ethics in mathematics.",
    "math.IT": "Covers theoretical and experimental aspects of information theory and coding.",
    "math.KT": "Algebraic and topological K-theory, relations with topology, commutative algebra, and operator algebras.",
    "math.LO": "Logic, set theory, point-set topology, formal mathematics.",
    "math.MG": "Euclidean, hyperbolic, discrete, convex, coarse geometry, comparisons in Riemannian geometry, symmetric spaces.",
    "math.MP": "Application of mathematics to problems in physics, mathematical methods for such applications, rigorous formulations of physical theories.",
    "math.NA": "Numerical algorithms for problems in analysis and algebra, scientific computation.",
    "math.NT": "Prime numbers, diophantine equations, analytic number theory, algebraic number theory, arithmetic geometry, Galois theory.",
    "math.OA": "Algebras of operators on Hilbert space, C^*-algebras, von Neumann algebras, non-commutative geometry.",
    "math.OC": "Operations research, linear programming, control theory, systems theory, optimal control, game theory.",
    "math.PR": "Theory and applications of probability and stochastic processes.",
    "math.QA": "Quantum groups, skein theories, operadic and diagrammatic algebra, quantum field theory.",
    "math.RA": "Non-commutative rings and algebras, non-associative algebras, universal algebra and lattice theory, linear algebra, semigroups.",
    "math.RT": "Linear representations of algebras and groups, Lie theory, associative algebras, multilinear algebra.",
    "math.SG": "Hamiltonian systems, symplectic flows, classical integrable systems.",
    "math.SP": "Schrodinger operators, operators on manifolds, general differential operators, numerical studies, integral operators, discrete models, resonances, non-self-adjoint operators, random operators/matrices.",
    "math.ST": "Applied, computational and theoretical statistics."
}

# Define the file path
json_file_path = "D:\\DST\\material\\Lable_n_meaning.json"

# Save to JSON file
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(labels_data, json_file, indent=4, ensure_ascii=False)

# Confirm the file was created
json_file_path
