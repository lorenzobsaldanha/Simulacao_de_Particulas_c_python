import ctypes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

# Carrega a biblioteca C
lib = ctypes.CDLL('./libparticle_sim.so')  

# Define os tipos de argumentos e retorno das funções C
lib.init_particles.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int] 
lib.init_particles.restype = None

lib.simulate_step.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int] 

lib.get_particle_data.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int] 
lib.get_particle_data.restype = ctypes.POINTER(ctypes.c_double)

lib.free_particle_data.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.free_particle_data.restype = None

lib.free_particles.argtypes = [ctypes.POINTER(ctypes.c_float)]
lib.free_particles.restype = None


def simulate_and_visualize(num_particles, num_frames):

    Particle = ctypes.POINTER(ctypes.c_float) 

    particles_data = (ctypes.c_float * (num_particles * 6))()  

    particles = ctypes.cast(particles_data, Particle)

    particles_ptr = ctypes.cast(particles_data, ctypes.POINTER(ctypes.c_float))
  
    lib.init_particles(particles_ptr, num_particles)

    
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    scat = ax.scatter([], [], s=20) 

    def update(frame):
        
        lib.simulate_step(particles_ptr, num_particles)
       
        data_ptr = lib.get_particle_data(particles_ptr, num_particles)

        positions = np.ctypeslib.as_array(data_ptr, shape=(num_particles * 2,))    
        x = positions[::2]
        y = positions[1::2]

        scat.set_offsets(np.c_[x, y])
        lib.free_particle_data(data_ptr)

        return scat,

    ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True)

    plt.title('Simulação de Partículas')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    lib.free_particles(particles_ptr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulação de Partículas com C e Python.")
    parser.add_argument("-n", "--num_particles", type=int, default=100, help="Número de partículas.")
    parser.add_argument("-f", "--num_frames", type=int, default=100, help="Número de frames da simulação.")

    args = parser.parse_args()

    num_particles = args.num_particles
    num_frames = args.num_frames

    simulate_and_visualize(num_particles, num_frames)