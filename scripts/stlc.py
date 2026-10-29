#!/usr/bin/env python3
"""Safe deterministic MVP: inspect, plan, and explicitly approved local demo execution."""
import argparse, json, sys, subprocess, datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from adapters.repositories.github_local import inventory

def load(config):
    path=Path(config).expanduser().resolve(strict=True)
    d=json.loads(path.read_text())
    base=path.parent
    for key in ('repo_path','requirements_path'):
        if key in d:
            p=Path(d[key]).expanduser()
            d[key]=str((base/p).resolve() if not p.is_absolute() else p.resolve())
    return d

def save(data, output):
    result=json.dumps(data,indent=2)
    if output:
        p=Path(output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(result+'\n')
    print(result)

def plan(d, inv):
    req=Path(d['requirements_path'])
    if not req.is_file(): raise ValueError('Requirement file does not exist')
    text=req.read_text(encoding='utf8')
    ids=[line.strip().split(':',1)[0].lstrip('- ').strip() for line in text.splitlines() if line.lstrip().startswith('- REQ-')]
    suites=[]
    if inv['signals']['backend']: suites.append({'id':'api','scope':'HTTP API positive/negative checks','status':'proposed'})
    if inv['signals']['frontend']: suites.append({'id':'frontend','scope':'frontend HTTP markup smoke; browser E2E not yet configured','status':'proposed'})
    return {'project':d['project'],'source_commit':inv['git_commit'],'requirements':ids,'suites':suites,'approval_required':True,'execution_status':'not_started'}

def run_demo(d,inv,approved):
    expected=(ROOT/'examples'/'demo-repo').resolve()
    if Path(d['repo_path']).resolve()!=expected: raise ValueError('v0.2 execution only allows bundled demo; external repos support inspect/plan only')
    if not approved or not d.get('execution_enabled',False): raise ValueError('Requires --approve and execution_enabled=true')
    cmd=[sys.executable,str(ROOT/'tests'/'run_demo.py')]
    done=subprocess.run(cmd,cwd=str(ROOT),capture_output=True,text=True,timeout=90,check=False)
    try: details=json.loads(done.stdout)
    except ValueError: details={'error':'invalid test runner output','stdout':done.stdout[-1000:]}
    return {'project':d['project'],'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'passed' if done.returncode==0 else 'failed','exit_code':done.returncode,'evidence':details,'stderr':done.stderr[-1000:]}

def main():
    parser=argparse.ArgumentParser(description='Agentic STLC safe local MVP')
    parser.add_argument('command',choices=['inspect','plan','run-demo'])
    parser.add_argument('--config',default='examples/demo.project.json')
    parser.add_argument('--output')
    parser.add_argument('--approve',action='store_true',help='Explicitly approve local demo execution')
    a=parser.parse_args()
    try:
        d=load(a.config); inv=inventory(d['repo_path'])
        result=inv if a.command=='inspect' else plan(d,inv) if a.command=='plan' else run_demo(d,inv,a.approve)
        save(result,a.output)
        if a.command=='run-demo' and result['exit_code']!=0: return 1
    except (OSError,ValueError,subprocess.TimeoutExpired) as exc:
        print(json.dumps({'status':'blocked','error':str(exc)}),file=sys.stderr); return 2
    return 0
if __name__=='__main__': raise SystemExit(main())
