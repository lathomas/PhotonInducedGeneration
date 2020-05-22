# PhotonInducedGeneration

cmsrel  CMSSW_7_1_21_patch2

cd CMSSW_7_1_21_patch2/src/

git clone https://github.com/lathomas/PhotonInducedGeneration

cmsenv 

To run locally, do: 

cmsRun MakeLHEGENSIMinonestep_bis.py


You can submit jobs to crab via the following command:

sh SubmitToCrab.sh  GamGamToMuMu_InelInel_SY_M-400to800_Pt-15toInf_CepGen-lpair-pythia6_13TeV


