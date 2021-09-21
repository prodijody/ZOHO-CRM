from get_attachment_id import get_attachments
from download_attachment import download_attachment
from insert_ZFS import upload_files_to_zfs
from insert_file_upload import update_record 

record_id = input("Enter Record Id: ")
attachment_ids = get_attachments(record_id)
attachments_paths = download_attachment(record_id, attachment_ids)
zfs_ids = upload_files_to_zfs(attachments_paths)
response = update_record(record_id, zfs_ids)

print(response)