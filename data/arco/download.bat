@echo off
echo Downloading training file from ARCO Research Group
curl -o "tmp.zip" "https://arcoresearch.com/wp-content/uploads/fall-dataset.zip"
powershell -Command "Expand-Archive -Path 'tmp.zip' -DestinationPath '.'"

if exist "tmp.zip" (
    del "tmp.zip"
)

if exist ".\fall-dataset\fall-dataset-raw" (
    move ".\fall-dataset\fall-dataset-raw" .\dataset
    rmdir /s /q ".\fall-dataset"
) else (
    echo "The specified path for 'fall-dataset-raw' does not exist."
)

if exist ".\dataset" (
    echo "Dataset folder created successfully."
) else (
    echo "Failed to create dataset folder."
)

echo Downloading testing dataset
curl -o "tmp.zip" "https://arcoresearch.com/wp-content/uploads/test_dataset.zip"
powershell -Command "Expand-Archive -Path 'tmp.zip' -DestinationPath '.'"

if exist "tmp.zip" (
    del "tmp.zip"
)

if exist ".\test_dataset" (
    echo "test_dataset folder created successfully."
) else (
    echo "Failed to create test_dataset folder."
)

echo Finish loading dataset file from ARCO
