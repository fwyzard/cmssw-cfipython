import FWCore.ParameterSet.Config as cms

egammaHLTFilteredSuperClusterProducer = cms.EDProducer('EgammaHLTFilteredSuperClusterProducer',
  cands = cms.InputTag('')
)
