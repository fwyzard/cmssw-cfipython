import FWCore.ParameterSet.Config as cms

hltHbhereco = cms.EDProducer('HcalHitReconstructor',
  pedestalSubtractionType = cms.int32(1),
  pedestalUpperLimit = cms.double(2.7),
  timeSlewParsType = cms.int32(3),
  timeSlewPars = cms.vdouble(
    9.27638,
    -2.05585,
    9.27638,
    -2.05585,
    9.27638,
    -2.05585
  )
)
