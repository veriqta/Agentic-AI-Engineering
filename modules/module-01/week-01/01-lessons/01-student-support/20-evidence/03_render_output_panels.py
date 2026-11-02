"""Render exact recorded subprocess output into labeled SVG panels."""
from pathlib import Path
import json,textwrap,html,shlex
l=Path(__file__).resolve().parents[1];e=l/'20-evidence/02-reference-run';o=l/'19-images'
def read(n):return json.loads((e/n).read_text())
def panel(title,sections,name):
 items=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">','<rect width="1080" height="1350" fill="#f1f6f3"/>','<rect x="40" y="40" width="1000" height="1270" rx="18" fill="white" stroke="#b7cec4"/>','<g font-family="Arial, sans-serif" fill="#12362b">']
 def text(s,y,size=21,bold=False):items.append(f'<text x="70" y="{y}" font-size="{size}"'+(' font-weight="bold"' if bold else '')+'>'+html.escape(s)+'</text>')
 text('VERIQTA ACADEMY | AGENTIC AI ENGINEERING',88,22,True)
 y=145
 for s in textwrap.wrap(title,43):text(s,y,36,True);y+=44
 text('Week 01, Lesson 01 | Actual execution, rendered output panel',y+10,21);y+=55
 text('Python '+read('02-environment.json')['python']+' | Local reference environment',y,19);y+=42
 for label,content in sections:
  text(label,y,21,True);y+=29
  for line in content.splitlines() or ['(empty stream)']:
   for wrapped in textwrap.wrap(line,92,replace_whitespace=False,drop_whitespace=False) or [' ']:
    text(wrapped,y,18);y+=24
  y+=18
 assert y<1235,(name,y)
 text('Rendered from real subprocess results, not a screenshot of a learner host.',1260,18)
 text('Raw command, streams, exit status and hashes: 20-evidence/02-reference-run.',1288,18)
 items+=['</g></svg>'];(o/(name+'.svg')).write_text('\n'.join(items)+'\n');print(name,y)
s=read('03-success.json');panel('A valid request returns JSON',[('Executed command, interpreter abbreviated as python3',shlex.join(['python3']+s['arguments'][1:])),('Actual stdout',s['stdout']),('Actual stderr',s['stderr']),('Actual exit code',str(s['exit_code'])),('What this demonstrates','The supplied status was normalized and processed. No real payment was verified and no access was granted.')],'01-success-output')
t=read('04-tests.json');panel('Nine test methods pass',[('Executed command, interpreter abbreviated as python3',shlex.join(['python3']+t['arguments'][1:])),('Actual test output',t['stdout']+t['stderr']),('Actual exit code',str(t['exit_code']))],'02-test-suite')
f=read('05-invalid.json');panel('Invalid input stops the request',[('Executed command, interpreter abbreviated as python3',shlex.join(['python3']+f['arguments'][1:])),('Actual stdout',f['stdout'] or '(empty stream)'),('Actual stderr',f['stderr']),('Actual exit code',str(f['exit_code'])),('What this demonstrates','The unsupported status was rejected before any success JSON was emitted.')],'03-invalid-input')
b=read('06-regression.json');a=read('07-recovery.json');panel('Detect a regression and verify recovery',[('Deliberate change, isolated temporary copy','Removed .lower() from the payment-status normalization. The reference source was not modified.'),('Actual failing-run excerpt, final 10 lines','\n'.join(b['stderr'].splitlines()[-10:])),('Actual failing exit code',str(b['exit_code'])),('Actual restored-run excerpt, final 4 lines','\n'.join(a['stderr'].splitlines()[-4:])),('Actual recovery exit code',str(a['exit_code']))],'04-regression-recovery')
