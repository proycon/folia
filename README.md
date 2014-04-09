FoLiA: Format for Linguistic Annotation
=========================================

*by Maarten van Gompel, Radboud University Nijmegen*

http://proycon.github.io/folia


FoLiA is an XML-based annotation format, suitable for the representation of
linguistically annotated language resources. FoLiA’s intended use is as a
format for storing and/or exchanging language resources, including corpora. Our
aim is to introduce a single rich format that can accomodate a wide variety of
linguistic annotation types through a single generalised paradigm. We do not
commit to any label set, language or linguistic theory. This is always left to
the developer of the language resource, and provides maximum flexibility.

XML is an inherently hierarchic format. FoLiA does justice to this by maximally
utilising a hierarchic, inline, setup. We inherit from the D-Coi format, which
posits to be loosely based on a minimal subset of TEI. Because of the
introduction of a new and much broader paradigm, FoLiA is not
backwards-compatible with D-Coi, i.e. validators for D-Coi will not accept
FoLiA XML. It is however easy to convert FoLiA to less complex or verbose
format s such as the D-Coi format, or plain-text. Converters are provided.

The main characteristics of FoLiA are:

 * **Generalised paradigm** - We use a generalised paradigm, with as few ad-hoc provisions for annotation types as possible.
 * **Expressivity** - The format is highly expressive, annotations can be expressed in great detail and with flexibility to the user’s needs, without forcing unwanted details. Moreover, FoLiA has generalised support for representing annotation alternatives, and annotation metadata such as information on annotator, time of annotation, and annotation confidence.
 * **Extensible** - Due to the generalised paradigm and the fact that the format does not commit to any label set, FoLiA is fairly easily extensible.
 * **Formalised** - The format is formalised, and can be validated on both a shallow and a deep level (the latter including tagset validation), and easily machine parsable, for which tools are provided.
 * **Practical** - FoLiA has been developed in a bottom-up fashion right alongside applications, libraries, and other toolkits and converters. Whilst the format is rich, we try to maintain it as simple and straightforward as possible, minimising the learning curve and making it easy to adopt FoLiA in practical applications.

The FoLiA format makes mixed-use of inline and stand-off annotation. Inline
annotation is used for annotations pertaining to single tokens, whilst
stand-off annotation in a separate annotation layers is adopted for annotation
types that span over multiple tokens. This provides FoLiA with the necessary
flexibility and extensibility to deal with various kinds of annotations.

Notable features are:

 * XML-based, UTF-8 encoded
 * Language and tagset independent
 * Can encode both tokenised as well as untokenised text + partial reconstructability of untokenised form even after tokenisation.
 * Generalised paradigm, extensible and flexible
 * Provenance support for all linguistic annotations: annotator, type (automatic or manual), time.
 * Used by various software projects and corpora, especially in the Dutch-Flemish NLP community

Resources
----------

 * [**Website**](http://proycon.github.io/folia)
 * [**Documentation**](http://github.com/proycon/folia/blob/master/docs/folia.pdf?raw=true)
 * [**RelaxNG schema**](http://github.com/proycon/folia/blob/master/schemas/folia.rng)
 * **Example** of a FoLiA document (with in-browser visualisation through XSL, use view source for XML): http://proycon.github.io/folia/example.xml
 * **FoLiA library for Python**: [``pynlpl.formats.folia``](http://github.com/proycon/pynlpl/blob/master/formats/folia.py)
 * **C++ Library**: [``libfolia``](http://ilk.uvt.nl/folia/download-libfolia.php), *by Ko van der Sloot (Tilburg University)*

Publications
-------------

* Maarten van Gompel & Martin Reynaert (2014). **FoLiA: A practical XML format for linguistic annotation - a descriptive and comparative study;** Computational Linguistics in the Netherlands Journal; 3:63-81; 2013.
* Maarten van Gompel (2014). **FoLiA: Format for Linguistic Annotation. Documentation.** Language and Speech Technology Technical Report Series LST-14-01. Radboud University Nijmegen.

More?
----------

Please consult the FoLiA website at http://proycon.github.io/folia for more!
