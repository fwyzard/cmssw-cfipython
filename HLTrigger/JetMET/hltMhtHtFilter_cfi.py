import FWCore.ParameterSet.Config as cms

hltMhtHtFilter = cms.EDFilter('HLTMhtHtFilter',
  inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  saveTags = cms.bool(False),
  minMht = cms.double(0),
  minPtJet = cms.vdouble(
    20,
    20
  ),
  minNJet = cms.int32(0),
  mode = cms.int32(2),
  etaJet = cms.vdouble(
    9999,
    9999
  ),
  usePt = cms.bool(True),
  minPT12 = cms.double(0),
  minMeff = cms.double(180),
  minHt = cms.double(0),
  minAlphaT = cms.double(0)
)
