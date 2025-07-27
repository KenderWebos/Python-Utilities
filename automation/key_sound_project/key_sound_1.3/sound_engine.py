import pygame
import numpy as np
import random

class SoundEngine:
    def __init__(self, config):
        self.sample_rate = config["sample_rate"]
        self.duration = config["duration"]
        pygame.mixer.init()
        # Notas musicales (A4, B4, C5, D5, E5, F5, G5, A5, etc.)
        self.musical_notes = [
            220.00, 246.94, 261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99, 880.00
        ]

    def get_musical_freq(self, pitch_range):
        # Filtra las notas musicales dentro del rango
        notes_in_range = [f for f in self.musical_notes if pitch_range[0] <= f <= pitch_range[1]]
        if notes_in_range:
            return random.choice(notes_in_range)
        # Si no hay notas en el rango, usa una frecuencia aleatoria normal
        return random.uniform(*pitch_range)

    def adsr_envelope(self, wave):
        n = len(wave)
        attack_time = int(0.05 * self.sample_rate)  # 50ms ataque
        decay_time = int(0.10 * self.sample_rate)   # 100ms decaimiento
        sustain_level = 0.7
        sustain_time = n - attack_time - decay_time
        if sustain_time < 0:
            sustain_time = 0
        # Construye la envolvente
        attack = np.linspace(0, 1, attack_time)
        decay = np.linspace(1, sustain_level, decay_time)
        sustain = np.ones(sustain_time) * sustain_level
        envelope = np.concatenate((attack, decay, sustain))
        envelope = envelope[:n]  # Asegura que tenga el mismo tamaño
        return wave * envelope

    def create_sound(self, freq):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), False)
        wave = 0.5 * np.sin(2 * np.pi * freq * t)
        wave = self.adsr_envelope(wave)
        stereo_wave = np.array([wave, wave]).T
        stereo_wave = np.ascontiguousarray(stereo_wave)
        return pygame.sndarray.make_sound((32767 * stereo_wave).astype(np.int16))

    def play_random_sound(self, pitch_range):
        freq = self.get_musical_freq(pitch_range)
        sound = self.create_sound(freq)
        sound.play()

    def close(self):
        pygame.mixer.quit() 