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

        # ==========================================
        # BPM
        # ==========================================

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

            features.bpm = round(
                tempo,
                2,
            )

        except Exception:

            pass

        # ==========================================
        # KEY
        # ==========================================

        try:

            chroma = np.mean(
                audio.chroma,
                axis=1,
            )

            notes = [
                "C",
                "C#",
                "D",
                "Eb",
                "E",
                "F",
                "F#",
                "G",
                "Ab",
                "A",
                "Bb",
                "B",
            ]

            index = int(np.argmax(chroma))

            features.musical_key = notes[index]

            features.key_strength = round(
                float(np.max(chroma)),
                4,
            )

        except Exception:

            pass

        # ==========================================
        # LOUDNESS
        # ==========================================

        try:

            rms_mean = float(
                np.mean(audio.rms)
            )

            if rms_mean > 0:

                loudness = 20 * np.log10(rms_mean)

                features.loudness = float(
                    round(
                        float(loudness),
                        2,
                    )
                )

        except Exception:

            pass

        # ==========================================
        # DYNAMIC RANGE
        # ==========================================

        try:

            rms_db = 20 * np.log10(

                np.maximum(

                    audio.rms,

                    1e-10,

                )

            )

            dynamic_range = np.max(

                rms_db

            ) - np.min(

                rms_db

            )

            features.dynamic_range = float(

                round(

                    float(dynamic_range),

                    2,

                )

            )

        except Exception:

            pass

        # ==========================================
        # REPLAYGAIN (estimación)
        # ==========================================

        try:

            if features.loudness is not None:

                reference = -18.0

                replaygain = reference - features.loudness

                features.replaygain = float(

                    round(

                        replaygain,

                        2,

                    )

                )

        except Exception:

            pass

                # ==========================================
        # ENERGY
        # ==========================================

        try:

            rms = float(np.mean(audio.rms))

            centroid = float(

                np.mean(

                    audio.spectral_centroid

                )

            )

            bandwidth = float(

                np.mean(

                    audio.spectral_bandwidth

                )

            )

            energy = (

                rms * 0.50 +

                (centroid / 5000.0) * 0.30 +

                (bandwidth / 5000.0) * 0.20

            )

            energy = max(

                0.0,

                min(

                    energy,

                    1.0,

                ),

            )

            features.energy = round(

                energy,

                3,

            )

        except Exception:

            pass

        # ==========================================
        # DANCEABILITY
        # ==========================================

        try:

            bpm = features.bpm

            if bpm is None:

                bpm = 120.0

            bpm_score = 1.0 - min(

                abs(

                    bpm - 128.0

                ) / 128.0,

                1.0,

            )

            tempogram = float(

                np.mean(

                    audio.tempogram

                )

            )

            tempogram = min(

                tempogram / 2.0,

                1.0,

            )

            zcr = float(

                np.mean(

                    audio.zero_crossing_rate

                )

            )

            zcr = min(

                zcr * 5.0,

                1.0,

            )

            rms = float(

                np.mean(

                    audio.rms

                )

            )

            rms = min(

                rms * 5.0,

                1.0,

            )

            danceability = (

                bpm_score * 0.40 +

                tempogram * 0.30 +

                rms * 0.20 +

                zcr * 0.10

            )

            danceability = max(

                0.0,

                min(

                    danceability,

                    1.0,

                ),

            )

            features.danceability = round(

                danceability,

                3,

            )

        except Exception:

            pass

        # ==========================================
        # ACOUSTICNESS
        # ==========================================

        try:

            flatness = float(
                np.mean(
                    audio.spectral_flatness
                )
            )

            rolloff = float(
                np.mean(
                    audio.spectral_rolloff
                )
            )

            centroid = float(
                np.mean(
                    audio.spectral_centroid
                )
            )

            rolloff /= audio.sample_rate / 2

            centroid /= audio.sample_rate / 2

            acousticness = (

                flatness * 0.55 +

                (1.0 - rolloff) * 0.25 +

                (1.0 - centroid) * 0.20

            )

            acousticness = max(

                0.0,

                min(

                    acousticness,

                    1.0,

                ),

            )

            features.acousticness = round(

                acousticness,

                3,

            )

        except Exception:

            pass

        # ==========================================
        # INSTRUMENTALNESS
        # ==========================================

        try:

            harmonic = np.mean(
                np.abs(
                    audio.harmonic
                )
            )

            percussive = np.mean(
                np.abs(
                    audio.percussive
                )
            )

            mfcc_var = np.var(
                audio.mfcc
            )

            harmonic_ratio = harmonic / (

                harmonic +

                percussive +

                1e-9

            )

            mfcc_score = max(

                0.0,

                1.0 -

                min(

                    mfcc_var / 4000.0,

                    1.0,

                ),

            )

            instrumentalness = (

                harmonic_ratio * 0.65 +

                mfcc_score * 0.35

            )

            instrumentalness = max(

                0.0,

                min(

                    instrumentalness,

                    1.0,

                ),

            )

            features.instrumentalness = round(

                instrumentalness,

                3,

            )

        except Exception:

            pass

        # ==========================================
        # SPEECHINESS
        # ==========================================

        try:

            zcr = float(

                np.mean(

                    audio.zero_crossing_rate

                )

            )

            centroid = float(

                np.mean(

                    audio.spectral_centroid

                )

            )

            bandwidth = float(

                np.mean(

                    audio.spectral_bandwidth

                )

            )

            centroid /= audio.sample_rate / 2

            bandwidth /= audio.sample_rate / 2

            speechiness = (

                zcr * 0.45 +

                centroid * 0.35 +

                bandwidth * 0.20

            )

            speechiness = max(

                0.0,

                min(

                    speechiness,

                    1.0,

                ),

            )

            features.speechiness = round(

                speechiness,

                3,

            )

        except Exception:

            pass

                # ==========================================
        # VALENCE
        # ==========================================

        try:

            energy = features.energy or 0.0

            dance = features.danceability or 0.0

            acoustic = features.acousticness or 0.0

            speech = features.speechiness or 0.0

            centroid = float(

                np.mean(

                    audio.spectral_centroid

                )

            )

            centroid /= audio.sample_rate / 2

            valence = (

                energy * 0.35 +

                dance * 0.30 +

                centroid * 0.20 +

                (1.0 - acoustic) * 0.10 +

                (1.0 - speech) * 0.05

            )

            valence = max(

                0.0,

                min(

                    valence,

                    1.0,

                ),

            )

            features.valence = round(

                valence,

                3,

            )

        except Exception:

            pass


        # ==========================================
        # BRIGHTNESS
        # ==========================================

        try:

            centroid = float(

                np.mean(

                    audio.spectral_centroid

                )

            )

            rolloff = float(

                np.mean(

                    audio.spectral_rolloff

                )

            )

            nyquist = audio.sample_rate / 2

            centroid /= nyquist

            rolloff /= nyquist

            brightness = (

                centroid * 0.55 +

                rolloff * 0.45

            )

            brightness = max(

                0.0,

                min(

                    brightness,

                    1.0,

                ),

            )

            features.brightness = round(

                brightness,

                3,

            )

        except Exception:

            pass
        
        print(
            f"[Music94] {song.title} -> {features.bpm:.2f} BPM"
        )

        return features