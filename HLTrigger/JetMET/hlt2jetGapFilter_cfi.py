import FWCore.ParameterSet.Config as cms

hlt2jetGapFilter = cms.EDFilter('HLT2jetGapFilter',
  inputTag = cms.InputTag('iterativeCone5CaloJets'),
  minEt = cms.double(90),
  minEta = cms.double(1.9),
  saveTags = cms.bool(False)
)
