import matplotlib.pyplot as plt
import os

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei']  # or 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

text = """16.5.7 应用

流匹配可以作为大规模生成系统中的一条重要技术路线.
在图像生成领域，一些文本到图像系统采用基于矫正流的流匹配框架，
并与 DiT (Diffusion Transformer) 等骨干网络结合，以改善生成质量和采样效率.
在视频生成领域，流匹配的直线传输路径也有助于在有限步数内生成时间上连贯的视频帧.

从更广的视角看，流匹配与扩散模型之间的边界并不绝对——
两者的核心技术（条件控制、无分类器引导、隐空间建模等）可以高度共享.
在连续时间表述下，二者都可以理解为学习从简单分布到数据分布的动力系统；
流匹配通过更直接的速度场回归和可设计的路径，提供了另一条高效技术路线.
"""

fig, ax = plt.subplots(figsize=(10, 6))
ax.text(0.05, 0.95, text, va='top', ha='left', fontsize=14, family='sans-serif', wrap=True)
ax.axis('off')
plt.tight_layout()

# Simulate textbook style
fig.patch.set_facecolor('#f8f8f8')
ax.set_facecolor('#ffffff')

# Add a border
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('#cccccc')

out_path = r'd:\大三上的资料\假期学习记录\组会汇报_FlowMatching\images\fm_application.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight')
print(f"Image saved to {out_path}")
