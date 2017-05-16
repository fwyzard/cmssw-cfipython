import FWCore.ParameterSet.Config as cms

electronNHitSeedProducer = cms.EDProducer('ElectronNHitSeedProducer',
  initialSeeds = cms.InputTag(''),
  vertices = cms.InputTag(''),
  beamSpot = cms.InputTag(''),
  measTkEvt = cms.InputTag(''),
  matcherConfig = cms.PSet(
    useRecoVertex = cms.bool(False),
    navSchool = cms.string('SimpleNavigationSchool'),
    detLayerGeom = cms.string('hltESPGlobalDetLayerGeometry'),
    minNrHitsValidLayerBins = cms.vint32(4),
    minNrHits = cms.vuint32(
      2,
      3
    )
  )
)
