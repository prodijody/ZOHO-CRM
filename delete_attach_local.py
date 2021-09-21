import os
def delete_attachments_local():
    dir = './Attachments'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print(f + " Deleted")

# delete_attachments_local()