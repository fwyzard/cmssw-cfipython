import FWCore.ParameterSet.Config as cms

triggerBxMonitor = cms.EDAnalyzer('TriggerBxMonitor',
  l1tResults = cms.untracked.InputTag('gtDigis'),
  hltResults = cms.untracked.InputTag('TriggerResults'),
  dqmPath = cms.untracked.string('HLT/TriggerBx')
)
