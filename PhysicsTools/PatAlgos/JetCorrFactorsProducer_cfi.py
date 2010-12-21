import FWCore.ParameterSet.Config as cms

JetCorrFactorsProducer = cms.EDProducer('JetCorrFactorsProducer',
  emf = cms.bool(False),
  flavorType = cms.string('J'),
  src = cms.InputTag('ak5CaloJets'),
  payload = cms.string('AK5Calo'),
  levels = cms.vstring(
    'L2Relative',
    'L3Absolute',
    'L5Flavor',
    'L7Parton'
  )
)
