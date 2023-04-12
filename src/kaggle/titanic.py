from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd

# 训练
train_data = TabularDataset(r"C:\Users\pozhe\Downloads\train.csv")
id, label = 'PassengerId', 'Survived'
predictor = TabularPredictor(label=label).fit(train_data.drop(columns=[id]))

# 预测
test_data = TabularDataset(r"C:\Users\pozhe\Downloads\test.csv")
preds = predictor.predict(test_data.drop(columns=[id]))
submission = pd.DataFrame({id: test_data[id], label: preds})
submission.to_csv(r"C:\Users\pozhe\Downloads\submission.csv", index=False)
