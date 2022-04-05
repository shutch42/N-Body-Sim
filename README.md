# Sequential and Barnes-Hut N-Body Simulation in Python  
This project was done as a part of my Applied Numerical Science class, but I've taken it on as my own personal project since then. Programming was done in Jupyter Notebooks using python with numpy and matplotlib. The most recent version of this project is in the BH-2D repository.

## How it works:
### Sequential N-Body: O(N<sup>2</sup>) Implementation  
1. Masses are loaded into body objects
2. Bodies are stored in an array to represent the entire system of masses
3. Bodies run through the N-body algorithm, which calculates position and velocity at each timestep using Newton's Law of Gravity
4. The algorithm returns a 3D vector of each position and velocity per timestep
5. Positions are animated using matplotlib in a 3D graph  
### Results: Uniform 125 Mass Sim
![uniform-mass-gif](https://github.com/shutch42/N-Body-Sim/blob/master/uniform-masses-sequential.gif)
----------------------------------
### Barnes-Hut N-Body: O(NlogN) Implementation
1. Masses are loaded into body objects
2. Bodies are loaded into an octTree, which stores the center of mass for each group of bodies in a quadrant
3. Positions and accelerations are calculated on each body using the octTree, which allows for estimation of distant or closely grouped masses
4. The algorithm returns each position and velocity per timestep
5. Positions are animated using matplotlib in a 3D graph
### Results: 1500 Mass Explosion Sim
![big-sim](https://github.com/shutch42/N-Body-Sim/blob/master/big-sim.gif)

## Problems:
- Matplotlib is very slow in generating animations for large sets of data
- The Barnes-Hut object oriented approach to solving this problem is much better suited to another language
- Multithreading is not implemented in this solution

## Conclusion:
This project is what put me down the rabbit hole of N-Body simulation. This is a working solution, but it could use some improvements. In the future, I will redo this problem in a different language, with a different graphics library, and with multithreading. I imagine that this could have much better results if the program is implemented in a way that uses CUDA cores.
