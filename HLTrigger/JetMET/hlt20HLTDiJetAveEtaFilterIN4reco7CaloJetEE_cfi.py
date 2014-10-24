import FWCore.ParameterSet.Config as cms

hlt20HLTDiJetAveEtaFilterIN4reco7CaloJetEE = cms.EDFilter('HLTDiCaloJetAveEtaFilter',
  saveTags = cms.bool(False),
  inputJetTag = cms.InputTag('hltIterativeCone5CaloJets'),
  minPtAve = cms.double(100),
  minPtJet = cms.double(50),
  minDphi = cms.double(-1),
  minTagEta = cms.double(-1),
  maxTagEta = cms.double(1.4),
  minProbeEta = cms.double(2.7),
  maxProbeEta = cms.double(5.5),
  triggerType = cms.int32(85)
)