import FWCore.ParameterSet.Config as cms

hltSingletRecoRecoEcalCandidate = cms.EDFilter('HLT1Photon',
  saveTags = cms.bool(False),
  inputTag = cms.InputTag('hltCollection'),
  triggerType = cms.int32(0),
  MinE = cms.double(-1),
  MinPt = cms.double(-1),
  MinMass = cms.double(-1),
  MaxEta = cms.double(-1),
  MinN = cms.int32(1)
)