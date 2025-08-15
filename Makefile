CC = gcc
CFLAGS = -Wall -Wextra -fPIC -O3
LDFLAGS = -shared
PYTHON = python  

all: libparticle_sim.so

libparticle_sim.so: particle_sim.c
	$(CC) $(CFLAGS) -o libparticle_sim.so particle_sim.c -lm $(LDFLAGS)

caso_estudo3:
	$(PYTHON) particle_sim.py -n 100

caso_estudo2: 
	$(PYTHON) particle_sim.py -n 35

caso_estudo1: 
	$(PYTHON) particle_sim.py -n 7	

clean:
	rm -f libparticle_sim.so
	