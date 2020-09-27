import librosa

y, sr = librosa.load("D:\\qqpdbgm\\Back3.wav", duration=60)
onset_env = librosa.onset.onset_strength(y, sr=sr)
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)


print(tempo)