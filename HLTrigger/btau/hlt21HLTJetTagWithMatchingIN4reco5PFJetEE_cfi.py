import FWCore.ParameterSet.Config as cms

hlt21HLTJetTagWithMatchingIN4reco5PFJetEE = cms.EDFilter('HLTPFJetTagWithMatching',
  saveTags = cms.bool(False),
  Jets = cms.InputTag('hltJetCollection'),
  JetTags = cms.InputTag('HLTJetTagWithMatchingCollection'),
  MinTag = cms.double(2),
  MaxTag = cms.double(999999),
  MinJets = cms.int32(1),
  TriggerType = cms.int32(0),
  deltaR = cms.double(0.1)
)
