# FUCKSCRIPT++: a low level language for a hypothetical brainfuck-based cpu architecture

Fuckscript++ is language designed to be compiled to brainfuck. Its intended as more easily readable and writable language than plain brainfuck, aiming to be to brainfuck what C is to normal machine code

IMPORTANT NOTE: Fuckscript is not complete yet. this is simply a specification, the proper compiler isnt there yet unfortunately. Btw, the reason im basing this off my own fuckscript project is because regular fuckscript will serve as an intermediary representation in the compilation process

# FUCKSCRIPT LANGUAGE SPECIFICATION

## SYNTAX

being C inspired, fuckscript is a semicolon language. semicolons show the compiler where a statement begins and ends.

Loops are put into square brackets (```[]```), not only cuz we just. dont have arrays rn. but also because thats what bf does.

fuckscript supports include statements, tho like C i do not plan on having a module system. Include statements simply will have to preprocessor paste the file youre including into the file youre including it into.

```@include std.fspp```

theyre prefixed with an @ and dont need parentheses to show that they arent actually used by the compiler and are only relevant to the preprocessor

> (note, we do not have a standard library yet an its not really a priority for me. Once the language is in a usable state i will work on making one tho)
## VARIABLES

variables can be declared like so:

```var x = 20;```

note that as of now, variables can only be integers. String support might be added in future versions of the specification.

## EXPRESSIONS

theyre just normal expressions. they have to be surrounded by parentheses and return a value. 

## LOOPS

right now there is only while loops. surround some code with ```while (expression) []``` to make it loop until the expression returns 0. (0 is used as a false statement since brainfuck doesnt support booleans)

#

right now thats all i have planned. I might add more things to the spec as the language grows, but for now this is everything i want to implement before moving on to more difficult things like functions
