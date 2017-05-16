import FWCore.ParameterSet.Config as cms

trackingRegionsFromSuperClusters = cms.EDProducer('TrackingRegionsFromSuperClustersEDProducer',
  RegionPSet = cms.PSet(
    ptMin = cms.double(1.5),
    originRadius = cms.double(0.2),
    originHalfLength = cms.double(15),
    deltaPhiRegion = cms.double(0.4),
    deltaEtaRegion = cms.double(0.1),
    useZInVertex = cms.bool(False),
    precise = cms.bool(True),
    whereToUseMeasTracker = cms.string('kNever'),
    beamSpot = cms.InputTag(''),
    vertices = cms.InputTag(''),
    superClusters = cms.VInputTag(),
    measurementTrackerEvent = cms.InputTag('')
  )
)
