import FWCore.ParameterSet.Config as cms

hcalTrigTowerGeometry = cms.ESProducer('HcalTrigTowerGeometryESProducer',
  hcalTopologyConstants = cms.PSet(
    mode = cms.string('HcalTopologyMode::LHC'),
    maxDepthHB = cms.int32(2),
    maxDepthHE = cms.int32(3)
  ),
  appendToDataLabel = cms.string('')
)
