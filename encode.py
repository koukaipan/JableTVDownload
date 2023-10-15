import os
import subprocess
def ffmpegEncode(folder_path, file_name, accelerator):
    if accelerator == 'nv-gpu': #GPU轉檔
        os.chdir(folder_path)
        try:
            subprocess.call(['ffmpeg', '-i', f'{file_name}.mp4','-c:v', 'h264_nvenc', '-b:v', '10000K',
                                '-threads', '5', f'f_{file_name}.mp4'])
            os.remove(os.path.join(folder_path, f'{file_name}.mp4'))
            os.rename(os.path.join(folder_path, f'f_{file_name}.mp4'), os.path.join(folder_path, f'{file_name}.mp4'))
            print("轉檔成功!")
        
        except:
            print("轉檔失敗!")
    elif accelerator == 'cpu': #CPU轉檔
        os.chdir(folder_path)
        try:
            subprocess.call(['ffmpeg', '-i', f'{file_name}.mp4', '-c', 'copy', '-tag:v', 'avc1',
                            f'f_{file_name}.mp4'])
            os.remove(os.path.join(folder_path, f'{file_name}.mp4'))
            os.rename(os.path.join(folder_path, f'f_{file_name}.mp4'), os.path.join(folder_path, f'{file_name}.mp4'))
            print("轉檔成功!")
        
        except:
            print("轉檔失敗!")
    else:
        return
