"""Generate the roadmap diagram used in README.md.

Usage:
    python3 scripts/gen_roadmap.py [output_path]

Default output: assets/roadmap.svg (relative to the repo root).
Edit the group titles and topics in the spine_group() calls and the
`cols` list below, then re-run the script.
"""
import sys
from pathlib import Path
from xml.sax.saxutils import escape as e

ROOT = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "assets" / "roadmap.svg"
W, H = 1000, 1275
FONT = "Inter, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
C = {
 'base': ('#DCEAF7', '#1F4E79', '#1F4E79'),
 'core': ('#D5F0E3', '#2F7D5B', '#1E5A40'),
 'par':  ('#E8E1F5', '#5B4B8A', '#3F3366'),
 'ai':   ('#FBE3D6', '#B5532A', '#8A3B1C'),
 'x':    ('#FDF3D8', '#B7791F', '#7A4E0E'),
}
s = []
a = s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">')
a(f'<rect width="{W}" height="{H}" rx="16" fill="#FFFFFF"/>')
a(f'<text x="500" y="52" text-anchor="middle" font-size="28" font-weight="700" fill="#1F2933">Learning Software Engineer 2027</text>')
a(f'<text x="500" y="80" text-anchor="middle" font-size="15" fill="#616E7C">Các nhóm kỹ năng kỹ sư phần mềm cần nắm vững cho năm 2027</text>')
LINE = '#52606D'
def line(x1,y1,x2,y2,dash=False,color=LINE,w=2.5):
    d = ' stroke-dasharray="5 5"' if dash else ''
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d} stroke-linecap="round"/>')
def pill(cx,cy,w,h,text,fill,stroke,color,size=14,bold=False,rx=None):
    rx = h/2 if rx is None else rx
    a(f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
    fw = ' font-weight="700"' if bold else ''
    a(f'<text x="{cx}" y="{cy+size*0.36}" text-anchor="middle" font-size="{size}"{fw} fill="{color}">{e(text)}</text>')
def node(cx,cy,w,text,kind):
    f,st,c = C[kind]
    pill(cx,cy,w,52,text,f,st,c,size=16,bold=True,rx=10)
def topic(cx,cy,text,kind,w=220,h=34):
    pill(cx,cy,w,h,text,'#FFFFFF',C[kind][1],'#1F2933',size=14)

# spine segments (drawn first, behind nodes)
line(500,130,500,560)
line(180,580,820,580)
for x in (180,500,820): line(x,560 if x==500 else 580,x,604)
for x in (180,500,820): line(x,858,x,890)
line(180,890,820,890); line(500,890,500,1050)

# start
pill(500,130,160,40,'Bắt đầu','#1F4E79','#1F4E79','#FFFFFF',size=15,bold=True)

def spine_group(y,title,kind,left,right):
    for i,t in enumerate(left):
        ty = y-22+44*i
        line(330,y,280,ty,dash=True,color='#9AA5B1',w=1.5); topic(170,ty,t,kind)
    for i,t in enumerate(right):
        ty = y-22+44*i
        line(670,y,720,ty,dash=True,color='#9AA5B1',w=1.5); topic(830,ty,t,kind)
    node(500,y,340,title,kind)

spine_group(225,'1 · Nền tảng khoa học máy tính','base',['Cấu trúc dữ liệu','Giải thuật'],['Hệ điều hành','Mạng máy tính'])
spine_group(345,'2 · Ngôn ngữ và kỹ thuật lập trình','base',['Ngôn ngữ chính','Clean code'],['Design pattern','Kiểm thử'])
spine_group(465,'3 · Backend và dữ liệu','core',['Thiết kế API','SQL và NoSQL'],['Cache, queue','Xác thực cơ bản'])

a(f'<text x="512" y="552" text-anchor="start" font-size="12" fill="#616E7C" font-style="italic">học song song</text>')

cols = [
 (180,'4 · System design',['Khả năng mở rộng','Dữ liệu phân tán','Nhất quán, chịu lỗi','Ghi quyết định (ADR)']),
 (500,'5 · Cloud và DevOps',['Docker, Kubernetes','Terraform (IaC)','CI/CD','Observability']),
 (820,'6 · Bảo mật ứng dụng',['OWASP Top 10','OAuth 2.0, OIDC','Quản lý secret','Quét lỗ hổng']),
]
f,st,c = C['par']
for cx,title,tops in cols:
    a(f'<rect x="{cx-140}" y="604" width="280" height="254" rx="14" fill="{f}" fill-opacity="0.45" stroke="{st}" stroke-width="1.2" stroke-dasharray="4 4"/>')
    node(cx,640,250,title,'par')
    for i,t in enumerate(tops):
        topic(cx,696+44*i,t,'par',w=230,h=32)

spine_group(950,'7 · AI engineering','ai',['LLM, tool use','RAG'],['Agent, MCP','Eval'])
pill(500,1050,280,44,'Cuối lộ trình · Capstone','#1F4E79','#1F4E79','#FFFFFF',size=16,bold=True)

f,st,c = C['x']
a(f'<rect x="60" y="1112" width="880" height="122" rx="14" fill="{f}" stroke="{st}" stroke-width="1.5" stroke-dasharray="6 5"/>')
a(f'<text x="500" y="1144" text-anchor="middle" font-size="15" font-weight="700" fill="{c}">Xuyên suốt mọi nhóm</text>')
for x,t in ((220,'Git, Linux shell'),(500,'AI coding assistant'),(780,'Ghi chép, tự đánh giá')):
    pill(x,1190,240,36,t,'#FFFFFF',st,'#1F2933',size=14)
a('</svg>')
out.write_text('\n'.join(s) + '\n', encoding='utf-8')
print(f'Wrote {out}')
