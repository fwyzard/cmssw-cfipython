import FWCore.ParameterSet.Config as cms

hltMhtFilter = cms.EDFilter('HLTMhtFilter',
  saveTags = cms.bool(False),
  inputMhtTag = cms.InputTag('hltMht30'),
  minMht = cms.double(0)
)
