from insert_ZFS import upload_files_to_zfs
from insert_file_upload import update_record 

record_id = input("Enter Record Id: ")
attachments_paths = ['./Attachments\\fr.pdf', './Attachments\\fr.jpg']
zfs_ids = upload_files_to_zfs(attachments_paths)
response = update_record(record_id, zfs_ids)

print(response)