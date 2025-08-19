# ML Models Summary

## 1. Attendance Prediction (Time Series)
- Model: Prophet (mock example)
- Features: session date
- Metric: RMSE ≈ 1.2 (low error in mock dataset)

## 2. Feedback Classifier (Sentiment Analysis)
- Model: Logistic Regression (mock example)
- Features: TF-IDF from comments
- Metric: Accuracy = 0.90, F1 = 0.88

## 3. Member Segmentation
- Model: KMeans clustering (k=3)
- Features: frequency, plan type, duration
- Metric: Silhouette score = 0.67

---
### Next Steps
- Expand dataset for better prediction power.
- Fine-tune classifier with more labeled feedback.
- Try hierarchical clustering for improved segments.
