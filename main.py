import os


dir="source_directory"
mp4_dir="related-directory"
pdf_dir="related-directory"
zip_dir="related-directory"
deb_dir="related-directory"
mp3_dir="related-directory"
extension_list={".mp4":mp4_dir,".mp3":mp3_dir,".zip":zip_dir,".deb":deb_dir,".pdf":pdf_dir}
print(extension_list)
for filename in os.listdir(dir):
 # extension=filename.split('.')
 # print(extension[-1])
    new_dir=dir+"/"+filename
    extension=os.path.splitext(filename)
    format_=extension[1]
    print(format_)
    if format_ in extension_list :
        destination=extension_list[format_]+"/"+filename
        if os.path.exists(destination):
            continue
        os.rename(new_dir,destination)



