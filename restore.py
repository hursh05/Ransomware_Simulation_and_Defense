def restore_from_s3(directory, bucket_name):
    s3_client = boto3.client('s3')
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            s3_client.download_file(bucket_name, file, os.path.join(subdir, file))
            print(f"Restored {file} from S3")

if __name__ == "__main__":
    directory_to_restore = "User/Desktop/Restored_files"
    s3_bucket = "north_east_backup_bucket_sample"
    restore_from_s3(directory_to_restore, s3_bucket)
