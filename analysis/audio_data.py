from dataclasses import dataclass

import numpy as np


@dataclass
class AudioData:

    samples: np.ndarray | None = None

    sample_rate: int = 0

    duration: float = 0.0

    channels: int = 1