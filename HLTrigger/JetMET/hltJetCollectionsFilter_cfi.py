import FWCore.ParameterSet.Config as cms

hltJetCollectionsFilter = cms.EDFilter('HLTJetCollectionsFilter',
  inputTag = cms.InputTag('hltIterativeCone5CaloJets'),
  saveTags = cms.bool(False),
  MinJetPt = cms.double(30),
  MaxAbsJetEta = cms.double(2.6),
  MinNJets = cms.uint32(1)
)
