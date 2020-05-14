# file parsed
[x]exclude gutenberg header & footer
[x]exclude book title
[x]exclude story titles
[x]exclude chapters

get rid of all non alphanumberic characters
[x]exclude punctuation(;:.,?!''""-&)
[x]exclude enclosing(()[]{})

open fil parsed as outfil

outfil.read() = string
