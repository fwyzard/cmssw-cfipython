import FWCore.ParameterSet.Config as cms

hltDiJetAveFilter = cms.EDFilter('HLTDiJetAveFilter',
  inputJetTag = cms.InputTag('hltIterativeCone5CaloJets'),
  saveTags = cms.bool(False),
  minPtAve = cms.double(100),
  minPtJet3 = cms.double(99999),
  minDphi = cms.double(-1)
)
