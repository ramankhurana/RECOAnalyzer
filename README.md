# RECOAnalyzer
#
## SETUP (using CMSSW_8_1_0_pre15):

```
mkdir ECFAProj
cd ECFAProj
git clone https://github.com/drankincms/RECOAnalyzer.git
scram b -j8
cd RECOAnalyzer
```

## RUN:
```
cd python
cmsRun runEff.py
```
## PLOT:
```
root -l -b -q EffPlot.C
```
