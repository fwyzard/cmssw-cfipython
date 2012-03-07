import FWCore.ParameterSet.Config as cms

hlt12HLTDoubletDZIN4reco20RecoChargedCandidateES1_E = cms.EDFilter('HLT2MuonMuonDZ',
  saveTags = cms.bool(False),
  originTag1 = cms.InputTag('hltOriginal1'),
  originTag2 = cms.InputTag('hltOriginal2'),
  inputTag1 = cms.InputTag('hltFiltered1'),
  inputTag2 = cms.InputTag('hltFiltered2'),
  triggerType1 = cms.int32(0),
  triggerType2 = cms.int32(0),
  MinDR = cms.double(-1),
  MaxDZ = cms.double(0.2),
  MinN = cms.int32(1)
)
