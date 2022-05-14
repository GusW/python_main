# Dynamic Programming for Machine Learning: Hidden Markov Models

## Hidden Markov Model

- Set of hidden states
- Set of possible observations
- Set of probabilities (Pi, a, b)
  - Pi (initial syllable)
  - a (following syllable) - transations probability
  - b (sound for syllable) - emission probability

```python

o - tter
           > mo - bile
au - to

V(t,s) = probability of ending at state S at time T given observations
```
