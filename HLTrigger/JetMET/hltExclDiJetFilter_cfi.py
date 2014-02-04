import FWCore.ParameterSet.Config as cms

hltExclDiJetFilter = cms.EDFilter('HLTExclDiJetFilter',
  inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  saveTag = cms.untracked.bool(False),
  minPtJet = cms.double(30),
  minHFe = cms.double(50),
  HF_OR = cms.bool(False)
)
