from dataclasses import dataclass, field

import numpy as np


@dataclass
class AudioData:

    samples: np.ndarray | None = None

    sample_rate: int = 0

    duration: float = 0.0

    channels: int = 1

    # ==========================================
    # CACHE DE FEATURES
    # ==========================================

    rms: np.ndarray | None = None

    onset_envelope: np.ndarray | None = None

    chroma: np.ndarray | None = None

    spectral_centroid: np.ndarray | None = None

    spectral_rolloff: np.ndarray | None = None

    spectral_bandwidth: np.ndarray | None = None

    spectral_flatness: np.ndarray | None = None

    zero_crossing_rate: np.ndarray | None = None

    mfcc: np.ndarray | None = None

    mel_spectrogram: np.ndarray | None = None

    tempogram: np.ndarray | None = None

    harmonic: np.ndarray | None = None

    percussive: np.ndarray | None = None

    extra: dict = field(default_factory=dict)