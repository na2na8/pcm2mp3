import os

# pcm files' list
def pcm_files(folder_path) :
    pcm_files = [f for f in os.listdir(folder_path) if f.endswith('.pcm')]
    return pcm_files

# convert
def convert(folder_path, output_folder_path, pcm_files) :
    # mp3 files that already have been made
    already_exist_mp3 = [f for f in os.listdir(output_folder_path if f.endswith('.mp3'))]

    for pcm_file in pcm_files :
        # if pcm file name is in already_exist_mp3, pass the converting
        if pcm_file[:-3]+'mp3' in already_exist_mp3 :
            continue

        pcm_path = ''
        if folder_path[-1] == '/' :
            pcm_path = folder_path + pcm_file
        else :
            pcm_path = folder_path + '/' + pcm_file
        
        mp3_path = ''
        if output_folder_path[-1] == '/' :
            mp3_path = output_folder_path + pcm_file[:-3] + 'mp3'
        else :
            mp3_path = output_folder_path + '/' + pcm_file[:-3] + 'mp3' 

        command = 'ffmpeg -f s16le -ar 44k -ac 1 -i ' + pcm_path + ' ' + mp3_path
        os.system(command)
