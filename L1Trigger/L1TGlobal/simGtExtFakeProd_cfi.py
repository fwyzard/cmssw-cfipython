import FWCore.ParameterSet.Config as cms

simGtExtFakeProd = cms.EDProducer('l1t::GtExternalFakeProducer',
  setBptxMinus = cms.bool(True),
  setBptxAND = cms.bool(True),
  bxFirst = cms.int32(-2),
  setBptxOR = cms.bool(True),
  bxLast = cms.int32(2),
  setBptxPlus = cms.bool(True)
)
