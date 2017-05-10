import FWCore.ParameterSet.Config as cms

hltL1MuonNoL2Selector = cms.EDProducer('HLTL1MuonNoL2Selector',
  InputObjects = cms.InputTag(''),
  L2CandTag = cms.InputTag('hltL2MuonCandidates'),
  L1CandTag = cms.InputTag(''),
  SeedMapTag = cms.InputTag('hltL2Muons'),
  L1MinPt = cms.double(-1),
  L1MaxEta = cms.double(5),
  L1MinQuality = cms.uint32(0)
)
