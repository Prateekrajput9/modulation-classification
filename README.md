# 📡 Machine Learning-Based Modulation Classification

> Deep learning-based classification of wireless signal modulation using CNNs on STFT spectrograms.

📄 Project Presentation: (see PPT in repo)

---

## 🚀 Overview

This project focuses on automatically identifying the **modulation scheme** of a received wireless signal using **raw IQ samples**.

Instead of using traditional signal processing methods, we leverage:

- 📊 STFT (Short-Time Fourier Transform)
- 🧠 Convolutional Neural Networks (CNN)

---

## 🎯 Objective

- Classify modulation schemes **without prior knowledge of transmitter**
- Handle noisy environments (**-10 dB to +20 dB SNR**)
- Build a **robust real-world system**

---

## 📊 Modulation Classes (12)

### 🔹 Digital (8)
- ASK (Amplitude Shift Keying)
- FSK (Frequency Shift Keying)
- BPSK
- QPSK
- 8-PSK
- 16-QAM
- 64-QAM
- MSK

### 🔹 Analog (4)
- DSB-TC
- DSB-SC
- SSB-SC
- PAM

---

## 🧠 Key Idea

Raw IQ signals are difficult for CNNs to interpret directly.

👉 We convert them into **2D spectrogram images using STFT**, enabling the model to learn **time-frequency patterns**.

---

## ⚙️ Pipeline
<img width="1039" height="615" alt="image" src="https://github.com/user-attachments/assets/61856c6b-f9c9-400f-b2fc-f2093cc42551" />

GNU Radio + PlutoSDR
↓
Raw IQ Data (4096 samples)
↓
STFT Transformation
↓
128×128 Spectrogram
↓
CNN Model (WirelessID_CNN_12)
↓
Predicted Modulation Class

---

## 📡 Dataset

- Generated using **GNU Radio + PlutoSDR**
- Sample length: **4096 (IQ)**
- SNR range: **-10 dB to +20 dB**
- Total samples: ~96,000
- Balanced dataset across all classes

Each sample contains:
- IQ values (interleaved)
- Modulation label
- SNR value

---

## 🖼️ STFT Preprocessing

- Window: Hann
- nperseg = 128
- noverlap = 64
- Log magnitude scaling
- FFT shift
- Min-max normalization

➡️ Output: **128×128 grayscale spectrogram**

---

## 🏗️ Model Architecture

**WirelessID_CNN_12**

- Input: `1 × 128 × 128`
- 4 Convolution Blocks:
  - Conv2D + BatchNorm + ReLU + MaxPool
- Fully Connected:
  - FC(128) → Output(12 classes)

---

## ⚙️ Training Configuration

- Optimizer: Adam  
- Learning Rate: 1e-3  
- Weight Decay: 1e-4  
- Loss: CrossEntropyLoss  
- Scheduler: CosineAnnealingLR  
- Epochs: 30  
- Batch Size: 32  
- Hardware: GPU (CUDA)

---

## 📈 Results

### ✅ Overall Performance
- Test Accuracy: **~94%**
- Validation Accuracy: **~93%**
- Stable convergence

### 📊 Accuracy vs SNR

| SNR (dB) | Accuracy |
|----------|----------|
| -10 dB   | 87%      |
| 0 dB     | 95%      |
| 10 dB    | 98%      |
| 20 dB    | 99%      |

---

## 📌 Per-Class Highlights

- Best:
  - BPSK → 97%
  - QPSK → 97%
  - DSB-TC → 97%

- Lowest:
  - ASK → 90%

---

## 🔍 Confusion Insights

- ASK ↔ DSB-SC confusion (similar spectral patterns)
- FSK ↔ MSK overlap
- QAM classes successfully distinguished

---

## 💡 Novelty

- ✅ Real SDR-based dataset (GNU Radio + PlutoSDR)
- ✅ STFT-based feature representation
- ✅ Single model across multiple SNR levels
- ✅ No manual feature engineering

---

## ⚠️ Challenges

- Low SNR reduces feature visibility
- Similar modulation patterns cause confusion
- Generalization across SNR levels

---

## 📁 Project Structure
modulation-classification/
│
├── data/
├── notebooks/
├── models/
├── utils/
├── results/
├── main.py
├── config.py
├── requirements.txt
└── README.md

---

## 🛠️ Installation & Usage

```bash
# Clone repository
git clone https://github.com/your-username/modulation-classification

# Install dependencies
pip install -r requirements.txt

# Run training
python main.py
