#!/usr/bin/env python3
from pathlib import Path
import json,sys
root=Path(__file__).resolve().parents[1]
errors=[]
for directory,required in [('agents',['AGENT.md','agent.yml','CHANGELOG.md']),('skills',['SKILL.md','agents/openai.yaml'])]:
 for folder in (root/directory).iterdir():
  if folder.is_dir():
   for name in required:
    if not (folder/name).is_file(): errors.append(f'{folder.name}: missing {name}')
for f in (root/'schemas').glob('*.json'):
 try: json.loads(f.read_text())
 except ValueError as e: errors.append(f'{f}: {e}')
for f in [root/'registry.yml',root/'workflows/full-stlc/workflow.yml']:
 if not f.exists(): errors.append(f'missing {f}')
for folder in (root/'skills').iterdir():
 if folder.is_dir() and not (folder/'SKILL.md').read_text().startswith('---\n'): errors.append(f'{folder.name}: bad frontmatter')
if errors:
 print('INVALID:',*errors,sep='\n- ');sys.exit(1)
print(f'OK: {len(list((root/"agents").iterdir()))} agents, {len(list((root/"skills").iterdir()))} skills, 2 schemas')
