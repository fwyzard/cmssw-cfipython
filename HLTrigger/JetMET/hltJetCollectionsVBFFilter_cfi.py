import FWCore.ParameterSet.Config as cms

hltJetCollectionsVBFFilter = cms.EDFilter('HLTJetCollectionsVBFFilter',
  inputTag = cms.InputTag('hltIterativeCone5CaloJets'),
  saveTags = cms.bool(False),
  SoftJetPt = cms.double(25),
  HardJetPt = cms.double(35),
  MinDeltaEta = cms.double(3),
  ThirdJetPt = cms.double(20),
  MaxAbsJetEta = cms.double(9999),
  MaxAbsThirdJetEta = cms.double(2.6),
  MinNJets = cms.uint32(2)
)
