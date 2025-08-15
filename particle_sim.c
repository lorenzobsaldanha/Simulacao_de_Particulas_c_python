#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
  double x, y;       
  double vx, vy;     
  double mass;       
} Particle;

#define NUM_PARTICLES 100
#define TIME_STEP 0.01
#define GRAVITY 0.1

void init_particles(Particle* particles, int num_particles) {
  for (int i = 0; i < num_particles; i++) {
    particles[i].x = (double)rand() / RAND_MAX * 10.0;   
    particles[i].y = (double)rand() / RAND_MAX * 10.0;   
    particles[i].vx = ((double)rand() / RAND_MAX - 0.5) * 2.0; 
    particles[i].vy = ((double)rand() / RAND_MAX - 0.5) * 2.0; 
    particles[i].mass = 1.0;   
  }
}

void update_particle(Particle* particle) {
  particle->vy += GRAVITY * TIME_STEP;
  particle->x += particle->vx * TIME_STEP;
  particle->y += particle->vy * TIME_STEP;

  if (particle->x < 0 || particle->x > 10) {
    particle->vx *= -1;
  }
  if (particle->y < 0 || particle->y > 10) {
    particle->vy *= -1;
  }
}

void simulate_step(Particle* particles, int num_particles) {
  for (int i = 0; i < num_particles; i++) {
    update_particle(&particles[i]);
  }
}

double* get_particle_data(Particle* particles, int num_particles) {
  double* data = (double*)malloc(num_particles * 2 * sizeof(double)); 
  if (data == NULL) {
    fprintf(stderr, "Erro ao alocar memória para os dados das partículas.\n");
    exit(1);
  }

  for (int i = 0; i < num_particles; i++) {
    data[i * 2] = particles[i].x;
    data[i * 2 + 1] = particles[i].y;
  }
  return data;
}

void free_particle_data(double* data) {
  free(data);
}

void free_particles(Particle* particles) {
    free(particles);
}
