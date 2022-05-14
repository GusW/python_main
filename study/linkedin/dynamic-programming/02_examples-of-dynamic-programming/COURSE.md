# Examples of Dynamic Programming

## Recurrence relation

- Simpliciy: The function has integer inputs.
- The function depends on itself.
- The final answer can be easily extracted from the function.

## The flowerbox problem

- Plant flowers in a soil whose spaces are defined by their amount of nutrients
- The higher the nutrient amount the taller the flower will be
- | \_ | X | \_ | \_ | X |
- | 3 | 10 | 3 | 1 | 2 |
- Adjancent spaces must be avoided once flowers compete for nutrients
- How to pick the best combination in order to maximize flower units?
  - Greedy: pick the highest and start from there
  - Not that obivous in different soil configurations
    - | \_ | X | \_ | X | \_ |
    - | 1 | 9 | 10 | 9 | 1 |
- f(i) = maximum total height in planting in 0, 1, ... i

  ```python
  f(i) = max {
      f(i-2) + Vi   # current spot i and the function of the last non-adjacent spot i-2
      f(i-1)        # the function of the last spot
  }

  solution:
  f(n-1)            # n = total number of spots
  ```

## The change making problem

- Coins with different denominations
- | 19c | 12c | 5c | 1C |
- Given a target `T0` and a set of denominations `Di`
- Use the amount of denominations you want as long as the sum does not go above the target
- Minimize number of coins to make `T0`
- Solution

  - Use greedy approach and start with biggest denomination below target `T0` or
  - Start with a smaller denomination

  ```python
  f(i) = min {
      f(i, T0-Di) + 1   # start with biggest denomination, have the target diminished by Di and add up a coin
      f(i-1, T0),       # start with the next denomination, still have the same target and add no coins
  }

  solution:
  f(n-1, t0) # n = number of denominations, t0 = original target
  ```

- Differently from the flowerbox-type problem, the solution here is bound to 2 integer variables `n` and `t` which means that the dependency graph is not linear and solving all possible ramifications of the problem (bottom-up approach) is suboptimal.
- Because not all the subproblems need to be solved, `memoization` means only the necessary ones are computed.
