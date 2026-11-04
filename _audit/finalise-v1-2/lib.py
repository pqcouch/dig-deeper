import sys
class D:
    def __init__(s,p): s.p=p; s.t=open(p,encoding='utf-8').read(); s.n=0
    def _line(s,prefix):
        L=s.t.split('\n'); h=[i for i,l in enumerate(L) if l.startswith(prefix)]
        if len(h)!=1: sys.exit(f'PREFIX {len(h)} matches: {prefix[:70]}')
        return L,h[0]
    def R(s,prefix,new):
        L,i=s._line(prefix); L[i]=new; s.t='\n'.join(L); s.n+=1
    def A(s,prefix,block):
        L,i=s._line(prefix); L.insert(i+1,block); s.t='\n'.join(L); s.n+=1
    def B(s,prefix,block):
        L,i=s._line(prefix); L.insert(i,block); s.t='\n'.join(L); s.n+=1
    def I(s,old,new):
        c=s.t.count(old)
        if c!=1: sys.exit(f'SUBSTR {c} matches: {old[:70]}')
        s.t=s.t.replace(old,new); s.n+=1
    def DEL(s,prefix):
        L,i=s._line(prefix); del L[i]; s.t='\n'.join(L); s.n+=1
    def save(s): open(s.p,'w',encoding='utf-8').write(s.t); print('saved',s.p,s.n,'edits')
