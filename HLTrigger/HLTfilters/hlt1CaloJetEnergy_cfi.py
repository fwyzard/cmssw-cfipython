import FWCore.ParameterSet.Config as cms

hlt1CaloJetEnergy = cms.EDFilter('HLT1CaloJetEnergy',
  inputTag = cms.InputTag('hltStoppedHSCPIterativeCone5CaloJets'),
  saveTag = cms.untracked.bool(False),
  MinE = cms.double(20),
  MaxEta = cms.double(3),
  MinN = cms.int32(1)
)
