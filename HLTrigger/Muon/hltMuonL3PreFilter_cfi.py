import FWCore.ParameterSet.Config as cms

hltMuonL3PreFilter = cms.EDFilter('HLTMuonL3PreFilter',
  BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
  CandTag = cms.InputTag('hltL3MuonCandidates'),
  PreviousCandTag = cms.InputTag(''),
  MinN = cms.int32(1),
  MaxEta = cms.double(2.5),
  MinNhits = cms.int32(0),
  MaxDr = cms.double(2),
  MaxDz = cms.double(9999),
  MinPt = cms.double(3),
  NSigmaPt = cms.double(0),
  saveTags = cms.bool(False)
)
