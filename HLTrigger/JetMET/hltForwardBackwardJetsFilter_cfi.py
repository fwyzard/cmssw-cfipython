import FWCore.ParameterSet.Config as cms

hltForwardBackwardJetsFilter = cms.EDFilter('HLTForwardBackwardJetsFilter',
  inputTag = cms.InputTag('hltIterativeCone5CaloJetsRegional'),
  saveTags = cms.bool(False),
  minPt = cms.double(15),
  minEta = cms.double(3),
  maxEta = cms.double(5.1)
)
