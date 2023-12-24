# Data Preprocessing Guidelines

In the ALERT project, effective data preprocessing is vital for accurately
analyzing accelerometer data. We are focusing on the magnitude of acceleration,
which simplifies the preprocessing by eliminating the need for standardizing the
coordinate system.

## Processing Accelerometer Data

- **Objective**: To process and analyze accelerometer data uniformly across
various datasets.
- **Magnitude Calculation**: The following equation will be used to calculate
the magnitude of acceleration. If the the watch lays flat, the magnitude should
equal to 9.8

$$
|A| = \sqrt{A_x^2+A_y^2+A_z^2}
$$

## Statistical Feature Extraction

1. **Maximum Peak**: The highest acceleration magnitude recorded, reflecting the
intensity of a movement or a fall.

2. **Range Pre-Peak**: The difference in acceleration magnitude before the
peak - from the lowest to the highest.

3. **Range Post-Peak**: The difference in acceleration magnitude after the
peak - from the lowest to the highest.

4. **Time Pre-Peak**: The time interval between the lowest and highest
acceleration magnitude before the peak.

5. **Time Post-Peak**: The time interval between the lowest and highest
acceleration magnitude after the peak.

6. **Mean Acceleration**: The average value of acceleration magnitude over a
defined time window.

7. **Median Acceleration**: The median value of acceleration magnitude,
indicating central tendency.

8. **Standard Deviation**: A measure of the variability in acceleration magnitude.

9. **Variance**: The square of the standard deviation, reflecting the spread in
acceleration data.

10. **Skewness**: A measure of the asymmetry of the acceleration distribution.

11. **Kurtosis**: Indicates the 'tailedness' of the acceleration distribution,
capturing extreme movements.

## Implementation Notes

- **Feature Calculation**: Calculate these statistical features for each
relevant segment of the accelerometer data.
- **Documentation**: Clearly document the feature extraction process for each
dataset for consistency and reproducibility.

## Future Plans

- As the project progresses, we may incorporate additional sensor data and
expand our statistical analysis.
- These preprocessing guidelines will be updated to accommodate such enhancements.

## Importance of Preprocessing

- Accurate preprocessing is essential for capturing the nuances of movement
patterns that are characteristic of falls.
- The selected statistical features are designed to provide a comprehensive
understanding of these patterns.

## Conclusion

- Following these preprocessing guidelines ensures that our dataset is processed
uniformly, making it suitable for analysis and model training.
- This approach is fundamental to the success of our machine learning models in
the ALERT project.
