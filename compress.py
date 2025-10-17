import os
from moviepy.editor import VideoFileClip

def convert_videos_to_compressed_gif(target_folder):
    """
    查找指定文件夹中的所有视频，并为每个视频在原地创建一个压缩后的GIF。
    原始视频文件不会被修改。
    """
    if not os.path.isdir(target_folder):
        print(f"错误：提供的路径不是一个文件夹: {target_folder}")
        return

    video_extensions = ('.mp4', '.mov', '.avi', '.mkv', '.wmv')
    
    print(f"开始扫描文件夹并转换视频为GIF: {target_folder}")

    for filename in os.listdir(target_folder):
        if filename.lower().endswith(video_extensions):
            video_path = os.path.join(target_folder, filename)
            base_name = os.path.splitext(filename)[0]
            output_gif_path = os.path.join(target_folder, f"{base_name}.gif")

            # 如果GIF已经存在，可以选择跳过以节省时间
            if os.path.exists(output_gif_path):
                print(f"GIF已存在，跳过: {filename}")
                continue

            clip = None
            try:
                print(f"\n--- 正在处理: {filename} ---")

                # 1. 加载视频
                clip = VideoFileClip(video_path)
                
                # 2. 【核心压缩步骤】
                #    - resize(width=480): 将GIF宽度统一调整为480像素，高度等比缩放。这是最有效的压缩手段。
                #    - write_gif(fps=12): 将帧率设置为12。帧率越低，文件越小。10-15是效果和体积的平衡点。
                print(" -> 正在生成压缩的GIF，请稍候...")
                clip.resize(width=480).write_gif(output_gif_path, fps=4, logger=None)
                
                print(f" -> 成功生成GIF: {os.path.basename(output_gif_path)}")

            except Exception as e:
                print(f"处理文件 {filename} 时发生错误: {e}")
            finally:
                # 确保释放资源
                if clip:
                    clip.close()
        
    print("\n--- 所有视频处理完成 ---")


if __name__ == "__main__":
    # 您的目标文件夹
    folder_to_process = r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\subsets\DH-SingleVid"
    
    convert_videos_to_compressed_gif(folder_to_process)