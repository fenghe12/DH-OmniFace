<div align="center">

<img src="https://raw.githubusercontent.com/luna-ai-lab/DH-FaceVid-1K/main/assets/logo.svg" alt="DH-FaceVid-1K Logo" width="150">


# DH-OmniFace: A Large-Scale and Multi-Attribute Dataset Suite for Controllable Face Video Generation

<span style="font-size: 24px; font-weight: bold;">🏆 Arxiv 2025 🏆</span>

[![Paper](https://img.shields.io/badge/arXiv-Paper-b31b1b?logo=arxiv&logoColor=b31b1b)](#)
[![Project Website](https://img.shields.io/badge/DH--FaceVid--1K-Website-4CAF50?logo=googlechrome&logoColor=white)](https://fenghe12.github.io/DH-OmniFace/)
[![Dataset v1.1](https://img.shields.io/badge/Request_Access-v1.0-8A2BE2?style=flat&logo=apache-spark&logoColor=white)](https://docs.google.com/forms/d/e/1FAIpQLSeSMkATTXO22YvLFj-qC_hDM8LCd912Y45cdyINU91HbgP9KQ/viewform?usp=header)

</div>

Official repository of **DH-OmniFace: A Large-Scale and Multi-Attribute Dataset Suite for Controllable Face Video Generation**.

*[He Feng](https://github.com/fenghe12), [Donglin Di](https://scholar.google.com/citations?hl=zh-CN&user=L8tcNioAAAAJ), [Tonghua Su](https://scholar.google.hk/citations?hl=zh-CN&user=67fxVzoAAAAJ), [Yin Chen](#), [Xiu Su](#), [Hongyan Xu](#), [Zhongjie Wang](#), [Xiangqian Wu](#), [Song Yang](#), and [Lei Fan](https://hellodfan.github.io/)*

---

## 📖 Dataset Overview

![Dataset Overview](static/images/figure1-0918.png)

Overview of the proposed DH-OmniFace. The suite includes seven components: DH-FaceVid-1K for talking face generation, DH-SingleVid for
complex body movements, DH-ReliFaceVid for diverse lighting conditions, DH-MVHeadVid for multi-view head poses, DH-EmoFaceVid for expressive
emotions, DH-LolFaceVid for authentic laughter, and DH-DrasFaceVid for large-angle head movements. The lower panels summarize our experiments:
i) fine-tuning generative backbones, ii) proposing the FACET benchmark, and iii) exploring joint training of face and full-body data to enhance quality and diversity in full-body video generation.

---

## 📥 Download

![Application](static\images\application.png)
**Scale:** 340k samples / 1.8k hrs duration / ~5 TB

If you wish to download the DH-OmniFace dataset, please follow these steps:

1.  **Fill out the request form**: To prevent misuse of the dataset, we require you to submit information for review and approval. Please carefully fill out [**this form**](https://docs.google.com/forms/d/e/1FAIpQLSeSMkATTXO22YvLFj-qC_hDM8LCd912Y45cdyINU91HbgP9KQ/viewform?usp=header). **You must use an official institutional email address and clearly state your research purpose.** Requests from personal email providers (e.g., Gmail, Outlook) will be rejected. When filling out the form, ensure your information is accurate, especially **your email address**, as this is where we will send the download instructions.

2.  **Await email delivery**: Once we receive and approve your submission, we will send you an email with download instructions, typically **within 2-3 working days**. Please keep an eye on your inbox, including the spam or junk mail folders, to avoid missing our message. We currently support the four download methods specified in the request form. For optimal performance, we recommend using either Aliyun Drive or Hugging Face.

3.  **Download the dataset**: After receiving the email, you can click the download link provided and follow the instructions on the page to complete the download process. If you encounter any issues or do not receive the email within a reasonable time, please contact us at **fenghe021209@gmail.com**.

**Note:** These video samples are sourced from crowd-sourcing platforms. To ensure the proper use of the data and prevent misuse, we manually review all download requests. By downloading and using this dataset, you are required to comply with [**the license agreement**](https://github.com/fenghe12/DH-OmniFace/blob/main/LICENSE). Thank you for your understanding and cooperation.

---

## 🚀 Open-source Plan

Our open-source roadmap is as follows. We will update the status here as we make progress.

- 🔄 Phase 1: Open all dataset videos and annotations (On-going)


---

## 🎬 Video Samples
### The videos have been cropped and compressed to ensure faster page loading, but this does not reflect the original quality.
### DH-FaceVid-1K
<table class="center" style="border-collapse: collapse; margin: auto;">
  <!-- Row 1: Numeric IDs -->
  <tr>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/000680.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/001106.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/001406.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/001592.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/002148.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/002728.gif" style="width: 100%;"></td>
  </tr>

  <!-- Row 2: Alphanumeric IDs -->
  <tr>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/0s1UUn9aSSw_7.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/39Br2A7lxac_22.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/3lfO6OCqcCA_0.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/BFs-a-hqs2I_9.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/Czb5Ml9VDsI_0.gif" style="width: 100%;"></td>
    <td width="20%" style="border: none; padding: 5px;"><img src="facevid/gifs/GrjEDguF59Q_0.gif" style="width: 100%;"></td>
  </tr>
</table>

### DH-EmoFaceVid  
The emotions include **happy, angry, fearful, disgusted, sad, and surprised**.
<table class="center" style="border-collapse: collapse; margin: auto;">
  <!-- Row 1 -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/001_happy_038.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/021_happy_030.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/002_angry_001.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/003_angry_037.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/005_fear_003.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/018_fear_51.gif" style="width: 100%;"></td>
  </tr>
  <!-- Row 2 -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/006_disgust_031.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/021_disgust_023.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/018_sad_036.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/045_sad_011.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/044_surprise_010.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="DH-EmoFaceVid/046_surprise_038.gif" style="width: 100%;"></td>
  </tr>
</table>


### DH-ReliFaceVid
<table class="center" style="border-collapse: collapse; margin: auto;">
  <!-- Row 1 -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0001_light1_0001.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0001_light2_0001.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0001_light5_0005.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0001_light6_0004.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0002_light2_0020.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0003_light1_0011.gif" style="width: 100%;"></td>
  </tr>

  <!-- Row 2 -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0003_light8_0013.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0011_light2_0008.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0014_light3_0012.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/0070_light2_0010.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/outdoor_0006_light6_0009.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/outdoor_0006_light8_0004.gif" style="width: 100%;"></td>
  </tr>

  <!-- Row 3 -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/outdoor_0008_light2_0011.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/outdoor_0009_light3_0006.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/outdoor_0041_light3_0017.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/outdoor_0042_light1_0010.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/outdoor_0051_light3_0008.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-ReliFaceVid/outdoor_0052_light4_0012.gif" style="width: 100%;"></td>
  </tr>
</table>

### DH-LolFaceVid
<table class="center" style="border-collapse: collapse; margin: auto;">
  <!-- New Row with your GIFs -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-LolFaceVid/2024_09_05_14_51_IMG_4368.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-LolFaceVid/VID_20240909_103040.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-LolFaceVid/VID_20240912_134857.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-LolFaceVid/VID20240909085206.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-LolFaceVid/VID20240920152148.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-LolFaceVid/VID20240922151142.gif" style="width: 100%;"></td>
  </tr>
</table>

### DH-DrasFaceVid

<table class="center" style="border-collapse: collapse; margin: auto;">
  <!-- New Row with your GIFs -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-DrasFaceVid/batch_04_004_VID20240823094316.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-DrasFaceVid/batch_04_002_VID20240822115129.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-DrasFaceVid/batch_03_034_VID20240821130848.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-DrasFaceVid/batch_03_033_VID20240821102408.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-DrasFaceVid/batch_02_030_VID20240820142103.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-DrasFaceVid/batch_01_026_VID_20240812084921.gif" style="width: 100%;"></td>
  </tr>
</table>

### DH-MVHeadVid
<table class="center" style="border-collapse: collapse; margin: auto;">
  <!-- Row 1 -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/001-张芳芳-女_cam3_VID_20240920_113946.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/004-李子豪-男_cam4_VID_20240926_222900.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/004-李子豪-男_cam4_VID_20240926_223654.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/005-王志胜-男_cam2_VID_20240927_194023.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/006-王晓雅-女_cam7_VID_20240924_211248.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/007-李晓光-男_cam2_VID_20240928_191226.gif" style="width: 100%;"></td>
  </tr>

  <!-- Row 2 -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/007-李晓光-男_cam5_VID_20240928_191828.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/008-王泽-男_cam4_VID_20240929_162344.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/008-王泽-男_cam6_VID_20240929_160811.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/009-张嫣然-女_cam4_VID_20240924_174540.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/010-李鹏飞-男_cam5_VID_20240930_224028.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-MVFaceVid/010-李鹏飞-男_cam8_VID_20240930_225926.gif" style="width: 100%;"></td>
  </tr>
</table>

### DH-SingleVid

<table class="center" style="border-collapse: collapse; margin: auto;">
  <!-- New Row with your GIFs -->
  <tr>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-SingleVid/dance-pose1.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-SingleVid/dance-pose2.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-SingleVid/gymnastic-pose2.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-SingleVid/scene-pose1.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-SingleVid/yoga-pose1-1.gif" style="width: 100%;"></td>
    <td width="16.6%" style="border: none; padding: 5px;"><img src="subsets/DH-SingleVid/yoga-pose1.gif" style="width: 100%;"></td>
  </tr>
</table>

### 📊 Datasets Comparison

Compared with other datasets, DH-OmniFace has a larger data volume, superior visual quality, and broader attribute coverage.

![Comparison](static/images/img_v3_02r4_cebe0894-d5db-4059-80e3-0f1bb1ba3e9g.jpg) 


---

## 📈 Statistics

Details of each subset.

![Statistics](static/images/img_v3_02r4_88423c55-6652-4cf9-89b0-a19261c1336g.jpg)

---

## ⚙️ Collection Pipeline

![Collection Pipeline](static/images/figure4_cropped.png)


Overview of the data curation pipeline, comprising four main stages: raw data acquisition, video preprocessing, noisy data filtering, and annotation
generation using Qwen2.5-VL and Llama 3, followed by two-stage manual verification.


---

## 🧠 Trained Models

**[Coming Soon]**

---

## ✒️ Citation

**[Coming Soon]**
<!-- If you find the DH-OmniFace dataset useful for your work, please consider citing our paper:
```
@inproceedings{di2025facevid,
      title = {DH-FaceVid-1K: A Large-Scale High-Quality Dataset for Face Video Generation},
      author = {Di, Donglin and Feng, He and Sun, Wenzhang and Ma, Yongjia and Li, Hao and Chen, Wei and Fan, Lei and Su, Tonghua and Yang, Xun},
      booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
      year = {2025}
}
``` -->
