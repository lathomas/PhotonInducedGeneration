from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()


config.General.workArea = 'MINIAODStepApril2020'
config.General.requestName = 'REQUESTNAME'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'MakeMINIAOD.py'
config.JobType.outputFiles = ['output.root']
config.Data.inputDataset = 'THEDATASET'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5

#config.JobType.numCores = 4
#config.JobType.inputFiles = ['zp_modlaurent_BM2_trunc.lhe']

#config.Data.outputPrimaryDataset = 'ZprimeSUSYBM1'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/user/lathomas/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'MINIAOD'


config.Site.storageSite = 'T2_BE_IIHE'
config.Site.blacklist = ['T2_US_Vanderbilt','T1_IT_CNAF']

config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

config.User.voGroup = 'becms'
