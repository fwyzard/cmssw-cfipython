import FWCore.ParameterSet.Config as cms

hltL1TSeed = cms.EDFilter('HLTL1TSeed',
  saveTags = cms.bool(False),
  L1SeedsLogicalExpression = cms.string(''),
  SaveTags = cms.bool(True),
  L1ObjectMapInputTag = cms.InputTag('hltGtStage2ObjectMap'),
  L1GlobalInputTag = cms.InputTag('hltGtStage2Digis'),
  L1MuonInputTag = cms.InputTag('hltGmtStage2Digis'),
  L1EGammaInputTag = cms.InputTag('hltCaloStage2Digis'),
  L1JetInputTag = cms.InputTag('hltCaloStage2Digis'),
  L1TauInputTag = cms.InputTag('hltCaloStage2Digis'),
  L1EtSumInputTag = cms.InputTag('hltCaloStage2Digis')
)
