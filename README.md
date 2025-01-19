
# Ransomware Simulation and Defense

## Project Overview

This project demonstrates how ransomware attacks can encrypt files and how defenses, such as backup and recovery, can mitigate the impact. The ransomware simulation script encrypts files within a given directory, while the defense script performs backups of critical files to AWS S3 and restores them in case of a ransomware attack.

### Technologies Used:
- Python
- AWS S3 (for backup and recovery)
- AWS Glacier (optional, for long-term storage)
- Cryptography library (for simulating encryption)

---

## Project Structure

```
ransomware-simulation-and-defense/
│
├── backup_restore.py       # Script for backing up and restoring files using AWS S3
├── encrypt_files.py        # Script for simulating the ransomware attack (encrypts files)
├── README.md               # Project documentation
└── requirements.txt        # Required Python libraries
```

---

## Setup Instructions

### 1. Install Dependencies

First, create a Python virtual environment and install the required libraries.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scriptsctivate
# On macOS/Linux:
source venv/bin/activate

# Install the required libraries
pip install -r requirements.txt
```

The **`requirements.txt`** file should include the following libraries:

```text
boto3==1.20.21
cryptography==3.4.7
```

### 2. AWS Setup

#### 2.1 Configure AWS Credentials

You need to set up your AWS credentials so that the scripts can interact with AWS services like S3 and Glacier.

##### Option 1: Using AWS CLI (Recommended)

Run the following command to configure your AWS credentials locally:

```bash
aws configure
```

You will be prompted to enter:
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region name** (e.g., `us-west-2`)
- **Default output format** (e.g., `json`)

These credentials will be stored in the `~/.aws/credentials` file.

##### Option 2: Using Environment Variables

Alternatively, you can set AWS credentials using environment variables directly in your script or terminal session.

```python
import os
import boto3

os.environ["AWS_ACCESS_KEY_ID"] = "your_access_key"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your_secret_key"
os.environ["AWS_DEFAULT_REGION"] = "us-west-2"

s3_client = boto3.client('s3')
```

---

## Usage

### 1. **Simulate Ransomware Attack**

Run the `encrypt_files.py` script to simulate a ransomware attack by encrypting all files in a given directory.

```bash
python encrypt_files.py
```

You can modify the `target_directory` variable in the script to specify the directory you want to simulate the attack on.

### 2. **Backup Files to AWS S3**

Run the `backup_restore.py` script to back up important files to your AWS S3 bucket. Before running the backup, make sure you’ve created an S3 bucket in your AWS account.

```bash
python backup_restore.py
```

Make sure to replace `your-s3-bucket-name` with your actual S3 bucket name in the script.

### 3. **Restore Files from AWS S3**

After simulating the ransomware attack, you can restore the encrypted files from the backup stored in your S3 bucket by running the restore function in the same `backup_restore.py` script.

```bash
python backup_restore.py
```

---

## Example: How It Works

1. **Backup**: Before running the ransomware simulation, you can run the backup script to upload your important files to AWS S3. This will protect your data in case of an attack.
   
2. **Ransomware Simulation**: The `encrypt_files.py` script encrypts files in the specified directory using the cryptography library. This simulates how ransomware might lock files.

3. **Recovery**: If the files are encrypted, you can recover them by restoring from the backup in S3.

---

## Notes

- Ensure that your AWS credentials have appropriate permissions for accessing and managing S3 (and Glacier, if used).
- The ransomware simulation **only encrypts files**; it is not a real attack and should only be used for educational purposes.
- AWS Glacier is used for long-term storage backups. If you choose to use Glacier for storing backups, remember that restoring files from Glacier may take a longer time compared to regular S3.

---

## Future Enhancements

- Implement automatic restoration from S3/Glacier after the ransomware attack.
- Improve the ransomware simulation to mimic more advanced encryption techniques.
- Integrate with additional cloud storage services like Google Cloud Storage or Azure Blob Storage for backup and recovery.

---
