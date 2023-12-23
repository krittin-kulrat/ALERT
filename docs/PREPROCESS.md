# Data Preprocessing Guidelines

In the ALERT project, preprocessing data from various sources is a critical step
to ensure uniformity and reliability in our analysis. Given the diversity in
dataset configurations and device coordinate systems, we establish a standard
preprocessing procedure.

## Standardizing Coordinate System

| ![Fitbit's accelerometer axis](https://dev.fitbit.com/images/guides/sensors/accelerometer-axis-cded279fb55c403a375d7a429a2ef1ea.jpg)|
| :--: |
| *[Fitbit's accelerometer axis](https://dev.fitbit.com/build/guides/sensors/accelerometer/)* |

- **Objective**: Align the data to a common coordinate system, consistent with
popular smartwatch standards like Fitbit and Garmin.
- **Coordinate System Specification**:
  - **X-Axis**: Parallel with the device’s screen, aligned with the top and bottom
  edges, extending in the left-right direction.
  - **Y-Axis**: Parallel with the device’s screen, aligned with the left and right
  edges, extending in the top-bottom direction.
  - **Z-Axis**: Perpendicular to the device’s screen, pointing upwards.

## Implementing Coordinate Standardization

- **Transforming Data**: For each dataset, transform the accelerometer data to align
with this specified coordinate system.
- **Uniformity Check**: Ensure that post-transformation, the data from all sources
adhere to this standardized orientation.
- **Documentation**: Clearly document the transformation process for each dataset,
including any assumptions or specific steps taken.

## Initial Focus on Accelerometer Data

- **Current Scope**: We are initially utilizing only accelerometer data to
establish the proof of concept.
- **Data Selection**: Carefully select and preprocess accelerometer data from
each dataset to align with our standard coordinate system.

## Future Integration of Gyroscope Data

- **Expansion Plan**: In the future, we intend to incorporate gyroscope data to
enhance our model’s capabilities.
- **Preprocessing Gyroscope Data**: Similar standardization procedures will be
developed for gyroscope data, ensuring consistency across all types of sensor data.
