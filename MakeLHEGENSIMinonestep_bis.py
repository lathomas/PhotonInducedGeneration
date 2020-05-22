# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/ThirteenTeV/LHE_DummyHadronizer_13TeV_cff.py --filein file:/user/lathomas/Generation/CMSSW_7_1_21_patch2/src/LHEForhomme/GamGamToMuMu_ElEl_M-120to200_Pt-15toInf_CepGen-lpair_13TeV.lhe --fileout file:LHEGENSIMonly_Forthomme.root --mc --eventcontent LHE,RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier LHE,GEN-SIM --conditions MCRUN2_71_V1::All --step GEN,SIM --magField 38T_PostLS1 --python_filename MakeLHEGENSIMinonestep_bis.py --no_exec -n 100
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
#process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')

process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(250)
)

# Input source
process.source = cms.Source("LHESource",
			    
#    fileNames = cms.untracked.vstring('file:/user/lathomas/Generation/CMSSW_7_1_21_patch2/src/LHEForhomme/GamGamToMuMu_InelEl_SY_M-800to1400_Pt-15toInf_CepGen-lpair-pythia6_13TeV.lhe'),
#    fileNames = cms.untracked.vstring('file:/user/lathomas/Generation/CMSSW_7_1_21_patch2/src/LHEForhomme/GamGamToMuMu_InelInel_SY_M-50to120_CepGen-lpair-pythia6_13TeV.lhe'),
#    fileNames = cms.untracked.vstring(['root://cms-xrd-global.cern.ch//store/user/lforthom/lhe/GamGamToEE_InelInel_SY_M-1400to2300_Pt-15toInf_CepGen-lpair-pythia6_13TeV.lhe']),
#    fileNames = cms.untracked.vstring(['file:/user/lathomas/Generation/CMSSW_7_1_21_patch2/src/LHEForhomme/GamGamToEE_InelEl_SY_M-1400to2300_Pt-15toInf_CepGen-lpair-pythia6_13TeV.lhe']),
#    fileNames = cms.untracked.vstring(['file:/user/lathomas/Generation/CMSSW_7_1_21_patch2/src/LHEForhomme/GamGamToEE_ElEl_M-50to120_Pt-15toInf_CepGen-lpair_13TeV.lhe']),
    fileNames = cms.untracked.vstring(['file:/user/lathomas/Generation/CMSSW_7_1_21_patch2/src/LHEForhomme/GamGamToEE_InelInel_SY_M-50to120_Pt-15toInf_CepGen-lpair-pythia6_13TeV.lhe']),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop LHEXMLStringProduct_*_*_*'),
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False)
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/ThirteenTeV/LHE_DummyHadronizer_13TeV_cff.py nevts:100'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.LHEEventContent.outputCommands,
    fileName = cms.untracked.string('file:LHEGENSIMonly_Forthomme.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('LHE')
    )
)

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:LHEGENSIMonly_Forthomme_inRAWSIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        skip_hadronization = cms.vstring('ProcessLevel:all = off', 
            'Check:event = off'),
        parameterSets = cms.vstring('skip_hadronization')
    )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.LHEoutput_step = cms.EndPath(process.LHEoutput)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.LHEoutput_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
