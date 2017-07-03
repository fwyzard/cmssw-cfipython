import FWCore.ParameterSet.Config as cms

hltTagAndProbeOfflineSource = cms.EDAnalyzer('HLTMuTagAndProbeOfflineSource',
  objs = cms.InputTag(''),
  tagAndProbeCollections = cms.VPSet(
  )
)
