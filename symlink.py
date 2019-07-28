import os

# os.rmdir('/home/nithin/*')

folders = ['Books', 'Calibre', 'Downloads', 'Git', 'Music', 'Pictures', 'Sahaja Yoga', 'SSR', 'Torrents', 'Videos']

for folder in folders:
    if os.path.isdir(f'/home/nithin/Documents/{folder}') and not os.path.isdir(f'/home/nithin/{folder}') :
        print(folder)
        os.symlink(f'/home/nithin/Documents/{folder}', f'/home/nithin/{folder}')
