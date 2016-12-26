# Sette e Mezzo
**TD method solves a simplified version of the card game [Sette e Mezzo][1]**  

For most Italian families, Christmas typically involves lots of hours of "Sette e Mezzo" playing.   

Here is a conservative, GTO solution to the game from the non-dealer perspective, expressed by the resulting State-Action Value Table. Reward is `+1` if player wins, `-1` if player loses.  

```sh
_ Score_Hit___Stand
[[ 0.5  -0.26 -1.  ]
 [ 1.   -0.36 -1.  ]
 [ 1.5  -0.39 -0.99]
 [ 2.   -0.5  -0.86]
 [ 2.5  -0.34 -0.89]
 [ 3.   -0.51 -0.85]
 [ 3.5  -0.48 -0.77]
 [ 4.   -0.6  -0.68]
 [ 4.5  -0.52 -0.61]
 [ 5.   -0.58 -0.39]
 [ 5.5  -0.49 -0.35]
 [ 6.   -0.57 -0.19]
 [ 6.5  -0.53  0.01]
 [ 7.   -0.5   0.4 ]
 [ 7.5  -1.    0.71]]
```
Note the table is somewhat inconsistent though: the pair (2.0, Stand) should be less or equal to (2.5, Stand). It is important to stress that the above is just an approximation. The above estimates will converge to their true value as the number of simulated episodes tends to infinity.  

**In summary, the GTO strategy consists of betting the maximum (then standing) when a `7` is dealt as first card, and betting the minimum (then damage controlling) in all other initial states.**   
To reproduce the result, just download the code and run it. It takes about 2 mins. 

### Requirements
* **Python**. Any version.

[1]: https://en.wikipedia.org/wiki/Sette_e_mezzo
