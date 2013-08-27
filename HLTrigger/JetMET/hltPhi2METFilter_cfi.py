import FWCore.ParameterSet.Config as cms

hltPhi2METFilter = cms.EDFilter('HLTPhi2METFilter',
  inputJetTag = cms.InputTag('iterativeCone5CaloJets'),
  inputMETTag = cms.InputTag('hlt1MET60'),
  saveTags = cms.bool(False),
  minDeltaPhi = cms.double(0.377),
  minEtJet2 = cms.double(60)
)
