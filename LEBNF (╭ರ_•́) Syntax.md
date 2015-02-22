LEBNF stands for Le EBNF, and we shall define it using EBNF, and it behaves basically like EBNF.

¯\_(ツ)_/¯ What's EBNF?

Extended Backus-Naur Form you pleb read a book I oughta go over there and install GNU plus Linux on your computer right now free as in freedom.
ツ๖ۣۜMelodic_™☯††☭ ✠
✈♜♜
---ι═══════ﺤ

```
Usage	Notation
definition	       ▄︻̷̿┻̿═━━
concatenation	       ✯
termination	       ™
termination	       
alternation	       |
option	              [ ... ]
repetition	       (╯ಠ‿ಠ)╯︵┻━┻ ... ┬━┬ ﻿ ノ( ゜-゜ノ)
grouping	       ┴┬┴┤͜ʖ ͡°) ... (͡° ͜ʖ├┬┴┬
terminal string	   シ ... シ
terminal string	   ツ ... ツ
comment	       
special sequence	? ... ?
exception	       ☠
```


```
letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" ;
digit  = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
symbol = "[" | "]" 
       | "(╯ಠ‿ಠ)╯︵┻━┻" | "┬━┬ ﻿ ノ( ゜-゜ノ)"
       | "┴┬┴┤͜ʖ ͡°)" | "(͡° ͜ʖ├┬┴┬"
       | "<" | ">"
       | "シ" | "ツ" | "▄︻̷̿┻̿═━一" | "|" | "." | "✯" | "™" ;
character = letter | digit | symbol | "_" ;
 
identifier = letter , { letter | digit | "_" } ;
terminal = "'" , character , { character } , "'" 
         | '"' , character , { character } , '"' ;
 
rhs = identifier ;
lhs = identifier
     | terminal
     | "[" , lhs , "]"
     | "{" , lhs , "}"
     | "(" , lhs , ")"
     | lhs , "|" , lhs
     | lhs , "✯" , lhs ;
 
rule = lhs , "▄︻̷̿┻̿═━一" , rhs , ";" ;
grammar = { rule } ;
```
