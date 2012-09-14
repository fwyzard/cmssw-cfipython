import FWCore.ParameterSet.Config as cms

hcalTrigTowerGeometrySLHC = cms.ESProducer('HcalTrigTowerGeometryESProducer',
  hcalTopologyConstants = cms.PSet(
    mode = cms.string('HcalTopologyMode::SLHC'),
    maxDepthHB = cms.int32(7),
    maxDepthHE = cms.int32(7)
  ),
  appendToDataLabel = cms.string('')
)
