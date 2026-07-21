from pathlib import Path

import numpy as np

from analysis.audio_data import AudioData
from analysis.backends.audio_backend import AudioBackend
from analysis.cache.audio_cache import AudioCache
from analysis.features.feature_set import FeatureSet


class LibrosaBackend(AudioBackend):

    def __init__(self):

        self.available = False
        self.librosa = None
        self.cache = AudioCache()

        try:

            import librosa

            self.librosa = librosa
            self.available = True

            print("[Music94] Librosa backend loaded.")

        except Exception as error:

            print(error)

    # ---------------------------------------------------------

    def load_audio(self, song):

        if self.cache.has(song.path):

            return self.cache.get(song.path)

        audio = AudioData()

        if not self.available:

            return audio

        try:

            path = Path(song.path)

            if not path.exists():

                return audio

            samples, sample_rate = self.librosa.load(
                path,
                sr=None,
                mono=True,
            )

            audio.samples = samples
            audio.sample_rate = sample_rate
            audio.duration = len(samples) / sample_rate
            audio.channels = 1

            # ==========================================
            # FEATURES PRECALCULADAS
            # ==========================================

            audio.rms = self.librosa.feature.rms(
                y=samples
            )

            audio.onset_envelope = self.librosa.onset.onset_strength(
                y=samples,
                sr=sample_rate,
            )

            audio.chroma = self.librosa.feature.chroma_stft(
                y=samples,
                sr=sample_rate,
            )

            audio.spectral_centroid = self.librosa.feature.spectral_centroid(
                y=samples,
                sr=sample_rate,
            )

            audio.spectral_rolloff = self.librosa.feature.spectral_rolloff(
                y=samples,
                sr=sample_rate,
            )

            audio.spectral_bandwidth = self.librosa.feature.spectral_bandwidth(
                y=samples,
                sr=sample_rate,
            )

            audio.spectral_flatness = self.librosa.feature.spectral_flatness(
                y=samples,
            )

            audio.zero_crossing_rate = self.librosa.feature.zero_crossing_rate(
                y=samples,
            )

            audio.mfcc = self.librosa.feature.mfcc(
                y=samples,
                sr=sample_rate,
            )

            audio.mel_spectrogram = self.librosa.feature.melspectrogram(
                y=samples,
                sr=sample_rate,
            )

            audio.tempogram = self.librosa.feature.tempogram(
                onset_envelope=audio.onset_envelope,
                sr=sample_rate,
            )

            harmonic, percussive = self.librosa.effects.hpss(
                samples
            )

            audio.harmonic = harmonic
            audio.percussive = percussive

            self.cache.put(song.path, audio)

        except Exception as error:

            print(error)

        return audio

    # ---------------------------------------------------------

    def extract_features(self, song):

        features = FeatureSet()

        audio = self.load_audio(song)

        if audio.samples is None:

            return features

        try:

            tempo, _ = self.librosa.beat.beat_track(
                y=audio.samples,
                sr=audio.sample_rate,
            )

            if isinstance(tempo, np.ndarray):

                if tempo.size == 0:

                    return features

                tempo = float(tempo.flat[0])

            else:

                tempo = float(tempo)

            features.bpm = round(tempo, 2)

            # ==========================================
            # KEY STRENGTH
            # ==========================================

            try:

                chroma = np.mean(audio.chroma, axis=1)

                features.key_strength = round(
                    float(np.max(chroma)),
                    4,
                )

            except Exception:

                features.key_strength = None

            print(
                f"[Music94] {song.title} -> {features.bpm:.2f} BPM"
            )

        except Exception as error:

            print(error)

        return features