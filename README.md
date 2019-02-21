# Evolution Simulator V.1.1.
This is a program that tries to simulate the evolution of a simple being.
## How does it work?
In this version, I simplified the previous version by merging the comsumption and production attributes to the comsumption attribute, so the only attributes that the being has are:
- The quantity of food that it consumes every tick;
- The quantity of food that it has stored.

When the food stored is below 0 the being dies.

Each generation, the beings that survived the longer will reproduce (asexually) and create new mutated beings and the cycle will repeat.

By simplifying the program somehow it broke and now the lifetime doesn´t evolve and just keeps stable.
