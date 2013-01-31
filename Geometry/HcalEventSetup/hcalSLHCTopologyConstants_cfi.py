import FWCore.ParameterSet.Config as cms

hcalSLHCTopologyConstants = cms.ESProducer('HcalTopologyIdealEP',
  mode = cms.string('HcalTopologyMode::SLHC'),
  maxDepthHB = cms.int32(7),
  maxDepthHE = cms.int32(7),
  appendToDataLabel = cms.string('')
)
