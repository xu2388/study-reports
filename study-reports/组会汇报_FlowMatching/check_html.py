import re

with open(r'd:\大三上的资料\假期学习记录\组会汇报_FlowMatching\FlowMatching_组会汇报.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section class="slide', html)
print('slide 数量:', len(sections))

opens = html.count('<section')
closes = html.count('</section>')
print(f'section 开: {opens}, 关: {closes}')

div_o = html.count('<div')
div_c = html.count('</div>')
print(f'div 开: {div_o}, 关: {div_c}')

if div_o == div_c and opens == closes:
    print('OK: 结构平衡')
else:
    print('WARN: 结构不平衡')

# 检查每个 section 内部结构
for i, m in enumerate(re.finditer(r'<section class="slide[^"]*">(.*?)</section>', html, re.S), 1):
    seg = m.group(1)
    so = seg.count('<section')
    sc = seg.count('</section>')
    do = seg.count('<div')
    dc = seg.count('</div>')
    has_inner = 'slide-inner' in seg
    print(f'  slide {i}: inner={has_inner}, 嵌套section={so}/{sc}, div平衡={do==dc}({do}/{dc})')
