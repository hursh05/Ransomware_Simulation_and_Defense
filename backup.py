
import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# Example: Backup a file to S3
def backup_to_s3(file_path, bucket_name):
    with open(file_path, 'rb') as file:
        s3_client.upload_fileobj(file, bucket_name, file_path)
    print(f"File {file_path} backed up to S3 bucket {bucket_name}")

# Example: Backup files to S3 recursively
def backup_directory_to_s3(directory_path, bucket_name):
    for subdir, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(subdir, file)
            backup_to_s3(file_path, bucket_name)

if __name__ == "__main__":
    directory_to_backup = "path/to/important/files"
    s3_bucket = "north_east_backup_bucket_sample"
    backup_directory_to_s3(directory_to_backup, s3_bucket)

    