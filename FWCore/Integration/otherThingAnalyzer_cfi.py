import FWCore.ParameterSet.Config as cms

otherThingAnalyzer = cms.EDProducer('ThingWithMergeProducer',
  changeIsEqualValue = cms.untracked.bool(False),
  labelsToGet = cms.untracked.vstring(),
  noPut = cms.untracked.bool(False)
)
