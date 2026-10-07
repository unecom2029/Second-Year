import re
def strip_slides(s):
    s=re.sub(r'\s*\((?:slides?|recording)[^()]*\)','',s)
    s=re.sub(r'(class="section-label">)[^<·"]*[Ss]lides?[^<·]*· ',r'\1',s)
    s=re.sub(r'(<span class="fig-src"><b>[^<]*</b>) · slides? [\d–,\s]+?(?=( · |</span>))',r'\1',s)
    s=s.replace('labeled by slide','labeled by source').replace('labeled by deck and slide','labeled by source')
    return s
