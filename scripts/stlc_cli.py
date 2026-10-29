#!/usr/bin/env python3
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser(description='Read-only STLC pilot preflight')
p.add_argument('command', choices=['inspect']);p.add_argument('config')
a=p.parse_args(); config=json.loads(Path(a.config).read_text())
required=['project','repo_path','requirements_path','environment']
missing=[k for k in required if not config.get(k)]
repo=Path(config.get('repo_path','/nonexistent'))
req=Path(config.get('requirements_path','/nonexistent'))
result={'mode':'read_only_preflight','project':config.get('project'),'config_valid':not missing,'missing_fields':missing,'repo_exists':repo.exists(),'requirements_exist':req.is_file(),'execution_performed':False,'status':'ready_for_discovery' if not missing and repo.exists() and req.is_file() else 'blocked','next_step':'Provide accessible local repository and requirements file, then connect an approved repository adapter.'}
print(json.dumps(result,indent=2))
