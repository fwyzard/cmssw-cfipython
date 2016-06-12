import FWCore.ParameterSet.Config as cms

tpClusterProducer = cms.EDProducer('ClusterTPAssociationProducer',
  simTrackSrc = cms.InputTag('g4SimHits'),
  pixelSimLinkSrc = cms.InputTag('simSiPixelDigis'),
  stripSimLinkSrc = cms.InputTag('simSiStripDigis'),
  phase2OTSimLinkSrc = cms.InputTag('simPh2OTDigis'),
  pixelClusterSrc = cms.InputTag('siPixelClusters'),
  stripClusterSrc = cms.InputTag('siStripClusters'),
  phase2OTClusterSrc = cms.InputTag('siPhase2Clusters'),
  trackingParticleSrc = cms.InputTag('mix', 'MergedTrackTruth')
)
