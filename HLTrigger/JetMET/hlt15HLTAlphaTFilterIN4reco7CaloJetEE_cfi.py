import FWCore.ParameterSet.Config as cms

hlt15HLTAlphaTFilterIN4reco7CaloJetEE = cms.EDFilter('HLTAlphaTCaloJetFilter',
  saveTags = cms.bool(False),
  inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  inputJetTagFastJet = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  minPtJet = cms.vdouble(
    20,
    20
  ),
  minNJet = cms.int32(0),
  etaJet = cms.vdouble(
    9999,
    9999
  ),
  minHt = cms.double(0),
  minAlphaT = cms.double(0),
  triggerType = cms.int32(85)
)
