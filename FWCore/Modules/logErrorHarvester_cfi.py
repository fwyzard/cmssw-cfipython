import FWCore.ParameterSet.Config as cms

logErrorHarvester = cms.EDProducer('LogErrorHarvester',
  excludeModules = cms.untracked.vstring(),
  includeModules = cms.untracked.vstring()
)
