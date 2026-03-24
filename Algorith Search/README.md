## a – Abnormal
## s – Sixteen
## alg – not playable versions
mostly brute-force searches with further optimization
## o – Optimized 
Optimized version that stops the creation of useless combination. Removes roughly 40.5% of combinations. Useless combination are:
* WS – back and forth movement: replacable by moves " " (nothing)
* SS&DD – repetition of two for S and D: replacable by moves "WW" & "AA" 
* WWW – tri-repetition (of any move): replacable by moves "S" (1*mirror-move)
## search – Custom shuffle reverse search. 
Used to see whether a (for inst "wasd") 4 move shuffle can be achieved with a different number of moves. Result: repetition did not accure for lenght <18. Further attempts in Bidirectional Search.
## (standalone)
First integrations of standalone algorith search engines. Optimization included and excluded versions.
## legal
An attempt to find some pattern for the increase in legal grid positions with each move. Solution: Purely mathematical. Applied my Rubik's cube knowledge :) – 16!/2
## 3x3
An attempt to find patterns that can be used for answering questions in the normal 4x4 grid just faster.
## pattern
An attempt to find reaccuring patterns. Turns out everything is possible except for two swap excluding the cursor. **Realization** same as game Fifteen. 
## Bidirectional Search
REVOLUTION!
* bidir test – one move shuffle search for lenght 5. Success.
* bidirectional – the revolutionary idea that found the solution. 

# Solution:
29 move algorithm 
For example: aasawaasasawaasasaawasasaawas

# Unanswered questions:
* Why 29?
* In game "Fifteen" swaping ```13, 14, 15``` to ```15, 13, 14``` also takes 29 moves. Coinsidence? I don't think so..
* For 3x3 legal count logic is different. Not 9!/2. Restrictions?