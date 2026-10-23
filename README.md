# AI-Based Network Intrusion Detector

**Author:** Samiksha Sathe  
**Project type:** Educational machine-learning demonstration

## Overview
This project demonstrates a Random Forest classifier that labels example network-traffic records as `Benign` or `Attack`. It prints evaluation metrics, displays a confusion matrix and feature-importance chart, predicts one example record, and saves the trained model.

## Important limitation
This version uses **synthetic demonstration data**. Labels are generated from selected input features, so high accuracy (including 100%) is expected. This is not evidence of real-world intrusion-detection performance. It does not monitor a live network and is not a production security system.

## Setup (Windows PowerShell)
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run
```powershell
python Samiksha_AI_Network_Intrusion_Detection.py
```

The script prints metrics, displays charts, and saves `intrusion_detection_model.pkl`.

## Future work
Evaluate on a genuine public intrusion-detection dataset such as CIC-IDS2017, review its format and terms, and report precision, recall, F1-score and false-positive rate on unseen data.

## Files
- `Samiksha_AI_Network_Intrusion_Detection.py` — project code
- `requirements.txt` — dependencies
- `Samiksha_ProjectReport.docx` — report
