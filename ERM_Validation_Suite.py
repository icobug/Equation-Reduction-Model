\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{geometry}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{listings} % За добавяне на Python кода

\geometry{margin=1in}

% Настройки за изгледа на кода
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    stringstyle=\color{red},
    commentstyle=\color{green!60!black},
    numbers=left,
    numberstyle=\tiny\color{gray},
    breaklines=true,
    frame=single,
    backgroundcolor=\color{gray!5}
}

\title{\textbf{The Equation Reduction Model: \\ A Comprehensive Framework for Algebraic Synthesis, Analysis, and Reduction}}
\author{\textbf{Hristo Valentinov Nedelchev} \\ \textit{Independent Researcher}}
\date{March 31, 2026}

\begin{document}

\maketitle

\begin{abstract}
This paper presents the \textbf{Equation Reduction Model (ERM)}, a pioneering discrete system designed to bridge the gap between continuous algebraic complexity and discrete logical stability[cite: 5]. By mapping variables to a minimal state space $\{-1, 0, 1\}$, the model provides a universal "Sieve" for testing equation validity and a "Generator" for synthesizing new algebraic structures[cite: 6]. We provide rigorous validation through symmetry testing, Shannon entropy analysis, and continuous-to-discrete mapping, proving the model's efficiency as a fundamental tool for computational mathematics, information theory, and education[cite: 7, 72].
\end{abstract}

\section{Introduction}
Mathematical complexity often obscures the underlying structural balance of equations[cite: 9, 74]. The ERM introduces a method to strip away numerical noise and reduce any algebraic relationship to its "discrete skeleton"[cite: 10]. This approach allows for:
\begin{itemize}
    \item Reduction of arbitrary equations to minimal forms while preserving essential relationships[cite: 78].
    \item Generation and evaluation of all possible discrete triples[cite: 77].
    \item Systematic analysis of balance, symmetry, and stability[cite: 11].
\end{itemize}

\section{Core Mathematical Principle}
For any three variables $(a, b, c)$ where $a, b, c \in \{-1, 0, 1\}$, we define the core energy function[cite: 14, 83]:
\begin{equation}
F(a, b, c) = a^2 + b^2 + c^2 - (ab + bc + ca)
\end{equation}

The model classifies triples into two fundamental categories[cite: 16, 85]:
\begin{itemize}
    \item \textbf{Valid (Stable/True):} If $F(a, b, c) > 0$[cite: 17, 86].
    \item \textbf{Invalid (Unstable/False):} If $F(a, b, c) = 0$[cite: 18, 86].
\end{itemize}

\section{Methodological Significance: The "Nedelchev Sieve"}
The ERM operates as a bidirectional gateway[cite: 21]:
\begin{enumerate}
    \item \textbf{Forward Mapping (Reduction):} Transforming complex, high-dimensional equations into discrete triples according to sign or relative value[cite: 22, 93]. This serves as a "logical judge" for mathematical hypotheses[cite: 23].
    \item \textbf{Inverse Synthesis (Generation):} Using the identified 24 valid discrete states as a "genetic blueprint" to construct new, balanced algebraic systems[cite: 24, 153].
\end{enumerate}

\section{Statistical and Information Validation}
To establish the model's scientific validity, three computational tests were conducted[cite: 26]:

\subsection{Permutation Symmetry}
The model was tested across all 27 permutations. The results confirmed \textbf{100\% structural invariance}[cite: 28, 29]. This proves that the ERM captures a fundamental algebraic symmetry independent of variable ordering[cite: 29].

\subsection{Information Entropy Analysis}
Using Shannon Entropy, we measured the information density[cite: 31]:
\begin{itemize}
    \item \textbf{Shannon Entropy (H):} 1.837 bits[cite: 32].
    \item \textbf{Entropy Efficiency:} 91.8\%[cite: 33].
\end{itemize}
The model optimally compresses algebraic data into four distinct energy states (0, 1, 3, 4)[cite: 34].

\subsection{Continuous-to-Discrete Mapping}
In a simulation of 1,000 random continuous states, the model successfully filtered 13.8\% of states as "Invalid"[cite: 36]. This confirms its utility as a logical sieve for real-world data and hypothesis testing[cite: 37].

\section{Results and Visualization}
The separation between "Invalid" $(F=0)$ and "Valid" states highlights the model's precision[cite: 39]. 

\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{Energy_Distribution_Plot.png}
    \caption{Distribution of Discrete Energy States. Green columns represent valid structures; Red represents the unstable state[cite: 55, 56].}
\end{figure}

\section{Conclusion}
The Equation Reduction Model enables discrete representation, generation, and reduction of equations while highlighting structural patterns[cite: 161, 162, 163, 164, 165]. It serves as a foundation for further research in discrete mathematics, machine learning, and theoretical physics[cite: 61, 62, 166].

\newpage
\appendix
\section{Python Implementation}
The following code provides computational verification and visualization of the model[cite: 157]:

\begin{lstlisting}
import matplotlib.pyplot as plt

def check_inequality(a, b, c):
    return a**2 + b**2 + c**2 > a*b + b*c + c*a

values = [-1, 0, 1]
results = []

for a in values:
    for b in values:
        for c in values:
            results.append((a, b, c, check_inequality(a, b, c)))

for triple in results:
    print(f"{triple[:3]} -> {triple[3]}")
\end{lstlisting}

\end{document}