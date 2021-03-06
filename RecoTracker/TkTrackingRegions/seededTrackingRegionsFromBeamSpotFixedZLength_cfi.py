import FWCore.ParameterSet.Config as cms

seededTrackingRegionsFromBeamSpotFixedZLength = cms.EDProducer('CandidateSeededTrackingRegionsEDProducer',
  RegionPSet = cms.PSet(
    mode = cms.string('BeamSpotFixed'),
    input = cms.InputTag(''),
    maxNRegions = cms.int32(10),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    vertexCollection = cms.InputTag('hltPixelVertices'),
    maxNVertices = cms.int32(1),
    ptMin = cms.double(0.9),
    originRadius = cms.double(0.2),
    zErrorBeamSpot = cms.double(24.2),
    deltaEta = cms.double(0.5),
    deltaPhi = cms.double(0.5),
    precise = cms.bool(True),
    nSigmaZVertex = cms.double(3),
    zErrorVetex = cms.double(0.2),
    nSigmaZBeamSpot = cms.double(4),
    whereToUseMeasurementTracker = cms.string('ForSiStrips'),
    measurementTrackerName = cms.InputTag(''),
    searchOpt = cms.bool(False)
  )
)
