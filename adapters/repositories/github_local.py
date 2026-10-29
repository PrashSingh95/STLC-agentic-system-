"""Read-only local Git checkout inventory; no clone, shell evaluation, or network."""
from pathlib import Path
import json, subprocess

IGNORE = {'.git','node_modules','.next','dist','build','coverage','venv','.venv','vendor','target'}
MAX_FILES = 5000

def inventory(repo_path):
    repo = Path(repo_path).expanduser().resolve(strict=True)
    if not repo.is_dir(): raise ValueError('Repository must be a directory')
    files = []
    for p in repo.rglob('*'):
        if any(part in IGNORE for part in p.relative_to(repo).parts): continue
        if p.is_symlink() or not p.is_file(): continue
        files.append(p.relative_to(repo).as_posix())
        if len(files) >= MAX_FILES: break
    files.sort()
    names=set(files)
    def any_suffix(*suffixes): return any(f.endswith(s) for f in files for s in suffixes)
    packages=[]
    for filename in ['package.json','frontend/package.json','backend/package.json','web/package.json','apps/web/package.json']:
        if filename in names:
            try:
                d=json.loads((repo/filename).read_text(encoding='utf8'))
                packages.append({'path':filename,'scripts':sorted(d.get('scripts',{})),'dependencies':sorted(set(d.get('dependencies',{}))|set(d.get('devDependencies',{})))})
            except (ValueError,UnicodeError): packages.append({'path':filename,'error':'invalid package metadata'})
    deps=set(x for pkg in packages for x in pkg.get('dependencies',[]))
    frameworks=sorted({name for name,token in [('React','react'),('Next.js','next'),('Vite','vite'),('Playwright','@playwright/test'),('Vitest','vitest'),('Express','express')] if token in deps})
    if 'go.mod' in names: frameworks.append('Go')
    if any_suffix('.py'): frameworks.append('Python')
    tests=[f for f in files if f.endswith(('.test.ts','.spec.ts','.test.js','.spec.js','_test.go','.test.tsx','.spec.tsx')) or f.startswith('tests/')]
    try:
        rev=subprocess.run(['git','-C',str(repo),'rev-parse','--short','HEAD'],capture_output=True,text=True,timeout=4,check=False)
        commit=rev.stdout.strip() if rev.returncode==0 else None
    except (FileNotFoundError,subprocess.TimeoutExpired): commit=None
    return {'repo_path':str(repo),'git_commit':commit,'provider':'github/local-checkout','frameworks':frameworks,'packages':packages,'existing_tests':tests[:100], 'signals':{'frontend':bool({'React','Next.js','Vite'} & set(frameworks)) or any_suffix('.html','.tsx') or 'server.mjs' in names,'backend':'Go' in frameworks or 'Express' in frameworks or any_suffix('.go') or 'server.mjs' in names},'file_count_scanned':len(files),'truncated':len(files)==MAX_FILES}
