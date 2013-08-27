import FWCore.ParameterSet.Config as cms

hltRapGapFilter = cms.EDFilter('HLTRapGapFilter',
  inputJetTag = cms.InputTag('iterativeCone5CaloJets'),
  saveTags = cms.bool(False),
  minEta = cms.double(3),
  maxEta = cms.double(5),
  caloThresh = cms.double(20)
)
