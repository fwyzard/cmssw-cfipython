import FWCore.ParameterSet.Config as cms

hltMuonL2PreFilter = cms.EDFilter('HLTMuonL2PreFilter',
  BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
  CandTag = cms.InputTag('hltL2MuonCandidates'),
  PreviousCandTag = cms.InputTag(''),
  SeedMapTag = cms.InputTag('hltL2Muons'),
  MinN = cms.int32(1),
  MaxEta = cms.double(2.5),
  AbsEtaBins = cms.vdouble(9999),
  MinNstations = cms.vint32(1),
  MinNhits = cms.vint32(0),
  MaxDr = cms.double(9999),
  MaxDz = cms.double(9999),
  MinPt = cms.double(0),
  NSigmaPt = cms.double(0),
  saveTags = cms.bool(False)
)
