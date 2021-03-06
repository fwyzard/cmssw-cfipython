import FWCore.ParameterSet.Config as cms

hcalTopologyIdeal = cms.ESProducer('HcalTopologyIdealEP',
  Exclude = cms.untracked.string(''),
  MergePosition = cms.untracked.bool(True),
  appendToDataLabel = cms.string('')
)
