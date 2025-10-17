import os
from moviepy.editor import VideoFileClip

# 输入文件路径列表
video_paths = [
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\001_happy_038.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\002_angry_001.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\003_angry_037.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\005_fear_003.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\006_disgust_031.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\018_fear_51.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\018_sad_036.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\021_happy_030.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\044_surprise_010.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\021_disgust_023.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\045_sad_011.mp4",
    r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid\046_surprise_038.mp4",
]

# 输出目录
output_dir = r"C:\Users\fenghe\Desktop\DH-OmniFace\DH-OmniFace\dh-faceemovid"

for video_path in video_paths:
    try:
        # 获取文件名（不含扩展名）
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        output_path = os.path.join(output_dir, base_name + ".gif")

        # 如果文件已存在，跳过
        if os.path.exists(output_path):
            print(f"⚠️ 已存在，跳过: {output_path}")
            continue

        # 读取视频并转为GIF
        clip = VideoFileClip(video_path)
        clip.write_gif(output_path, fps=10)
        clip.close()

        print(f"✅ 转换完成: {output_path}")

    except Exception as e:
        print(f"❌ 转换失败: {video_path}，错误：{e}")
