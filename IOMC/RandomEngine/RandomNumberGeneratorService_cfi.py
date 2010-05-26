import FWCore.ParameterSet.Config as cms

RandomNumberGeneratorService = cms.Service('RandomNumberGeneratorService',
  restoreStateLabel = cms.untracked.string(''),
  saveFileName = cms.untracked.string(''),
  restoreFileName = cms.untracked.string('')
)
