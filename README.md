# Abbreviations and File Map

**To play go to /SOLVED/abnormal-sixteen-opt-SOLVED_finito.py**

*changing ```solution=0``` to ```solution=1``` gives you the shuffle as well as ultimate power moves ;)*


## a – Abnormal
## s – Sixteen
## alg – not playable versions
mostly brute-force searches with further optimization
## o – Optimized 
Optimized version that stops the creation of useless combination. Removes roughly 40.5% of combinations. Useless combination are:
* WS – back and forth movement: replaceable by moves " " (nothing)
* SS&DD – repetition of two for S and D: replaceable by moves "WW" & "AA" 
* WWW – tri-repetition (of any move): replaceable by moves "S" (1*mirror-move)
## search – Custom shuffle reverse search. 
Used to see whether a (for inst "wasd") 4 move shuffle can be achieved with a different number of moves. Result: repetition did not occur for length <18. Further attempts in Bidirectional Search.
## (standalone)
First integrations of standalone algorithm search engines. Optimization included and excluded versions.
## legal
An attempt to find some pattern for the increase in legal grid positions with each move. Solution: Purely mathematical. Applied my Rubik's cube knowledge :) – 16!/2
## 3x3
An attempt to find patterns that can be used for answering questions in the normal 4x4 grid just faster.
## pattern
An attempt to find recurring patterns. Turns out everything is possible except for two swap excluding the cursor. **Realization** same as game Fifteen. 
## Bidirectional Search
REVOLUTION!
* bidir test – one move shuffle search for lenght 5. Success.
* bidirectional – the revolutionary idea that found the solution. 
