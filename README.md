BPSO
====

Combinatorial Problem Solver Using a Binary/Discrete Particle Swarm Optimizer (Python implementation)

## Intro

Particle Swarm Optimization (PSO) is a population-based stochastic optimization method, inspired by the social interactions of animals or insects in nature. Most of the PSO applications have been solving continuous problems. This implementation of PSO is aimed to solve combinatorial problems (Binary PSO) such as Knapsack Problem or TSP (Traveling Salesman Problem).

## Usage

    $ python pso/Main.py

## Dependencies
    
  - Numpy
  - Scipy
  - matplotlib

## Details

Standard Model:

    vid = vid + cε1 (pid − xid) + cε2 (pgd − xid),
    xid = xid + vid

where `vid` - `i`-th particle velocity vector, `d` - problem dimension, `cε1`, `cε2` - random normal distributed independent values, `xid` - i-th particle position, `pid` - i-th particle best position, `pgd` - neighborhoods’ best position.

The binary version of the model stays exactly the same with the following assumptions:
    
- Velocity is represented as a probability which is constrained to `[0.0, 1.0]` (using logistic transformation)
- Particles best and current positions are now integer values in `{0,1}` 
- The resulting change in position is defined by the following rule:

    ```
    if (rand() < S(vid)) then xid = 1
    else xid = 0
    ```
    
where `S(vid)` is a sigmoid limiting transformation function, `rand()` - random value uniformly distributed between `[0.0, 1.0]`.

Current implementation does not use Hamiltonian Cycles, matrix representations or fuzzing operators.
