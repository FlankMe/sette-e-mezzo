# Sette e Mezzo
**TD method solves a simplified version of the card game [Sette e Mezzo][1]**  

For most Italian families, Christmas typically involves lots of hours of "Sette e Mezzo" playing.   

Here is a conservative, GTO solution to the game from the non-dealer perspective, expressed by the resulting State-Action Value Table. Reward is `+1` if player wins, `-1` if player loses.  

```sh
_ Score_Hit___Stand
[[ 0.5  -0.17 -1.  ]
 [ 1.   -0.35 -1.  ]
 [ 1.5  -0.21 -0.93]
 [ 2.   -0.33 -1.  ]
 [ 2.5  -0.37 -0.97]
 [ 3.   -0.5  -0.93]
 [ 3.5  -0.29 -0.84]
 [ 4.   -0.49 -0.72]
 [ 4.5  -0.45 -0.59]
 [ 5.   -0.51 -0.64]
 [ 5.5  -0.46 -0.17]
 [ 6.   -0.35 -0.09]
 [ 6.5  -0.38  0.03]
 [ 7.   -0.73  0.7 ]
 [ 7.5  -1.    0.72]]
```
Note the table is somewhat inconsistent though: the pair (1.5, Stand) should be less or equal to (2.0, Stand). It is important to stress that the above is just an approximation. The above estimates will converge to their true value as the number of simulated episodes tends to infinity.  

**In summary, the GTO strategy consists of betting the maximum (then standing) when a `7` is dealt as first card, and betting the minimum (then damage controlling) in all other initial states.**   
To reproduce the result, just download the code and run it. It takes about 2 mins. 

### Requirements
* **Python**. Any version.

[1]: https://en.wikipedia.org/wiki/Sette_e_mezzo
