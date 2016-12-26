# Sette e Mezzo
**TD method solves a simplified version of the card game [Sette e Mezzo][1]**  

For most Italian families, Christmas typically involves lots of hours of "Sette e Mezzo" playing.   

Here is a tentative, conservative, GTO solution to the game from the non-dealer perspective, expressed by the resulting State-Action Value Table. Reward is `+1` if player wins, `-1` if player loses.  

```sh
_ Value_Hit___Stand
[[ 0.5  -0.17 -1.  ]
 [ 1.   -0.44 -1.  ]
 [ 1.5  -0.17 -0.97]
 [ 2.   -0.44 -0.91]
 [ 2.5  -0.49 -0.93]
 [ 3.   -0.57 -0.82]
 [ 3.5  -0.36 -0.71]
 [ 4.   -0.45 -0.92]
 [ 4.5  -0.45 -0.79]
 [ 5.   -0.58 -0.75]
 [ 5.5  -0.45 -0.52]
 [ 6.   -0.5  -0.15]
 [ 6.5  -0.35  0.3 ]
 [ 7.   -0.65  0.37]
 [ 7.5  -1.    0.77]]
```

Effectively, the GTO strategy consists of betting the maximum (then standing) when a 7 is dealt as first card, and betting the minimum (then damage controlling) in all other initial states.   
To reproduce the result, just download the code and run it. It takes about 2 mins. 

### Requirements
* **Python**. Any version.

[1]: https://en.wikipedia.org/wiki/Sette_e_mezzo
