import FWCore.ParameterSet.Config as cms

hltFatJetMassFilter = cms.EDFilter('HLTFatJetMassFilter',
  inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  saveTags = cms.bool(False),
  minMass = cms.double(0),
  fatJetDeltaR = cms.double(1.1),
  maxDeltaEta = cms.double(10)
)
