import FWCore.ParameterSet.Config as cms

hcalTopologyConstants = cms.ESProducer('HcalTopologyIdealEP',
  mode = cms.string('HcalTopologyMode::LHC'),
  maxDepthHB = cms.int32(2),
  maxDepthHE = cms.int32(3),
  appendToDataLabel = cms.string('')
)
