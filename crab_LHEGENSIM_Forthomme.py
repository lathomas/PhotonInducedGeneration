
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'THEREQUESTNAME'
config.General.workArea = 'crabworkarea_April2020'

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'theconfig.py'
#config.JobType.inputFiles = ['DYToLL120to200.lhe']

config.Data.outputPrimaryDataset = 'LHENAME'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 250
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'LHEGENSIMStep'


config.Site.storageSite = 'T2_BE_IIHE'
config.Site.blacklist = ['T2_US_Vanderbilt','T1_IT_CNAF']

config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']


