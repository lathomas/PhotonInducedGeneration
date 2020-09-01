# PhotonInducedGeneration

All steps except HLT should be run on 10_6_4. 
 
<code>cmsrel  CMSSW_10_6_4</code>

<code>cd CMSSW_10_6_4/src/</code>

<code>git clone https://github.com/lathomas/PhotonInducedGeneration -b ul17</code>

<code>cmsenv</code>

To run: 

<code>cmsRun MakeX.py</code>

where X=LHEGENSIM_forcrab,RAWnoHLT,AOD,MINIAOD. The output of the previous step should be provided as input to the next step (obviously...). For LHEGENSIM you need to update the inputFiles to a valid LHE file. 

<b>Important note: the HLT step MUST be run on 9_4_14_UL_patch1. It will crash on 10_6.</b>
​
<b>Crab submission:</b> 

Use the following script:

<code>sh SubmitX.py</code>



