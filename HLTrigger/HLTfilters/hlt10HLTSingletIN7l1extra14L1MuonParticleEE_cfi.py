import FWCore.ParameterSet.Config as cms

hlt10HLTSingletIN7l1extra14L1MuonParticleEE = cms.EDFilter('HLTLevel1Muon',
  saveTags = cms.bool(False),
  inputTag = cms.InputTag('hltCollection'),
  triggerType = cms.int32(0),
  MinE = cms.double(-1),
  MinPt = cms.double(-1),
  MinMass = cms.double(-1),
  MaxEta = cms.double(-1),
  MinN = cms.int32(1)
)