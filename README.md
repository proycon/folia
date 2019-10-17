<div align="center">
  <img src="https://raw.githubusercontent.com/proycon/folia/master/logo.png" width="200" />
</div>

# FoLiA: Format for Linguistic Annotation

[![tests](https://travis-ci.org/proycon/folia.svg?branch=master)](https://travis-ci.org/proycon/folia)
[![documentation](http://readthedocs.org/projects/folia/badge/?version=latest)](http://foliapy.readthedocs.io/en/latest/?badge=latest)
[![lamabadge](http://applejack.science.ru.nl/lamabadge.php/folia)](http://applejack.science.ru.nl/languagemachines/)
[![DOI](https://zenodo.org/badge/1948022.svg)](https://zenodo.org/badge/latestdoi/1948022)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

[Documentation](http://foliapy.readthedocs.io/en/latest/?badge=latest) | [Examples](https://github.com/proycon/folia/tree/master/examples) | [Python Library](https://pypi.org/project/FoLiA/) | [Python Library Documentation](https://foliapy.readthedocs.io/en/latest/) | [C++ Library](https://github.com/LanguageMachines/libfolia) | [FoLiA-Tools](https://github.com/proycon/foliatools) | [FoLiA Utilities](https://github.com/LanguageMachines/foliautils) | [FLAT: Web-based Annotation environment](https://github.com/proycon/flat)

*by Maarten van Gompel, Radboud University Nijmegen*

<https://proycon.github.io/folia>

FoLiA is an XML-based annotation format, suitable for the representation
of linguistically annotated language resources. FoLiA's intended use is
as a format for storing and/or exchanging language resources, including
corpora. Our aim is to introduce a single rich format that can
accommodate a wide variety of linguistic annotation types through a
single generalised paradigm. We do not commit to any label set, language
or linguistic theory. This is always left to the developer of the
language resource, and provides maximum flexibility.

XML is an inherently hierarchic format. FoLiA does justice to this by
maximally utilising a hierarchic, inline, setup. We inherit from the
D-Coi format, which posits to be loosely based on a minimal subset of
TEI. Because of the introduction of a new and much broader paradigm,
FoLiA is not backwards-compatible with D-Coi, i.e. validators for D-Coi
will not accept FoLiA XML. It is however easy to convert FoLiA to less
complex or verbose formats such as the D-Coi format, or plain-text.
Converters are provided.

The main characteristics of FoLiA are:

-   **Generalised paradigm** - We use a generalised paradigm, with as
    few ad-hoc provisions for annotation types as possible.
-   **Expressivity** - The format is highly expressive, annotations can
    be expressed in great detail and with flexibility to the user's
    needs, without forcing unwanted details. Moreover, FoLiA has
    generalised support for representing annotation alternatives, and
    annotation metadata such as information on annotator, time of
    annotation, and annotation confidence.
-   **Extensible** - Due to the generalised paradigm and the fact that
    the format does not commit to any label set, FoLiA is fairly easily
    extensible.
-   **Formalised** - The format is formalised, and can be validated on
    both a shallow and a deep level (the latter including tagset
    validation), and easily machine parsable, for which tools are
    provided.
-   **Practical** - FoLiA has been developed in a bottom-up fashion
    right alongside applications, libraries, and other toolkits and
    converters. Whilst the format is rich, we try to maintain it as
    simple and straightforward as possible, minimising the learning
    curve and making it easy to adopt FoLiA in practical applications.

The FoLiA format makes mixed-use of inline and stand-off annotation.
Inline annotation is used for annotations pertaining to single tokens,
whilst stand-off annotation in a separate annotation layers is adopted
for annotation types that span over multiple tokens. This provides FoLiA
with the necessary flexibility and extensibility to deal with various
kinds of annotations.

Notable features are:

-   XML-based, UTF-8 encoded
-   Language and tagset independent
-   Can encode both tokenised as well as untokenised text + partial
    reconstructability of untokenised form even after tokenisation.
-   Generalised paradigm, extensible and flexible
-   Provenance support for all linguistic annotations: annotator, type
    (automatic or manual), time.
-   Used by various software projects and corpora, especially in the
    Dutch-Flemish NLP community

Paradigm Schema
===============

<div align="center">
  <img src="https://github.com/proycon/folia/blob/master/docs/folia_paradigm2.png" width="800" />
</div>

Resources
=========

-   [Website](https://proycon.github.io/folia) - **Please visit this
    FoLiA website for more information**
-   [Documentation](https://folia.readthedocs.io)
-   [RelaxNG schema](http://github.com/proycon/folia/blob/master/schemas/folia.rng)
    (not sufficient for full validation, use the
    [foliavalidator](https://github.com/proycon/foliatools) or
    [folialint](https://github.com/LanguageMachines/libfolia) tool!)
-   [Examples of FoLiA documents](https://github.com/proycon/folia/tree/master/examples)
-   [FoLiApy: FoLiA library for Python](https://github.com/proycon/foliapy) (`pip install folia`)
    -   [Library documentation](https://foliapy.readthedocs.io)
-   [libfolia: FoLiA library C++](https://github.com/LanguageMachines/libfolia)
-   [FoLiA Tools: Various command-line tools for FoLiA](https://github.com/proycon/foliatools)
    (`pip install folia-tools`)
-   [FoLiA Utilities: Various command-line tools for FoLiA](https://github.com/LanguageMachines/foliautils)
-   [FLAT: A web-based annotation environment](https://github.com/proycon/flat)

A more extensive list of FoLiA-capable software is maintained on the
[FoLiA website](https://proycon.github.io/folia)

Publications
============

See the [FoLiA website](https://proycon.github.io/folia) for more
publications and full text links.

-   Maarten van Gompel (2019). FoLiA: Format for Linguistic Annotation -
    Documentation. Language and Speech Technology Technical Report
    Series. Radboud University Nijmegen.
-   Maarten van Gompel, Ko van der Sloot, Martin Reynaert, Antal van den
    Bosch (2017). **FoLiA in Practice: The Infrastructure of a
    Linguistic Annotation Format.** In: CLARIN in the Low Countries.
    Eds: Jan Odijk and Arjan van Hessen. Pp. 71-81.
    [PDF](https://www.jstor.org/stable/j.ctv3t5qjk.13?seq=1#metadata_info_tab_contents)
-   Maarten van Gompel & Martin Reynaert (2014). **FoLiA: A practical
    XML format for linguistic annotation - a descriptive and comparative
    study;** Computational Linguistics in the Netherlands Journal;
    3:63-81; 2013. [PDF](https://clinjournal.org/clinj/article/view/26/22)
-   Maarten van Gompel (2014). **FoLiA: Format for Linguistic
    Annotation. Documentation.** Language and Speech Technology
    Technical Report Series LST-14-01. Radboud University Nijmegen.
