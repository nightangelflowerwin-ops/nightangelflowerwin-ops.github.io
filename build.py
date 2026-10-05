import json
from pathlib import Path
root=Path(__file__).resolve().parent
data=json.loads((root/'portfolio.json').read_text(encoding='utf-8'))
assert data['name']=='Stephen Shore'
ids={project['id'] for project in data['projects']}
assert len(ids)==len(data['projects'])
assert all(set(skill['projects'])<=ids for skill in data['skills'])
page=(root/'template.html').read_text(encoding='utf-8').replace('__PORTFOLIO_DATA__',json.dumps(data,ensure_ascii=False).replace('</','<'+chr(92)+'/'))
(root/'index.html').write_text(page,encoding='utf-8')
print('Built portfolio')
