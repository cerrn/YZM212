import numpy as np
from hmmlearn import hmm

model_ev = hmm.MultinomialHMM(n_components=2, init_params="", params="te")
model_ev.startprob_ = np.array([1.0, 0.0]) 
model_ev.transmat_ = np.array([
    [0.6, 0.4], 
    [0.2, 0.8]  
])
model_ev.emissionprob_ = np.array([
    [0.7, 0.3], 
    [0.1, 0.9] 
])

model_okul = hmm.MultinomialHMM(n_components=2, init_params="", params="te")
model_okul.startprob_ = np.array([0.5, 0.5])
model_okul.transmat_ = np.array([
    [0.5, 0.5],
    [0.5, 0.5]
])
model_okul.emissionprob_ = np.array([
    [0.5, 0.5],
    [0.5, 0.5]
])

test_data = np.array([[0, 1]]).T

score_ev = model_ev.score(test_data)
score_okul = model_okul.score(test_data)

print("--- HMM Kelime Sınıflandırıcı ---")
print(f"EV Modeli Log-Likelihood Puanı: {score_ev:.4f}")
print(f"OKUL Modeli Log-Likelihood Puanı: {score_okul:.4f}")

if score_ev > score_okul:
    print("Sonuç: Duyulan kelime büyük ihtimalle 'EV'")
else:
    print("Sonuç: Duyulan kelime büyük ihtimalle 'OKUL'")