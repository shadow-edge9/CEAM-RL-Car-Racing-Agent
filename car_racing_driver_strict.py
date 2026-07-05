import gymnasium as gym
import numpy as np
import pygame

#this function was written by AI, but I'm not concerned with the crashing part yet.
#All I wanted to see is how a normal Racing Car agent should work and penalize ME if I stay off track for too long

def analyze_telemetry(obs):

    # 1. Define a wider impact zone to account for camera zoom at high speeds
    # This captures y-coordinates 55 to 85, and x-coordinates 28 to 68
    impact_zone = obs[55:85, 28:68].copy()

    # 2. Black out the vehicle's chassis in the center of the zone.
    # We must make this mask wide enough to account for the car rotating during drifts.
    # If we don't, the red paint of the car will trigger the "red kerb" sensor!
    impact_zone[7:25, 10:30] = [0, 0, 0]

    # Flatten the pixels for rapid color analysis
    pixels = impact_zone.reshape(-1, 3)


    # 4. Off-Track Detection (Grass)
    # Grass emits a very strong green signal (G > 200)
    grass_pixels = np.sum(pixels[:, 1] > 200)

    # Total pixels = 1200. Masked car = 360. Viewable area = 840 pixels.
    # If more than 85% of the viewable area is grass, you are entirely off the tarmac.
    is_off_track = (grass_pixels / 840) > 0.85
    #this variable is of concern to me rn. I shouldn't be off track for too long or else restart.

    return is_off_track


# Initializing environment
env = gym.make(
    "CarRacing-v3",
    render_mode="human",
    continuous=True,
    max_episode_steps=5000
)
obs, info = env.reset()

clock = pygame.time.Clock()

print("==================================================")
print(" Q-BRANCH ADVANCED TELEMETRY ENGAGED")
print(" Rules of Engagement:")
print("   - 0.5 seconds fully off-track = Reset")
print("   - Touching Red/White Kerbs = INSTANT Reset")
print(" Controls: UP (Gas), DOWN (Brake), L/R (Steer)")
print("==================================================")

running = True
off_track_frames = 0
FRAME_LIMIT = 30  # 60 FPS * 0.5 seconds = 30 frames

while running:
    # Default state
    steering = 0.0
    gas = 0.0
    brake = 0.0

    # Check for manual exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Intercept keyboard inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_LEFT]:
        steering = -0.6
    if keys[pygame.K_RIGHT]:
        steering = 0.6
    if keys[pygame.K_UP]:
        gas = 0.4
    if keys[pygame.K_DOWN]:
        brake = 0.8

    action = np.array([steering, gas, brake], dtype=np.float32)

    # Advance the simulation
    obs, reward, terminated, truncated, info = env.step(action)

    # --- TELEMETRY CHECK ---
    is_off_track = analyze_telemetry(obs)

    # 2. Grass Excursion Check (0.5 Second Tolerance)
    if is_off_track:
        off_track_frames += 1
    else:
        off_track_frames = 0

    if off_track_frames >= FRAME_LIMIT:
        print("\n[ALERT] Vehicle off-track for 0.5s. Mission failed. Resetting...")
        obs, info = env.reset()
        off_track_frames = 0

    # --- MISSION OUTCOMES ---
    if terminated:
        print("\nImmaculate driving! Track completed. Returning to base...")
        running = False
    elif truncated:
        print("\nSimulation timed out. Resetting...")
        obs, info = env.reset()
        off_track_frames = 0

    # Cap the simulation at 60 FPS
    clock.tick(60)

env.close()
pygame.quit()
print("Simulation deactivated.")