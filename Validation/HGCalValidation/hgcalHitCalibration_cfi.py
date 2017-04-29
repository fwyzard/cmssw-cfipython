import FWCore.ParameterSet.Config as cms

hgcalHitCalibration = cms.EDAnalyzer('HGCalHitCalibration',
  detector = cms.string('all'),
  rawRecHits = cms.bool(True)
)
