.. _features:

Features
===============

In addition to a main class, an arbitrary number of *features* can be
added to *any* annotation element that takes a set. Each feature pertains to a specific
*subset* in that set and assigns a *class* in the subset. The subsets and classes therein are defined in the
set definition (See :ref:`set_definition`), so may be entirely user-defined.

The element ``<feat>`` is used to add features to any kind of annotation. In
the following example we make use of a subset we invented which ties a lemma to
its plural form. This is just an example, you can think of any subset you like and associate all kinds of information
with it.

.. code-block:: xml

 <lemma class="house">
   <feat subset="plural" class="houses" />
 </lemma>

.. note::

    Do make sure not to use features and create subsets if there is already a more appropriate FoLiA annotation
    available. For example; don't use a part-of-speech subset in a lemma set, because there is already :ref:`pos_annotation` for that.

A more thorough example for part-of-speech tags with features will be explained
in Section~\ref{sec:posfeat}.

Some annotation types take *predefined subsets* because some features are very commonly used. These subsets have clearly
defined semantics. However, it still depends on the set on whether these can be used, and which classes these take.
Whenever subsets are predefined by FoLiA, they can be assigned directly using *XML attributes*. Consider the
following example of lexical semantic sense annotation, in which subset ``synset`` is a predefined subset.

.. code-block:: xml

    <sense class="X" synset="Y" />

This is semantically equivalent to:

.. code-block:: xml

    <sense class="X">
        <feat subset="synset" class="Y" />
    </sense>


The following example of event annotation with the feature with predefined
subset ``actor`` is similar:

.. code-block:: xml

    <event class="tweet" actor="John Doe">
     ...
    </event>

.. code-block:: xml

    <event class="tweet">
     <feat subset="actor" class="John Doe" />
     ...
    </event>

Features can also be used to assign multiple classes within the same subset,
which is impossible with main classes. In the following example the event is
associated with a list of two actors. In this case the XML attribute shortcut
no longer suffices, and the ``<feat>`` element must be used explicitly.

.. TODO: is this really implemented well in the libraries??
.. code-block:: xml
    <event class="conversation">
     <feat subset="actor" class="John Doe" />
     <feat subset="actor" class="Jane Doe" />
     <p>...</p>
    </event>

To recap: the ``<feat>`` element can always be used freely to associate
*any* additional classes of *any* designed subset with *any*
annotation element. For certain elements, there are predefined subsets, in
which case you can assign them using the XML attribute shortcut. This, however,
only applies to the predefined subsets.

Another elaborate example of features can be found in the section on :ref:`pos_annotation`.
