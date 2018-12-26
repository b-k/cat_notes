I'm an economist/statistician/game theorist, but I'm not a mathematician.  I wanted
to learn Category Theory, but being that I'm not in an academic setting and this isn't
something economists usually do, I was on my own with the textbooks.

Here are my notes. Some would be very obvious to a mathematician, but are sufficiently
outside my usual way of thinking that I felt them worth clarifying to myself, and writing
down to verify I understand them clearly. I made them public because maybe, if you're also
somebody who knows a relatively good amount of math but is not a mathematician, they may
be useful to you too.

Math is _extremely_ vocabulary-heavy. Every statement, every theorem, is of the form
_define a thing, then define another thing; these things are related via a relationship
we have defined_. You could conceivably read a book in a language you don't speak by
looking up every word, but if you hope to make any progress
in reasonable time you will need to know the basic vocabulary without thinking too much
about it. So much of the content in this repository is in the form of flash cards. Keeping
to the spirit of mathematics, the great majority of cards cover definitions.

This repository, then, includes a document of general conceptual notes to myself, in
`cat_notes.tex`, and a much longer set of flash cards, in `cat_cards.tex`.

License: CC-BY-NC-SA.


#### Technical
Everything is in LaTeX; I have no idea how else one would do this. If you have
the (updated rewrite) XeLaTeX installed, run `make doc` to compile. Run `make cards` to
generate the card set.

The commutative diagrams essential to category theory use tikz-cd. You'll have to
have the appropriate tikz packages installed, and the additional tikz-related files
in this repository should get you the rest of the way. The python script calls pdfjam
and pdfcrop, which may already be part of your LaTeX installation.

Generate the flash cards via `make cards`, which runs a python script (a hack that
is all but a shell script) to generate a randomized set of cards, one front on a page
followed by one back on the next. This is the format you want for going through flash
cards on your telephone. If you'd like to actually print them, change `onecard` at the
top of `cat_cards.tex` to one of the standard formats in the flash cards package like
`avery5371`.
