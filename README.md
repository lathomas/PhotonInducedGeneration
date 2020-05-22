# PhotonInducedGeneration

<code>cmsrel  CMSSW_7_1_21_patch2</code>

<code>cd CMSSW_7_1_21_patch2/src/</code>

<code>git clone https://github.com/lathomas/PhotonInducedGeneration</code>

<code>cmsenv</code>

To run locally, do: 

<code>cmsRun MakeLHEGENSIMinonestep_bis.py</code>


<b>Crab submission:</b> 
Use the following script:

<code>sh SubmitToCrab.sh  GamGamToMuMu_InelInel_SY_M-400to800_Pt-15toInf_CepGen-lpair-pythia6_13TeV</code>


<b>Important note</b> 

If you want to generate the config file directly from the cmsDriver command, you should use :

<code>cmsDriver Configuration/GenProduction/python/ThirteenTeV/LHE_DummyHadronizer_13TeV_cff.py --filein file:/user/lathomas/Generation/CMSSW_7_1_21_patch2/src/LHEForhomme/GamGamToMuMu_ElEl_M-120to200_Pt-15toInf_CepGen-lpair_13TeV.lhe --fileout file:LHEGENSIMonly_Forthomme.root --mc --eventcontent LHE,RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier LHE,GEN-SIM --conditions MCRUN2_71_V1::All --step GEN,SIM --magField 38T_PostLS1 --python_filename MakeLHEGENSIMinonestep_bis.py --no_exec -n 100 <code>

<b>AND</b> make the following change in the config file:

<code>#process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')</code>

<code>process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')</code>



