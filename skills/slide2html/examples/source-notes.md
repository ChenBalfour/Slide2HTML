# Synthetic lecture notes / 合成讲义

This is a design and interaction fixture, not a real course. Headings are source locators. No assessments, deadlines, instructor, semester, or grades are specified.

## Orientation / 导读

Topic: Learning from data / 从数据中学习.
This lecture introduces generalization, overfitting, and regularization. The central question is how to learn useful patterns instead of memorizing examples.
本讲介绍泛化、过拟合和正则化，核心问题是如何学习有用的规律，而非记住样本。

## 01 Generalization / 泛化

Generalization is a model's ability to perform well on unseen data from the target distribution. Evaluate on data not used to fit the model; holdout performance estimates rather than guarantees future performance.
泛化是模型在来自目标分布的未见数据上表现良好的能力。评估数据不应参与模型拟合；留出集表现是对未来性能的估计，而非保证。

## 02 Overfitting / 过拟合

Overfitting occurs when a model fits training-specific variation that does not transfer to unseen data. Low training error alone is not evidence of strong generalization. Validation data helps select model settings; repeatedly tuning on the test set undermines its independence.
过拟合发生在模型拟合了训练数据特有、不能迁移到未见数据的变化时。仅有较低训练误差不足以证明泛化良好。验证集用于选择模型设置；反复利用测试集调参会破坏测试的独立性。

## 03 Regularization / 正则化

Regularization adds a preference or constraint to learning. One example is L2-penalized least squares:
J(w) = (1/n) Σᵢ (yᵢ − xᵢᵀw)² + λ‖w‖₂², with λ ≥ 0.
n is the sample count; xᵢ is the feature vector; yᵢ is the target; w is the parameter vector; λ controls penalty strength. This fixture omits an intercept. Stronger penalties can reduce variance but may increase bias; they do not guarantee better results.
正则化在学习中加入偏好或约束。示例为带 L2 惩罚的最小二乘。n 为样本数，xᵢ 为特征向量，yᵢ 为目标，w 为参数，λ 控制惩罚强度；本例省略截距。更强的惩罚可能降低方差，也可能增加偏差，并不保证结果更好。

## Relationships / 概念关系

Overfitting threatens generalization; regularization is one approach to address it. Compare models using independent evaluation, not training fit alone.
过拟合会威胁泛化；正则化是应对它的方法之一。比较模型应使用独立评估，而非只看训练拟合。
