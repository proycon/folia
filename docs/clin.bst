% BibTeX standard bibliography style `kluwer' (one of the harvard family)
    % version 0.99a for BibTeX versions 0.99a or later, LaTeX version 2.09.
    % Copyright (C) 1991, all rights reserved.
    % Copying of this file is authorized only if either
    % (1) you make absolutely no changes to your copy, including name, or
    % (2) if you do make changes, you name it something other than
    % btxbst.doc, plain.bst, unsrt.bst, alpha.bst, abbrv.bst, agsm.bst,
        % dcu.bst or kluwer.bst.
    % This restriction helps ensure that all standard styles are identical.
    % The file harvard.tex has the documentation for this style.

% ACKNOWLEDGEMENT:
%   This document is a modified version of alpha.bst to which it owes much of
%   its functionality.
%   The functions format.lab.names.full, format.names, format.names.ed, format.editors and supporting functions (like bbl.etal) come from compling.bst
%   (http://ron.artstein.org/resources/compling.bst)

% AUTHOR
%   Peter Williams, Key Centre for Design Quality, Sydney University
%   e-mail: peterw@archsci.arch.su.oz.au

% CHANGES for CLIN2007 Proceedings, March 2008
% Suzan Verberne, Dept. of Linguistics, Radboud University Nijmegen,
% e-mail s.verberne@let.ru.nl
% With thanks to Hendri Hondorp and Ron Artstein
% Changed:
% - A citation to a publication with more than 2 authors is now formatted as (First Author et al. Year) 
%   A citation to a publication with exactly 2 authors is formatted as (First Author and Second Author Year)
% - "edn" as in 'xth edition' is changed to "ed."
% - The Fields 'series' and 'number' of a @PhdThesis-type entry are now also shown in the result
% - A field type \url added to all publication types
% - In the list of author names, the order of first and last names has been changed to "Author, First, Second Author, Third Author and Fourth Author"
%   (here, the ordinal denotes the first name and the word 'Author' the last name)
% - A whitespace added before '(year)' in the bibliography

% CHANGES December 2011 by Peter Kleiweg
% Bug fix in function format.number.series


ENTRY
  { address
    author
    booktitle
    chapter
    edition
    editor
    howpublished
    institution
    journal
    key
    month
    note
    number
    organization
    pages
    publisher
    school
    series
    title
    type
    volume
    year
    url
  }
  { field.used }
  { extra.label sort.label list.year }

INTEGERS { output.state before.all mid.sentence after.sentence after.block }

FUNCTION {init.state.consts}
{ #0 'before.all :=
  #1 'mid.sentence :=
  #2 'after.sentence :=
  #3 'after.block :=
}

STRINGS { s t f }

FUNCTION {output.nonnull}
{ 's :=
  output.state mid.sentence =
    { ", " * write$ }
    { output.state after.block =
    { add.period$ write$
      newline$
      "\newblock " write$
    }
    { output.state before.all =
        'write$
        { add.period$ " " * write$ }
      if$
    }
      if$
      mid.sentence 'output.state :=
    }
  if$
  s
}

FUNCTION {output}
{ duplicate$ empty$
    'pop$
    'output.nonnull
  if$
}

FUNCTION {output.check}
{ 't :=
  duplicate$ empty$
    { pop$ "empty " t * " in " * cite$ * warning$ }
    'output.nonnull
  if$
}

FUNCTION {item.check}
{ 't :=
  empty$
    { "empty " t * " in " * cite$ * warning$ }
    { skip$ }
  if$
}

FUNCTION {fin.entry}
{ add.period$
  write$
  newline$
}

FUNCTION {new.block}
{ output.state before.all =
    'skip$
    { after.block 'output.state := }
  if$
}

FUNCTION {not}
{   { #0 }
    { #1 }
  if$
}

FUNCTION {and}
{   'skip$
    { pop$ #0 }
  if$
}

FUNCTION {or}
{   { pop$ #1 }
    'skip$
  if$
}

FUNCTION {field.or.null}
{ duplicate$ empty$
    { pop$ "" }
    'skip$
  if$
}

FUNCTION {emphasize}
{ duplicate$ empty$
    { pop$ "" }
    { "{\em " swap$ * "}" * }
  if$
}


FUNCTION {embolden}
{ duplicate$ empty$
    { pop$ "" }
    { "{\bf " swap$ * "}" * }
  if$
}

FUNCTION {quote}
{ duplicate$ empty$
    { pop$ "" }
    { "`" swap$ * "'" * }
  if$
}
FUNCTION {bibinfo.check}
{ swap$
  duplicate$ missing$
    {
      pop$ pop$
      ""
    }
    { duplicate$ empty$
        {
          swap$ pop$
        }
        { swap$
          pop$
        }
      if$
    }
  if$
}
FUNCTION {bibinfo.warn}
{ swap$
  duplicate$ missing$
    {
      swap$ "missing " swap$ * " in " * cite$ * warning$ pop$
      ""
    }
    { duplicate$ empty$
        {
          swap$ "empty " swap$ * " in " * cite$ * warning$
        }
        { swap$
          pop$
        }
      if$
    }
  if$
}
INTEGERS { nameptr namesleft numnames }
STRINGS  { bibinfo}
FUNCTION {bbl.editors}
{ "editors" }

FUNCTION {bbl.editor}
{ "editor" }

FUNCTION {bbl.etal}
{ "et~al." }

FUNCTION {bbl.and}
{ "and"}

FUNCTION {space.word}
{ " " swap$ * " " * }

FUNCTION {format.names}
{ 'bibinfo :=
  duplicate$ empty$ 'skip$ {
  's :=
  "" 't :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr
      duplicate$ #1 >
        { "{ff~}{vv~}{ll}{, jj}" }
        { "{vv~}{ll}{, ff}{, jj}" }
      if$
      format.name$
      bibinfo bibinfo.check
      't :=
      nameptr #1 >
        {
          namesleft #1 >
            { ", " * t * }
            {
              numnames #2 >
                { "," * }
                'skip$
              if$
              s nameptr "{ll}" format.name$ duplicate$ "others" =
                { 't := }
                { pop$ }
              if$
              t "others" =
                {
                  " " * bbl.etal *
                }
                {
                  bbl.and
                  space.word * t *
                }
              if$
            }
          if$
        }
        't
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
  } if$
}
FUNCTION {format.names.ed}
{
  'bibinfo :=
  duplicate$ empty$ 'skip$ {
  's :=
  "" 't :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr
      "{ff~}{vv~}{ll}{, jj}"
      format.name$
      bibinfo bibinfo.check
      't :=
      nameptr #1 >
        {
          namesleft #1 >
            { ", " * t * }
            {
              numnames #2 >
                { "," * }
                'skip$
              if$
              s nameptr "{ll}" format.name$ duplicate$ "others" =
                { 't := }
                { pop$ }
              if$
              t "others" =
                {

                  " " * bbl.etal *
                }
                {
                  bbl.and
                  space.word * t *
                }
              if$
            }
          if$
        }
        't
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
  } if$
}
FUNCTION {format.key}
{ empty$
    { key field.or.null }
    { "" }
  if$
}

FUNCTION {format.authors}
{ author "author" format.names
}
FUNCTION {get.bbl.editor}
{ editor num.names$ #1 > 'bbl.editors 'bbl.editor if$ }

FUNCTION {format.editors}
{ editor "editor" format.names duplicate$ empty$ 'skip$
    {
      "," *
      " " *
      get.bbl.editor
      *
    }
  if$
}

FUNCTION {format.title}
{ title empty$
    { "" }
    { title "t" change.case$ }
  if$
}

FUNCTION {n.dashify}
{ 't :=
  ""
    { t empty$ not }
    { t #1 #1 substring$ "-" =
    { t #1 #2 substring$ "--" = not
        { "--" *
          t #2 global.max$ substring$ 't :=
        }
        {   { t #1 #1 substring$ "-" = }
        { "-" *
          t #2 global.max$ substring$ 't :=
        }
          while$
        }
      if$
    }
    { t #1 #1 substring$ *
      t #2 global.max$ substring$ 't :=
    }
      if$
    }
  while$
}

FUNCTION {format.btitle}
{ title emphasize
}

FUNCTION {tie.or.space.connect}
{ duplicate$ text.length$ #3 <
    { "~" }
    { " " }
  if$
  swap$ * *
}

FUNCTION {either.or.check}
{ empty$
    'pop$
    { "can't use both " swap$ * " fields in " * cite$ * warning$ }
  if$
}

FUNCTION {format.bvolume}
{ volume empty$
    { "" }
    { "Vol." volume tie.or.space.connect
      series empty$
    'skip$
    { " of " * series emphasize * }
      if$
%      "volume and number" number either.or.check
    }
  if$
}

FUNCTION {format.number.series}
{ volume empty$
    { number empty$
        { series field.or.null }
        { output.state mid.sentence =
            { "number" }
            { "Number" }
          if$
          number tie.or.space.connect
          series empty$
            { "there's a number but no series in " cite$ * warning$ }
            { " in " * series emphasize * }
          if$
        }
      if$
    }
    { "" }
  if$
}

FUNCTION {format.edition}
{ edition empty$
    { "" }
    { output.state mid.sentence =
    { edition "l" change.case$ " ed." * }
    { edition "t" change.case$ " ed." * }
      if$
    }
  if$
}

INTEGERS { multiresult }

FUNCTION {multi.page.check}
{ 't :=
  #0 'multiresult :=
    { multiresult not
      t empty$ not
      and
    }
    { t #1 #1 substring$
      duplicate$ "-" =
      swap$ duplicate$ "," =
      swap$ "+" =
      or or
    { #1 'multiresult := }
    { t #2 global.max$ substring$ 't := }
      if$
    }
  while$
  multiresult
}

FUNCTION {format.pages}
{ pages empty$
    { "" }
    { pages multi.page.check
    { "pp.~" pages n.dashify * }
    { "p.~" pages * }
      if$
    }
  if$
}

FUNCTION {format.vol.num.pages}
{ volume embolden field.or.null
  number empty$
    'skip$
    { " (" number * ")" * *
      volume empty$
    { "there's a number but no volume in " cite$ * warning$ }
    'skip$
      if$
    }
  if$
  pages empty$
    'skip$
    { duplicate$ empty$
    { pop$ format.pages }
    { ",~pp.~" * pages n.dashify * }
      if$
    }
  if$
}

FUNCTION {format.chapter.pages}
{ chapter empty$
    'format.pages
    { type empty$
    { "chapter" }
    { type "l" change.case$ }
      if$
      chapter tie.or.space.connect
      pages empty$
    'skip$
    { ", " * format.pages * }
      if$
    }
  if$
}

FUNCTION {format.in.ed.booktitle}
{ booktitle empty$
    { "" }
    { editor empty$
    { booktitle emphasize }
    { "{\em in} " format.editors * ", " * booktitle emphasize * }
      if$
    }
  if$
}

FUNCTION {empty.misc.check}
{ author empty$ title empty$ howpublished empty$
  month empty$ year empty$ note empty$ url empty$
  and and and and and
  key empty$ not and
    { "all relevant fields are empty in " cite$ * warning$ }
    'skip$
  if$
}

FUNCTION {format.thesis.type}
{ type empty$
    'skip$
    { pop$
      type "t" change.case$
    }
  if$
}

FUNCTION {format.tr.number}
{ type empty$
    { "Technical Report" }
    'type
  if$
  number empty$
    { "t" change.case$ }
    { number tie.or.space.connect }
  if$
}

FUNCTION {format.article.crossref}
{ key empty$
    { journal empty$
    { "need key or journal for " cite$ * " to crossref " * crossref *
      warning$
      ""
    }
    { "in {\em " journal * "\/}" * " \cite{" * crossref * "}" *
        }
      if$
    }
    { " {\em in} \citeasnoun{" crossref * "}" * }
  if$
}

FUNCTION {format.book.crossref}
{ volume empty$
    { "empty volume in " cite$ * "'s crossref of " * crossref * warning$
      "in "
    }
    { "Vol." volume tie.or.space.connect
      " of " *
    }
  if$
  editor empty$
  editor field.or.null author field.or.null =
  or
    { key empty$
    { series empty$
        { "need editor, key, or series for " cite$ * " to crossref " *
          crossref * warning$
          "" *
        }
        { "{\em " * series * "\/}" * " \cite{" * crossref * "}" *}
      if$
    }
    { " \citeasnoun{" * crossref * "}" * }
      if$
    }
    { " \citeasnoun{" * crossref * "}" * }
  if$
}

FUNCTION {format.incoll.inproc.crossref}
{ editor empty$
  editor field.or.null author field.or.null =
  or
    {
      key empty$
    { booktitle empty$
        { "need editor, key, or booktitle for " cite$ * " to crossref " *
          crossref * warning$
          ""
        }
        { "in {\em " booktitle * "\/}" * " \cite{" * crossref * "}" *}
      if$
    }
    { " {\em in} \citeasnoun{" crossref * "}" * }
      if$
    }
    {  " {\em in} \citeasnoun{" crossref * "}" * }
  if$
}

INTEGERS { len }

FUNCTION {chop.word}
{ 's :=
  'len :=
  s #1 len substring$ =
    { s len #1 + global.max$ substring$ }
    's
  if$
}


FUNCTION {format.lab.names.full}
{ 's :=
   "" 't :=
  s #1 "{vv~}{ll}" format.name$
  s num.names$ duplicate$
  #2 >
    { #2 =
      { pop$ s format.names }
      { " " * bbl.etal * }
      if$
    }
    { #2 <
        'skip$
        { s #2 "{ff }{vv }{ll}{ jj}" format.name$ "others" =
            {
              " " * bbl.etal *
            }
            { bbl.and space.word * s #2 "{vv~}{ll}" format.name$
              * }
          if$
        }
      if$
    }
  if$
}

FUNCTION {format.lab.names.abbr}
{ 's :=
  s num.names$ 'numnames :=
  numnames #1 >
    { numnames #2 >
    { s #1 "{vv~}{ll}" format.name$ " et~al." * }
    { s #2 "{ff }{vv }{ll}{ jj}" format.name$ "others" =
            { s #1 "{vv~}{ll}" format.name$ " et~al." * }
        { s #1 "{vv~}{ll}" format.name$ " and " *
              s #2 "{vv~}{ll}" format.name$ * 
            }
          if$
        }
      if$
    }
    { s #1 "{vv~}{ll}" format.name$ }
  if$
}




INTEGERS { author.field editor.field organization.field title.field key.field}


FUNCTION {init.field.constants}
{ #0 'author.field :=
  #1 'editor.field :=
  #2 'organization.field :=
  #3 'title.field :=
  #4 'key.field :=
}

FUNCTION {make.list.label}
{ author.field field.used =
    { format.authors }
    { editor.field field.used =
        { format.editors }
        { organization.field field.used =
            { "The " #4 organization chop.word #3 text.prefix$ }
            { title.field field.used =
                { format.btitle }
                { key.field field.used =
                    { key #3 text.prefix$ }
                    { "Internal error :001 on " cite$ * " label" * warning$ }
                  if$
                }
              if$
            }
          if$
        }
      if$
    }
  if$
}

FUNCTION {make.full.label}
{ author.field field.used =
    { author format.lab.names.full }
    { editor.field field.used =
        { editor format.lab.names.full }
        { organization.field field.used =
            { "The " #4 organization chop.word #3 text.prefix$ }
            { title.field field.used =
                { format.btitle }
                { key.field field.used =
                    { key #3 text.prefix$ }
                    { "Internal error :001 on " cite$ * " label" * warning$ }
                  if$
                }
              if$
            }
          if$
        }
      if$
    }
  if$
}

FUNCTION {make.abbr.label}
{ author.field field.used =
    { author format.lab.names.abbr }
    { editor.field field.used =
        { editor format.lab.names.abbr }
        { organization.field field.used =
            { "The " #4 organization chop.word #3 text.prefix$ }
            { title.field field.used =
                { format.btitle }
                { key.field field.used =
                    { key #3 text.prefix$ }
                    { "Internal error :001 on " cite$ * " label" * warning$ }
                  if$
                }
              if$
            }
          if$
        }
      if$
    }
  if$
}

FUNCTION {output.bibitem}
{ 
  "\harvarditem[" write$
  make.abbr.label write$
  "]{" write$
  make.full.label write$
  "}{" write$
  list.year write$
  "}{" write$
  cite$ write$
  "}" write$
  ""
  before.all 'output.state :=
}

FUNCTION {list.label.output}
{ make.list.label write$
}

FUNCTION {book}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  author empty$
    { editor "author and editor" item.check }
    { crossref missing$
    { "author and editor" editor either.or.check }
    'skip$
      if$
    }
  if$
  title.field field.used =
    { skip$ }
    { format.btitle "title" output.check }
  if$
  crossref missing$
    { format.bvolume output
      format.number.series output
      format.edition output
      publisher "publisher" output.check
      address output

    }
    { format.book.crossref output.nonnull
      format.edition output
    }
  if$
  new.block
  note output
  new.block
  url output
  fin.entry
}

FUNCTION {booklet}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  title.field field.used =
    { skip$ }
    { format.title "title" output.check }
  if$
  howpublished output
  address output
  new.block
  note output
  new.block
  url output
  fin.entry
}

FUNCTION {inbook}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  author empty$
    { editor "author and editor" item.check }
    { crossref missing$
    { "author and editor" editor either.or.check }
    'skip$
      if$
    }
  if$
  title.field field.used =
    { skip$ }
    { format.btitle "title" output.check }
  if$
  crossref missing$
    { format.bvolume output
      format.number.series output
      format.edition output
      publisher "publisher" output.check
      address output
    }
    { format.book.crossref output.nonnull
      format.edition output
    }
  if$
  format.chapter.pages "chapter and pages" output.check
  new.block
  note output
  new.block
  url output
  fin.entry
}

FUNCTION {inproceedings}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  title.field field.used =
    { skip$ }
    { format.title "title" output.check }
  if$
  author "author" item.check
  crossref missing$
    { format.in.ed.booktitle "booktitle" output.check
      format.bvolume output
      format.number.series output
      address empty$
        { organization output
          publisher output
        }
        { organization output
          publisher output
          address output.nonnull
        }
      if$
    }
    { format.incoll.inproc.crossref output.nonnull
    }
  if$
  format.chapter.pages output
  new.block
  note output
  new.block
  url output
  fin.entry
}


FUNCTION {article}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  author "author" item.check
  title.field field.used =
    { skip$ }
    { format.title "title" output.check }
  if$
  crossref missing$
    { journal emphasize "journal" duplicate$ item.check
      pages empty$
        {
          output
        }
        {
          " " *
          format.vol.num.pages * output
        }
      if$
    }
    { format.article.crossref output.nonnull
      format.pages output
    }
  if$
%  format.pages output
  publisher "publisher" output.check
  address output
  new.block
  note output
  new.block
  url output
  fin.entry

}

FUNCTION {incollection}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  title.field field.used =
    { skip$ }
    { format.title "title" output.check }
  if$
  author "author" item.check
  crossref missing$
    { format.in.ed.booktitle "booktitle" output.check
      format.edition output
      format.bvolume output
      format.number.series output
      publisher "publisher" output.check
      address output
    }
    { format.incoll.inproc.crossref output.nonnull
    }
  if$
  format.chapter.pages output
  new.block
  note output
  new.block
  url output
  fin.entry
}



FUNCTION {conference} { inproceedings }

FUNCTION {manual}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  title.field field.used =
    { skip$ }
    { format.btitle "title" output.check }
  if$
  format.edition output
  author empty$
    { organization empty$
    { address output
    }
    'skip$
      if$
    }
    { organization output
      address output
    }
  if$
  new.block
  note output
  new.block
  url output
  fin.entry
}

FUNCTION {mastersthesis}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  author "author" item.check
  title.field field.used =
    { skip$ }
    { format.title emphasize "title" output.check }
  if$
  "Master's thesis" format.thesis.type output.nonnull
  school "school" output.check
  address output
  new.block
  note output
  new.block
  url output
  fin.entry
}



FUNCTION {misc}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  author "author" item.check
  title.field field.used =
    { skip$ }
    { format.title "title" output.check }
  if$
  crossref missing$
    { journal emphasize "journal" duplicate$ item.check
      pages empty$
        {
          output
        }
        {
          " " *
          format.vol.num.pages * output
        }
      if$
    }
    { format.article.crossref output.nonnull
      format.pages output
    }
  if$
  new.block
  note output
  new.block
  url output
  fin.entry
}

FUNCTION {phdthesis}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  author "author" item.check
  title.field field.used =
    { skip$ }
    { format.btitle "title" output.check }
  if$
  "PhD thesis" format.thesis.type output.nonnull
  school "school" output.check
  format.number.series output
  address output
  new.block
  note output
  new.block
  url output
  fin.entry
}

FUNCTION {proceedings}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  title.field field.used =
    { skip$ }
    { format.btitle "title" output.check }
  if$
  format.bvolume output
  format.number.series output
  address empty$
    { editor empty$
    { skip$ }
    { organization output
    }
      if$
      publisher output
    }
    { editor empty$
    'skip$
    { organization output }
      if$
      publisher output
      address output.nonnull
    }
  if$
  new.block
  note output
  new.block
  url output
  fin.entry
}

FUNCTION {techreport}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  author "author" item.check
  title.field field.used =
    { skip$ }
    { format.title "title" output.check }
  if$
  format.tr.number emphasize output.nonnull
  institution "institution" output.check
  address output
  new.block
  note output
  new.block
  url output
  fin.entry
}

FUNCTION {unpublished}
{ output.bibitem
  list.label.output
  " (" list.year * ")" * output.nonnull
  author "author" item.check
  title.field field.used =
    { skip$ }
    { format.title "title" output.check }
  if$
  note "note" output.check
  new.block
  url output
  fin.entry
}

FUNCTION {default.type} { misc }

MACRO {jan} {"January"}

MACRO {feb} {"February"}

MACRO {mar} {"March"}

MACRO {apr} {"April"}

MACRO {may} {"May"}

MACRO {jun} {"June"}

MACRO {jul} {"July"}

MACRO {aug} {"August"}

MACRO {sep} {"September"}

MACRO {oct} {"October"}

MACRO {nov} {"November"}

MACRO {dec} {"December"}

MACRO {acmcs} {"ACM Computing Surveys"}

MACRO {acta} {"Acta Informatica"}

MACRO {cacm} {"Communications of the ACM"}

MACRO {ibmjrd} {"IBM Journal of Research and Development"}

MACRO {ibmsj} {"IBM Systems Journal"}

MACRO {ieeese} {"IEEE Transactions on Software Engineering"}

MACRO {ieeetc} {"IEEE Transactions on Computers"}

MACRO {ieeetcad}
 {"IEEE Transactions on Computer-Aided Design of Integrated Circuits"}

MACRO {ipl} {"Information Processing Letters"}

MACRO {jacm} {"Journal of the ACM"}

MACRO {jcss} {"Journal of Computer and System Sciences"}

MACRO {scp} {"Science of Computer Programming"}

MACRO {sicomp} {"SIAM Journal on Computing"}

MACRO {tocs} {"ACM Transactions on Computer Systems"}

MACRO {tods} {"ACM Transactions on Database Systems"}

MACRO {tog} {"ACM Transactions on Graphics"}

MACRO {toms} {"ACM Transactions on Mathematical Software"}

MACRO {toois} {"ACM Transactions on Office Information Systems"}

MACRO {toplas} {"ACM Transactions on Programming Languages and Systems"}

MACRO {tcs} {"Theoretical Computer Science"}

READ

EXECUTE {init.field.constants}

FUNCTION {sortify}
{ purify$
  "l" change.case$
}

FUNCTION {author.key.label}
{ author empty$
    { key empty$
    { title.field 'field.used := }
    { key.field 'field.used := }
      if$
    }
    { author.field 'field.used := }
  if$
}

FUNCTION {author.editor.key.label}
{ author empty$
    { editor empty$
    { key empty$
        { title.field 'field.used := }
        { key.field 'field.used := }
      if$
    }
    { editor.field 'field.used := }
      if$
    }
    { author.field 'field.used := }
  if$
}

FUNCTION {author.key.organization.label}
{ author empty$
    { key empty$
    { organization empty$
        { title.field 'field.used := }
        { organization.field 'field.used := }
      if$
    }
    { key.field 'field.used := }
      if$
    }
    { author.field 'field.used := }
  if$
}

FUNCTION {editor.key.organization.label}
{ editor empty$
    { key empty$
    { organization empty$
        { title.field 'field.used := }
        { organization.field 'field.used := }
      if$
    }
    { key.field 'field.used := }
      if$
    }
    { editor.field 'field.used := }
  if$
}

FUNCTION {sort.format.title}
{ 't :=
  "A " #2
    "An " #3
      "The " #4 t chop.word
    chop.word
  chop.word
  sortify
  #1 global.max$ substring$
}

FUNCTION {calc.label}
{ type$ "book" =
  type$ "inbook" =
  or
    'author.editor.key.label
    { type$ "proceedings" =
    'editor.key.organization.label
    { type$ "manual" =
        'author.key.organization.label
        'author.key.label
      if$
    }
      if$
    }
  if$
  make.abbr.label
  title.field field.used =
    { sort.format.title }
    { sortify }
  if$
  year field.or.null purify$ #-1 #4 substring$ sortify
  *
  'sort.label :=
}

FUNCTION {first.presort}
{ calc.label
  sort.label
  title.field field.used =
    { skip$ }
    { "    "
      *
      make.list.label sortify
      *
      "    "
      *
      title field.or.null
      sort.format.title
      *
    }
  if$
  #1 entry.max$ substring$
  'sort.key$ :=
}

ITERATE {first.presort}

SORT

STRINGS { last.sort.label next.extra }

INTEGERS { last.extra.num }

FUNCTION {initialize.last.extra.num}
{ #0 int.to.chr$ 'last.sort.label :=
  "" 'next.extra :=
  #0 'last.extra.num :=
}

FUNCTION {forward.pass}
{ last.sort.label sort.label =
    { last.extra.num #1 + 'last.extra.num :=
      last.extra.num int.to.chr$ 'extra.label :=
    }
    { "a" chr.to.int$ 'last.extra.num :=
      "" 'extra.label :=
      sort.label 'last.sort.label :=
    }
  if$
}

FUNCTION {reverse.pass}
{ next.extra "b" =
    { "a" 'extra.label := }
    'skip$
  if$
  year empty$
    { "n.d." extra.label * 'list.year := }
    { year extra.label * 'list.year := }
  if$
  extra.label 'next.extra :=
}

EXECUTE {initialize.last.extra.num}

ITERATE {forward.pass}

REVERSE {reverse.pass}

FUNCTION {second.presort}
{ make.list.label
  title.field field.used =
    { sort.format.title }
    { sortify }
  if$
  "    "
  *
  list.year field.or.null sortify
  *
  "    "
  *
  title.field field.used =
    { skip$ }
    { title field.or.null
      sort.format.title
      *
    }
  if$
  #1 entry.max$ substring$
  'sort.key$ :=
}

ITERATE {second.presort}

SORT

FUNCTION {begin.bib}
{ preamble$ empty$
    'skip$
    { preamble$ write$ newline$ }
  if$
  "\begin{thebibliography}{xx}" write$ newline$
}

EXECUTE {begin.bib}

EXECUTE {init.state.consts}

ITERATE {call.type$}

FUNCTION {end.bib}
{ newline$
  "\end{thebibliography}" write$ newline$
}

EXECUTE {end.bib}



