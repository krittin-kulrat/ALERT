@echo off
setlocal

echo Downloading file...
curl -L -o "downloaded_file.zip" "https://figshare.com/ndownloader/files/11826395"

echo Extracting file...
powershell -Command "Expand-Archive -Path 'downloaded_file.zip' -DestinationPath '.'"

echo Checking MD5 checksum...
set "expectedMD5=5ea9f4cb6277272d2f5f3f94e8ed456f"
for /f "delims=" %%a in ('certutil -hashfile "downloaded_file.zip" MD5 ^| find /v "certutil" ^| find /v ":"') do (
    set "fileMD5=%%a"
)

if /i "%fileMD5%"=="%expectedMD5%" (
    echo MD5 checksum is correct.
    del "downloaded_file.zip"
    echo Downloaded file deleted.
) else (
    echo MD5 checksum does not match.
    echo Expected: %expectedMD5%
    echo Found:    %fileMD5%
)

endlocal
