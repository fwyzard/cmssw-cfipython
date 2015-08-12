import FWCore.ParameterSet.Config as cms

saver = cms.EDAnalyzer('DQMFileSaverOnline',
  backupLumiCount = cms.untracked.int32(10),
  tag = cms.untracked.string('UNKNOWN'),
  producer = cms.untracked.string('DQM'),
  referenceHandling = cms.untracked.string('all'),
  referenceRequireStatus = cms.untracked.int32(100),
  path = cms.untracked.string('./')
)
