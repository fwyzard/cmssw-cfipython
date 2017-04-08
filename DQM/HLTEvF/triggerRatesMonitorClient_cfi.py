import FWCore.ParameterSet.Config as cms

triggerRatesMonitorClient = cms.EDAnalyzer('TriggerRatesMonitorClient',
  dqmPath = cms.untracked.string('HLT/Datasets')
)
