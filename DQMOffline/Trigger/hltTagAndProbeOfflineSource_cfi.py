import FWCore.ParameterSet.Config as cms

hltTagAndProbeOfflineSource = cms.EDAnalyzer('HLTEleTagAndProbeOfflineSource',
  objs = cms.InputTag(''),
  tagAndProbeCollections = cms.VPSet(
  )
)
