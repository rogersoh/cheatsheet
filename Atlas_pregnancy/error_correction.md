# Error correction in the Atlas of the physilogy of pregnancy

Jupyter file
http://localhost:8888/notebooks/Preconception/clalit_pregnancy_090523_preconception.ipynb

Error msg:  
Passing a set as an indexer is not supported. Use a list instead.

old code:
```
tdf    = reg_res.loc[set(tests).intersection(metadata.loc[metadata.Group == groups[0]].index)].copy().sort_values(by='coeff')
```
new code: 
```
tdf    = reg_res.loc[sorted(set(tests).intersection(metadata.loc[metadata.Group == groups[0]].index))].copy().sort_values(by='coeff')
```